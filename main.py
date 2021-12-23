from user import User
from follow import Follow
from unfollow import Unfollow


def show_hollywood(user: User) -> None:
    """Show users you follow, but they don't follow you back."""
    hollywood = user.get_hollywood_list()
    for account in hollywood:
        print(account)


def show_non_mutual(user: User) -> None:
    """Show users that follow you, but you don't follow them back."""
    non_mutual = user.get_not_mutual_list()
    for account in non_mutual:
        print(account)


def follow(user: User, operation: int) -> None:
    """Follow user(s) given the type of follow operation.
    Operations:
    1 = Follow a single user
    2 = Follow all followers
    """
    if operation == 1:
        username = input("Enter the username of who to follow:\n")
        follow_single(user, username)
    elif operation == 2:
        follow_all(user)


def follow_single(user: User, username: str) -> None:
    """Helper method for follow() to follow a single user."""
    flw = Follow(user)
    flw.follow(username)


def follow_all(user: User) -> None:
    """Helper method for follow() to follow all followers."""
    flw = Follow(user)
    flw.follow_all_followers()


def unfollow(user: User, operation: int) -> None:
    """Unfollow user(s) given the type of unfollow operation.
    Operations:
    1 = Unfollow a single user
    2 = Unfollow every user
    3 = Unfollow all users who don't follow you back
    """
    if operation == 1:
        username = input("Enter the username of who to unfollow:\n")
        unfollow_single(user, username)
    elif operation == 2:
        unfollow_all(user)
    elif operation == 3:
        unfollow_non_mutual(user)


def unfollow_single(user: User, username: str) -> None:
    """Helper method for unfollow() to unfollow a single user."""
    unflw = Unfollow(user)
    unflw.unfollow(username)


def unfollow_all(user: User) -> None:
    """Helper method for unfollow() to unfollow all users."""
    unflw = Unfollow(user)
    unflw.unfollow_all()


def unfollow_non_mutual(user: User) -> None:
    """Helper method for unfollow() to unfollow all users who don't follow
    <user> back."""
    unflw = Unfollow(user)
    unflw.unfollow_hollywood()


def remove_follower(user: User, username: str) -> None:
    """Remove <username> as a follower of <user>."""
    flw = Follow(user)
    flw.remove_follower(username)


if __name__ == "__main__":
    print("=" * 40)
    print(" " * 7 + "instatool by ashenafee")
    print("=" * 40)

    # Get user to login
    print("Login with your credentials...")
    input_username = input("Username:\t")
    input_password = input("Password:\t")
    print("=" * 40)

    print(f"Logging on as {input_username}...")
    ig_user = User(input_username, input_password)
    print(f"Successfully logged on as {input_username}!")
    print("=" * 40)

    # Main menu
    flag = True
    while flag:
        print("[1] Show users that don't follow you\n"
              "[2] Show users that you don't follow\n\n"
              "[3] Follow a specific user\n"
              "[4] Follow all followers back\n\n"
              "[5] Unfollow a specific user\n"
              "[6] Unfollow all users\n"
              "[7] Unfollow all non-reciprocating users\n\n"
              "[8] Remove a specific follower\n" + "-" * 40)
        choice = input("Choice (i.e. 1):\t")
        print("=" * 40)

        if choice == "1":
            show_hollywood(ig_user)
        elif choice == "2":
            show_non_mutual(ig_user)
        elif choice == "3":
            follow(ig_user, 1)
        elif choice == "4":
            follow(ig_user, 2)
        elif choice == "5":
            unfollow(ig_user, 1)
        elif choice == "6":
            unfollow(ig_user, 2)
        elif choice == "7":
            unfollow(ig_user, 3)
        elif choice == "8":
            to_unfollow = input("Username:\n")
            remove_follower(ig_user, to_unfollow)

        # Ask if user wants to exit
        print("=" * 40)
        choice = input("Return to main menu (Y/N)?\t")
        if choice.upper() != "Y":
            flag = False
            print("Exiting instatool...")
