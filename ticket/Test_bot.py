from rocketchat_API.rocketchat import RocketChat
from pprint import pprint
from random import randint
from time import sleep
import json

rocket = RocketChat('dolly', '1Seey0u', server_url="http://chat.anserglob.ua")
users_list = rocket.users_list().json()


def rocket_confirm(id,text,name):
    textMessage = "Ваша заявка #{}:\n \"{}\" - выполнена. Спасибки".format(id, text)
    copy = "Копия от {} ".format(name)
    for i in users_list["users"]:
        if name in i["name"]:
            username = i["username"]
            rocket.chat_post_message(textMessage, room_id="@"+username)
            rocket.chat_post_message(copy+textMessage, room_id="@"+"Mikhail.Zarechniy")
    return("done")

# class Rock:
#     def __init__(
#             self,
#             user = "dolly",
#             password = ""
#     ):
#         pass
