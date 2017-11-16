from common_utils.upi_status_check import get_payment_status
from zrpayment.models import Payments


def poll_payments_for_lastest_status():
    payments = Payments.objects.filter(
        status=Payments.status[0][0]
    )
    # TODO: define status field in Payments model
    print 'polling payments status for queryset ', payments

    for payment_obj in payments:
        response = get_payment_status(payment_obj.vendor_txn_id)
        if response:
            if response['status'] == "CONFIRMED":
                payment_obj.status = Payments.status[1][0]
                payment_obj.transaction_response_json["%s_RESPONSE" % response['status']] = response
            elif response['status'] == "FAILED":
                payment_obj.status = Payments.status[2][0]
                payment_obj.transaction_response_json["%s_RESPONSE" % response['status']] = response
            elif response['status'] == "EXPIRED":
                payment_obj.status = Payments.status[5][0]
                payment_obj.transaction_response_json["%s_RESPONSE" % response['status']] = response

            payment_obj.save()
