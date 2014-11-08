YoPy
====

A simple Yo! API for python.

As of now, you can:
<ol>
	<li>Get the number of subscribers</li>
	<li>Send a Yo! to all subscribers</li>
	<li>Send a Yo! to a specific user</li>
</ol>

YoPy requires a Yo! API access token. You can get one by registering at http://dev.justyo.co/

Dependencies
============
This version of YoPy is designed to work within Google App Engine

Installation
============
To install, simple copy <code>yopy.py</code> to the <code>Lib</code> folder of your Python installation.

Usage
=====
YoPy works with Python as supported by Google App Engine<br/>
Here is a Python 2 example :

	import yopy

	token = <your_api_token>
	username = "PARTHDHAR"
	link = "https://github.com/espice/YoPy"
	location = "37.864849,-119.538361"

	yo = yopy.Yo(token)
	print yo.number()
	yo.yo_all(link)
	yo.yo_user(username, link=link)
	yo.yo_user(username, location=location)

Parth Dhar<br/>
2014