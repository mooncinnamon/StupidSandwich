import discord
import asyncio
import requests
import threading
from bs4 import BeautifulSoup

client = discord.Client()
url = 'https://bglog.me/server/'
value = 3
loading_time = 60

type1 = 'icon-circle s1'
type2 = 'icon-circle s2'
type3 = 'icon-circle s3'


@asyncio.coroutine
def bs4store():
    global value

    code = requests.get(url)
    plain_text = code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    text = soup.select('body > div.i-container > div.server.box > i')
    text2 = soup.select('body > div.i-container > div.online.box')
    out = text2[0].find('span').text

    print(out.encode('euc-kr'))
    outtext = str(text[0])

    if(outtext.find(type1)):
        value = 0
    elif(outtext.find(type2)):
        value = 1
    elif(outtext.find(type3)):
        value = 2
 
    yield from asyncio.sleep(loading_time) 
    asyncio.async(bs4store())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    try:
        print('start parsing infi loop!')
        loop_store = asyncio.get_event_loop()
        loop_store.create_task(bs4store())
#        loop_store.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print('step: loop.close()')
#        loop_store.close()

@client.event
async def on_message(message):
    msg = message.content.replace("<@"+client.user.id+"> ","")    

    if msg.startswith('!sandwich'):

        if(value == 0):
            text = 'Great Sandwich!'
        elif(value == 1):
            text = 'SoSo Sandwich!'
        elif(value == 2):
            text = 'Fuck Sandwich!'
        elif(value == 3):
            text = 'Store is Close!'

        await client.send_message(message.channel, text)

def main():
    client.run('Mzg3MjE3ODI1OTUwODU5Mjg0.DQb-TA.7THd8Op7iyIxp24A5Ff1qeGhDKs')

if __name__ == "__main__":
    main()
