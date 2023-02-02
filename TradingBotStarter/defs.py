API_KEY = "475688acdafd540bb5cefbc4598320ce-9d23b71c959601a2b046590bc09df83d"
ACCOUNT_ID = "101-001-13800215-001"
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'

SECURE_HEADER = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

BUY = 1
SELL = -1
NONE = 0