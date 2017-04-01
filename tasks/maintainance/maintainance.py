import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers["Content-Type"] = "text/plain"\
        self.response.write("Congratulations, it's a web app!")

    app = webapp.WSGIApplication([
    ('/updateRSS/daily', MainPage.get)
    ,('/.*', MainPage.get)], debug=True)
