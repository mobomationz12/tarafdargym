from requests import get
from re import findall
import os
import json
import glob
from rubika.client import Bot
from requests import post
import requests
from rubika.tools import Tools
from rubika.encryption import encryption
from gtts import gTTS
from mutagen.mp3 import MP3
import time
import random
import urllib
import io
from random import choice
from re import findall
from random import randint
from re import findall
from requests import get
from json import load , dump
import time
import random
import glob
from PIL import Image
 
bot = Bot("AppName", auth="tnuqjhohmjbzmmruqdcvdxefxztxcmui")
 
target = "g0uia80bb4208009b4e5f79897f60387"

channell = "c0zJzy0e2c6e5793fd68f54ec777cda4"

chat = "u"

bot.sendMessage(target, "MoboBot Satarted Now✅😌")


def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me","@","1.2.3.4","rubika.ir","rubika"]
	for i in links:
		if i in msg:
			return True
			
def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData
	
# static variable
answered, sleeped, retries = [], False, {}

alerts, blacklist = [] , []

def alert(guid,user,link=False):
	alerts.append(guid)
	coun = int(alerts.count(guid))

	hasInsult = "فحش ممنوع میباشد!!!\n\n"
	if link : haslink = "گزاشتن لینک در گروه ممنوع میباشد .\n\n"

	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (1/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (2/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")

	elif coun == 3:
		blacklist.append(guid)
		bot.sendMessage(target, "🚫 کاربر [ @"+user+" ] \n (3/3) اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .")
		bot.banGroupMember(target, guid)
		bot.sendMessage(msg.get("author_object_guid"),"متاسفانه شما بدلیل تبلیغات از گروه حذف شدید\nباید قوانین گروه را مطالعه می کردید❗️")

while True:
	# time.sleep(15)
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		for msg in messages:
			try:
				if msg["type"]=="Text" and not msg.get("message_id") in answered:
					if not sleeped:
						if hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
							guid = msg.get("author_object_guid")
							user = bot.getUserInfo(guid)["data"]["user"]["username"]
							bot.deleteMessages(target, [msg.get("message_id")])
							alert(guid,user,True)
							
						elif msg.get("text") == "ربات خاموش شو" or msg.get("text") == "!stop" and msg.get("author_object_guid") in admins :
							try:
								sleeped = True
								bot.sendMessage(target, "✅ ربات اکنون خاموش است", message_id=msg.get("message_id"))
							except:
								print("err off bot")
								
						elif msg.get("text") == "!restart" or msg.get("text") == "/restart" and msg.get("author_object_guid") in admins :
							try:
								sleeped = True
								bot.sendMessage(target, "خوب بزار خودمو تعمیر کنم.....🔧🔨", message_id=msg.get("message_id"))
								sleeped = False
								ans = ["با موفقیت دیباگ شدم✅","ربات با موفقیت ریستارت شد😃😸","MoboBot Has Restarted","بارگزاری مجدد با موفقیت انجام شد🎉😚","ربات روان تر و بهتر اجرا میشود 🔥"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err Restart bot")

										
						elif msg.get("text").startswith("حذف") and msg.get("author_object_guid") in admins :
							try:
								number = int(msg.get("text").split(" ")[1])
								answered.reverse()
								bot.deleteMessages(target, answered[0:number])

								bot.sendMessage(target, "✅ "+ str(number) +" پیام اخیر با موفقیت حذف شد", message_id=msg.get("message_id"))
								answered.reverse()

							except IndexError:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "✅ پیام با موفقیت حذف شد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text").startswith("!sargarmi"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "بخش سرگرمی موبوبات😜\n\n-۱🥵!jorat : رندوم یه جرعت حقیقت میده\n\n-۲🤗!dialog : دیالوگ ماندگار\n\n-۳🤫!dastan : داستان های طنز و جالب\n\n-۴😇!hadis : حدیث و سخنان پیامبران \n\n-۵🥲!alaki_masalan : جوک های الکی مثلا\n\n-۶🥳!khatere  : خاطره \n\n-۷😕!pa_na_pa : جوک های پ ن پ\n\n-۸🤲!zekr : ذکر ایام هفته\n\n-9🚶‍♂!bio : بیوگرافی\n\n-10🤔!danestani : ارسال عکس دانستنی\n\n-11🤣!jok : جوک بامزه\n\n-12📜!sher : شعر\n\n-13😃!ghazal : غزل حافظ\n\n\n\n🤖ربات اختصاصی موبومیشن🤖").text
								bot.sendMessage(target, ") ارسال شد✅", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "ارسال شد✅", message_id=msg.get("message_id"))												

						elif msg.get("text").startswith("!karbordi"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "بخش کاربردی موبوبات🥺🎉\n\n-۱💰!arz : دریافت لحظه ای قیمت ارز\n\n-۲🔮!tabir : تعبیر خواب شما\n\n-۳📿!chistan : آن چیست که چیستان است\n\n-۴💷!gold : قیمت طلا\n\n-۵⏰!time : ساعت\n\n-۶📆!date : تاریخ(میلادی)\n\n-۷🗣!speak : تبدیل متن به فایل صوتی\n\n-۸📝!trans : مترجم کلمات انگلیسی\n\n-۹📥!add : اضافه کردن عضو به گروه\n\n-۱۰📤!link : دعوت دوست به گروه\n\n-۱۱🖼!weather : دریاف اب و هوای منطقه شما\n\n-۱۲💌!send :  ارسال پیام ناشناس\n\n-۱۳📦!chanell : اضافه کردن عضو به کانال\n\n-۱۴🕹!game : لیستی از بازی های تفننی و مهیج\n\n-۱۵😌!name_good : نام شاخ\n\n-۱۶😀!minecraft : مبهم ماینکرافت\n\n-۱۷🎉!ping گرفتن پینگ سایت\n\n-۱۸🖼!shot گرفت شات از متن با ریپلای روی آن\n\n\n\n🤖ربات اختصاصی موبومیشن").text
								bot.sendMessage(target, ") ارسال شد✅", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "ارسال شد✅", message_id=msg.get("message_id"))
								
						elif msg.get("text").startswith("!modiriat"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "بخش مدیریت موبوبات🔥\n\n\n-۱📱!stop : خاموش کردن موبوبات\n\n-۲📲!start : روشن کردن موبوبات\n\n-۳🔒!lock : قفل گروه\n\n-۴🔓!unlock : بازکردن گروه\n\n-۵🔐!ban : حذف عضو از گروه\n\n-۶📍!pin : سنجاق پیام \n\n-۷📌!unpin : برداشتن سنجاق\n\n-۸✂️!del : پاک کردن پیام به تعداد مشخص\n\n-۹📔!join : عضو شدن ربات در گروه های دیگه\n\n-۱۰♋️!post : ارسال پیامی خاص به کانال موبومیشن\n\n-۱۱🚷!user : گرفتن اطلاعات کاربر\n\n-۱۲💢!alter اخطار به کاربر\n\n-۱۳📝!learn : یادبگیر ربات\n\n-۱۴📉!admin افزودن ادمین\n\n-۱۵📈!leave_admin حذف ادمین\n\n-۱۶⛓!tab_on تبلیغات و سین زن\n\n-۱۷💡!start_cal : شروع ویسکال\n\n-۱۸🛌!finish_cal : اتمام ویسکال\n\n-۱۹🪄!azad : آزاد کردن کاربر از لیست‌سیاه\n\n\n\n🤖ربات اختصاصی موبومیشن").text
								bot.sendMessage(target, ") ارسال شد✅", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "ارسال شد✅", message_id=msg.get("message_id"))																																			

						elif msg.get("text").startswith("دستورات"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌لیست‌دستورات‌موبوبات😜👇\n\n\nسرگرمی✨(جوک😂،حدیث‌🔥و‌.....)\n!sargarmi‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌\n\nکاربردی🔩(بگو🗣،دعوت📨و....)\n!karbordi‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌\n\nمدیریت🔊(دسترسی‌ادمین‌هاو....)\n!modiriat\n\n\nموفق باشید✨.").text
								bot.sendMessage(target, ") ارسال شد✅", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "ارسال شد✅", message_id=msg.get("message_id"))
								
						elif msg.get("text").startswith("!ban") and msg.get("author_object_guid") in admins :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									bot.banGroupMember(target, guid)
									# bot.sendMessage(target, "✅ کاربر با موفقیت از گروه اخراج شد", message_id=msg.get("message_id"))
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
									
							except IndexError:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, "✅ کاربر با موفقیت از گروه اخراج شد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))

						elif msg.get("text").startswith("رل") or msg.get("text").startswith("رل میخوام") or msg.get("text").startswith("رل می خوام") or msg.get("text").startswith("رل پی"):
							try:
								bot.sendMessage(target, "اینجا هرزه خونه نیست بیشعور😒💔 ", message_id=msg.get("message_id"))
							except:
								print("err he")
								
						elif msg.get("text").startswith("😋") or msg.get("text").startswith("😛") or msg.get("text").startswith("😝") or msg.get("text").startswith("😜") or msg.get("text").startswith("🤪"):
							try:
								bot.sendMessage(target, "زبونتو بکن تو عه🙄👿", message_id=msg.get("message_id"))
							except:
								print("err answer zabon")

						elif msg.get("text").startswith("😘") or msg.get("text").startswith("😍"):
							try:
								bot.sendMessage(target, "زود فامیل میشیا🤫", message_id=msg.get("message_id"))
							except:
								print("err ghalb")

						elif msg.get("text").startswith("ادمین جون") or msg.get("text").startswith("mohamad"):
							try:
								bot.sendMessage(target, "بابایی دارن صدات میکنن😁🙂", message_id=msg.get("message_id"))
							except:
								print("err bone")
								
						elif msg["text"] == "قفل گیف" or msg["text"] == "/gif_lock":
								gif_lock = True
								bot.sendMessage(target, "✅ قفل گیف و استیکر فعال شد .", msg["message_id"])

						elif msg.get("text").startswith("زر نزن") or msg.get("text").startswith("زر"):
							try:
								bot.sendMessage(target, "😁💋رژ بزن", message_id=msg.get("message_id"))
							except:
								print("err answer hay")

						elif msg.get("text").startswith("فدات") or msg.get("text").startswith("فداتم"):
							try:
								bot.sendMessage(target, "نشی جیگر😻💖", message_id=msg.get("message_id"))
							except:
								print("err fadat")

						elif msg.get("text").startswith("☹️") or msg.get("text").startswith("🙁") or msg.get("text").startswith("😕"):
							try:
								bot.sendMessage(target, "بغض نکن دیگه😰 بخند", message_id=msg.get("message_id"))
							except:
								print("err akhm")

						elif msg.get("text") == ".":
							try:
								bot.sendMessage(target, "به بابات بگو برات نت بخره😂🤣💔🖤", message_id=msg.get("message_id"))
							except:
								print("error net")		
								 

						elif msg.get("text").startswith("عکس بفرست"):
							try:
								f = open('/storage/emulated/0/mytobot/now.png')
								p = Image.open('now.png')
								bot.sendPhoto(target, 'now.png', p.size,message_id=msg["message_id"])
							except:
								print("err send image")

						elif msg.get("text").startswith("شات"):
							try:
						            if msg.get('reply_to_message_id') != None:
							            msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
							            if msg_reply_info['text'] != None:
								            text = msg_reply_info['text']
								            res = get('https://api.otherapi.tk/carbon?type=create&code=' + text + '&theme=vscode')
								            if res.status_code == 200 and res.content != b'':
									            b2 = res.content
									            print('get the image')
									            f = open('image.jpg','wb')
									            f.write(b2)
									            f.close()
									            p = Image.open('image.jpg')
									            bot.sendPhoto(target, 'image.jpg', p.size,message_id=msg.get("message_id"))
								            else:
									            bot.sendMessage(target, 'ارتباط با سرور ناموفق',message_id=msg.get("message_id"))
							            else:
								            bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg.get("message_id"))
						            else:
							            bot.sendMessage(target, 'لطفا روی یک پیام ریپلای بزنید',message_id=msg.get("message_id"))
							except:
								print("err unpin")
								 
						elif msg.get("text").startswith("!chanell"):
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										blacklist.remove(guid)
										bot.inviteChannel(channell, [guid])
										bot.sendMessage(target, "✅ کاربر مورد نظر با موفقیت به کانال افزوده شد", message_id=msg.get("message_id"))
									else:
										bot.sendMessage(target, "❌ کاربر محدود میباشد", message_id=msg.get("message_id"))
								else:
									bot.inviteChannel(channell, [guid])
									bot.sendMessage(target, "✅ کاربر مورد نظر با موفقیت به کانال افزوده شد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "دستور رو اشتباه میزنی🚫😶", message_id=msg.get("message_id"))



						elif msg.get("text").startswith("!add") or msg.get("text").startswith("عضو") :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										alerts.remove(guid)
										alerts.remove(guid)
										alerts.remove(guid)
										blacklist.remove(guid)

										bot.invite(target, [guid])
									else:
										bot.sendMessage(target, "❌ کاربر محدود میباشد", message_id=msg.get("message_id"))
								else:
									bot.invite(target, [guid])
									bot.sendMessage(target, "✅ کاربر اکنون عضو گروه است", message_id=msg.get("message_id"))	
							except:
								bot.sendMessage(target, "دستور رو اشتباه میزنی🚫😶", message_id=msg.get("message_id"))
								
						elif msg.get("text").startswith("!del_alert") or msg.get("text").startswith("!حذف اخطار") :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										alerts.remove(guid)
										alerts.remove(guid)
										alerts.remove(guid)
								bot.alerts.remove(target, [guid])
								bot.sendMessage(target, "✅ اطلاعات اخطار پاک شد ", message_id=msg.get("message_id"))

							except IndexError:
								bot.sendMessage(target, "دستور رو درست بزن 🤌😶", message_id=msg.get("message_id"))
							
							except:
								bot.sendMessage(target, "دستور رو اشتباه میزنی🚫😶", message_id=msg.get("message_id"))
												
						elif msg.get("text") == "!info":
							try:
								rules = open("help.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
					
						elif msg.get("text").startswith("بوسم کن") or msg.get("text").startswith("بوس بده"):
							try:
								bot.sendMessage(target, "💋🙈", message_id=msg.get("message_id"))
							except:
								print("err bose")
											 
						elif msg.get("text").startswith("آپدیت دستورات") and msg.get("author_object_guid") in admins:
							try:
								rules = open("help.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت قوانین")))
								bot.sendMessage(target, "دستورات ربات جدید تر و بروز تر شد :)♡", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))
						
						elif msg.get("text") == "متحدین":
							try:
								rules = open("motahed.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("\N{bird}")
						
						elif msg["text"].startswith("!join") or msg["text"].startswith("!joining"):
							try:
								text = str(msg["text"].replace("!join","").replace("!joining",""))

								bot.joinGroup(str(text))
								bot.sendMessage(target,"در گروه "+str(text)+ " شدم", message_id=msg.get("message_id"))

							except:
								print("err poker answer")
										 								 	 								 
						
						elif msg.get("text").startswith("!link") :
								bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "هلو مای فرند 😸👋\n\nببخشید که اومدم پیویت 😿🙌\nخواستم دعوتت کنم به موبومیشن کوچیک ترین رسانه #فیلم | #انیمیشن | #انیمه و کلی چیزای دیگه\nلطفا عضو کانالمون شو و خوشحالمون کن 😍👇❤️\n@mobomation\n\n\nدر ضمن اگر حوصلت سر رفته و تنهایی میتوتی با عضو شدن تو گپ اختصاصی موبومیشن دوستای جدید پیدا کنی😍👇\nhttps://rubika.ir/joing/BIJIHEAD0CUSNMTJDQRZQIVXDQRCPUKJ"+" ".join(msg.get("text").split(" ")[2:]))
								bot.sendMessage(target, "کاربر با موفقیت به گروه دعوت شد 😍🙌", 
message_id=msg.get("message_id"))
							
						elif msg.get("text") == "تنوع غذا":
							try:
								bot.sendMessage(target, "بستنی با چایی")
								bot.sendMessage(target, "چایی با شیرینی")
								bot.sendMessage(target, "شیرینی خامه ای")
								bot.sendMessage(target, "قهوه و شیرینی")
								bot.sendMessage(target, "قهوه بستنی")
								bot.sendMessage(target, "اب")
								bot.sendMessage(target, "‌‍‍‌‍‍‌🩸💥و در اخر مرگ!💥🩸")
							except:
								print("err poker answer")
										 								 	 								 
						elif msg.get("text").startswith("آپدیت متحدین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("motahed.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت متحدین")))
								bot.sendMessage(target, "متحدین ربات جدید تر و بروز تر شد :)♡", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))
						
						elif msg.get("text") == "ادمین":
							try:
								rules = open("admin.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								 
						elif msg.get("text").startswith("آپدیت ادمین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("admin.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت ادمین")))
								bot.sendMessage(target, "لیست ادمین ها جدید تر شدن♡", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))
						
						elif msg.get("text").startswith("یادبگیر") and msg.get("author_object_guid") in admins:
							try:
								data = msg.get("text").split("\n")
								f = open("learn.json","w",encoding="utf")
								f.write(str(data[1] + "|=|" + data[2] + "|/|" + "\n" ))
								f.close()
								bot.sendMessage(target, "آها یاد گرفتم✅", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))
								
						elif msg.get("text") == "درباره":
							try:
								rules = open("tozihat.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
							
						elif msg.get("text") == "!help":
							try:
								rules = open("grop.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								 
						elif msg.get("text").startswith("آپدیت گروه") and msg.get("author_object_guid") in admins:
							try:
								rules = open("grop.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت گروه")))
								bot.sendMessage(target, "کمک گروه ربات جدید تر و بروز تر شد :)♡", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))
									 
						elif msg.get("text") == "توضیحات":
							try:
								rules = open("tozihat.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
							
						elif msg.get("text").startswith("!send @") and msg.get("author_object_guid") in admins:
							try:
								bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "💬 شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
								bot.sendMessage(target, "پیام ارسال شد ✅", message_id=msg.get("message_id"))
							except:
								print("err send")		
										
						elif msg.get("text").startswith("آپدیت توضیحات") and msg.get("author_object_guid") in admins:
							try:
								rules = open("tozihat.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت")))
								bot.sendMessage(target, "توضیحات ربات جدید تر و بروز تر شد :)♡", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))	
				    
						elif msg.get("text") == "بروزرسانی":
							try:
								rules = open("berozresani.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								 
						elif msg.get("text").startswith("آپدیت بروزرسانی") and msg.get("author_object_guid") in admins:
							try:
								rules = open("berozresani.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت")))
								bot.sendMessage(target, "بروزرسانی ربات جدید تر و بروز تر شد :)♡", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))				        	 			   			 			
						elif msg["text"].startswith("!number") or msg["text"].startswith("!number"):
							try:
								response = get(f"http://api.codebazan.ir/adad/?text={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
							
						elif msg.get("text") == "!time":
							try:
								bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))
							except:
								print("err time answer")
						
						elif msg.get("text").startswith("!game") or msg.get("text").startswith("بازی"):
							try:
								bot.sendMessage(target, " به بخش بازی و سرگرمی خوش امدید 😍🎉8\n اکشن \n ورزشی \n پرتحرک \n پازل \n را وارد کنید", message_id=msg.get("message_id"))
							except:
								print("err bone")

						elif msg.get("text").startswith("پازل"):
							try:
								bot.sendMessage(target, "🏮-بخش پازل \n • پازل بلاکی \n ➖ https://b2n.ir/MC_rBOT5 \n • ساحل پاپ \n ➖ https://b2n.ir/MC_rBOT14 \n • جمع اعداد \n ➖ https://b2n.ir/MC_rBOT15 \n 🔴 راهنمایی: یکی از لینک ها را انتخاب کرده و کلیک کنید ؛ گزینه PLAY رو بزنید", message_id=msg.get("message_id"))
							except:
								print("err bone")

						elif msg.get("text").startswith("پر تحرک") or msg.get("text").startswith("پرتحرک"):
							try:
								bot.sendMessage(target, "💥- بخش پرتحرک \n • گربه دیوانه  \n ➖ https://b2n.ir/MC_rBOT4 \n • ماهی بادکنکی \n ➖ https://b2n.ir/MC_rBOT13 \n • دینگ دانگ \n ➖ https://b2n.ir/MC_rBOT12 \n 🔴 راهنمایی: یکی از لینک ها را انتخاب کرده و کلیک کنید ؛ گزینه PLAY رو بزنید", message_id=msg.get("message_id"))
							except:
								print("err bone")

						elif msg.get("text").startswith("اکشن"):
							try:
								bot.sendMessage(target, "- بخش اکشن \n • نینجای جاذبه  \n ➖ https://b2n.ir/MC_rBOT3 \n • رانندگی کن یا بمیر \n ➖ https://b2n.ir/MC_rBOT9 \n • کونگ فو \n ➖ https://b2n.ir/MC_rBOT11 \n 🔴 راهنمایی: یکی از لینک ها را انتخاب کرده و کلیک کنید ؛ گزینه PLAY رو بزنید", message_id=msg.get("message_id"))
							except:
								print("err bone")

						elif msg.get("text").startswith("ورزشی"):
							try:
								bot.sendMessage(target, "🏀- بخش ورزشی  \n • فوتبال استار  \n ➖ https://b2n.ir/MC_rBOT2 \n • بسکتبال \n ➖ https://b2n.ir/MC_rBOT24 \n • پادشاه شوت کننده \n ➖ https://b2n.ir/MC_rBOT255 \n 🔴 راهنمایی: یکی از لینک ها را انتخاب کرده و کلیک کنید ؛ گزینه PLAY رو بزنید", message_id=msg.get("message_id"))
							except:
								print("err bone")		 		 
						elif msg.get("text").startswith("نسخه") or msg.get("text").startswith("/noskh") or msg.get("text").startswith("!noskh") or msg.get("text").startswith("\noskh"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "1⃣• نسخه 0.1.1 \n https://rubika.ir/MineShine_APK/BJJEAHGJDCJFGEG \n 2⃣• نسخه 0.2.0 \n https://rubika.ir/MineShine_APK/BJJEBFGJGDDIGEG \n 3⃣• نسخه 0.6.0 \n https://rubika.ir/MineShine_APK/BJJEDFHAGABGGEG \n 4⃣• نسخه 0.9.1 \n https://rubika.ir/MineShine_APK/BJJEDFHAGABGGEG \n 5⃣•نسخه 0.13.0 \n https://rubika.ir/MineShine_APK/BJJEEEHBADBIGEG \n 6⃣• نسخه 0.13.2  \n https://rubika.ir/MineShine_APK/BJJEEHHBBHDEGEG \n 7⃣• نسخه 1.2.7  \nhttps://rubika.ir/MineShine_APK/BJJIGJJGACBCGEG \n 8⃣• نسخه 1.8.0 \n https://rubika.ir/MineShine_APK/CAAJJJFBDBHHGEG \n 9⃣• نسخه 1.10.0 \n https://rubika.ir/MineShine_APK/CABEIHHIIHJGGEG \n 🔟• نسخه 1.11.4 \n https://rubika.ir/MineShine_APK/CABIGJJIECEIGEG \n 1⃣1⃣• نسخه 1.12.1 \n https://rubika.ir/MineShine_APK/CABIIIJJCHJIGEG \n 2⃣1⃣• نسخه 1.13.1 \n https://rubika.ir/MineShine_APK/CABJCFAAIBFBGEG \n 4⃣1⃣• نسخه 1.14.30 \n https://rubika.ir/MineShine_APK/CACCGEBHDEJFGEG \n5⃣1⃣• نسخه 1.16.40 \b https://rubika.ir/MineShine_APK/CACFGDDADFAJGEG \n 6⃣1⃣• نسخه 1.17.30 \n https://rubika.ir/MineShine_APK/CACJFDEJJDGIGEG \n 7⃣1⃣• نسخه 1.18.12\nhttps://rubika.ir/MineShine_APK/CBBHJDGAJFEHGEG").text
								bot.sendMessage(target, "دستور را درست وارد کنید ❌", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه برایت فرستادم 🌹", message_id=msg["message_id"])						
						
						elif msg.get("text") == "ایموجی":
							try:
								ans = ["😀","😃","😁","😆","😅","😂","🤣","😭","😗","😙","😚","😘","🥰","😍","🥳","🤗","🙃","🙂","☺️","😊","😏","😌","😉","🤭","😶","😐","😑","😔","😋","😛","😝","😜","🤪","🤔","🤨","🧐","🙄","😒","😤","😠","😡","🤬","☹️","🙁","😟","🥺","😳","😬","🤐","🤫","😰","😨","😧","😦","😮","😯","😲","😱","🤯","😢","😥","😓","😞","😖","😣","😩","🤤","🥱","😴","😪","🤢","🤮","🤧","🤒","🤕","🥴","😵","🥵","🥶","😷","😇","🤠","🤑","😎","🤓","🤥"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err date")		
						
						elif msg.get("text") == "!date":
							try:
								bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))
							except:
								print("err date")
						
						elif msg.get("text") == "سلاپ":
							try:
								bot.sendMessage(target, " سلاپ داپ زبونپ بستهپ:/", message_id=msg.get("message_id"))
							except:
								print("err poker answer")
						
						elif msg.get("text").startswith("!user"):
							try:
								users = msg.get("text").split(" ")[1][1:]
								guids = bot.getInfoByUsername(users)["data"]["user"]["first_name"]
								guid1 = bot.getInfoByUsername(users)["data"]["user"]["username"]
								guid2 = bot.getInfoByUsername(users)["data"]["user"]["bio"]
								guid3 = bot.getInfoByUsername(users)["data"]["user"]["user_guid"]
								if not guids in admins:
									bot.sendMessage(target, f"نام شما: || {guids} || \n آیدی شما: || {guid1} || \n بیوی شما: || {guid2} || \n گوید شما: || {guid3} || ", message_id=msg.get("message_id"))
									
								else:
									bot.sendMessage(target, "❌ شما فقط می توانید اطلاعات کاربران عادی دربیارید", message_id=msg.get("message_id"))
									
							except IndexError:
								guidZZ = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								userVxz = bot.getUserInfo(guidzVz)["data"]["chat"]["abs_object"]["object_guid"]
								user1 = bot.getInfoByUsername(userVxz)["data"]["user"]["first_name"]
								user2 = bot.getInfoByUsername(userVxz)["data"]["user"]["username"]
								user3 = bot.getInfoByUsername(userVxz)["data"]["user"]["bio"]
								user4 = bot.getInfoByUsername(userVxz)["data"]["user"]["user_guid"]
								if not guids in admins:
									bot.sendMessage(target, f"نام شما: || {user1} || \n آیدی شما: || {user2} || \n بیوی شما: || {user3} || \n گوید شما: || {user4} || ", message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, "❌ شما فقط می توانید اطلاعات کاربران عادی دربیارید", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
						
						elif msg.get("text").startswith("والا") or msg.get("text").startswith("بمولا"):
							try:
								bot.sendMessage(target, "اره جون عمت 😞😂", message_id=msg.get("message_id"))
							except:
								print("err luagh")
														
						elif msg.get("text") == "قوانین":
							try:
								rules = open("ghavanin.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								 
						elif msg.get("text").startswith("آپدیت قوانین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("ghavanin.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت قوانین")))
								bot.sendMessage(target, "لیست قوانین ها جدید تر شدن♡", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))								
						elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
							try:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "پیام مورد نظر پاک شد...", message_id=msg.get("message_id"))
							except:
								print("err pak")
								
						elif msg.get("text").startswith("!cal") or msg.get("text").startswith("!cal"):
							msd = msg.get("text")
							if plus == True:
								try:
									call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
									if call[1] == "+":
										try:
											am = float(call[0]) + float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
											plus = False
										except:
											print("err answer +")
										
									elif call[1] == "-":
										try:
											am = float(call[0]) - float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer -")
										
									elif call[1] == "*":
										try:
											am = float(call[0]) * float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer *")
										
									elif call[1] == "/":
										try:
											am = float(call[0]) / float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer /")
											
								except IndexError:
									bot.sendMessage(target, "متاسفانه دستور شما اشتباه میباشد!" ,message_id=msg.get("message_id"))
									plus= True
									
						elif msg.get("text") == "!guid":
							try:
								GAPE = bot.getGroupInfo(target)["data"]["group"]["group_title"]
								guidu = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								useru = bot.getUserInfo(guidu)["data"]["user"]["username"]
								if not guidu in admins:
									bot.sendMessage(target, f"کاربر {useru} یک عضو ساده و بدون دسترسی در گروه {GAPE} میباشد 🔥👐", message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, f"کاربر {useru} یک ادمین در گروه {GAPE} میباشد 🤏😁", message_id=msg.get("message_id"))
							except:
								print('analiz user')
						
						elif msg.get("text").startswith("!admin") and msg.get("author_object_guid") in admins:
							try:
								setadminf = msg.get("text").split(" ")[1][1:]
								setadmind = bot.getInfoByUsername(setadminf)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getInfoByUsername(setadminf)["data"]["user"]["first_name"]
								if not setadmind in admins:
									bot.setGroupAdmin(target,setadmind)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت آدمین شد", message_id=msg.get("message_id"))
									
								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
									
							except IndexError:
								guidzz = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								userz = bot.getUserInfo(guidzz)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getUserInfo(userz)["data"]["user"]["first_name"]
								if not userz in admins:
									bot.setGroupAdmin(target,userz)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت آدمین شد", message_id=msg.get("message_id"))
									
								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
							except:
								print('error setadmin')
							
						elif msg.get("text").startswith("بگو"):
							try:
								if msg.get('reply_to_message_id') != None:
									bego1 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego1['text'] != None:
										texts= bego1['text']
										bot.sendMessage(target,texts, message_id=msg.get("message_id"))
										print('error begho')
								else:
									bot.sendMessage(target, 'رو متن مورد نظر ریپ نزدید❌',message_id=msg["message_id"])
							except:
								print('error begho')
			

						elif msg.get("text").startswith("پسورد") or msg.get("text").startswith("!password"):
							try:
								response = get(f"http://api.codebazan.ir/password/?length={msg['text'].split()[1]}").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("چیستان") or msg.get("text").startswith("!chistan") or msg.get("text").startswith("chistan"):
							try:
								response = get("https://api.codebazan.ir/chistan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])
								
						elif hasInsult(msg.get("text"))[0] and not msg.get("author_object_guid") in admins :
							try:
								print("gav fosh dadh")
								bot.deleteMessages(target, [str(msg.get("message_id"))])
								print("fohsh pak shod")
							except:
								print("err del fohsh Bug")
				
						elif msg.get("text").startswith("هکرم"):
							try:
								bot.sendMessage(chat['object_guid'], 'خــو اولــن بــکــیــرم بــعــدــشــم پــســره گــلــم مـــنـــو بـــهـــک مــنــتـــظـــرم😹💔',chat['last_message']['message_id'])
								print('sended response') 
								
							except:
								print("err del fohsh Bug")

						elif msg.get("text").startswith("!trans"):
							try:
								responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
								al = [responser["result"]]
								bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستور رو درست وارد کن دیگه😁", message_id=msg["message_id"])
								
						elif msg.get("text") == "سینگل":
							try:
								rules = open("Single.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text").startswith("خبم ت خبی") or msg.get("text").startswith("خوبیم تو خوبی") or msg.get("text").startswith("تو خوبی") or msg.get("text").startswith("مرسی تو خوبی") or msg.get("text").startswith("خوبی") or msg.get("text").startswith("خبی") :
							try:
								user = bot.getUserInfo(msg["author_object_guid"])["data"]["user"]["first_name"]
								ans =[" بخوبیت " +user+ " جون دل☺💖"," بخوبیت " +user+ " عزیزم🥺🤍"," بخوبیت " +user+ " خوشگله😍🌹"," بخوبیت " +user+ " زبیام☺🌈"," بخوبیت" +user+ " نفسم 😉💛"," بخوبیت" +user+ " عشقم🥰❤"," بخوبیت " +user+ " عزیز دلم😕❤"," بخوبیت " +user+ " جذاب لعنتی🥺❤","بخوبیت " +user+ " زیبای وحشی🥺🖤","بخوبیت " +user+ " عشق خنگم😅🧡"," بخوبیت " +user+ "زیبای عاشق😍❤","خبم" +user+ "جونم ت خبی🥺🤍","فدات" +user+ "نفسم🙂💚","خوبم" +user+ "جونم بخوبیت🙂💖","بخوبیت" +user+ "عزیزم🌹😃","تو خوبی" +user+ "نفس ؟😉💕","خوبم تو خوبی" +user+ "جیگرم ، چخبرا","بخوبیت " +user+ " جون دلم 🙃🤍","بخوبیت " +user+ " عزیزم🥺🤍","بخوبیت " +user+ " خوشگلم😆🔥","بخوبیت "+user+ " خوشگله☺🌈"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err poker answer")
							
					
						elif msg.get("text") == "پشمام":
							try:
								bot.sendMessage(target, "بریزه😐", message_id=msg.get("message_id"))
							except:
								print("err poker answer")
								 	
						
						elif msg.get("text").startswith("هعپ") or msg.get("text").startswith("هعی") or msg.get("text").startswith("هم...") or msg.get("text").startswith("هوف") or msg.get("text").startswith("هف") or msg.get("text").startswith("هف"):
							try:
								bot.sendMessage(target,'حوصله نداری تو هم ؟🙂' ,message_id=msg.get("message_id"))
							except:
								print("err hello")
								
						elif msg.get("text").startswith("اصل") or msg.get("text").startswith("اصل؟") or msg.get("text").startswith("اصل پلیز") or msg.get("text").startswith("اصل بده") or msg.get("text").startswith("اصل بد") or msg.get("text").startswith("اسمت چیه"):
							try:
								bot.sendMessage(target,'ورلد باتم ۱۷ کرج🙂💋' ,message_id=msg.get("message_id"))
							except:
								print("err hello")
								
						elif msg.get("text").startswith("توروخدا") or msg.get("text").startswith("لطفا") or msg.get("text").startswith("خواهشا") or msg.get("text").startswith("جون من") or msg.get("text").startswith("تورو خدا") or msg.get("text").startswith("جواب بده"):
							try:
								bot.sendMessage(target,'عه نمیخوام ولم کن 😐😑' ,message_id=msg.get("message_id"))
							except:
								print("err hello")
	
						elif msg.get("text").startswith("🤍") or msg.get("text").startswith("💚") or msg.get("text").startswith("💛") or msg.get("text").startswith("💜") or msg.get("text").startswith("💙") or msg.get("text").startswith("🧡") or msg.get("text").startswith("🖤") or msg.get("text").startswith("🤎") or msg.get("text").startswith("❤"):
							try:
								bot.sendMessage(target,'وای قلباتو 😍💋' ,message_id=msg.get("message_id"))
							except:
								print("err hello")							 
						elif msg.get("text").startswith("توروخدا") or msg.get("text").startswith("لطفا") or msg.get("text").startswith("خواهشن") or msg.get("text").startswith("الو") or msg.get("text").startswith("التماست میکنم") or msg.get("text").startswith("التماس میکنم"):
							try:
								bot.sendMessage(target,'عه ولمون کن کنجد باقالی😐👊' ,message_id=msg.get("message_id"))
							except:
								print("err hello")
								
						elif msg.get("text").startswith("الاغ") or msg.get("text").startswith("گاو") or msg.get("text").startswith("میمون") or msg.get("text").startswith("خر") or msg.get("text").startswith("گوسفند") or msg.get("text").startswith("میمون"):
							try:
								bot.sendMessage(target,'خودتی😐غلط کنی همچین حرفایی بزنی😑' ,message_id=msg.get("message_id"))
							except:
								print("err hello")
							
						elif msg.get("text").startswith("جونم") or msg.get("text").startswith("بله") or msg.get("text").startswith("جان") or msg.get("text").startswith("جانن") or msg.get("text").startswith("بفرما") or msg.get("text").startswith("چیه"):
							try:
								bot.sendMessage(target,'خوب خدارو شکر جواب داد\n نمرده👍😐' ,message_id=msg.get("message_id"))
							except:
								print("err hello")
							
						elif msg.get("text").startswith("بای") or msg.get("text").startswith("رفتم") or msg.get("text").startswith("من رفتم") or msg.get("text").startswith("من بای") or msg.get("text").startswith("بحی") or msg.get("text").startswith("خداحافظ"):
							try:
								ans = ["بای گلم😚","gooood bay","بسلامت عزیزم 😍❤️","بری که برنگردی 😃😂","بحی داپش🤙","👋👋"," برگردی که دلتنگت میشم هاا😝😞","گپ خودته تعارف نداشته باشیا ! 😏😅","خدا حافظ قربونت بشم ✨ 😍😍"]
								bot.sendMessage(target,random.choice(ans),message_id=msg.get("message_id"))
							except:
								print("err hello")
									
						elif msg.get("text").startswith("سلام") or msg.get("text").startswith("سلم") or msg.get("text").startswith("صلام") or msg.get("text").startswith("صلم") or msg.get("text").startswith("سیلام") or msg.get("text").startswith("صیلام") or msg.get("text").startswith("شلام"):
							try:
								ans = ["آقا 😍 🌈","عشقم 🌚🌺","خان 🤓💋","جووووون🤩🍓","خشگلم🌛🍁","عسل بابا👳‍♂🙋‍♂","نفسکم🙇‍♀💖"," 🌷عزیزم","هِلوووو😚","heloooo","به روی ماهت گلم😘","چند بار سلام میکنی؟😐","هِلوووو عزیزم😃","دلام نفسم🙃💋","شلام شلام شلام💝","بفرما تو گپ خودتونه 😅","واییی وایییی ببین کی اومده 😍😍"]
								bot.sendMessage(target,random.choice(ans),message_id=msg.get("message_id"))
							except:
								print("err hello")
						  
						elif msg.get("text") == "خوش اومدی":
							try:
								bot.sendMessage(target, "اره البته اگه قوانینو رعایت کنن\n\nادمینا از ممبرا بدترن:/", message_id=msg.get("message_id"))
							except:
								print("err poker answer")
		 
						elif msg.get("text").startswith("ممنون") or msg.get("text").startswith("مرسی"):
							try:
								bot.sendMessage(target, "خواهش میکنم عزیزم😍♥", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
							
						elif msg.get("text") == "زر نزن باو":
							try:
								bot.sendMessage(target, "اگه بزنه چی میشه ؟ :/", message_id=msg.get("message_id"))
							except:
								print("err poker answer")		
						elif msg.get("text").startswith("خوبی") or msg.get("text").startswith("خبی"):
							try:
								bot.sendMessage(target, "تو چطوری؟🤪", message_id=msg.get("message_id"))
							except:
								print("err answer hay")

						elif msg.get("text").startswith("😡😡😡") or msg.get("text").startswith("😡"):
							try:
								bot.sendMessage(target, "ببخشید دیگه تکرار نمیشه :(", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
								 
						
								
						elif msg.get("text").startswith("چه خبر") or msg.get("text").startswith("چخبر"):
							try:
								bot.sendMessage(target, "ســلامـتیت😍♥", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
								
						elif msg.get("text") == "ســلامـتیت😍♥":
							try:
								bot.sendMessage(target, "تو چخبر؟ :)", message_id=msg.get("message_id"))
							except:
								print("err poker answer")	

						elif msg.get("text").startswith("جرعت حقیقت"):
							try:
								ans = ["کی و انتخاب می کنی (اونی که دوست داره یا اونی که دوسش داری)؟","تا حالا خاستگار داشتی یا رفتی؟💍","از یکی از اتاق ها خونه عکس بده.🚪","تا حالا با فیلم گریه کردی؟😢","بزرگترین اتفاق زندگیت؟","آخرین باری که گریه کردی کی بود؟","رل داری یا داشتی؟","عطر مورد علاقت؟💄","تو دستشویی به چی فکر می کنی؟🚽","از یکی از جوشای صورتت عکس بده😬","اگه اونی که دوسش داری بهت خیانت کنه چیکار می کنی؟","تو فامیل از کی متنفری؟","دوس داری الان ازدواج کنی؟🥰","رقاص خوبی هستی تو عروسیا؟🕺🏿💃🏻","خوشتیپی یا خوش‌قیافه؟😎","پروف ست بذار.","کی تو گروه صداش تخمی تره؟👩🏻‍🎤👨🏻‍🎤","حاضری واسه یه هفته جنسیتت رو عوض کنی؟","تا حالا دخانیات مصرف کردی؟🚬","اسم مامان و بابات چیه؟","به کدوم یکی از اعضای بدنت افتخار می کنی؟👄","کسی تا به حال تو رو لخت دیده?","رو کی تو گپ کراش داری؟","از من چقدر خوشت میاد؟","سیگار کشیدی؟","با کی رابطه داشتی؟","با چن تا دختر بودی؟","عاشق شدی","از من چقدر بدت میاد","دل کسیو شکوندی","کسی دلتو شکوندی","تاب حال ب خودکشی فک کردی","اگه سفره یه طرف به مریخ انتخاب بشی و یه نفر رو با خودت میتونی ببری اون کیه؟😍","اگه به دنیا اومدنت دست خودت بود تو کدوم کشور دنیا میومدی؟😂","ایران بهترین کشور دنیا؟😐😂","بزرگترین ترس زندگیت چیه؟ 👻","ماشین زمان داشتی به گذشت سفر میکردی یا آینده و چرا؟ 😳","ورزش مورد علاقت؟🤔","عدد مورد علاقه ات","بزرگترین هدفت که رسیدن بهش تقریبا غیر ممکنه چیه؟ تعریف کن؟🤔","هدفت واسه زندگی چیه؟💥","اگه امشب آخرین شبت باشه چه چیزی واسه آخرین بار بهم میگی؟😐🤔","تا به حال به خودکشی فکر کردی؟😃","سه نفر ک دوست داری باهاشون بری بهشت رو نام ببر؟✨","دوست داری چجوری بمیری😂","بدترین خاطره کودکیت چیه؟😢😂","الگو زندگیت کیه؟🤓","دوست داشتن رو معنی کن!🙃","بیا پی مخمو بزن!😎","حیوان مورد علاقه ات؟😍","تخم مرغ بزن به سرت عکس بده🤪","دلت واسه کی تنگ شده؟🙁","بزرگترین آرزو زندگیت؟✨","تاریخ تولدت؟👶","چقدر به عشق اعتماد داری؟💥","یه چیزی درمورد من بگو! ","در عوض ۲۰  میلیون پول حاضری موهاتو بزنی؟🤑","بی مزه ترین خاطره زندگیت؟😒","منفی ترین فرد زندگیت؟😒","یکی از کار های که میری رو مخ بقیه؟😐","بدترین بلایی که سر معلمت آوردی؟","خاطره بدی که از مدرسه داری؟😁","عکس از سابقه سرچ گوگلت بده!😝"]
								bot.sendMessage(target,random.choice(ans),message_id=msg.get("message_id"))
							except:
								print("err hello")
								
						elif msg.get("text") == "ممل":
							try:
								bot.sendMessage(target, "یبار دیگه بوگو صدای باباییمو بشنوم😍♥", message_id=msg.get("message_id"))
							except:
								print("err poker answer")
										
						elif msg.get("text") == "لینک":
							try:
								rules = open("link.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								 
						elif msg.get("text").startswith("آپدیت لینک") and msg.get("author_object_guid") in admins:
							try:
								rules = open("admin.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت لینک")))
								bot.sendMessage(target, "لینک گروه بروز شد♡", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))
									 
						elif msg.get("text") == "من اومدم":
							try:
								bot.sendMessage(target, "خوش اومدی😐", message_id=msg.get("message_id"))
							except:
								print("err poker answer")			 						
						elif msg.get("text") == "ربات":
							try:
								user = bot.getUserInfo(msg["author_object_guid"])["data"]["user"]["first_name"]
								ans =["جــونـم " +user+ " خــوشـگلم ☺❤","بـفـرما " +user+ " عـشـقـم 🍫😁","جــون دلـم " +user+ " نــفس 😍🌹","جــون دلـم " +user+ " نــفس 🙊🔗","بـفـرما " +user+ " مهــربـونم 😢💝","امـر کـن " +user+ " قـشـنگم 🌷😋","جــونـم عشـــقم " +user+ " مهــربـونم 😝❤","بـفـرما " +user+ " عـزیـزم 😍🌹","جــونـم عشـــقم " +user+ " نـفــسم 🙊🔗","جــون ربـات " +user+ " خــوشـگلم 😍🌹","امـر کـن " +user+ " خــوشـگلم 😍❤","جــون دلـم " +user+ " نــفس ☺❤","جــون ربـات " +user+ " عـزیـزم 🙈🌹","جــونـم " +user+ " نــفس 🌷😋"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err poker answer")
							
						elif msg.get("text").startswith("رل") or msg.get("text").startswith("رلین"):
							try:
								bot.sendMessage(target, "این حرف کوفتیو نزن\nبا تشکر🤝🙂", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
								
						elif msg.get("text").startswith("😂") or msg.get("text").startswith("🤣"):
							try:
								bot.sendMessage(target, "خنده هاشو.....😌", message_id=msg.get("message_id"))
							except:
								print("err luagh")
								
						elif msg.get("text").startswith("هیق") or msg.get("text").startswith("هق"):
							try:
								bot.sendMessage(target, "گریه نکن زار زار نیبرما ب بازار میفروشمت .‌..😂💋", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
								       
						elif msg.get("text").startswith("کراش") or msg.get("text").startswith("کراشین"):
							try:
								bot.sendMessage(target, "این حرفو نزن🤝🙂", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
								
						elif msg.get("text") == "بای":
							try:
								bot.sendMessage(target, "بسلامت انشالله😄🚶‍♂", message_id=msg.get("message_id"))
							except:
								print("err poker answer")
								
						elif msg.get("text") == "😐":
							try:
								bot.sendMessage(target, "😑😐", message_id=msg.get("message_id"))
							except:
								print("err poker answer")
					
						elif msg.get("text") == "محمد":
							try:
								bot.sendMessage(target, "ایدی اونو برای چی میخوای ؟!😐😡", message_id=msg.get("message_id"))
							except:
								print("err poker answer")			
						elif msg.get("text") == "ایموجی":
							try:
								ans = ["😀","😃","😁","😆","😅","😂","🤣","😭","😗","😙","😚","😘","🥰","😍","🥳","🤗","🙃","🙂","☺️","😊","😏","😌","😉","🤭","😶","😐","😑","😔","😋","😛","😝","😜","🤪","🤔","🤨","🧐","🙄","😒","😤","😠","😡","🤬","☹️","🙁","😟","🥺","😳","😬","🤐","🤫","😰","😨","😧","😦","😮","😯","😲","😱","🤯","😢","😥","😓","😞","😖","😣","😩","🤤","🥱","😴","😪","🤢","🤮","🤧","🤒","🤕","🥴","😵","🥵","🥶","😷","😇","🤠","🤑","😎","🤓","🤥"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err poker answer")
								
						elif msg.get("text") == "پری":
							try:
								bot.sendMessage(target, "خط قرمزمهههههه😡\nبخدا کارت ضروری نباشه پارتتت میکنم😤", message_id=msg.get("message_id"))
							except:
								print("err poker answer")	
					
						elif msg.get("text") == "گل":
							try:
								ans = ["💐","🌹","🌷","🌺","🌸","🏵️","🌻","🌼","💮"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err poker answer")
						
						elif msg.get("text") == "انه":
							try:
								bot.sendMessage(target, "اون قشنگ منه نمیزارم اذیتش کنی🙁😢", message_id=msg.get("message_id"))
							except:
								print("err poker answer")															
						elif msg.get("text") == "!pin" and msg.get("author_object_guid") in admins :
							try:
								bot.pin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))
							except:
								print("err pin")
								
						elif msg.get("text").startswith("جون") or msg.get("text").startswith("جووون"):
							try:
								bot.sendMessage(target, "بخورمت :/", message_id=msg.get("message_id"))
							except:
								print("err luagh")
						
						elif msg.get("text").startswith("عرر") or msg.get("text").startswith("عررررر"):
							try:
								bot.sendMessage(target, "مگه خری ؟ 🐴 :)", message_id=msg.get("message_id"))
							except:
								print("err luagh")
								
						elif msg.get("text").startswith("اره") or msg.get("text").startswith("اهوم"):
							try:
								bot.sendMessage(target, "باشع:)", message_id=msg.get("message_id"))
							except:
								print("err luagh")
							
						elif msg.get("text").startswith("مرگ") or msg.get("text").startswith("زهر"):
							try:
								bot.sendMessage(target, "چرا ؟!😞💔", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")	
								
						elif msg.get("text").startswith("کوفت") or msg.get("text").startswith("درد"):
							try:
								bot.sendMessage(target, "ب جونت 😂💋", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
					
						
												
						elif msg.get("text").startswith("شب خوش") or msg.get("text").startswith("شب بخیر"):
							try:
								bot.sendMessage(target, "شبت شکلاتی 🍫🥺", message_id=msg.get("message_id"))
							except:
								print("err luagh")
						
						
						elif msg.get("text") == "ممد":
							try:
								bot.sendMessage(target, "ممد پیدرته بگو آقا محمد😎", message_id=msg.get("message_id"))
							except:
								print("err poker answer")		
						elif msg.get("text") == "آقا محمد":
							try:
								bot.sendMessage(target, "آفرین پسر خوب😚🤩", message_id=msg.get("message_id"))
							except:
								print("err poker answer")		
						elif msg.get("text") == "مدیر":
							try:
								bot.sendMessage(target, "کارت باهاش چیه ؟🤭/nبفرما مدیر منم :)", message_id=msg.get("message_id"))
							except:
								print("err poker answer")

						if msg.get("text").startswith("تغیر پروفایل"):
							try:
								if msg.get("author_object_guid") in admins:
								   profile = ["/storage/emulated/0/myrobot/p1.jpg",]
								   photo= choice(profile)
								   bot.uploadAvatar(target,photo)
								else:
									bot.sendMessage(target, '❌ شما اجازه تغیر پرفایل گروه را ندارید',message_id=msg.get("message_id"))
							except:
								print("err profile gap")				
										
						elif msg.get("text") == "بیا بخورش":
							try:
								bot.sendMessage(target, "تو بیا سیستمامو بخور عزیزم🤓😜", message_id=msg.get("message_id"))
							except:
								print("err poker answer")		
						elif msg.get("text").startswith("😭😭") or msg.get("text").startswith("😭"):
							try:
								bot.sendMessage(target, "گریه نکن عزیزم😭😭", message_id=msg.get("message_id"))
							except:
								print("err luagh")		 									
						elif msg.get("text").startswith("!leave_admin") and msg.get("author_object_guid") in admins:
							try:
								deletadminS = msg.get("text").split(" ")[1][1:]
								setdeletadminS = bot.getInfoByUsername(deletadminS)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getInfoByUsername(deletadminS)["data"]["user"]["first_name"]
								if setdeletadminS in admins:
									bot.deleteGroupAdmin(target,setdeletadminS)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت از آدمین بودن برکنار شد", message_id=msg.get("message_id"))
									
								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
									
							except IndexError:
								guidzVz = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								userVz = bot.getUserInfo(guidzVz)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getUserInfo(userVz)["data"]["user"]["first_name"]
								if  userVz in admins:
									bot.deleteGroupAdmin(target,userVz)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت از آدمین بودن برکنار شد", message_id=msg.get("message_id"))
									
								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
							except:
								print('error setdeletadmin')
								
						elif msg.get("text").startswith("حصله") or msg.get("text").startswith("حصله ندارم"):
							try:
								bot.sendMessage(target, "والا چیزی به ذهنم نمیرسه 😞", message_id=msg.get("message_id"))
							except:
								print("err luagh")
									
						elif msg.get("text").startswith("پاره") or msg.get("text").startswith("پارهههه"):
							try:
								bot.sendMessage(target, "اجر پاره :/", message_id=msg.get("message_id"))
							except:
								print("err luagh")
								
						elif msg.get("text").startswith("!post"):
							try:
								if msg.get('reply_to_message_id') != None:
									bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego2['text'] != None:
										textss= bego2['text']
										kanal = textss
										bot.sendMessage(channell, kanal)
									bot.sendMessage(target,"نتیجه به کانال ارسال شد >•<😶",message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه به کانال ارسال شد >•<", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("!azad") or msg.get("text").startswith("ازاد") and msg.get("author_object_guid") in admins :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									bot.unbanGroupMember(target, guid)
									bot.sendMessage(target, "✅ کاربر مورد نظر با موفقیت آزاد شد", message_id=msg.get("message_id"))
									# bot.sendMessage(target, "✅ کاربر با موفقیت از گروه اخراج شد", message_id=msg.get("message_id"))
								else :
									bot.sendMessage(target, "❌ شما آدمین نمی باشید", message_id=msg.get("message_id"))
							except:
								print("err unpin")
								
						elif msg.get("text") == "!unpin" and msg.get("author_object_guid") in admins :
							try:
								bot.unpin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg.get("message_id"))
							except:
								print("err unpin")
			
			            
						elif msg.get("text").startswith("!start_cal"):
							try:
								bot.startVoiceChat(target)
								bot.sendMessage(target, "✅ با موفقیت ایجاد شد", message_id=msg.get("message_id"))
							except:
								print("err call voice")	
								
						elif msg.get("text").startswith("!finish_cal"):
							try:
								bot.finishVoiceChat(target)
								bot.sendMessage(target, "✅ با موفقیت قطع شد", message_id=msg.get("message_id"))
							except:
								print("err call voice")
			 			 
						elif msg.get("text").startswith("!trans"):
							try:
								responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
								al = [responser["result"]]
								bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستور رو درست وارد کن دیگه😁", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("!font"):
							try:
								response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
								bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستور رو درست بزن 🤌😶😁", message_id=msg["message_id"])
						
						elif msg.get("text") == "!tab_on":
							try:
								bot.sendMessage(target, "🤖در پیام بعدی لینک گروه مورد نظر را ثبت نمائید🤖\nمثال:\n\nجوین گروه\nhttps://rubika.ir/joinc/BEDJEHGJ0LXSIPACCXGCQCBIJBZESKWA")
							except:
								print("error ersal start1")

						elif msg.get("text").startswith("جوین گروه"):
							try:
								yourlink = open("target.txt","w",encoding='utf-8').write(str(msg.get("text").strip("جوین گروه")))
								bot.sendMessage(target,  "✅ با موفقیت لینک گروه مورد نظر ثبت شد")
								bot.sendMessage(target,  "\n🤖بنر خود را برای تبلیغات در پیام بعدی ثبت نمائید🤖\n\nمثال رو پیامی که می خواهید پخش شود ریپ بزنید و بگویید [ ثبت تبلیغ ]\n")
							except:
								print("error sabt_link-tabligh")

						elif msg.get("text").startswith("ثبت تبلیغ"):
							try:
								if msg.get('reply_to_message_id') != None:
									banner = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if banner['text'] != None:
										matnbanner= banner['text']
										matntabligh = open("matnTABLIGH.txt","w",encoding='utf-8').write(str(matnbanner))
								bot.sendMessage(target, "✅  \n\nمتن مورد نظر برای تبلیغات ثبت شد\nبرای شروع تبلیغات [ تبلیغ کن ] را وارد کنید", message_id=msg.get("message_id"))
							except:
								print("err save tabligh")

						elif msg.get("text").startswith("تبلیغ کن"):
							while True:
								sleep(5)
								tabyligh = open("matnTABLIGH.txt","r",encoding='utf-8').read()
								tabgligh = open("target.txt","r",encoding='utf-8').read()
								tabeligh = bot.joinGroup(tabgligh)
								tabrligh = tabeligh['data']['group']['group_guid']
								bot.sendMessage(tabrligh,tabyligh)
								bot.leaveGroup(tabrligh)
							
								
						elif msg.get("text").startswith("جوک") or msg.get("text").startswith("jok") or msg.get("text").startswith("!jok"):
							try:
								response = get("https://api.codebazan.ir/jok/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "دستور رو اشتباه میزنی🚫😶", message_id=msg["message_id"])
							
						elif msg.get("text").startswith("ذکر") or msg.get("text").startswith("zekr") or msg.get("text").startswith("!zekr"):
							try:
								response = get("http://api.codebazan.ir/zekr/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("حدیث") or msg.get("text").startswith("hadis") or msg.get("text").startswith("!hadis"):
							try:
								response = get("http://api.codebazan.ir/hadis/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی تو ارسال پیش اومد!", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("بیو") or msg.get("text").startswith("bio") or msg.get("text").startswith("!bio"):
							try:
								response = get("https://api.codebazan.ir/bio/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی تو ارسال پیش اومد!", message_id=msg["message_id"])
						
						elif msg["text"].startswith("!weather"):
							try:
								response = get(f"https://api.codebazan.ir/weather/?city={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("!dialog"):
							try:
								response = get("http://api.codebazan.ir/dialog/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "متاسفانه تو ارسال مشکلی پیش اومد!", message_id=msg["message_id"])
							
						elif msg.get("text").startswith("دانستنی") or msg.get("text").startswith("!danestani"):
								try:
									response = get("http://api.codebazan.ir/danestani/pic").content
									with open("shot.jpg","wb") as shot: shot.write(response)
									bot.sendPhoto(target, "./shot.jpg", [650,370], caption="@mobomation", message_id=msg["message_id"])
									os.remove('./shot.jpg')
								except:
									print("err cbz danesh")
									
								
						elif msg.get("text").startswith("پ ن پ") or msg.get("text").startswith("!pa_na_pa") or msg.get("text").startswith("په نه په"):
							try:
								response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "شرمنده فکر کنم اینترنت ندارم نتونستم بفرستم😑💔", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("الکی مثلا") or msg.get("text").startswith("!alaki_masalan"):
							try:
								response = get("http://api.codebazan.ir/jok/alaki-masalan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "نشد بفرستم:(", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("داستان") or msg.get("text").startswith("!dastan"):
							try:
								response = get("http://api.codebazan.ir/dastan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "فکر کنم اینترنت ندارم نتونستم بفرستم😑💔", message_id=msg["message_id"])
							
						elif msg.get("text").startswith("!ping"):
							try:
								responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
								bot.sendMessage(target, responser,message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستور رو درست بزن 🤌😶", message_id=msg["message_id"])
								
						elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
							try:
								print("Yek ahmagh forwared Zad")
								bot.deleteMessages(target, [str(msg.get("message_id"))])
								print("tabligh forearedi pak shod")
							except:
								print("err delete forwared")
						
						elif msg.get("text").startswith("جیغ") or msg.get("text").startswith("جیغغغغ"):
							try:
								bot.sendMessage(target, "مگه جن دیدی ‌🤭", message_id=msg.get("message_id"))
							except:
								print("err luagh")
		
						elif msg.get("text") == "حالت آرام" and msg.get("author_object_guid") in admins:
							try:
								number = 3
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "حالت آرام برای"+str(number)+"ثانیه بدلیل کنترل بهتر گروه فعال شد✅🙂", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
					
						elif msg.get("text") == "موبوبات":
							try:
								ans = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n جان کاری داشتید","🎓\n🙂\n🧥\n👖 \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print('server mobo bug')
													
						elif msg.get("text") == "!speak" or msg.get("text") == "speak" or msg.get("text") == "Speak" or msg.get("text") == "بگو":
							try:
								if msg.get('reply_to_message_id') != None:
									msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if msg_reply_info['text'] != None:
										text = msg_reply_info['text']
										speech = gTTS(text)
										changed_voice = io.BytesIO()
										speech.write_to_fp(changed_voice)
										b2 = changed_voice.getvalue()
										changed_voice.seek(0)
										audio = MP3(changed_voice)
										dur = audio.info.length
										dur = dur * 1000
										f = open('sound.ogg','wb')
										f.write(b2)
										f.close()
										bot.sendVoice(target , 'sound.ogg', dur,message_id=msg["message_id"])
										os.remove('sound.ogg')
										print('sended voice')
								else:
									bot.sendMessage(target, 'باید روی یه متن ریپ بزنی😕✅',message_id=msg["message_id"])
							except:
								print('server gtts bug')

						elif msg.get("text").startswith("!gold"):
							try:
								responser = get(f"http://api.codebazan.ir/arz/?type={msg.get('text').split()[1]}").json()
								bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

						elif msg["text"].startswith("!arz"):
						        response = get("http://api.codebazan.ir/arz/").text
						        #print("\n".join(list(response["result"].values())))
						        try:
							        bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
							        bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
						        except:
							        bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])

						elif msg.get("text").startswith("خاطره") or msg.get("text").startswith("khatere") or msg.get("text").startswith("!khatere"):
							try:
								response = get("http://api.codebazan.ir/jok/khatere").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "لطفا دستور رابه طورصحیح وارد کنید❌", message_id=msg["message_id"])

						elif msg.get("text").startswith("نام شاخ"):
						
							try:
								response = get("https://api.codebazan.ir/name/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])

						elif msg.get("text").startswith("!tabir"):
							try:
								responser = get(f"https://api.codebazan.ir/tabir/?text={msg.get('text').split()[1]}").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

						elif msg.get("text").startswith("دیالوک") or msg.get("text").startswith("dialog") or msg.get("text").startswith("!dialog"):
							try:
								response = get("http://api.codebazan.ir/dialog/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "متاسفانه تو ارسال مشکلی پیش اومد!", message_id=msg["message_id"])


						elif msg.get("text").startswith("!sher"):
							try:
								response = get("https://api.codebazan.ir/ghazalsaadi/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "مشکلی پیش اومد!", message_id=msg["message_id"])										
								
						elif msg.get("text") == "برداشتن حالت آرام" and msg.get("author_object_guid") in admins:
							try:
								number = 0
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "حالت آرام برداشته شد 👌🙂", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "دستور رو درست بزن 🤌😶", message_id=msg.get("message_id"))

						elif msg.get("text").startswith("!alater") and msg.get("author_object_guid") in admins:
							try:
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									alert(guid,user)
									
								else :
									bot.sendMessage(target, "چیزی زدی ؟؟؟کاربر ادمینه🤣😂", message_id=msg.get("message_id"))
									
							except IndexError:
								guid = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								if not guid in admins:
									alert(guid,user)
								else:
									bot.sendMessage(target, "❌ چیزی زدی ؟؟؟کاربر ادمینه🤣😂", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ دستور رو اشتباه میزنی🚫😶", message_id=msg.get("message_id"))



						elif msg.get("text") == "!lock" and msg.get("author_object_guid") in admins :
							try:
								bot.setMembersAccess(target, ["AddMember"])
								bot.sendMessage(target, "🔒 گروه بسته شد و تا زمان باز شدن نمیتونید چت کنید🙃🤌", message_id=msg.get("message_id"))
							except:
								print("err lock GP")

						elif msg.get("text") == "!unlock" or msg.get("text") == "!unlock" and msg.get("author_object_guid") in admins :
							try:
								bot.setMembersAccess(target, ["SendMessages","AddMember"])
								bot.sendMessage(target, "🔓 گروه بازه و میتونید چت کنید😃🤌", message_id=msg.get("message_id"))
							except:
								print("err unlock GP")

					else:
						if msg.get("text") == "ربات روشن شو" or msg.get("text") == "!start" and msg.get("author_object_guid") in admins :
							try:
								sleeped = False
								bot.sendMessage(target, "با موفقیت روشنم کردی 🥰✅", message_id=msg.get("message_id"))
							except:
								print("err on bot")
							
				elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
					name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
					data = msg['event_data']
					if data["type"]=="RemoveGroupMembers":
						try:
								user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
								bot.sendMessage(target, f"کاربر به نام {user} و در زمان ({time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour})ازگروه حذف شد به دلیل رعایت نکردن قوانین", message_id=msg["message_id"])
								bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err rm member answer")
				
					if msg.get("text").startswith("بگو"):
						bot.sendMessage(Guid, "".join(msg.get("text")[3:]))
									
					elif data["type"]=="								AddedGroupMembers":
						try:
								user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
								bot.sendMessage(target, f"خوش اومدی {user} جونم😍❤️\n\nخوش اومدی به {name} لطفا قوانینو رعایت کن 😊✨\n\nزمان ورود⏰:\n\n{time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour} \n\nتاریخ ورود📅 :\n{time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday} \n برای اطلاعات بیشتر از کلمه(قوانین)استفاده کنید😊و برای اطلاعات بیشتر دستورات ربات ازکلمه ی \n!info", message_id=msg["message_id"])
								bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err add member answer")
					
					elif data["type"]=="LeaveGroup":
						try:
								user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
								bot.sendMessage(target, f"کاربر{user} گروه  {name} رو ترک کرد 😢💔 \nتاریخ و ساعت ترک کردن📅\n{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}\n{time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}✨", message_id=msg["message_id"])
								bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err Leave member Answer")
								 		
					elif data["type"]=="JoinedGroupByLink":
						try:
								user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
								bot.sendMessage(target, f"خوش اومدی {user} جونم😍❤️\n\nخوش اومدی به {name} لطفا قوانینو رعایت کن 😊✨\n\nزمان ورود⏰:\n\n{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec} \n\nتاریخ ورود📅 :\n{time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday} \n برای اطلاعات بیشتر از کلمه(قوانین)استفاده کنید😊و برای اطلاعات بیشتر دستورات ربات ازکلمه ی \n!info", message_id=msg["message_id"])
								bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err Joined member Answer")
							
				else:
					if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("message_id")])
						guid = msg.get("author_object_guid")
						user = bot.getUserInfo(guid)["data"]["user"]["username"]
						bot.deleteMessages(target, [msg.get("message_id")])
						alert(guid,user,True)
					
					continue
			except:
				continue

			answered.append(msg.get("message_id"))
			print("[" + msg.get("message_id")+ "] >>> " + msg.get("text") + "\n")

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
