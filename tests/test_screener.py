from unittest import TestCase
from dividend.screener import Screener

class TestScreener(TestCase):
	def test_is_string(self):
		s = Screener.test()
		self.assertTrue(isinstance(s,str))