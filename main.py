#-----------------------------------------------------------------------
#			CS 496 - Mobile and Cloud Software Development
#				Oregon State University - Summer 2016
#						Assignment 1: Hello Cloud
#
# Author: James Pool
# ONID: 932664412
# OSU Email: poolj@oregonstate.edu
# Date: 26 June 2016
#
# Program Filename: Readme.md
# Description: main function for CS 496 Assignment 1. Adapted from 
#			   the python quickstart guide: 
# https://cloud.google.com/appengine/docs/python/quickstart#download_the_hello_world_app
#-----------------------------------------------------------------------

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
