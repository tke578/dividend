class DividendGrowth:
  def parse(response):
    record = dict()
    record["ticker"]            = response.get('symbol', {}).get('text', '')
    record["company_name"]      = response.get('stock_name,security_category', {}).get('text', '')
    record["payout_ratio"]      = response.get('payout_ratio', '')
    record["payout_frequency"]  = response.get('closest_payment_frequency', '')
    record["consecutive_years_of_growth"] = response.get('consective_year_of_growth', '')
    return record