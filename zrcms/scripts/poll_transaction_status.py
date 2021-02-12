# coding: utf-8import osimport djangoimport syscur_dir = os.path.dirname(os.path.realpath(__file__))sys.path.append(os.path.join(cur_dir, '..'))  # NOQAsys.path.append(os.path.join(cur_dir, '..', '..'))import settings  # NOQAos.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')  # NOQAdjango.setup()  # NOQAimport jsonfrom time import sleepimport requestsfrom common_utils import email_utilsfrom zrcms.env_vars import EKO_DEVELOPER_KEY, EKO_INITIATOR_ID, EKO_TRANSACTION_ENQUIRY_URLfrom zrtransaction.models import Transactionfrom zrtransaction.utils.constants import POLL_EXCLUDED_STATUS, TX_STATUS_AWAITED, TX_STATUS_FAIL, TX_STATUS_REFUND_PENDING, TX_STATUS_REFUNDED, TX_STATUS_SUCCESS, TRANSACTION_STATUS_SUCCESS, TRANSACTION_STATUS_REFUND_PENDING, TRANSACTION_STATUS_REFUNDEDfrom zrwallet.models import WalletTransactionsfrom django.db import transaction as dj_transactionimport tracebackimport hmacimport base64import hashlibimport timedef poll_transaction_status_for_refund():    """    # staging secret_key and secret_key_timestamp generation    secret_key_timestamp = str(int(round(time.time() * 1000)))    key = 'f74c50a1-f705-4634-9cda-30a477df91b7'    dig = hmac.new(base64.b64encode(key.encode()), secret_key_timestamp.encode(), hashlib.sha256).digest()    secret_key = base64.b64encode(dig).decode()    """    # live secret_key and secret_key_timestamp generation    secret_key_timestamp = str(int(round(time.time() * 1000)))    key = '2a749041-360c-42d3-9cf7-6d4e550d31b6'    dig = hmac.new(base64.b64encode(key.encode()), secret_key_timestamp.encode(), hashlib.sha256).digest()    secret_key = base64.b64encode(dig).decode()    try:        with dj_transaction.atomic():            transactions = Transaction.objects.select_for_update().exclude(status__in=POLL_EXCLUDED_STATUS).order_by('id')            # exclude success, failure, refunded only take transactions with pending and refund pending status            print('polling transaction status for queryset ', transactions)            for transaction in transactions:                try:                    # sleep(1)                    txn_id = transaction.vendor_txn_id                    # Old parameters for header                    # headers = {'developer_key': EKO_DEVELOPER_KEY, 'cache-control': "no-cache"}                    headers = {'developer_key': EKO_DEVELOPER_KEY, 'cache-control': "no-cache",                               'secret-key': secret_key,                               'secret-key-timestamp': secret_key_timestamp}                    #url = EKO_TRANSACTION_ENQUIRY_URL + txn_id + '?initiator_id=' + EKO_INITIATOR_ID                    url = EKO_TRANSACTION_ENQUIRY_URL + 2156859231 + '?initiator_id=' + EKO_INITIATOR_ID                    print('making eko api request ', 'URL: ', url, 'headers: ', headers)                    response_data = requests.get(url, headers=headers).json()                    print(response_data, response_data['status'])                    # refer to eko documentation for tx_status responses http://developers.eko.co.in/docs/index.html                    if response_data['status'] == 0:                        if int(response_data['data']['tx_status']) == TX_STATUS_SUCCESS:                            print(' transaction ', transaction.vendor_txn_id)                            transaction.status = TRANSACTION_STATUS_SUCCESS                            transaction.save()                            if transaction.transaction_response_json is None:                                transaction.transaction_response_json = dict(poll_success_response=json.dumps(response_data))                            else:                                transaction.transaction_response_json['poll_success_response'] = json.dumps(response_data)                            transaction.save()                        elif int(response_data['data']['tx_status']) == TX_STATUS_FAIL:                            # transaction.status = TRANSACTION_STATUS_FAILURE                            transaction.save()                            if transaction.transaction_response_json is None:                                transaction.transaction_response_json = dict(poll_failure_response=json.dumps(response_data))                            else:                                transaction.transaction_response_json['poll_failure_response'] = json.dumps(response_data)                            transaction.save()                            #     send a mail to the zrupee tech                            email_utils.send_email(                                'Error in EKO refund polling!',                                'tech@zrupee.com',                                'payment_status_error',                                {                                    'url': url,                                    'response_json': json.dumps(response_data)                                },                                is_html=True                            )                        elif int(response_data['data']['tx_status']) == TX_STATUS_AWAITED:                            pass                        elif int(response_data['data']['tx_status']) == TX_STATUS_REFUND_PENDING:                            if transaction.status != TRANSACTION_STATUS_REFUND_PENDING:                                if transaction.transaction_response_json is None:                                    transaction.transaction_response_json = dict(                                        poll_refund_pending_response=json.dumps(response_data))                                else:                                    transaction.transaction_response_json['poll_refund_pending_response'] = json.dumps(response_data)                            transaction.status = TRANSACTION_STATUS_REFUND_PENDING                            transaction.save()                        elif int(response_data['data']['tx_status']) == TX_STATUS_REFUNDED and transaction.status != 'R':                            merchant_wallet = transaction.user.wallet                            refund_amount = transaction.amount + transaction.additional_charges                            wallet_log = WalletTransactions()                            wallet_log.wallet = merchant_wallet                            wallet_log.transaction = transaction                            if transaction.type.name.upper() == 'DMT':                                merchant_wallet.dmt_balance += refund_amount                                merchant_wallet.save()                                wallet_log.dmt_balance = refund_amount                                wallet_log.dmt_closing_balance = merchant_wallet.dmt_balance                            else:                                merchant_wallet.non_dmt_balance += refund_amount                                merchant_wallet.save()                                wallet_log.non_dmt_balance = refund_amount                                wallet_log.non_dmt_closing_balance = wallet_log.non_dmt_balance                            wallet_log.save()                            transaction.status = TRANSACTION_STATUS_REFUNDED                            transaction.save()                            if transaction.transaction_response_json is None:                                transaction.transaction_response_json = dict(poll_refunded_response=json.dumps(response_data))                            else:                                transaction.transaction_response_json['poll_refunded_response'] = json.dumps(response_data)                            transaction.save()                except Exception as e:                    print((transaction, transaction.pk))                    print((traceback.format_exc()))                    print('1 error -> ', e)    except Exception as e:        # print(transaction, transaction.pk, transaction.is_commission_created)        print((traceback.format_exc()))        print('2 error -> ', e)poll_transaction_status_for_refund()