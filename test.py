import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('jego-972d19158581.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM')

sheet1 = doc.worksheet('시트1')
sheet2 = doc.worksheet('시트2')

client = discord.Client()



@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='업무외지원', type=1))




@client.event
async def on_message(message):
	global gc #정산
	global creds	#정산
    
#	if message.content.startswith('!재고'):
#		SearchID = message.content[len('!재고')+1:]
#		gc = gspread.authorize(creds)
#		wks = gc.open('오전재고').worksheet('시트1')
#		
#		wks.update_acell('A1', SearchID)
#		result = wks.acell('B1').value
 #           
#		embed = discord.Embed(
#			title = ' :calling:  ' + SearchID + ' 재고현황! ',
#			description= '```' + SearchID + ' 오전까지 내역입니다. ' + result + '실시간조회가 아니라서 다소 차이가 있을수 있습니다. ```',
#			color=0xff00ff
#			)
#		await client.send_message(message.channel, embed=embed)
 #           
#	if message.content.startswith('!모델명'):
#		SearchID = message.content[len('!모델명')+1:]
#		gc = gspread.authorize(creds)
#		wks = gc.open('오전재고').worksheet('시트2')
#		wks.update_acell('A1', SearchID)
#		result = wks.acell('B1').value
#		
#		embed = discord.Embed(
#			title = ' :printer:  모델명 코드 리스트 ',
#			description= '```' + SearchID + ' 모델명 코드는 ' + result + ' ```',
#			color=0x0000ff
#			)
#		await client.send_message(message.channel, embed=embed)



	if message.content.startswith('!주사위'):
		randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
		print(randomNum)
		if randomNum == 1:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
		if randomNum == 2:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
		if randomNum ==3:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
		if randomNum ==4:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
		if randomNum ==5:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
		if randomNum ==6:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))
			
			
			
			
	if message.content.startswith("!복권"):
		Text = ""
		number = [1, 2, 3, 4, 5, 6, 7]
		count = 0
		for i in range(0, 7):
			num = random.randrange(1, 46)
			number[i] = num
			if count >= 1:
				for i2 in range(0, i):
					if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
						numberText = number[i]
						print("작동 이전값 : " + str(numberText))
						number[i] = random.randrange(1, 46)
						numberText = number[i]
						print("작동 현재값 : " + str(numberText))
						if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
							numberText = number[i]
							print("작동 이전값 : " + str(numberText))
							number[i] = random.randrange(1, 46)
							numberText = number[i]
							print("작동 현재값 : " + str(numberText))
							if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
								numberText = number[i]
								print("작동 이전값 : " + str(numberText))
								number[i] = random.randrange(1, 46)
								numberText = number[i]
								print("작동 현재값 : " + str(numberText))

			count = count + 1
			Text = Text + "  " + str(number[i])
			
		print(Text.strip())
		embed = discord.Embed(
			title="복권 숫자!",
			description=Text.strip(),
			colour=discord.Color.red()
		)
		await client.send_message(message.channel, embed=embed)
			
			
access_token = os.environ["BOT_TOKEN"]
git_access_token = os.environ["GIT_TOKEN"]
client.run(access_token)
