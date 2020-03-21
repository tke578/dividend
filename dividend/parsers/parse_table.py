from parsers.attributes import Attributes
from parsers.overview import Overview
from parsers.dividend_growth import DividendGrowth

class ParseTable:
  def parsers(self, table_view):
    parsers = {
      "overview": Overview,
      "dividend-growth": DividendGrowth,
      "attributes": Attributes
    }
    return parsers[table_view].parse