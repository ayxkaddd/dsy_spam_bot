import os
import sys
import time
import random

from pyrogram import Client, filters

app = Client('my_account')

msg_list = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 56, 68]


@app.on_message(filters.command('spam', prefixes='$'))
def ebatMoskaliv(_, msg):
    global msg_list
    duration = msg.text.split(' ')[-1]
    try:
        while True:
            time.sleep(int(duration))
            msgId = random.choice(msg_list)
            app.forward_messages(
                chat_id = msg.chat.id,
                from_chat_id = -1001712265605,
                message_ids = int(msgId)
            )
            print(f'Done! msg sent to {msg.chat.title}')
    except Exception as ex:
        print(f'some exception - {ex}')

        
@app.on_message(filters.command('stop', prefixes='$'))
def stop(_, msg):
    print('ok stop\npress ctrl + z')
    sys.exit()
       

if __name__ == '__main__':
    app.run()
