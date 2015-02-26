

from date import date
import csv

def read_parentURLs(i):
	"""Reads the URLs from the Parent URLs CSV"""
	with open('parentURLs.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		return URL

def read_reqURLs(i):
	"""Reads the URLs from the Requested Parent URLs CSV"""
	with open('requested_parentURLs.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "generating base url", i+1
		return URL


def read_subURLs(i):
	with open('subpages.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "generating subpage", i+1
		return URL


def read_speechURLs(i):
	with open('speechurls.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "creating file", i+1
		return URL

