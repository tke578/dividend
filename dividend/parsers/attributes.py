class Attributes:
  def parse(response):
    record = dict()
    record["ticker"]            = response.get('symbol', {}).get('text', '')
    record["company_name"]      = response.get('stock_name,security_category', {}).get('text', '')
    record["sector"]            = response.get('sector')
    record["industry"]          = response.get('industry')
    record["market_cap"]        = response.get('market_cap')
    record["dow_30"]            = response.get('dow_30')
    record["share_type"]        = response.get('share_type')
    record["qualified_dividend"] =  response.get('closest_payment_qualification')
    return record