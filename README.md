# instatool
A simple multi-purpose tool for Instagram.

## setup
Make sure you have the latest version of Python installed.

Once that's set, pull up a terminal window and execute the following:

`pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0`

This installs the dependency for this script to work.

## usage
Run `main.py` and enter your username and password at the prompts.

You will be greeted with a main menu full of options. The options are:

| Option | Purpose                              |
|--------|--------------------------------------|
| 1      | Show users that don't follow you     |
| 2      | Show users that you don't follow     |
| 3      | Follow a specific user               |
| 4      | Follow all followers back            |
| 5      | Unfollow a specific user             |
| 6      | Unfollow all users                   |
| 7      | Unfollow all non-reciprocating users |
| 8      | Remove a specific follower           |

Depending on your chosen option, different things will be outputted to the console.
