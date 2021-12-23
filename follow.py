from user import User


class Follow:
    """An object meant to follow users."""

    def __init__(self, user: User):
        self.user = user
        self.api = user.get_api()

    def follow(self, username: str) -> bool:
        """Follow a specific user, given a username."""
        print(f"Following {username}...")
        self.api.friendships_create(
            self.api.username_info(username)["user"]["pk"])
        print("Followed!")
        return True

    def follow_all_followers(self) -> bool:
        """Follow all users that follow self.user."""
        print(f"Following all users that follow {self.user.get_username()}...")
        hollywood = self.user.get_hollywood_list()
        for user in hollywood:
            self.api.friendships_destroy(
                self.api.username_info(user)["user"]["pk"])
        print("Unfollowed all hollywood users!")
        return True

    def remove_follower(self, username: str) -> bool:
        """Remove a follower, given a username."""
        print(f"Removing {username} from your followers...")
        self.api.remove_follower(self.api.username_info(username)["user"]["pk"])
        print("Removed!")
        return True
