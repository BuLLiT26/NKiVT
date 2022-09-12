import json
from requests_info import *
from settings import *


def main():
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)

    def send_message_for_user(user_id, message_send):
        vk_session.method(
            "messages.send", {
                "user_id": user_id,
                "message": message_send,
                "random_id": 0})

    def send_message_for_group(peer_id, message_send):
        vk_session.method(
            "messages.send", {
                "peer_id": peer_id,
                "message": message_send,
                "random_id": 0})

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.message.from_id
            peer_id = event.message.peer_id
            message_split = event.message.text.split()
            print(message_split)
            if event.from_chat:
                if message_split[0].lower() == "reg":
                    for first in response:
                        dateDay = time.ctime(int(first['date']))
                        groupID = first['groupId']
                        groupName = first['group']
                        sort = first['sort']
                        itemName = first['subject']
                        teacherName = first['teacher']
                        teacherId = first['teacherId']
                        classRoom = first['classroom']
                        Tue = 'Вторник'
                        Wed = 'Среда'
                        Thu = 'Четверг'
                        Fri = 'Пятница'
                        Sat = 'Суббота'
                        if dateDay.split()[0] == 'Tue':
                            text_message = ['{}*{}*{}*{}*{}'.format(sort + 1, itemName, Tue, teacherName, classRoom)]
                            for sender in text_message:
                                send_message_for_group(peer_id, sender)
                                break


if __name__ == '__main__':
    main()
