import os

ENVIRONMENT = os.getenv('APP_ENVIRONMENT', 'local')

LOCAL_SECRET_KEY = ')cgcw7ffq2&_zbcj-icg5dym7tzsum5#=nf4e5ay4snjp6hl_b'
SECRET_KEY = os.getenv('APP_SECRET_KEY', LOCAL_SECRET_KEY)

# EKO credentials
# Trying to get the credentials from environment Variables, falling back to sandbox environment
EKO_INITIATOR_ID = os.getenv('EKO_INITIATOR_ID', '9910028267')
EKO_DEVELOPER_KEY = os.getenv('EKO_DEVELOPER_KEY', 'becbbce45f79c6f5109f848acd540567')
EKO_TRANSACTION_ENQUIRY_URL = os.getenv('EKO_TRANSACTION_ENQUIRY_URL',
                                        'https://staging.eko.co.in:25004/ekoapi/v1/transactions/')


QUICKWALLET_ZR_PARTERNERID = os.getenv('QUICKWALLET_ZR_PARTERNERID', '293')
QUICKWALLET_SECRET = os.getenv('QUICKWALLET_SECRET', '2z9WyZ823Q78kER')
QUICKWALLET_API_CRUD_URL = os.getenv('QUICKWALLET_API_CRUD_URL',
                                        'https://uat.quikwallet.com/api/partner/{0}/merchants/crud'.format(QUICKWALLET_ZR_PARTERNERID))
QUICKWALLET_API_CARD_URL = os.getenv('QUICKWALLET_API_CARD_URL',
                                        'https://uat.quikwallet.com/api/partner/{0}/loyaltycards/create'.format(QUICKWALLET_ZR_PARTERNERID))
QUICKWALLET_API_LISTCARD_URL = os.getenv('QUICKWALLET_API_LISTCARD_URL',
                                        'https://uat.quikwallet.com/api/partner/{0}/loyaltycards'.format(QUICKWALLET_ZR_PARTERNERID))
