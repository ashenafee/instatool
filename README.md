# instatool
A simple unfollowing tool for Instagram.

## setup
Make sure you have the latest version of Python installed.

Once that's set, pull up a terminal window and execute the following:

`pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0`

This installs the dependency for this script to work.

## usage
Run `main.py` and enter your username and password at the prompts.

The script will gather all of your followers, the users you follow,
and unfollow anyone who you follow that doesn't follow you.