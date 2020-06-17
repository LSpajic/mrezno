class CookieList:
	def __init__(self):
		self._context=dict()
	def put(self, vrijednost, podatci):
		self._context[vrijednost] = podatci
	def get(self,vrijednost):
		return self._context.get(vrijednost)
		