import discord
import datetime
from keep_alive import keep_alive
import os 
import sqlite3
from sql import *
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":


    print(datetime.datetime.now())
    print("Version:",discord.__version__)
    client = discord.Client()
    #PYTHONASYNCIODEBUG=0

    #*****Character/Word Moderator app
    prohibited_words=[]
    def mod_scan(message):
      for x in message.content():
        if x in prohibited_words:
          return True
          #modlog infraction & msg to user
        else:
          return False


    #*************D I S C O R D***************
    @client.event
    async def on_ready():
      print("***********DISCORD MODERATOR APP*************")
      print("Active Bot: {}".format(client.user))
      print("Guild ID:",str(client.guilds).split()[1].replace("id=",""))

      for guild in client.guilds:
        print("Guild Name:",guild)
      
      print("--Channels Available:--","*******************",sep="\n")
      for channel in guild.channels:
          print(channel)
      
      #AUTHDATABASE
      try:

        print(count(Database,Table,"USER"))
        [print(x) for x in display(Database,Table)]
        print("Database {} and Table {} exist".format(Database,Table))
        
      except:
        create_table(Database,Table)
        print("Created new database {} and table {}".format(Database,Table))
      #LOGDATABASE  
      try:
        print(count(Database,"LOG","DATE"))
        [print(x) for x in display(Database,"LOG")]
        log_insert(Database, "LOG")
      except:
        create_log(Database,"LOG")
        print("Created new database {} and table {}".format(Database,"LOG"))
    @client.event
    async def on_member_join(member):
      print("Member Joined")
      print(member.bot)
      await member.send("Thanks for joining, welcome to our Community! Please introduce yourself on the Introductions Channel to gain access to post!")


    @client.event
    async def on_member_remove(member):

      await member.send("We appreciate your contributions to our community!")
      print(f"A member has left: {member}")
      

    #sends dm to author
    @client.event
    async def on_message(message):  
      if message.author != client.user:
        print(f"Message Channel:****{message.channel}****", message.channel.id)
        print("GUILD:",message.guild)
        #print("Guild Channels", message.guild.channels )
        print("AUTHOR:",message.author)
        print("CONTENT:",message.content,"length",len(message.content))
        #print("Mentions:",message.mentions,message.channel_mentions,message.raw_channel_mentions)
        await message.author.send ("Test")
        #await message.channel.send("BOTtest")
        #await message.channel.purge(limit=100)
        print(message.channel.id)
        if str(message.channel.id) == "661365410674769939" and len(message.content)>10:
            insert_data(Database,Table,message.author)
            print("Inserted Table Entry")
            await message.author.send("We appreciate you introducing yourself! Feel free to actively contribute to our community!")
        else:
          print("_----_-")
          if authscan(Database,Table,message.author):
            pass
          else:
            await message.author.send("In order to post within our Discord, please introduce yourself first in Introductions! Thank you!")
            await message.delete()
            print("Message Deleted, User has not introduced themselves")
          
           
    #channel = discord.utils.get(message.guild.channels, id=message.channel.id)
    #await channel.send("test")

    #********************************************

    #Establish Database



    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Database.db")
    with sqlite3.connect(db_path) as db:
      pass




    keep_alive()
    token = os.environ.get("bot_secret")
    client.run(token)

    search(Database,Table)