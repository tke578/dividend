from dividend.parsers.attributes import Attributes
from dividend.parsers.overview import Overview
from dividend.parsers.dividend_growth import DividendGrowth
from dividend.errors import InvalidChoice

class ParseTable:
  def parsers(self, table_view):
    parsers = {
      "overview": Overview,
      "dividend-growth": DividendGrowth,
      "attributes": Attributes
    }
    try:
    	return parsers[table_view].parse
    except KeyError:
    	raise InvalidChoice(f'Invalid table view, valid choices are {list(parsers.keys())}')