import urlparse

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class RedirectPage(webapp.RequestHandler):
    def handle(self):
        path = self.request.path
        if path.endswith("/"):
            path += "index.html"
        self.redirect(urlparse.urljoin('http://fcdn.pozytywnie.pl/archive/', path.strip("/")))

    def post(self):
        self.handle()

    def get(self):
        self.handle()

application = webapp.WSGIApplication(
    [('/.*', RedirectPage)],
    debug=False,
)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
