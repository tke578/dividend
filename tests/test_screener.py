import requests
from unittest import TestCase
from dividend.screener import Screener
from dividend.errors import InvalidChoice, BadRequest

class TestScreener(TestCase):

	def api_endpoint(self):
		return 'https://www.dividend.com/api/data_set'

	def payload(self):
		return {
			"tm":"3-screener",
			"r":"Webpage#1350",
			"only":["meta","data"]
		}

	def test_api_endpoint(self):
		response = requests.post(url=self.api_endpoint(), json=self.payload())
		self.assertEqual(response.status_code, 200)

	def test_invalid_table_view_choice(self):
		with self.assertRaises(InvalidChoice):
			Screener(table='blah')

	def test_invalid_filters(self):
		with self.assertRaises(BadRequest):
			Screener(filters='test')
		with self.assertRaises(BadRequest):
			Screener(filters=('test', 'test'))
		with self.assertRaises(BadRequest):
			Screener(filters=[123])
			
	def test_is_string(self):
		s = Screener.test()
		self.assertTrue(isinstance(s,str))