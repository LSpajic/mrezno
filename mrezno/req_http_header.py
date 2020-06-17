class RequestHttpHeader:
	def __init__(self):
		self._method = None
		self._cookies = {}
	
	@staticmethod
	def parse_from_string(header_string):
		result_header = RequestHttpHeader()
		header_dict = RequestHttpHeader.parse_http_header(header_string)

		#tu ga popuni iz header_string
		result_header._method = header_dict['method']
		result_header._path = header_dict['path']
		result_header._protocol = header_dict['protocol']
		result_header._user_agent = header_dict['user-agent']
		result_header._host = header_dict['host']

		if "cookie" in header_dict.keys():
			lista_cookieja = header_dict["cookie"].split(";")
			
			for cookie in  lista_cookieja:
				name, value = cookie.split("=")
				result_header._cookies[name] = value
		
		return result_header

	def get_method(self):
		return self._method
	def get_path(self):
		return self._path
	def get_protocol(self):
		return self._protocol
	def get_user_agent(self):
		return self._user_agent
	def get_host(self):
		return self._host
	def get_cookie_by_name(self, name):
		return self._cookies.get(name)
	
	@staticmethod
	def parse_http_header(cli_msg):
		header_dicti={}
		#print("EVO " + cli_msg)
		header_to_parse = cli_msg.split("\r\n")
		redpr = header_to_parse[0].split()
		print("--------------------",redpr)
		
		header_dicti["method"] = redpr[0]
		header_dicti["protocol"] = redpr[2]
		header_dicti["path"] = redpr[1]

		for red in header_to_parse[1:]:
			red = red.split(": ")

			try:
				header_dicti[red[0].lower()] = red[1]
			except IndexError:
				print("Nisam uspio parsirati {}".format(red))
				continue

		#print(header_dicti)
		return header_dicti