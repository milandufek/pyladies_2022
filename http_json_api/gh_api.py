import requests


with open('token.txt') as file_:
    token = file_.read().strip()

headers = {'Authorization': 'token ' + token}

url_user = 'https://api.github.com/user'
# resp = requests.get(url_user)  # this fails on 401 response
resp = requests.get(url_user, headers=headers)
resp.raise_for_status()
# print(resp.text)
data = resp.json()
print(data)

#
## Method PUT
#

# start the repo
gh_api = requests.put('https://api.github.com/user/starred/milandufek/naucse-python', headers=headers)
gh_api.raise_for_status()

# CHeck the result here in web browser :)
#  https://github.com/milandufek/naucse-python/stargazers
