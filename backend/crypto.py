from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def crypto_to_usd(id):
    crypto = cg.get_price(ids= id , vs_currencies= 'usd')
    x = crypto[id]['usd']
    return x