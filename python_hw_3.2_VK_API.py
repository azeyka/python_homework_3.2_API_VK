# APP_ID = 6784328
# https://oauth.vk.com/authorize?client_id=6784328&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52
import requests


class User():

  def __init__(self, token, id):
    self.token = token
    self.id = id

  def Get_friends_list(self):
    params = {
      'user_id': self.id,
      'order': 'name',
      'fields': 'domain',
      'access_token': self.token,
      'v': '5.92'
    }
    response = requests.get('https://api.vk.com/method/friends.get',
                            params)

    return response.json()['response']['items']

  def __and__(self, compared_user):
    user_friends = self.Get_friends_list()
    compared_user_friends = compared_user.Get_friends_list()
    mutual_friends = []
    for friend in user_friends:
      if friend in compared_user_friends:
        friend = User(self.token, friend['id'])
        mutual_friends.append(friend)

    return mutual_friends

  def __str__(self):
    params = {
      'access_token': self.token,
      'user_ids': self.id,
      'fields': 'domain',
      'v': '5.92'
    }
    response = requests.get('https://api.vk.com/method/users.get',
                            params)

    return 'https://vk.com/' + response.json()['response'][0]['domain']

token = '88058fabc35d443ad9f365bfd068b6ccdeb703237c32bfb81153716a3831625a34b8c7d2ed7a8efea3aa0'

user1 = User(token, 37906069)
user2 = User(token, 85228780)

mutual_friends = user1 & user2
print('Общие друзья ({}):'.format(len(mutual_friends)))
for friend in mutual_friends:
  print(friend)
