import json
import requests
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'


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

    def get_mutual_friends(self, checking_user):
        params = self.get_params()
        params['source_uid'] = self.user_id
        params['target_uid'] = checking_user.user_id
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params=params
        )

        return response.json()['response']

    def __and__(self, other):
        mutual_users = self.get_mutual_friends(other)

        return [User(i) for i in mutual_users]

    def get_list_groups(self):
        """
        Метод возвращает список всех групп пользователя
        :return: list
        """
        params = self.get_params()
        params['extended'] = 1
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params=params
        )
        print('.', end='')

        return response.json()['response']['items']

    def get_group_members(self, group):
        """
        Метод возвращает список друзей в группе.
        :param group: id группы, в которой смотрим друзей
        :return: list
        """
        params = self.get_params()
        params['group_id'] = group
        params['filter'] = 'friends'
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params=params
        )
        print('.', end='')

        return response.json()['response']

    def find_solo_groups(self, groups):
        """
        Метод записывает формирует и записывает данные в json файл.
        :param groups:
        :return:
        """
        group_solo_list = []
        for group in groups:
            group_response = self.get_group_members(group['id'])

            if not group_response['items']:
                temp = {
                    'name': group['name'],
                    'gid': group['id'],
                    'members_count': group_response['count'],
                }

                group_solo_list.append(temp)

        with open('groups.json', 'w+t', encoding='utf-8') as f:
            json.dump(group_solo_list, f, ensure_ascii=False)


if __name__ == '__main__':
    # user1 = User('179741620')
    user = User('171691064')
    user.find_solo_groups(user.get_list_groups())
