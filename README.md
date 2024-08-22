import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print(f"Error for {username}: {response.status_code}")
        return None

def print_user_info(user_info):
    if user_info:
        print(f"Name: {user_info['name']}")
        print(f"Bio: {user_info['bio']}")
        print(f"Public Repositories: {user_info['public_repos']}")
        print(f"Followers: {user_info['followers']}")
        print(f"Following: {user_info['following']}")
        print()

def main():
    usernames = input("Enter GitHub usernames (separated by spaces): ").split()
    
    for username in usernames:
        user_info = get_github_user_info(username)
        print_user_info(user_info)

if __name__ == "__main__":
    main()
