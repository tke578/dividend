class Overview:
  def parse(response):
    record = dict()
    record["ticker"]          = response.get('symbol', {}).get('text', '')
    record["dividend_yield"]  = response.get('latest_yield', '')
    record["price"]           = response.get('last_price', '')
    record["annual_payout"]   = response.get('annualized_payout', '')
    record["upcoming_dividend_ex_date"] = response.get('closest_payment_ex_date', '')
    record["upcoming_payment_payable_date"] = response.get('closest_payment_payable_date', '')
    record["url"] = response.get('symbol', {}).get('url', '')
    return record