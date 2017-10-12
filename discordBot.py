import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

def add_to_file(nombre_archivo,item):
	if not os.path.isfile(nombre_archivo):
		list = []
	else:
		with open(nombre_archivo,"rb") as file:
			list = pickle.load(file)
	list.append(item)
	with open(nombre_archivo,"wb") as file:
		pickle.dump(list,file)
	
def remove_from_file(nombre_archivo,item):
	with open(nombre_archivo,"rb") as file:
		list = pickle.load(file)
	list.remove(item)
	with open(nombre_archivo,"wb") as file:
		pickle.dump(list,file)
		
def get_random(nombre_archivo):
	with open(nombre_archivo,"rb") as file:
		list = pickle.load(file)
	return random.choice(list)
	
def verified(id):
	if id == '145898789733924864':
		return True
	else:
		return False
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game = discord.Game(name = 'Paladins'))
	
@client.event
async def on_message(message):
	#hola
	if message.content.startswith('!hola'):
		await client.send_message(message.channel, 'hola we')
		
	#paladins
	
	elif message.content.startswith('paladins'):
		item = get_random("paladins.pk1")
		await client.send_message(message.channel, item)
		
	elif message.content.startswith('!addpaladins'):
		if verified(message.author.id) == True:
			add_to_file("paladins.pk1",message.content[12:])
			await client.send_message(message.channel, 'ok.')
			
	elif message.content.startswith('!deletepaladins'):
		if verified(message.author.id) == True:
			remove_from_file("paladins.pk1",message.content[15:])
			await client.send_message(message.channel, 'chaufa')
			
	#chicken dinner
	elif message.content.startswith('!addchicken'):
		if verified(message.author.id) == True:
			add_to_file("chicken.pk1",message.content[11:])
			await client.send_message(message.channel, 'ok.')
			
	elif message.content.startswith('chicken dinner'):
		item = get_random("chicken.pk1")
		await client.send_message(message.channel,item)
		
	elif message.content.startswith('!deletechicken'):
		if verified(message.author.id) == True:
			remove_from_file("chicken.pk1",message.content[14:])
			await client.send_message(message.channel, 'chaufa')
	
	#esports ready
	elif message.content.startswith('!addesportsready'):
		if verified(message.author.id) == True:
			add_to_file("esports_ready.pk1",message.content[16:])
			await client.send_message(message.channel, 'E S P O R T S R E A D Y')
			
	elif message.content.startswith('esports ready'):
		item = get_random("esports_ready.pk1")
		await client.send_message(message.channel,item)
		await client.send_message(message.channel,'E S P O R T S R E A D Y')
		
	elif message.content.startswith('!deleteesportsready'):
		if verified(message.author.id) == True:
			remove_from_file("esports_ready.pk1",message.content[19:])
			await client.send_message(message.channel, 'chaufa')
	
	#nani
	elif message.content.startswith('!addnani'):
		if verified(message.author.id) == True:
			add_to_file("nani.pk1",message.content[8:])
			await client.send_message(message.channel, 'ok')
			
	elif message.content.startswith('nani'):
		item = get_random("nani.pk1")
		await client.send_message(message.channel,item)
		await client.send_message(message.channel,'O M A E W A M O U S H I N D E I R U')
		
	elif message.content.startswith('!deletenani'):
		if verified(message.author.id) == True:
			remove_from_file("nani.pk1",message.content[11:])
			await client.send_message(message.channel, 'chaufa')
	#party hard
	elif message.content.startswith('!addpartyhard'):
		if verified(message.author.id) == True:
			add_to_file("partyhard.pk1",message.content[13:])
			await client.send_message(message.channel, 'ok')
			
	elif message.content.startswith('party hard'):
		item = get_random("partyhard.pk1")
		await client.send_message(message.channel,item)
		await client.send_message(message.channel,'P A R T Y H A R D')
		
	elif message.content.startswith('!deletepartyhard'):
		if verified(message.author.id) == True:
			remove_from_file("partyhard.pk1",message.content[16:])
			await client.send_message(message.channel, 'chaufa')
	elif message.content.startswith('pan'):
		await client.send_message(message.channel, 'https://images-na.ssl-images-amazon.com/images/I/71mpDDga9PL._SL1072_.jpg')
	#commandos
	elif message.content.startswith('!comandos'):
		mensaje = ("```" + 
				  '!hola' + '\n' +
				  'paladins' + '\n' +
				  'chicken dinner' + '\n' +
				  'esports ready' + '\n' +
				  '```')
					
		await client.send_message(message.channel, mensaje)
client.run('MzY3NzQ4MDM2MTA3MDQyODE4.DL_7mg.hYAdIyOFWRurU0o_xWhfK5pR9IE')
