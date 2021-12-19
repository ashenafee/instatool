if __name__ == "__main__":
    from instagram_private_api import Client
    import followers as f
    import unfollow as uf

    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    api = Client(user_name, password)
    user = api.user_feed(user_id=api.authenticated_user_id, max_id=None)

    # Create the list of followers
    f.followers_to_txt(api=api)
    followers = f.followers_to_lst()

    # Create the list of following
    f.following_to_txt(api=api)
    following = f.following_to_lst()

    # Create the list of dnf
    f.does_not_follow(following, followers)
    dnf = f.dnf_to_lst()

    # Create the list of dnf ids
    dnf_ids = uf.dnf_to_ids(api=api, dnf_list=dnf)

    # Unfollow the dnf
    uf.unfollow(api, dnf_ids)
    print("Unfollowed every user in dnf.txt")