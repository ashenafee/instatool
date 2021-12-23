from user import User


class Unfollow:
    """An object meant to unfollow users."""

    def __init__(self, user: User):
        self.user = user
        self.api = user.get_api()

    def unfollow(self, username: str) -> bool:
        """Unfollow a specific user, given a username."""
        print(f"Unfollowing {username}...")
        self.api.friendships_destroy(
            self.api.username_info(username)["user"]["pk"])
        print("Unfollowed!")
        return True

    def unfollow_all(self) -> bool:
        """Unfollow all users that self.user follows."""
        print(
            f"Unfollowing all users that {self.user.get_username()} follows...")
        following = self.user.get_following_list()
        for user in following:
            self.api.friendships_destroy(
                self.api.username_info(user)["user"]["pk"])
        print("Unfollowed all users!")
        return True

    def unfollow_hollywood(self) -> bool:
        """Unfollow all users that don't follow self.user back."""
        print(
            f"Unfollowing all users that don't follow "
            f"{self.user.get_username()} back...")
        hollywood = self.user.get_hollywood_list()
        for user in hollywood:
            self.api.friendships_destroy(
                self.api.username_info(user)["user"]["pk"])
        print("Unfollowed all hollywood users!")
        return True
