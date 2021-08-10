import telethon
from telethon import TelegramClient, events, sync
import config 
from config import *
from telethon.sync import TelegramClient
from telethon import functions, types
import time 
import colorama
from colorama import init, deinit
from colorama import Fore, Back, Style
namber = 0
tamesl = 1440






colorama.init()
print(Fore.GREEN + '╔═══╗╔══╗╔══╗─╔═══╗╔══╗╔══╗╔╗╔══╗╔══╗╔════╗╔═══╗─╔╗──╔══╗', "Автор https://t.me/Xacker_Name")
print(Fore.GREEN + '║╔═╗║║╔╗║║╔╗╚╗║╔═╗║╚╗╔╝║╔═╝║║║╔═╝║╔╗║╚═╗╔═╝║╔══╝╔╝║──║╔╗║', "Автор https://t.me/Xacker_Name")
print(Fore.GREEN + '║╚═╝║║║║║║║╚╗║║╚═╝║─║║─║╚═╗║╚╝║──║╚╝║──║║──║║╔═╗╚╗║──║║║║', "Автор https://t.me/Xacker_Name")
print(Fore.GREEN + '║╔══╝║║║║║║─║║║╔══╝─║║─╚═╗║║╔╗║──║╔╗║──║║──║║╚╗║─║║──║║║║', "Автор https://t.me/Xacker_Name")
print(Fore.GREEN + '║║───║╚╝║║╚═╝║║║───╔╝╚╗╔═╝║║║║╚═╗║║║║──║║──║╚═╝║─║║╔╗║╚╝║', "Автор https://t.me/Xacker_Name")
print(Fore.GREEN + '╚╝───╚══╝╚═══╝╚╝───╚══╝╚══╝╚╝╚══╝╚╝╚╝──╚╝──╚═══╝─╚╝╚╝╚══╝', "Автор https://t.me/Xacker_Name")

print(' ')
print(' ')
print(' ')




print(Fore.GREEN + 'Введите ваш никнейм в телеграме через "@":')












nikname = input()
channel1 = "@vvzaimkaa"
channel2 = "@piarsam"
channel3 = "@prmoneycom"
channel4 = "@SOLVPiar"
channel5 = "@Piarsyper"
channel6 = "@nevvpiarchat"
channel7 = "@piarmix"
channel8 = "@pro100PiarGroup"
channel9 = "@peargroupssilok"
channel10 = "@PIAR_Advertising"
channel11 = "@vpchatpiarvzaim"
channel12 = "@Tophad"
channel13 = "@first_ua2"
channel14 = "@besplatnyipiar"
channel15 = "@prvitali"
channel16 = "@reklamachat_vp_piar2"
channel17 = "@vp_telegram"
channel18 = "@freechat2"
channel19 = "@spam_piarchic"
channel20 = "@piarchats"
channel21 = "@adversity_place"
channel22 = "@prsiberia"
channel23 = "@reklamachat_vp_piar3"
channel24 = "@piardublechat"
channel25 = "@vzaimopiar94"
channel26 = "@piarworldbusiness"
channel27 = "@PRnorules"
channel28 = "@PiarFactory"
channel29 = "@pr_for_alll"
channel30 = "@FREE_PIARN"
channel31 = "@public_relations_gr"
channel32 = "@piar_rus1"
channel33 = "@lara_eng"
channel34 = "@r_piar"
channel35 = "@propiar1337"
channel36 = "@TGPR_RealType"
channel37 = "@TvoiTempRosta"
channel38 = "@vzaimn0"
channel39 = "@piarking1"
channel40 = "@piarhot"
channel41 = "@piarbotov"
channel42 = "@rabotatyt777"
channel43 = "@Reklameyser"
channel44 = "@boom_piar"
channel45 = "@piar100procentov"
channel46 = "@pr_free_ar"
channel47 = "@prchat12"
channel48 = "@piarsya"
channel49 = "@prodvinchat"
channel50 = "@all_hyips"
channel51 = "@deep_piar"
channel52 = "@VP_PIARchik"
channel53 = "@piaremma"
channel54 = "@piar_kanali"
channel55 = "@piar_one"
channel56 = "@remlamapiar"
channel57 = "@MoshPiar"
channel58 = "@bazar_top"
channel59 = "@channelPR"
channel60 = "@freePRchannel"
channel61 = "@SpamPromoGroup4"
channel62 = "@Piar_Chat_ViP"
channel63 = "@Piarsya_besplatno"
channel64 = "@hat_Piar_vremya"
channel65 = "@chat_3"
channel66 = "@piargrupp9" 
channel67 = "@SHAt37"
channel68 = "@vzamenvse"
channel69 = "@vvzaimkaa"
channel70 = "@Spammers2"
channel71 = "@piarchat22021"
channel72 = "@PRchatik"
channel73 = "@frradv"
channel74 = "@PR_bespredel"
channel75 = "@piar_chatvz"
channel76 = "@pr_chat3"
channel77 = "@piar_tlgr"
channel78 = "@pr_chat"
channel79 = "@SPAMPIAR"
channel80 = "@PRvTelegramme"
channel81 = "@lucky_piar"
channel82 = "@BLACKPIAR35"
channel83 = "@piar_11"
channel84 = "@piar_grin"
channel85 = "@prpodpiska"
channel86 = "@piarimgrupy"
channel87 = "@P1Rchat"
channel88 = "@piarbezgran"
channel89 = "@VipPiarChannel"
channel90 = "@piar_reklama1"
channel91 = "@piariiik"
channel92 = "@piar_only"
channel93 = "@P_RGroup3" #
channel94 = "@PiArTim"
channel95 = "@Fly_Up"
channel96 = "@rp_piar_chat_reklama"
channel97 = "@pr_spamm"
channel98 = "@nekto_me"
channel99 = "@piar_insaider" #
channel100 = "@test_piar"



















