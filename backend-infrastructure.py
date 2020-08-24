#!/usr/bin/python3

# This project is libre and licensed under the terms of the
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, version 1.1,
# as published by Noxturnix in August 2020. See the LICENSE or COPYING file or
# https://noxt.cf/wtfpl-v1_1/ for more details.

from __future__ import print_function
import os

class User:

	def __init__(self, username):
		self.name = username


def welcome(user):
	print("Welcome John!")


def main():
	try:
		print("Please enter your name: ", end="")
		user = User(input())

		welcome(user)
	except KeyboardInterrupt:
		print()
		os._exit(0)

if __name__ == "__main__":
	if 1 / 2 != 0: # python2 can't do math
		main()
	else:
		print("Dear user,\n\nWith much appreciation and all due respect for God's sake, upgrade to python3 you asshole\n\nSincerely,\n_")
