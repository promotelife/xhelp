import tornado.wsgi
import tornado.web

import hashlib

import sae
from wxServer import wxServer


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, world! - Tornado")
class wxhelp(tornado.web.RequestHandler):
	def get(self): 
		token="promotelife"
		signature=self.get_argument("signature","")
		timestamp=self.get_argument("timestamp","")
		nonce=self.get_argument("nonce","")
		echostr=self.get_argument("echostr","") 

		tmplist = [token, timestamp, nonce]
		tmplist.sort()
		tmpstr = ''.join(tmplist)
		hashstr = hashlib.sha1(tmpstr).hexdigest()
		if hashstr == signature:
			self.write(echostr) #success
		else:
			self.write("False")  #fail
	def post(self):
		wxwerver=wxServer(self.request.body)
		self.write(wxwerver.run())




settings = {
	'debug': True,
}

handlers = [
	(r"/", MainHandler),
	(r'/promotelife', wxhelp),
]


tornado_app = tornado.wsgi.WSGIApplication(**settings)
tornado_app.add_handlers(r'.*', handlers)

application = sae.create_wsgi_app(tornado_app)


