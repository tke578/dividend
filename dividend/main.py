from screener import Screener


def search_stock(table='', **kwargs):
	if not table:
		return Screener(**kwargs)
	return Screener(table=table, **kwargs)
