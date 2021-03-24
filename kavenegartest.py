import requests

# Check kavenegar API and url

def inform_ali(price):
    API_Key = 'my_API'
    url = 'https://api.kavenegar.com/v3/{API_Key}/sms/send.json' #check kavenegar
    payload = {'receptor':'09031304243','message':'Time to buy, the price is {price}'}
    r = requests.post(url,data=payload)
    print(r)


low_price = 5000

# Check coinbase API

response = requests.get('https://api.coinbase.com/v4/prices/buy?currency=USD',
                        proxies={'https':'socks5://127.0.0.1:1080'})       

price = float(response.json()['data']['amount'])

if (price <= low_price):
    inform_ali(price)