class Non200Response(Exception):
	"""For non 200 response"""
	def __init__(self, url):
		super(Non200Response, self).__init__(f'Url returned a non 200 response {url}')

class BadRequest(Exception):
	"""Bad Requests"""
	def __init__(self, error_msg):
		super(BadRequest, self).__init__(f'{error_msg}')

class InvalidChoice(Exception):
	"""Invalid Choices used in table view"""
	def __init__(self, msg):
		super(InvalidChoice, self).__init__(f'{msg}')
