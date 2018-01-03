#!/usr/bin/env python

import requests
import sys
import config as cfg
import json
import time

'''
Code is not working as of now, need some modifications.

'''

print '\n[-] Incomplete code. Work in Progress\n'

username = sys.argv[1]
access_token = cfg.github_access_token
print username

def find_repos(username):
	print "\t\t\t[+]Finding repos for %s" % (username)
	list_repos = []
	url = "https://api.github.com/users/%s/repos?access_token=%s" % (username, access_token)
	req = requests.get(url)
	if 'API rate limit exceeded' not in req.text:
		for repos in json.loads(req.content):
			repos['full_name']
			if repos['fork'] == False:
				list_repos.append(repos['full_name'])
		return list_repos
	else:
		return []

def find_commits(repo_name):
	print "\t\t\t[+]Finding commits for %s..." % (repo_name)
	list_commits = []
	for x in xrange(1,10):
		url = "https://api.github.com/repos/%s/commits?page=%s&access_token=%s" % (repo_name, x, access_token)
		req = requests.get(url)
		data = json.loads(req.content)
		for commits in data:
			try:
				list_commits.append(commits['sha'])
			except:
				print "Empty Repo"
		if (len(data) != 30):
			return list_commits
		else:
			print "[+]..Heading to next page..."
	return list_commits
	print "Too many commits, search manually."

master_dict = {}
list_repos = find_repos(username)
if list_repos != []:
	print "Following repos found :"
	count = 0
	for x in list_repos:
		count = count + 1
		print '%s. %s' % (count, x)
	print "\n-----------------------------\n"

	for repo_name in list_repos:
		master_dict[repo_name] = find_commits(repo_name)
	print "\n-----------------------------\n"
	print "Done. Printing master list. {Repo:[commit1,commit2]}.."
	#finding commits from list

	print master_dict

	for abc in master_dict.keys():
		print "Commits for %s:" % (abc)
		for xyz in master_dict[abc]:
			print xyz
		print "\n"
else:
	print 'Rate limiting Exceeded.'


