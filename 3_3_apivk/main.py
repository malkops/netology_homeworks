import requests
TOKEN = '1176b3bbc11d44465b442acfbe67a8bffb092ea05e6b661991e1721836180def2ab03dce65a4c3579fc37'


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

        return set(self.get_list_friends()) & set(response.json()['response'])

    def __and__(self, other):
        mutual_users = self.get_mutual_friends(other)

        return [User(i) for i in mutual_users]


user1 = User('179741620')
user2 = User('378209621')
for us in user1 & user2:
    print(us.user_id)
