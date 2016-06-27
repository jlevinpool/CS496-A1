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
# Description: main function for CS 496 Assignment 1. 

# Adapted from:
#   Python quickstart guide: 
# https://cloud.google.com/appengine/docs/python/quickstart#download_the_hello_world_app
#   The Reponse class:
# https://cloud.google.com/appengine/docs/python/tools/webapp/responseclass#Introduction
#-----------------------------------------------------------------------

import webapp2
import datetime

class MainPage(webapp2.RequestHandler):
    def get(self):
        current_date = datetime.datetime.utcnow()
        current_str = current_date.strftime("%d %b %Y %H:%M:%S PST")
        
        self.response.write("<html><body>")
        self.response.write("<strong>CS 496 - Assignment 1</strong>")
        self.response.write("<p>The time is: " + current_str + "</p>")
        self.response.write("</body></html>")
		
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
