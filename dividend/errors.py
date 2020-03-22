class Non200Response(Exception):
	"""For non 200 response"""
	def __init__(self, url):
		super(Non200Response, self).__init__(f'Url returned a non 200 response {url}')

class BadRequest(Exception):
	"""Bad Requests"""
	def __init__(self, error_msg):
		super(BadRequest).__init__(f'Something bad happened {error_msg}')