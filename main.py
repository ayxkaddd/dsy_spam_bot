import os
import sys
import time
import random

import DiscordRPC

from pyrogram import Client, filters

app = Client('my_account')

msg_list = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 56, 68, 69]

rpc = DiscordRPC.RPC.Set_ID(app_id=971671418238541894)


button = DiscordRPC.button(
  button_one_label="GitHub",
  button_one_url="https://github.com/ayxkaddd/dsy_spam_bot",
  button_two_label="Telegram",
  button_two_url="https://t.me/likahqjq"
  )

@app.on_message(filters.command('spam', prefixes='$'))
def ebatMoskaliv(_, msg):
    global msg_list, button
    duration = msg.text.split(' ')[-1]
    count = 0
    try:
        while True:
            count += 1
            rpc.set_activity(
                  state="Козак спамить русні! Доєднуйся до ДСУ",
                  details=f"Повідомлень відправлено: {count}",
                  timestamp=rpc.timestamp(),
                  large_image="dsy_logo",
                  large_text="DsyBot",
                  buttons=button
                )
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