##################################################################
#1
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel1
))
namber = namber +1
print([namber],"Успешно подписались на", channel1, "с", nikname)
##################################################################
##################################################################
#2
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel2
))
namber = namber +1
print([namber], "Успешно подписались на", channel2, "с", nikname)
##################################################################
##################################################################
#3
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel3
))
namber = namber +1
print([namber], "Успешно подписались на", channel3, "с", nikname)
##################################################################
##################################################################
#4
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel4
))
namber = namber +1
print([namber], "Успешно подписались на", channel4, "с", nikname)
##################################################################
##################################################################
#5
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel5
))
namber = namber +1
print([namber], "Успешно подписались на", channel5, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#6
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel6
))
namber = namber +1
print([namber], "Успешно подписались на", channel6, "с", nikname)
##################################################################
##################################################################
#7
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel7
))
namber = namber +1
print([namber], "Успешно подписались на", channel7, "с", nikname)
##################################################################
##################################################################
#8
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel8
))
namber = namber +1
print([namber], "Успешно подписались на", channel8, "с", nikname)
##################################################################
##################################################################
#9
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel9
))
namber = namber +1
print([namber], "Успешно подписались на", channel9, "с", nikname)
##################################################################
##################################################################
#10
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel10
))
namber = namber +1
print([namber], "Успешно подписались на", channel10, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#11
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel11
))
namber = namber +1
print([namber], "Успешно подписались на", channel11, "с", nikname)
##################################################################
##################################################################
#12
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel12
))
namber = namber +1
print([namber], "Успешно подписались на", channel12, "с", nikname)
##################################################################
##################################################################
#13
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel13
))
namber = namber +1
print([namber], "Успешно подписались на", channel13, "с", nikname)
##################################################################
##################################################################
#14
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel14
))
namber = namber +1
print([namber], "Успешно подписались на", channel14, "с", nikname)
##################################################################
##################################################################
#15
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel15
))
namber = namber +1
print([namber], "Успешно подписались на", channel15, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#16
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel16
))
namber = namber +1
print([namber], "Успешно подписались на", channel16, "с", nikname)
##################################################################
##################################################################
#17
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel17
))
namber = namber +1
print([namber], "Успешно подписались на", channel17, "с", nikname)
##################################################################
##################################################################
#18
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel18
))
namber = namber +1
print([namber], "Успешно подписались на", channel18, "с", nikname)
##################################################################
##################################################################
#19
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel19
))
namber = namber +1
print([namber], "Успешно подписались на", channel19, "с", nikname)
##################################################################
##################################################################
#20
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel20
))
namber = namber +1
print([namber], "Успешно подписались на", channel20, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#21
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel21
))
namber = namber +1
print([namber], "Успешно подписались на", channel21, "с", nikname)
##################################################################
##################################################################
#22
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel22
))
namber = namber +1
print([namber], "Успешно подписались на", channel22, "с", nikname)
##################################################################
##################################################################
#23
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel23
))
namber = namber +1
print([namber], "Успешно подписались на", channel23, "с", nikname)
##################################################################
##################################################################
#24
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel24
))
namber = namber +1
print([namber], "Успешно подписались на", channel24, "с", nikname)
##################################################################
##################################################################
#25
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel25
))
namber = namber +1
print([namber], "Успешно подписались на", channel25, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#26
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel26
))
namber = namber +1
print([namber], "Успешно подписались на", channel26, "с", nikname)
##################################################################
##################################################################
#27
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel27
))
namber = namber +1
print([namber], "Успешно подписались на", channel27, "с", nikname)
##################################################################
##################################################################
#28
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel28
))
namber = namber +1
print([namber], "Успешно подписались на", channel28, "с", nikname)
##################################################################
##################################################################
#29
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel29
))
namber = namber +1
print([namber], "Успешно подписались на", channel29, "с", nikname)
##################################################################
##################################################################
#30
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel30
))
namber = namber +1
print([namber], "Успешно подписались на", channel30, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#31
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel31
))
namber = namber +1
print([namber], "Успешно подписались на", channel31, "с", nikname)
##################################################################
##################################################################
#32
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel32
))
namber = namber +1
print([namber], "Успешно подписались на", channel32, "с", nikname)
##################################################################
##################################################################
#33
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel33
))
namber = namber +1
print([namber], "Успешно подписались на", channel33, "с", nikname)
##################################################################
##################################################################
#34
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel34
))
namber = namber +1
print([namber], "Успешно подписались на", channel34, "с", nikname)
##################################################################
##################################################################
#35
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel35
))
namber = namber +1
print([namber], "Успешно подписались на", channel35, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#36
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel36
))
namber = namber +1
print([namber], "Успешно подписались на", channel36, "с", nikname)
##################################################################
##################################################################
#37
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel37
))
namber = namber +1
print([namber], "Успешно подписались на", channel37, "с", nikname)
##################################################################
##################################################################
#38
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel38
))
namber = namber +1
print([namber], "Успешно подписались на", channel38, "с", nikname)
##################################################################
##################################################################
#39
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel39
))
namber = namber +1
print([namber], "Успешно подписались на", channel39, "с", nikname)
##################################################################
##################################################################
#40
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel40
))
namber = namber +1
print([namber], "Успешно подписались на", channel40, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#41
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel41
))
namber = namber +1
print([namber], "Успешно подписались на", channel41, "с", nikname)
##################################################################
##################################################################
#42
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel42
))
namber = namber +1
print([namber], "Успешно подписались на", channel42, "с", nikname)
##################################################################
##################################################################
#43
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel43
))
namber = namber +1
print([namber], "Успешно подписались на", channel43, "с", nikname)
##################################################################
##################################################################
#44
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel44
))
namber = namber +1
print([namber], "Успешно подписались на", channel44, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#45
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel45
))
namber = namber +1
print([namber], "Успешно подписались на", channel45, "с", nikname)
##################################################################
##################################################################
#46
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel46
))
namber = namber +1
print([namber], "Успешно подписались на", channel46, "с", nikname)
##################################################################
##################################################################
#47
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel47
))
namber = namber +1
print([namber], "Успешно подписались на", channel47, "с", nikname)
##################################################################
##################################################################
#48
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel48
))
namber = namber +1
print([namber], "Успешно подписались на", channel48, "с", nikname)
##################################################################
##################################################################
#49
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel49
))
namber = namber +1
print([namber], "Успешно подписались на", channel49, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#50
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel50
))
namber = namber +1
print([namber], "Успешно подписались на", channel50, "с", nikname)
##################################################################
##################################################################
#51
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel51
))
namber = namber +1
print([namber], "Успешно подписались на", channel51, "с", nikname)
##################################################################
##################################################################
#52
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel52
))
namber = namber +1
print([namber], "Успешно подписались на", channel40, "с", nikname)
##################################################################
##################################################################
#53
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel53
))
namber = namber +1
print([namber], "Успешно подписались на", channel53, "с", nikname)
##################################################################
##################################################################
#54
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel54
))
namber = namber +1
print([namber], "Успешно подписались на", channel54, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#55
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel55
))
namber = namber +1
print([namber], "Успешно подписались на", channel55, "с", nikname)
##################################################################
##################################################################
#56
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel56
))
namber = namber +1
print([namber], "Успешно подписались на", channel56, "с", nikname)
##################################################################
##################################################################
#57
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel57
))
namber = namber +1
print([namber], "Успешно подписались на", channel57, "с", nikname)
##################################################################
##################################################################
#58
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel58
))
namber = namber +1
print([namber], "Успешно подписались на", channel58, "с", nikname)
##################################################################
##################################################################
#59
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel59
))
namber = namber +1
print([namber], "Успешно подписались на", channel59, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#60
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel60
))
namber = namber +1
print([namber], "Успешно подписались на", channel60, "с", nikname)
##################################################################
##################################################################
#61
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel61
))
namber = namber +1
print([namber], "Успешно подписались на", channel61, "с", nikname)
##################################################################
##################################################################
#62
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel62
))
namber = namber +1
print([namber], "Успешно подписались на", channel62, "с", nikname)
##################################################################
##################################################################
#63
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel63
))
namber = namber +1
print([namber], "Успешно подписались на", channel63, "с", nikname)
##################################################################
##################################################################
#64
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel64
))
namber = namber +1
print([namber], "Успешно подписались на", channel64, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#65
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel65
))
namber = namber +1
print([namber], "Успешно подписались на", channel65, "с", nikname)
##################################################################
##################################################################
#66
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel66
))
namber = namber +1
print([namber], "Успешно подписались на", channel66, "с", nikname)
##################################################################
##################################################################
#67
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel67
))
namber = namber +1
print([namber], "Успешно подписались на", channel67, "с", nikname)
##################################################################
##################################################################
#68
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel68
))
namber = namber +1
print([namber], "Успешно подписались на", channel68, "с", nikname)
##################################################################
##################################################################
#69
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel69
))
namber = namber +1
print([namber], "Успешно подписались на", channel69, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#70
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel70
))
namber = namber +1
print([namber], "Успешно подписались на", channel70, "с", nikname)
##################################################################
##################################################################
#71
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel71
))
namber = namber +1
print([namber], "Успешно подписались на", channel71, "с", nikname)
##################################################################
##################################################################
#72
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel72
))
namber = namber +1
print([namber], "Успешно подписались на", channel72, "с", nikname)
##################################################################
##################################################################
#73
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel73
))
namber = namber +1
print([namber], "Успешно подписались на", channel73, "с", nikname)
##################################################################
##################################################################
#74
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel74
))
namber = namber +1
print([namber], "Успешно подписались на", channel74, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#75
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel75
))
namber = namber +1
print([namber], "Успешно подписались на", channel75, "с", nikname)
##################################################################
##################################################################
#76
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel76
))
namber = namber +1
print([namber], "Успешно подписались на", channel76, "с", nikname)
##################################################################
##################################################################
#77
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel77
))
namber = namber +1
print([namber], "Успешно подписались на", channel77, "с", nikname)
##################################################################
##################################################################
#78
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel78
))
namber = namber +1
print([namber], "Успешно подписались на", channel78, "с", nikname)
##################################################################
##################################################################
#79
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel79
))
namber = namber +1
print([namber], "Успешно подписались на", channel79, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#80
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel80
))
namber = namber +1
print([namber], "Успешно подписались на", channel80, "с", nikname)
##################################################################
##################################################################
#81
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel81
))
namber = namber +1
print([namber], "Успешно подписались на", channel81, "с", nikname)
##################################################################
##################################################################
#82
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel82
))
namber = namber +1
print([namber], "Успешно подписались на", channel82, "с", nikname)
##################################################################
##################################################################
#83
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel83
))
namber = namber +1
print([namber], "Успешно подписались на", channel83, "с", nikname)
##################################################################
##################################################################
#84
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel84
))
namber = namber +1
print([namber], "Успешно подписались на", channel84, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#85
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel85
))
namber = namber +1
print([namber], "Успешно подписались на", channel85, "с", nikname)
##################################################################
##################################################################
#86
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel86
))
namber = namber +1
print([namber], "Успешно подписались на", channel86, "с", nikname)
##################################################################
##################################################################
#87
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel87
))
namber = namber +1
print([namber], "Успешно подписались на", channel87, "с", nikname)
##################################################################
##################################################################
#88
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel88
))
namber = namber +1
print([namber], "Успешно подписались на", channel88, "с", nikname)
##################################################################
##################################################################
#89
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel89
))
namber = namber +1
print([namber], "Успешно подписались на", channel89, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#90
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel90
))
namber = namber +1
print([namber], "Успешно подписались на", channel90, "с", nikname)
##################################################################
##################################################################
#91
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel91
))
namber = namber +1
print([namber], "Успешно подписались на", channel91, "с", nikname)
##################################################################
##################################################################
#92
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel92
))
namber = namber +1
print([namber], "Успешно подписались на", channel92, "с", nikname)
##################################################################
##################################################################
#93
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel93
))
namber = namber +1
print([namber], "Успешно подписались на", channel40, "с", nikname)
##################################################################
##################################################################
#94
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel94
))
namber = namber +1
print([namber], "Успешно подписались на", channel94, "с", nikname)
##################################################################
##################################################################
#ОЖИДАНИЕ
print('Ожидание начато! Ожидаем:', tamesl, "в секундах")
time.sleep(tamesl)
print('Осталась 1 минута!')
time.sleep(60)
print('Ожидание закончено! Прошло:', tamesl + 60, "в секундах")
#ОЖИДАНИЕ
##################################################################
##################################################################
#95
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel95
))
namber = namber +1
print([namber], "Успешно подписались на", channel95, "с", nikname)
##################################################################
##################################################################
#96
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel96
))
namber = namber +1
print([namber], "Успешно подписались на", channel96, "с", nikname)
##################################################################
##################################################################
#97
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel97
))
namber = namber +1
print([namber], "Успешно подписались на", channel97, "с", nikname)
##################################################################
##################################################################
#98
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel98
))
namber = namber +1
print([namber], "Успешно подписались на", channel98, "с", nikname)
##################################################################
##################################################################
#99
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel99
))
namber = namber +1
print([namber], "Успешно подписались на", channel99, "с", nikname)
##################################################################
##################################################################
time.sleep(270)
##################################################################
##################################################################
#100
with TelegramClient('session_name', api_id, api_hash) as client:
	result = client(functions.channels.JoinChannelRequest(
   channel = channel100
))
namber = namber +1
print([namber], "Успешно подписались на", channel100, "с", nikname)
##################################################################
##################################################################


print("Скрипт зашёл во все чаты!")
input("Нажмите Enter для выхода!")











































































