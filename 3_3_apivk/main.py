import requests
TOKEN = 'a6fc08e9317c3e0ac6a14aef0025704f3398c53f906a6038028825742d23a09745dcfb74942be220141b0'


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params=params
        )

        return f"https://vk.com/{response.json()['response'][0]['id']}"

    def get_params(self):
        return {
            'access_token': TOKEN,
            'v': '5.89',
            'user_ids': self.user_id,
        }

    def get_list_friends(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params=params
        )

        return response.json()['response']['items']

    def get_mutual_friends(self, user):
        params = self.get_params()
        params['source_uid'] = self.user_id
        params['target_uid'] = user.user_id
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params=params
        )

        return response.json()['response']

    def __and__(self, other):
        mutual_users = self.get_mutual_friends(other)

        return [User(i) for i in mutual_users]


if __name__ == '__main__':
    user1 = User('179741620')
    user2 = User('378209621')
    mutual = user1 & user2
    for us in mutual:
        print(us.user_id)
