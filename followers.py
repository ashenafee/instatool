from typing import List


def followers_to_txt(api, max_id=None) -> None:
    """Output a file containing a list of all followers of the authenticated user."""
    if max_id is not None:
        followers = api.user_followers(api.authenticated_user_id, rank_token=api.generate_uuid(), max_id=max_id)
    else:
        followers = api.user_followers(api.authenticated_user_id, rank_token=api.generate_uuid())
    for follower in followers['users']:
        # Print followers to text file
        with open('followers.txt', 'a') as f:
            f.write(follower['username'] + '\n')
    # Break recursion if there is no next_max_id
    if followers['next_max_id'] is None:
        return
    else:
        followers_to_txt(api, followers['next_max_id'])

def followers_to_lst() -> List[str]:
    """Return a list of all followers of the authenticated user."""
    with open('followers.txt', 'r') as f:
        temp = f.readlines()
    followers = []
    for user in temp:
        followers.append(user.strip())
    return followers

def following_to_txt(api, max_id=None):
    """Output a file containing a list of all users the authenticated user is following."""
    if max_id is not None:
        following = api.user_following(api.authenticated_user_id, rank_token=api.generate_uuid(), max_id=max_id)
    else:
        following = api.user_following(api.authenticated_user_id, rank_token=api.generate_uuid())
    for user in following['users']:
        # Print following to text file
        with open('following_id.txt', 'a') as f:
            f.write(user['username'] + '\n')
    # Break recursion if there is no next_max_id
    if following['next_max_id'] is None:
        return
    else:
        following_to_txt(api, following['next_max_id'])

def following_to_lst() -> List[str]:
    """Return a list of all users the authenticated user is following."""
    with open('following_id.txt', 'r') as f:
        temp = f.readlines()
    following = []
    for user in temp:
        following.append(user.strip())
    return following

def does_not_follow(following, followers) -> None:
    """Output a file containing all users the authenticated user is following but not following back."""
    for user in following:
        if user not in followers:
            with open('dnf.txt', 'a') as f:
                f.write(user + '\n')

def dnf_to_lst() -> List[str]:
    """Return a list of all users the authenticated user is following but not following back."""
    with open('dnf.txt', 'r') as f:
        temp = f.readlines()
    dnf = []
    for user in temp:
        dnf.append(user.strip())
    return dnf