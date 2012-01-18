import simplejson as json
import urlparse

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class RedirectPage(webapp.RequestHandler):
    def handle(self):
        path = self.request.path
        if path.endswith("/"):
            path += "index.html"
        self.redirect(urlparse.urljoin('https://d31nkok4v6vad6.cloudfront.net/static/', path.strip("/")) +
            "#" + getattr(self, "signed_request", ""))

    def post(self):
        try:
            signed_request = self.request.get('signed_request')
            if signed_request:
                _, payload = signed_request.split('.', 1)
                self.signed_request = payload
        except:
            pass

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
