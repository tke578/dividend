import json
import requests
import asyncio
import aiohttp
from aiohttp import ClientSession


class AsyncRequests:

  def __init__(self, payload, scrape_func):
    self.payload = payload
    self.scrape_func = scrape_func
    self._total_records = 0
    self.records = None
    self._pages_to_request = self._initial_request()

  def _initial_request(self):
    try:
      response = requests.post(url="https://www.dividend.com/api/data_set", json=self.payload)
      total =  int(response.json().get('meta', {}).get('total_pages', 1))
      if total > 200:
        return 200
      return total
    except Exception as e:
      print(e)
      return 1

  def scrape(self, response):
    results = []
    try:
      for equity in response["data"]:
        parsed_response = self.scrape_func(equity)
        #print(parsed_response)
        self._total_records += 1 
        results.append(parsed_response)
      return results
    except KeyError:
      return result

  async def fetch_html(self, url: str, session: ClientSession, data: dict) -> str:
    resp = await session.request(method="POST", url=url, json=data)
    resp.raise_for_status()
    html =  await resp.json()
    return self.scrape(html)

  async def make_requests(self, url: str, payload: dict) -> None:
    async with ClientSession() as session:
        tasks = []
        for i in range(1,self._pages_to_request+1):
          payload["page"] = i
          tasks.append(
            self.fetch_html(url=url, session=session, data=payload)
          )

        results = await asyncio.gather(*tasks)
        self.records = [ equities for sub_list in results for equities in sub_list ]
        
        #print(json.dumps(results, indent=4, sort_keys=True))
  def run(self):
    run_async = asyncio.get_event_loop()
    run_async.run_until_complete(self.make_requests(url='https://www.dividend.com/api/data_set', payload=self.payload))
    return self.records