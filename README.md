# dividend

*The Unofficial API for dividend.com*

Installation
-----

This package has been uploaded to [Pypi](https://pypi.org/project/dividend/), to install the latest package:

``` pip install dividend```

### Using the Screener

```
from dividend.screener import Screener

filters = { "f_7_min": 100. "f_7_max": 500 } #Share price between $100 and $500

equities = Screener(filters=filters)

equities.data
[{'ticker': 'YMZBY', 'company_name': 'Yamazaki Baking Co Ltd - ADR', 'payout_ratio': '0.00%', 'payout_frequency': 'N/A', 'consecutive_years_of_growth': '0'}...]

equities.total_records
136
```
#### Screener Tables

There are 3 table views to choose from; ```'overview', 'attributes' & 'dividend-growth'```

You can change table view when initialzing ```Screener(table='overview')```

The default is set to ```'overview'```


#### Screener Filters

You can pass in an arbitrary amount of valid filters.Each filter has a correspondng key name. To find the corresponding key, you will need to parse the screener web page url params.

The filter params follows a alphanumeric convention. For instance, if you wish to filter by sector which are in Basic Materials, the filter params will look as follows: ```f_1=Basic%20Materials```

The  filer object: ```filters = { "f_1": ["Basic Materials"] }```


Filters with checkboxes are passed as a collection of array strings. Filters with ranges are passed with a min and max values and can also accept boolean values.


Current limit is 4000 records to minimze large requests. If you wish to receive more than the limit, create issue ticket.

