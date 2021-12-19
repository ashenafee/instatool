from instagram_private_api import Client, ClientCompatPatch
from typing import List

def get_user_id(api, username) -> str:
    """Return the user id of the user with the given username."""
    user_info = api.username_info(username)
    return user_info['user']['pk']

def dnf_to_ids(api, dnf_list) -> List[str]:
    """Return a list of all IDs of users the authenticated user is following but not following back."""
    dnf_ids = []
    for user in dnf_list:
        dnf_ids.append(get_user_id(api, user))
    return dnf_ids

def unfollow(api, dnf_ids) -> None:
    """Unfollow all users in the dnf_ids list."""
    for user_id in dnf_ids:
        api.friendships_destroy(user_id)
