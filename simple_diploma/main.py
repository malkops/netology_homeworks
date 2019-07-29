import json
import requests
import time
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

    def __and__(self, other):
        mutual_users = self.get_mutual_friends(other)

        return [User(i) for i in mutual_users]

    def get_params(self):
        return {
            'access_token': TOKEN,
            'v': '5.89',
            'user_id': self.user_id,
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

    def get_list_groups(self):
        """
        Метод возвращает список всех групп пользователя
        :return: list
        """
        params = self.get_params()
        params['extended'] = 1
        time.sleep(1)
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params=params
        )
        print('.', end='')

        try:
            response.json()['response']['items']
        except Exception:
            return set()
        return response.json()['response']['items']

    def get_group_members(self, group):
        """
        Метод возвращает список друзей в группе.
        :param group: id группы, в которой смотрим друзей
        :return: list
        """
        params = self.get_params()
        params['group_id'] = group
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params=params
        )
        print('.', end='')

        return response.json()['response']['count']

    def find_solo_groups(self, groups):
        """
        Метод записывает формирует и записывает данные в json файл.
        :param groups:
        :return:
        """
        user_groups = {x['id'] for x in groups}
        friends_list = set(self.get_list_friends())

        temp_friends_list = [User(x) for x in friends_list]
        all_groups = set()
        for user in temp_friends_list:
            friend_groups = {x['id'] for x in user.get_list_groups()}
            if friend_groups:
                all_groups.update(friend_groups)
        user_groups = user_groups.difference(all_groups)
        result = []
        for group in groups:
            group_id = group['id']
            if group_id in user_groups:
                members_count = self.get_group_members(group_id)
                temp = {
                    'name': group['name'],
                    'gid': group_id,
                    'members_count': members_count,
                }
                result.append(temp)

        with open('groups.json', 'w+t', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)


if __name__ == '__main__':
    user_id = input('Введите id пользователя: ')
    user = User(user_id)
    user.find_solo_groups(user.get_list_groups())
    print('\nJson записан в файл. На этом все :)')
