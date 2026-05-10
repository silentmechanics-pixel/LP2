#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
#

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):

    def get(self):

        self.response.out.write('''
        <h2>Factorial Program</h2>

        <form method="post">

            Enter Number:
            <input type="text" name="num">

            <input type="submit" value="Find Factorial">

        </form>
        ''')

    def post(self):

        num = int(self.request.get('num'))

        fact = 1

        for i in range(1, num + 1):

            fact = fact * i

        self.response.out.write("Factorial = %d" % fact)


def main():

    application = webapp.WSGIApplication(
        [('/', MainHandler)],
        debug=True
    )

    util.run_wsgi_app(application)


if __name__ == '__main__':

    main()
