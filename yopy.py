#!/usr/bin/env python
"""
A simple Yo! API for python.

As of now, you can:
	1.Get the number of subscribers
	2.Send a Yo! to all subscribers
	3.Send a Yo! to a specific user

YoPy requires a Yo! API access token. You can get one by registering at http://dev.justyo.co/

Parth Dhar
2014
"""
from google.appengine.api import urlfetch

class Yo:
	def __init__(self, token):
		self.token = token

	def number(self):
		"""
		Function to GET the the number of subscribers of the API user account.
		Returns number of subscribers as an integer.
		If request is unsuccessful, raises an error.
		"""
		number_url = "https://api.justyo.co/subscribers_count/?api_token=" + self.token
		number = urlfetch.fetch(number_url)
		if number.status_code == requests.codes.ok:
		    return number.json()["result"]
		else:
			number.raise_for_status()

	def yo_all(self, *link):
		"""
		Function to send a Yo to all subscribers of the API user account.
		If request is successful, returns true.
		If request is unsuccessful, raises an error.
		"""
		yoall_data = {"api_token": self.token}
		for kw in kwargs:
			youser_data.update( { kw:kwargs[kw] } )
		yoall_url = "https://api.justyo.co/yoall/"
		yoall = urlfetch.fetch(url=yoall_url, payload=yoall_data, method=urlfetch.POST)
		if yoall.status_code == requests.codes.created:
			return True
		else:
			yoall.raise_for_status()

	def yo_user(self, username, **kwargs):
		"""
		Function to send a Yo to a specific username.
		If request is successful, returns true.
		If request is unsuccessful, raises an error.
		"""
		username = username.upper()
		youser_data = {"api_token": self.token, "username": username}
		for kw in kwargs:
			youser_data.update( { kw:kwargs[kw] } )
		youser_url = "https://api.justyo.co/yo/"
		youser = urlfetch.fetch(url=youser_url, payload=youser_data, method=urlfetch.POST)
		if youser.status_code == requests.codes.ok:
		    return True
		else:
			yoall.raise_for_status()