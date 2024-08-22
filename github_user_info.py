import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    username = input("Enter the GitHub username: ")
    user_info = get_github_user_info(username)
    
    if user_info:
        print(f"Name: {user_info['name']}")
        print(f"Bio: {user_info['bio']}")
        print(f"Public Repositories: {user_info['public_repos']}")
        print(f"Followers: {user_info['followers']}")
        print(f"Following: {user_info['following']}")

if __name__ == "__main__":
    main()
