import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from rude_phrases import rude_phrases
from phrases import phrases
from nefor import nefor
from posledny_words import posledny_words

print("    █████╗ ███╗  ██╗ ██████╗ ███████╗██╗     ")
print("   ██╔══██╗████╗ ██║██╔════╝ ██╔════╝██║     ")
print("   ███████║██╔██╗██║██║  ██╗ █████╗  ██║     ")
print("   ██╔══██║██║╚████║██║  ╚██╗██╔══╝  ██║     ")
print("   ██║  ██║██║ ╚███║╚██████╔╝███████╗███████╗")
print("   ╚═╝  ╚═╝╚═╝  ╚══╝ ╚═════╝ ╚══════╝╚══════╝")
print("._____________________________________________.")
print("|                                             |")
print("|---------------->Здравствуйте<---------------|")
print("|---------------------------------------------|")
print("|---->Это бот ANGEL, работающий на vk_api<----|")
print("|---------------------------------------------|")
print("|--------------->Бот уже запущен<-------------|")
print("|---------------------------------------------|")
print("|----------->Приятного использования<---------|")
print("|---------------------------------------------|")
print("|------------------------------>dev. hervamto<|")
print("|_____________________________________________|")
print(" ")

# Здесь нужно указать свой токен ВКонтакте
token = 'токен'

vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)

def send_message(user_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # Если пришло новое сообщение и это текстовое сообщение
        user_id = event.user_id
        message = event.text.lower()  # Приводим текст к нижнему регистру для удобства обработки
        
        if message in phrases:
            send_message(user_id, phrases[message])
            print(f"Отправлен ответ на фразу: '{message}'")
        elif any(word in message for word in ['ахуела', 'ахуела?', 'бля', 'блять', 'блядь', 'сука', 'шлюха', 'шалава', 'собака', 'ебанная', 'ебливая', 'ебанутая', 'пидор', 'пидорас', 'гандон', 'уебан', 'крыса', 'шлюшка', 'шалашовка', 'блядина', 'нахуй', 'хуй', 'хуёво', 'пизда', 'пиздачок', 'пиздачёк', 'пиздачек', 'пиздец', 'хер', 'мать']):
            # Если обнаружено матерное слово, выбираем случайную фразу из списка rude_phrases)
            rude_response = random.choice(rude_phrases)
            send_message(user_id, rude_response)
            print(f"Мат:'{message}'")
        elif message == 'привет' or message == 'ку':
            random_greeting = random.choice(['привет😊', 'приветик❤️'])
            send_message(user_id, random_greeting)
            print(f"Приветствие")
        elif message == 'пока' or message == 'покеда' or message == 'споки' or message == 'до свидания':
            posledny_words_response = random.choice(posledny_words)
            send_message(user_id, posledny_words_response)
            print(f"Последние слова: '{message}'")
        elif any(word in message for word in ['димон', 'дима','hervamto']):
            random_greeting = random.choice(['э бля батю не трогай', 'оск разрбов, пизда тебе, тут feedback включен'])
            send_message(user_id, random_greeting)
            print(f"трогают разраба: '{message}' ")
        else:
            nefor_response = random.choice(nefor)
            send_message(user_id, nefor_response)
            #использование неформальных ответов файл nefor)
            print(f"Фраза не распознана: '{message}'") 


