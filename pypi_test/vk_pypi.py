import vk


with open('token_vk.txt', 'r') as file:
    token_vk = file.readline()

user_info = vk.API(access_token=token_vk, v='5.131')


def get_info(user_ids):
    user_dict = {}
    for user in user_info.users.get(user_ids=user_ids):
        user_id, first_name, last_name, can_access_closed, is_closed = list(user.values())
        user_dict[user_id] = {'Имя': first_name, 'Фамилия': last_name}
    return user_dict
