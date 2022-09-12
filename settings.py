import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# /////////////////////////////////////////#
#                                          #
#        Переменные основного файла        #
#                                          #
# /////////////////////////////////////////#
token = "vk1.a.XhvWy05wfLkLGd4eAC3B_i3eC3EKqlvaKmIiBboxow3jG9K5Z_NaM6NpTeBVPzsFQCOTstNQEIo-dI-9ZhwAkyCtS4IDRl75uAtf_zb6QDpbYZVNwVxx2I2TJpn70JnMehriSgEd9fU95MSDgKkdXAMXT3e09fP_dnL_s6oIdVCB8XhJPrftQFf8d8Yh-WBw"
bot_id = '215796895'
hello_text = "Привет,пользователь"
# /////////////////////////////////////////#
#                                          #
#   Регистрация бота в сети через логпул   #
# /////////////////////////////////////////#
vk_session = vk_api.VkApi(
    token=token)
longpoll = VkBotLongPoll(vk_session, bot_id)

