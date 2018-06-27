# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from googletrans import Translator




#jangan merubah bagian ini untuk menghargai saya
#jika ada yg ingin di tanyakan hubungi
# id line : araragi. (pakai titik) 


#jika ingin jadi selfboT di LINE() isi dengan token yg sama swmua

#______________________________________________
#______________________________________________
botStart = time.time()
araragiayane = LINE('EunNwpJXrzt1KhTXQbo5.0UMp7YtLt9ZHspdwIZWgPq.JzQkoOESFGho4GARWQ+atqB0bBcWP1P4MRInQcavb+s=') 
araragiayane.log("Auth Token : " + str(araragiayane.authToken))
lineSettings = araragiayane.getSettings()
araragiayaneProfile = araragiayane.getProfile()
araragiayaneMID = araragiayane.profile.mid
oepoll = OEPoll(araragiayane)

ayane = LINE('EunNwpJXrzt1KhTXQbo5.0UMp7YtLt9ZHspdwIZWgPq.JzQkoOESFGho4GARWQ+atqB0bBcWP1P4MRInQcavb+s=') 
ayane.log("Auth Token : " + str(ayane.authToken))
lineSettings = ayane.getSettings()
ayaneProfile = ayane.getProfile()
ayaneMID = ayane.profile.mid
oepoll = OEPoll(ayane) 

aryane = LINE('EuwrUJotJl9z73LEW5Ae.NnWPYXrsfOYTRMjXCBEM7G.Xn8B3lDEc80ygZW0kjuYZP40bZCXs8dMafF8/XgRCSY=') 
aryane.log("Auth Token : " + str (aryane.authToken))
lineSettings = aryane.getSettings()
aryaneProfile = aryane.getProfile()
aryaneMID = aryane.profile.mid
oepoll = OEPoll(aryane) 

                 #[[[[[[[[[induk&akunutama]]]]]]]]]#

arisys = LINE('EuwrUJotJl9z73LEW5Ae.NnWPYXrsfOYTRMjXCBEM7G.Xn8B3lDEc80ygZW0kjuYZP40bZCXs8dMafF8/XgRCSY=') 
arisys.log("Auth Token : " + str (arisys.authToken))
lineSettings = arisys.getSettings()
arisysProfile = arisys.getProfile()
arisysMID = arisys.profile.mid
oepoll = OEPoll(arisys) 
#END OPERATIONS______________________________________________
#______________________________________________






#______________________________________________
#______________________________________________
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = arisysProfile.displayName
myProfile["statusMessage"] = arisysProfile.statusMessage
myProfile["pictureStatus"] = arisysProfile.pictureStatus
#END OPERATIONS______________________________________________
#______________________________________________






#______________________________________________
#______________________________________________
arBot = [araragiayaneMID,ayaneMID,aryaneMID]
ARZA = [araragiayane,ayane,aryane] 
admin = {
    "u9cdc29cb1452168cadae627171b7a6ee", #my
    "u529ed08e968ba9d107784186eb66b76a", #ayane
    "ua5f2cbc325816777be5ef529eb920c50", #agy
     ayaneMID,
     aryaneMID,
     arisysMID, 
     arisysMID
} 
msg_dict = {}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
bl = [""]
#END OPERATIONS______________________________________________
#______________________________________________








#______________________________________________
#______________________________________________
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ INFO ] BOT RESETED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    arisys.log("[ EROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        arisys.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#END OPERATIONS______________________________________________
#______________________________________________








#______________________________________________
#______________________________________________
def helpmessage():
    helpMessage = """╔════════════════
║ ☂⃟👑⃟₳ṛḁ̶ṝấḡḭ⃟ᵃᵞ⃟🛡️⃟࿐ 
╠════════════════
║ Helping
╠════════════════
║╔═══════════════
║╠☂࿐help
║╠☂࿐helpsett
║╠☂࿐helpkikc
║╠☂࿐helpgroup
║╠☂࿐helpadmin
║╠═══════════════
║╠☂࿐me
║╠☂࿐mename
║╠☂࿐mymid
║╠☂࿐mybio
║╠☂࿐mycover
║╠☂࿐mypicture
║╠═══════════════
║╠☂࿐contact @
║╠☂࿐mid @
║╠☂࿐name @
║╠☂࿐bio @
║║☂࿐cover @
║╠☂࿐pictures @
║╠═══════════════
║╠☂࿐rebot
║╠☂࿐runtime
║╠☂࿐speed/sp
║╠☂࿐set (setting) 
║╠☂࿐removeallchat
║╠☂࿐about
║╠☂࿐fl (friend)
║╠☂࿐Gbc̶vc [bc voice] 
║╠☂࿐Cbcv̶c̶ [utk kontak]
║╠☂࿐G̶bc
║╠☂࿐Fbc
║╚════════════════
║ A̶y̶a̶n̶e 💕 (˶◕‿◕˶✿) 
╚═════════════════"""
    return helpMessage


def helpmessagegroup():
    helpMessageGroup = """╔════════════════
║ ☂⃟👑⃟₳ṛḁ̶ṝấḡḭ⃟ᵃᵞ⃟🛡️⃟࿐ 
╠════════════════
║ Helping Group
╠════════════════
║╔═══════════════
║╠☂࿐gowner
║╠☂࿐curl/ourl
║╠☂࿐gurl
║╠☂࿐lg
║╠☂࿐gb
║╠☂࿐ginfo
║╠☂࿐cancel
║╠☂࿐gn (nama)
║╠☂࿐inv (mid)
║╠☂࿐banlist
║╠☂࿐unban @
║╠☂࿐ban @
║╠☂࿐clear ban
║╠☂࿐kill ban
║╠☂࿐killbanall
║╠☂࿐Vk [kick] 
║╠☂࿐Spam [on/off] [jumlah] [text] 
║╠☂࿐killbanall
║╚════════════════
║ A̶y̶a̶n̶e 💕 (˶◕‿◕˶✿) 
╚═════════════════"""
    return helpMessageGroup


def helpmessagesetting():
    helpMessageSetting = """╔════════════════
║ ☂⃟👑⃟₳ṛḁ̶ṝấḡḭ⃟ᵃᵞ⃟🛡️⃟࿐ 
╠════════════════
║ Helping Setting
╠════════════════
║╔═══════════════
║╠☂࿐groupprotect 
║╠☂࿐inviteprotect 
║╠☂࿐qr
║╠☂࿐contact
║╠☂࿐add
║╠☂࿐qrjoin
║╠☂࿐join
║╠☂࿐tag
║╠☂࿐reread
║╠☂࿐read
║╠☂࿐seejoin
║╠☂࿐seeleave
║╠☂࿐kc 
║╠☂࿐ck
║╠☂࿐timeline
║╚════════════════
║ A̶y̶a̶n̶e 💕 (˶◕‿◕˶✿) 
╚═════════════════"""
    return helpMessageSetting


def helpmessageadmin():
    helpMessageAdmin = """╔════════════════
║ ☂⃟👑⃟₳ṛḁ̶ṝấḡḭ⃟ᵃᵞ⃟🛡️⃟࿐ 
╠════════════════
║ Helping Admin
╠════════════════
║╔═══════════════
║╠☂࿐op @ 
║╠☂࿐deop @
║╠☂࿐oplist (Daftar)
║╠☂࿐op:
║╠☂࿐deop:
║╠☂࿐opmid
║╠☂࿐sn (set sider)
║╠☂࿐sf (del set)
║╠☂࿐r (cek sider)
║╠☂࿐inv:
║╠☂࿐/invitemeto
║╚════════════════
║ A̶y̶a̶n̶e 💕 (˶◕‿◕˶✿) 
╚═════════════════"""
    return helpMessageAdmin
#END OPERATIONS______________________________________________
#______________________________________________








#______________________________________________
#______________________________________________
def lineBot(op):
    try:
        if op.type == 0:
            return
            
        if op.type == 1:
            print("[1] UPDATE_PROFILE")
            
        if op.type == 2:
            print ("[2] UPDATE_PROFILE" ) 
            
        if op.type == 3:
            print ("[3] REGISTER_USERID ") 
           
        if op.type == 4:
            print ("[4] ADD_CONTACT ")
            
        if op.type == 5:
            contact = arisys.getContact(op.param1)
            print ("[ 5 ] NOTICED ADDERS CONTACT: " + contact.displayName)
            if settings["autoAdd"] == True:
                arisys.findAndAddContactsByMid(op.param1)
                arisys.sendMessage(op.param1, "[ Responded ]\n\nNah ketahuan kak {} ☜（ﾟ∀ﾟ☜） add aku diem diem \n\nCreator : http://line.me/ti/p/~araragi. ".format(str(contact.displayName)), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
       
        if op.type == 6:
            print("[6] BLOCK_CONTACT")
           
        if op.type == 7:
            print("[7] UNBLOCK_CONTACT")
           
        if op.type == 8:
            print("[8] NOTIFIED_RECOMMEND_CONTACT")
           
        if op.type == 9:
            print("[9] CREATE_GROUP")
           
        if op.type == 10:
            print("[10] UPDATE_GROUP")
            
        if op.type == 11:
            print("[11] NOTIFIED_UPDATE_GROUP")
            
        if op.type == 11:
            group = arisys.getGroup(op.param1)
            contact = arisys.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = arisys.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    arisys.updateGroup(gs)
                    invsend = 0
                    arisys.sendMessage(op.param1,arisys.getContact(op.param2).displayName + "Heh kutil baby jagan Mainan group seenak nya ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    random.choice(ARZA).kickoutFromGroup(op.param1,[op.param2])
                    arisys.kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][target] = True
                    
        if op.type == 13:
            contact1 = arisys.getContact(op.param2)
            contact2 = arisys.getContact(op.param3)
            group = arisys.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    random.choice(ARZA).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(ARZA).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(ARZA).kickoutFromGroup(op.param1,[op.param2])
                    arisys.cancelGroupInvitation(op.param1,[op.param3])
                    arisys.kickoutFromGroup(op.param1,[op.param3])
                    arisys.kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][target] = True
                    
            if arisysMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('[ Responded ]\n\nHai kakak (☞^o^)☞ ')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "\nMakasih udah undang aku ya (˶◕‿◕˶✿)  Salam kenal\nHai kamu sider salam kenal juga buat mu (┛◉Д◉)┛彡┻━┻ "
                        arisys.acceptGroupInvitation(op.param1)
                        arisys.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
                        
            if arisysMID in op.param3:
                if settings["autoPtt"] == True:
                    arisys.acceptGroupInvitation(op.param1)
                    arisys.sendMessage(op.param1, "[ Responded ]\n\nHai kak maaf aku di suruh mampir aja (≧∇≦)/(≧∇≦)/", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    arisys.leaveGroup(op.param1)
                    
        if op.type == 15:
            contact1 = arisys.getContact(op.param2)
            group = arisys.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[ Responded ]\n\nYah kok pergi (⋟﹏⋞) ')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "\nbalik ke {} lagi kapan kapan ya ☜（ﾟ∀ﾟ☜）".format(str(group.name))
                    arisys.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
                    
        if op.type == 17:
            contact1 = arisys.getContact(op.param2)
            group = arisys.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[ Responded ]\n\nWelcome (≧∇≦)/ ')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "\nBaik baik di {} ya jangan lupa cek note, kalau ada (˶◕‿◕˶✿) jangan nakal kambingg (┛◉Д◉)┛彡┻━┻".format(str(group.name))
                    arisys.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
                    
        if op.type == 19:
            if settings["blacklist"] == True:
                if op.param2 in admin:
                    random.choice(ARZA).kickoutFromGroup(op.param1,[op.param2])
                    arisys.kickoutFromGroup(op.param1,[op.param2])
                    
        if op.type == 19:
            contact1 = arisys.getContact(op.param2)
            group = arisys.getGroup(op.param1)
            contact2 = arisys.getContact(op.param3)
            print ("[19] KICK OUT FROM GROUP: " + str(group.name) + "\n" + op.param1 +"\nNama: " + contact1.displayName + "\nMid:" + contact1.mid + "\nNama: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('Warning 凸ಠ益ಠ)凸')
                            arr = []
                            mention1 = "@Araragi"
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + 'kickout '
                            mention2 = "@kick "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            arisys.kickoutFromGroup(op.param1,[op.param2])
                            settings["blacklist"][op.param2] = True
                            time.sleep(0.1)
                            arisys.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    else:
                        arisys.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('Warning 凸ಠ益ಠ)凸')
                        arr = []
                        mention1 = "@araragi "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + 'kickout  '
                        mention2 = "@kick "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        arisys.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
                else:
                    pass
                    
        if op.type == 19:
            contact1 = arisys.getContact(op.param2)
            group = arisys.getGroup(op.param1)
            contact2 = arisys.getContact(op.param3)
            print ("[19]KICKOUT : " + str(group.name) + "\n" + op.param1 +"\nPelaku: " + contact1.displayName + "\nMid: " + contact1.mid + "\nKorban" + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    arisys.kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][op.param2] = True
            else:
                pass
            if araragiayaneMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19] Group: " + str(group.name) +"\nPelaku: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        arisys.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ARZA).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("Group :\n["+op.param1+"]\nKorban  :\n["+op.param2+"]\nBlacklist。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = arisys.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    arisys.updateGroup(G)
                    invsend = 0
                    Ti = arisys.reissueGroupTicket(op.param1)
                    araragiayane.acceptGroupInvitationByTicket(op.param1, Ti)
                    ayane.acceptGroupInvitationByTicket(op.param1, Ti)
                    arisys.acceptGroupInvitationByTicket(op.param1, Ti)
                    aryane.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    arisys.updateGroup(G)
                    
            if ayaneMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19] Group: " + str(group.name) +"\nPelaku: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        arisys.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ARZA).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("Group  : \n["+op.param1+"]\nKorban  :\n["+op.param2+"]\nblacklist。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = arisys.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    arisys.updateGroup(G)
                    invsend = 0
                    Ti = arisys.reissueGroupTicket(op.param1)
                    araragiayane.acceptGroupInvitationByTicket(op.param1, Ti)
                    ayane.acceptGroupInvitationByTicket(op.param1, Ti)
                    arisys.acceptGroupInvitationByTicket(op.param1, Ti)
                    aryane.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    araragi.updateGroup(G)
                    
            if arisysMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]Group: " + str(group.name) +"\nPelaku: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        aryane.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ARZA).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("Group  :\n["+op.param1+"]\nKorban  :\n["+op.param2+"]\nblacklist。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = aryane.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    aryane.updateGroup(G)
                    invsend = 0
                    Ti = aryane.reissueGroupTicket(op.param1)
                    araragiayane.acceptGroupInvitationByTicket(op.param1, Ti)
                    ayane.acceptGroupInvitationByTicket(op.param1, Ti)
                    arisys.acceptGroupInvitationByTicket(op.param1, Ti)
                    aryane.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    araragi.updateGroup(G)
                    
            if aryaneMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]Group : " + str(group.name) +"\nPelaku: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        araragi.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ARZA).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("Group  :\n["+op.param1+"]\nKorban  :\n["+op.param2+"]\nBlacklist。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = araragiayane.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    araragiayane.updateGroup(G)
                    invsend = 0
                    Ti = araragiayane.reissueGroupTicket(op.param1)
                    araragiayane.acceptGroupInvitationByTicket(op.param1, Ti)
                    ayane.acceptGroupInvitationByTicket(op.param1, Ti)
                    arisys.acceptGroupInvitationByTicket(op.param1, Ti)
                    aryane.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    araragiayane.updateGroup(G)
       
        if op.type == 20:
            print("[20] CREATE_ROOM")
            
        if op.type == 21:
            print("[21] INVITE_INTO_ROOM")
            
        if op.type == 22:
            print("[22] NOTIFIED_INVITE_INTO_ROOM")
                
        if op.type == 23:
            print("[23] LEAVE_ROOM")
           
        if op.type == 24:
            print("[24] NOTIFIED_LEAVE_ROOM")
            
        if op.type == 25:
            print("[25] SEND_MESSAGE")
       
        if op.type == 22:
            print ("[22] NOTICED LEAVE GROUP")
            if settings["autoLeave"] == True:
                arisys.leaveRoom(op.param1)
        
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != arisys.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ INFO ]"
                    ret_ += "\nID   : {}".format(stk_id)
                    ret_ += "\nID   : {}".format(pkg_id)
                    ret_ += "\nURL  : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\nWEB  ：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ INFO ]"
                    arisys.sendMessage(to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    arisys.sendImageWithURL(to, path)
                    
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = arisys.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = arisys.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        arisys.sendMessage(msg.to,"[NAMA]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Check]:\n" + contact.statusMessage + "\n[URL]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[COVER]:\n" + str(cu), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    else:
                        contact = arisys.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = arisys.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        arisys.sendMessage(msg.to,"[NAMA]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Check]:\n" + contact.statusMessage + "\n[URL]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[COVER]:\n" + str(cu), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                       
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in black["blacklist"]:
                        araragi.sendMessage(to, "Sudah ada di daftar hitam ")
                        settings["wblack"] = False
                    else:
                        black["blacklist"][msg.contentMetadata["mid"]] = True
                        araragi.sendMessage(to, "Ditambahkan ke daftar hitam ")
                        settings["wblack"] = False
                    backupData()
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in black["blacklist"]:
                        del black["blacklist"][msg.contentMetadata["mid"]]
                        araragi.sendMessage(to, "Daftar Hitam telah ditutup ")
                        settings["dblack"] = False
                    else:
                        araragi.sendMessage(to, "Dia tidak masuk daftar hitam ")
                        settings["dblack"] = False
                    backupData()          
                      
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s\n%s\n"%("---[Share Post]---","[Creator]:")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[Keterangan]:\n" + msg.contentMetadata["text"] + "\n(Hanya Menampilkan kan 💯 kata)" + "\n[Url]:\n" + msg.contentMetadata["postEndUrl"]
                            arisys.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "---[Post]---\n[Created ]:\n" + msg.contentMetadata["text"] + "\n(Hanya menampilkan 💯 kata)"
                        ret_ += "\n[Url]:\n" + msg.contentMetadata["postEndUrl"]
                        arisys.sendMessage(msg.to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
#END OPERATIONS______________________________________________
#______________________________________________

      
                        


#______________________________________________
#______________________________________________
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if msg.text in ["help"]:
                    helpMessage = helpmessage()
                    arisys.sendMessage(to, str(helpMessage), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'helpkick':
                    helpMessageKick = helpmessagekick()
                    arisys.sendMessage(to, str(helpMessageKick), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'helpadmin':
                    helpMessageAdmin = helpmessageadmin()
                    arisys.sendMessage(to, str(helpMessageAdmin), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'helpgroup':
                    helpMessageGroup = helpmessagegroup()
                    arisys.sendMessage(to, str(helpMessageGroup), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'helpsett':
                    helpMessageSetting = helpmessagesetting()
                    arisys.sendMessage(to, str(helpMessageSetting), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'creator':
                    arisys.sendMessage(to, "My Creator:", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
#END OPERATIONS______________________________________________
#______________________________________________                   
                  
                 
                
               
              
             
#______________________________________________
#______________________________________________             
                elif text.lower() == '#bye':
                    araragiayane.leaveGroup(msg.to)
                    ayane.leaveGroup(msg.to)
                    aryane.leaveGroup(msg.to)
                elif text.lower() == '#join':
                    G = ayane.getGroup(msg.to)
                    if G.preventedJoinByTicket == False:
                        arisys.updateGroup(G)
                        invsend = 0
                        Ti = arisys.reissueGroupTicket(msg.to)
                        araragiayane.acceptGroupInvitationByTicket(msg.to, Ti)
                        aryane.acceptGroupInvitationByTicket(msg.to, Ti)
                        ayane.acceptGroupInvitationByTicket(msg.to, Ti) 
                        G.preventedJoinByTicket = True
                        arisys.updateGroup(G)
                    else:
                        G.preventedJoinByTicket = False
                        arisys.updateGroup(G)
                        invsend = 0
                        Ti = arisys.reissueGroupTicket(msg.to)
                        araragiayane.acceptGroupInvitationByTicket(msg.to, Ti)
                        aryane.acceptGroupInvitationByTicket(msg.to, Ti)
                        ayane.acceptGroupInvitationByTicket(msg.to, Ti) 
                        G.preventedJoinByTicket = True
                        arisys.updateGroup(G)
#END OPERATIONS______________________________________________
#______________________________________________                       
                      
                     
                    
                   
                  
                

#______________________________________________
#______________________________________________                    
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = arisys.getAllContactIds()
                    for manusia in t:
                        arisys.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = arisys.getGroupIdsJoined()
                    for manusia in n:
                        arisys.sendMessage(manusia,(bctxt))
                elif "Gbcvc " in msg.text:
                    bctxt = msg.text.replace("Bcvoice ", "")
                    bc = ("Broadcastvoice ")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = arisys.getGroupIdsJoined()
                    for manusia in n:
                        arisys.sendAudio(manusia, 'tts.mp3')
 
                elif "Cbcvc " in msg.text:
                    bctxt = msg.text.replace("Cbcvoice ", "")
                    bc = ("Broadcastvoice ]")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = arisys.getAllContactIdsJoined()
                    for manusia in n:
                        arisys.sendAudio(manusia, 'tts.mp3')
#END OPERATIONS______________________________________________
#______________________________________________






#______________________________________________
#______________________________________________                        
                elif "Zk" in msg.text:
                    gs = arisys.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    arisys.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    arisys.kickoutFromGroup(msg.to,[midd])
                    arisys.findAndAddContactsByMid(midd)
                    arisys.inviteIntoGroup(msg.to,[midd])
                    arisys.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = arisys.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    arisys.kickoutFromGroup(msg.to,[target])
                                    arisys.findAndAddContactsByMid(target)
                                    arisys.inviteIntoGroup(msg.to,[target])
                                    arisys.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
#END OPERATIONS______________________________________________
#______________________________________________






#______________________________________________
#______________________________________________                                                  
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = arisys.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = arisys.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            arisys.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        arisys.sendMessage(to, "Batal\nWaktu: %s Seconds" % (elapsed_time))
                        arisys.sendMessage(to, "Jumlah:" + sinvitee)
                    else:
                        arisys.sendMessage(to, "Tidak ada daftar pendingan")                    
                elif text.lower() == 'gcancel':
                    gid = arisys.getGroupIdsInvited() 
                    start = time.time()
                    for i in gid:
                        arisys.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    arisys.sendMessage(to, "Semua Undangan Dibatalkan")
                    arisys.sendMessage(to, "Waktu: %s Seconds" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = arisys.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        arisys.updateGroup(X)
                    else:
                        arisys.sendMessage(msg.to,"Hanya di group")
#END OPERATIONS______________________________________________
#______________________________________________                       
                      
                     
                    
                   
                  
#______________________________________________
#______________________________________________                  
                elif text.lower().startswith('op '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        arisys.sendMessage(to, "Target Telah di tambahkan dalam daftar admin")
                elif text.lower().startswith('deop '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        arisys.sendMessage(to, "Target Telah di hapus dari Daftar Admin")
                elif text.lower().startswith('mop:'):
                        midd = msg.text.replace("mop:","")
                        admin.append(str(midd))
                        arisys.sendMessage(to, "Target Telah di tambahkan dalam daftar admin") 
                        backupData()
                elif text.lower().startswith('mdp:'):
                        midd = msg.text.replace("mdp:","")
                        admin.remove(str(midd))
                        arisys.sendMessage(to, "Target Telah di hapus dari Daftar Admin") 
                        backupData()
                elif text.lower() == 'opmid':
                    if admin == []:
                        arisys.sendMessage(to, "Tidak Ada Admin")
                    else:
                        mc = "Daftar admin："
                        for mi_d in admin:
                            mc += "\n-> " + mi_d
                        arisys.sendMessage(to, mc)
                elif text.lower() == 'oplist':
                    if admin == []:
                        arisys.sendMessage(to, "Admin Kosong")
                    else:
                        mc = "Daftar Admin："
                        for mi_d in admin:
                            mc += "\n ➡ " + arisys.getContact(mi_d).displayName
                        arisys.sendMessage(to, mc)                    
#END OPERATIONS______________________________________________
#______________________________________________






#______________________________________________
#______________________________________________                        
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = arisys.getContact(u)
                        cu = arisys.getProfileCoverURL(mid=u)
                        try:
                            arisys.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nStatus:\n" + contact.statusMessage + "\n\nurl :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nSampul :\n" + str(cu))
                        except:
                            arisys.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nStatus:\n" + contact.statusMessage + "\n\nsampul:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    arisys.findAndAddContactsByMid(midd)
                    arisys.inviteIntoGroup(msg.to,[midd])
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (text+"\n")
                    if txt[1] == "on":
                        if jmlh <= 10000:
                            for x in range(jmlh):
                                arisys.sendMessage(msg.to, text, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                        else:
                            arisys.sendMessage(msg.to, "Out Of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 10000:
                            arisys.sendMessage(msg.to, tulisan, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'Araragikanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                        else:
                            arisys.sendMessage(msg.to, "Out Of Range!")
                elif "take" in msg.text:
                    list_ = msg.text.split(":")
                    try:
                        arisys.acceptGroupInvitationByTicket(list_[1],list_[2])
                        G = arisys.getGroup(list_[1])
                        if G.preventedJoinByTicket == True:
                            pass
                        else:
                            G.preventedJoinByTicket = True
                            arisys.updateGroup(G)
                    except:
                        arisys.sendMessage(msg.to,"error\n"+list_[1]+'\n'+list_[2])     
#END OPERATIONS______________________________________________
#______________________________________________                       
                      
                     
                    
                   
                  
#______________________________________________
#______________________________________________                  
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] BLACKLIST")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    araragiayane.sendMessage(to, "target masuk dalam blacklist")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] BLACKLIST")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    araragiayane.sendMessage(to, "target di kluarkan dalam Blacklist ")
                                except:
                                    pass
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    araragiayane.sendMessage(to, "Daftar blacklist di bersihkan")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        araragiayane.sendMessage(to, "Tidak ada daftar hitam ")
                    else:
                        araragiayane.sendMessage(to, "Tidak ada daftar hitam ")
                        try:
                            mc = "BLACKLIST\n\n"
                            for mi_d in settings["blacklist"]:
                                mc += "✅ " + araragiayane.getContact(mi_d).displayName + "\n"
                            araragiayane.sendMessage(to, mc)
                        except:
                            pass
                elif text.lower() == 'banmid':
                    if settings["blacklist"] == {}:
                        araragiayane.sendMessage(to, "Tidak ada daftar hitam ")
                    else:
                        araragiayane.sendMessage(to, "Tidak ada daftar hitam ")
                        try:
                            mc = "BLACKLIST\n\n"
                            for mi_d in settings["blacklist"]:
                                mc += "✅ " + mi_d + "\n"
                            araragiayane.sendMessage(to, mc)
                        except:
                            pass
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = arisys.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            arisys.sendMessage(to, "Blacklist kosong")
                            return
                        for jj in matched_list:
                            arisys.kickoutFromGroup(to, [jj])
                            arisys.sendMessage(to, "Berhasil menyingkirkan para pidana")
                elif text.lower() == 'killbanall':
                    gid = arisys.getGroupIdsJoined()
                    group = arisys.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        arisys.sendMessage(to, "Kosong")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                arisys.kickoutFromGroup(i, [jj])
                            arisys.sendMessage(i, "Berhasil menyingkirkan para pidana di semua group")
#END OPERATIONS______________________________________________
#______________________________________________







#______________________________________________
#______________________________________________                            
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        arisys.sendMessage(to, "Silahakan masukan ID group target")
                    else:
                        try:
                            arisys.findAndAddContactsByMid(msg._from)
                            arisys.inviteIntoGroup(gid,[msg._from])
                        except:
                            arisys.sendMessage(to, "Eror 404")
                elif msg.text in ["fl"]:
                    anl = arisys.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+arisys.getContact(q).displayName + "\n"
                    arisys.sendMessage(msg.to,"「 Daftar 」\n"+ap+"Nomor : "+str(len(anl)))
#END OPERATIONS______________________________________________
#______________________________________________





#______________________________________________
#______________________________________________                       
                elif text.lower() == 'sp':
                    start = time.time()
                    elapsed_time = (time.time() - start)/0.0005
                    arisys.sendMessage(to,format(str(elapsed_time)) + " seconds", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    ayane.sendMessage(to,format(str(elapsed_time)) + " seconds", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    start2 = time.time()
                    elapsed_time = (time.time() - start)/0.0005
                    aryane.sendMessage(to,format(str(elapsed_time)) + " Seconds", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    ayane.sendMessage(to,'Speeds up the system \n' + str1 + ' Seconds', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    elapsed_time = time.time() - start
                    araragiayane.sendMessage(to,'Commands Reaction \n' + format(str(elapsed_time)) + ' Seconds', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'reset':
                    arisys.sendMessage(to, "Program berhasil di restart", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    arisys.sendMessage(to, "Program Processing {}".format(str(runtime)), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u9cdc29cb1452168cadae627171b7a6ee"
                        creator = arisys.getContact(owner)
                        contact = arisys.getContact(arisysMID)
                        grouplist = arisys.getGroupIdsJoined()
                        contactlist = arisys.getAllContactIds()
                        blockedlist = arisys.getBlockedContactIds()
                        ret_ = "╔══[ About Self ]"
                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Beta Test"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚══[ ☂⃟👑⃟₳ṛḁ̶ṝấḡḭ⃟ᵃᵞ⃟🛡️⃟࿐ ]"
                        arisys.sendMessage(to, str(ret_))
                    except Exception as e:
                        arisys.sendMessage(msg.to, str(e))
                        
#settingan___________________________________________________________________________________________________________________
                        
                elif text.lower() == 'set':
                    try:
                        ret_ = "[ STATUS ]"
                        if settings["autoAdd"] == True: ret_ += "\n✅ AutoAdders "
                        else: ret_ += "\n❌ AutoAdders "
                        if settings["autoJoin"] == True: ret_ += "\n✅ Auto Joined "
                        else: ret_ += "\n❌ Auto Joined "
                        if settings["autoJoinTicket"] == True: ret_ += "\n✅ Joined ticktet "
                        else: ret_ += "\n❌ Joined ticktet "
                        if settings["autoLeave"] == True: ret_ += "\n✅ Auto leave group "
                        else: ret_ += "\n❌ Auto leave group "
                        if settings["autoRead"] == True: ret_ += "\n✅ Read messages "
                        else: ret_ += "\n❌ Read messages "
                        if settings["protect"] == True: ret_ += "\n✅ Protected "
                        else: ret_ += "\n❌ Protected "
                        if settings["inviteprotect"] == True: ret_ += "\n✅ Protect Invit "
                        else: ret_ += "\n❌ Protect Invite "
                        if settings["qrprotect"] == True: ret_ += "\n✅ Qr Protection "
                        else: ret_ += "\n❌ Qr Protection "
                        if settings["contact"] == True: ret_ += "\n✅ Kontack "
                        else: ret_ += "\n❌ Kontak "
                        if settings["reread"] == True: ret_ += "\n✅ Unsend Message "
                        else: ret_ += "\n❌ Unsend message"
                        if settings["detectMention"] == False: ret_ += "\n✅ Detect Mention "
                        else: ret_ += "\n❌ Detect mention "
                        if settings["checkSticker"] == True: ret_ += "\n✅ Check Stikers "
                        else: ret_ += "\n❌ Check stikers "
                        if settings["kickContact"] == True: ret_ += "\n✅ Kick kontak "
                        else: ret_ += "\n❌ Kick kontak "
                        if settings["autoPtt"] == True: ret_ += "\n✅ Automatically Ptt "
                        else: ret_ += "\n❌ Automatically Ptt "
                        if settings["seeLeave"] == True: ret_ += "\n✅ Sambutan Leave "
                        else: ret_ += "\n❌ Sambutan Leave "
                        if settings["seeJoin"] == True: ret_ += "\n✅ Sambutan Join "
                        else: ret_ += "\n❌ Sambutan Join "
                        if settings["timeline"] == True: ret_ += "\n✅ Timeline "
                        else: ret_ += "\n❌ TimeLine "
                        arisys.sendMessage(to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                    except Exception as e:
                        arisys.sendMessage(msg.to, str(e), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/0hNF8lHc2jEWkFFTwbewpuPjlQHwRyOxchfXsMWnIWRwt7JVM7OnNZBnJFGgl8IlU5OXVeXCZFSA18', 'AGENT_NAME': 'AraragiKanega', 'AGENT_LINK': 'http://line.me/ti/p/~araragi.'})
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    arisys.sendMessage(to, "System Auto add di hidupkan ")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    arisys.sendMessage(to, "System auto add di matikan")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    arisys.sendMessage(to, "System join otomatis di hidupkan")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    arisys.sendMessage(to, "System joim otomatis di matikan")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    arisys.sendMessage(to, "System Otomatis leave di hidupkan")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    arisys.sendMessage(to, "System otomatis leave di matikan")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    arisys.sendMessage(to, "System Cek kontak di hidupkan")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    arisys.sendMessage(to, "System cek kontak di matikan")
                elif text.lower() == 'groupprotect on':
                    settings["protect"] = True
                    arisys.sendMessage(to, "System protection group di hidupkan")
                elif text.lower() == 'groupprotect off':
                    settings["protect"] = False
                    arisys.sendMessage(to, "System Protection group di matikan")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    arisys.sendMessage(to, "System Protect invite di hidupkan")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    arisys.sendMessage(to, "System Protect invite di matikan ")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    arisys.sendMessage(to, "System Protect qr di hidupkan")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    arisys.sendMessage(to, "System protect qr di matikan")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    arisys.sendMessage(to, "System unsend di hidupkan")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    arisys.sendMessage(to, "System unsend di matikan")
                elif text.lower() == 'un on':
                    settings["reread"] = True
                    arisys.sendMessage(to, "System unsend di hidupkan")
                elif text.lower() == 'un off':
                    settings["reread"] = False
                    arisys.sendMessage(to, "System unsend di matikan")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    arisys.sendMessage(to, "System otomatis read di hidupkan")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    arisys.sendMessage(to, "System otomatis read di matikan")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    arisys.sendMessage(to, "System join otomatis via qr di hidupkan")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    arisys.sendMessage(to, "System join otomatis via qr di matikan")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = False
                    arisys.sendMessage(to, "System respon summon di hidupkan")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = True
                    arisys.sendMessage(to, "System respon summon di matikan")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    arisys.sendMessage(to, "System Check stikers di hidupkan")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    arisys.sendMessage(to, "System check stikers di matikan")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    arisys.sendMessage(to, "System kick kontak di hidupkan")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    arisys.sendMessage(to, "System kick konta di mstikan")
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    arisys.sendMessage(to, "System leave otomatis di hidupkan")
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    arisys.sendMessage(to, "System leave otomatis di matikan")
                elif text.lower() == 'timeline on':
                    settings["timeline"] = True
                    arisys.sendMessage(to, "System Check Timeline di hidupkan")
                elif text.lower() == 'timeline off':
                    settings["timeline"] = False
                    arisys.sendMessage(to, "System check Timeline di matikan")
                elif text.lower() == 'seejoin on':
                    settings["seeJoin"] = True
                    arisys.sendMessage(to, "System Sambutan join di hidupkan")
                elif text.lower() == 'seejoin off':
                    settings["seeJoin"] = False
                    arisys.sendMessage(to, "System Sambutan join matikan")
                elif text.lower() == 'seeleave on':
                    settings["seeLeave"] = True
                    arisys.sendMessage(to, "System Sambutan leave di hidupkan")
                elif text.lower() == 'seeleave off':
                    settings["seeLeave"] = False
                    arisys.sendMessage(to, "System Sambutan leave di matikan") 
#END OPERATIONS______________________________________________
#______________________________________________







                   
#______________________________________________
#______________________________________________                    
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    arisys.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    arisys.sendMessage(msg.to,"" +  sender)
                elif text.lower() == 'myname':
                    me = arisys.getContact(sender)
                    arisys.sendMessage(msg.to,"" + me.displayName)
                elif text.lower() == 'mybio':
                    me = arisys.getContact(sender)
                    arisys.sendMessage(msg.to,"" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = arisys.getContact(sender)
                    arisys.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = arisys.getContact(sender)
                    cover = arisys.getProfileCoverURL(sender)
                    arisys.sendImageWithURL(msg.to, cover)
                elif text.lower() == 'removeallchat':
                    araragiayane.removeAllMessages(op.param2)
                    aryane.removeAllMessages(op.param2)
                    ayane.removeAllMessages(op.param2)
                    arisys.sendMessage(to, "Berhasil hapus semua chat")    
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = arisys.getContact(ls)
                            mi_d = contact.mid
                            arisys.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        arisys.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = arisys.getContact(ls)
                            arisys.sendMessage(msg.to, "" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = arisys.getContact(ls)
                            arisys.sendMessage(msg.to, "" + contact.statusMessage)
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + arisys.getContact(ls).pictureStatus
                            arisys.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("mpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + arisys.getContact(ls).pictureStatus
                            arisys.sendVideoWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = arisys.getProfileCoverURL(ls)
                                arisys.sendImageWithURL(msg.to, str(path))  
#END OPERATIONS______________________________________________
#______________________________________________





                              
#______________________________________________
#______________________________________________                              
                elif text.lower() == 'gowner':
                    group = arisys.getGroup(to)
                    GS = group.creator.mid
                    arisys.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = arisys.getGroup(to)
                    arisys.sendMessage(to, "[ID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = arisys.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = arisys.reissueGroupTicket(to)
                            arisys.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            arisys.sendMessage(to, "Silahkan Buka Url terlebih dahulu".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = arisys.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            arisys.sendMessage(to, "Url group sudah di aktifkan")
                        else:
                            G.preventedJoinByTicket = False
                            arisys.updateGroup(G)
                            arisys.sendMessage(to, "Berhasil mengaktifkan url group oleh system")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = arisys.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            arisys.sendMessage(to, "Url group sudah di Nonaktifkan")
                        else:
                            G.preventedJoinByTicket = True
                            arisys.updateGroup(G)
                            arisys.sendMessage(to, "Berhasil menonaktifkan url group oleh system")
                elif text.lower() == 'ginfo':
                    group = arisys.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak Di kenal"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Open"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(arisys.reissueGroupTicket(group.id)))
                    else:
                        gQr = "Close"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(arisys.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    arisys.sendMessage(to, str(ret_))
                    arisys.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = arisys.getGroup(to)
                        ret_ = "[Daftar anggota]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[Total： {} Ekor]".format(str(len(group.members)))
                        arisys.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        groups = arisys.groups
                        ret_ = "[Daftar Group]"
                        no = 0 + 1
                        for gid in groups:
                            group = arisys.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[Total {} group]".format(str(len(groups)))
                        arisys.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
                    group = arisys.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        arisys.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
#END OPERATIONS______________________________________________
#______________________________________________                      
                      
                     
                    
             


      
#______________________________________________
#______________________________________________                   
                elif text.lower() == 'sn':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                arisys.sendMessage(msg.to,"Sider siap untuk di cyduk 􀨁􀇝looking right􏿿")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            arisys.sendMessage(msg.to, "Setel Titik baca:\n" + readTime)
                elif text.lower() == 'sf':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        arisys.sendMessage(msg.to,"Titik baca telah di tutup")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        arisys.sendMessage(msg.to, "Berhasil di setting ulang :\n" + readTime)
                elif text.lower() == 'sr':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nWaktu : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        arisys.sendMessage(msg.to, "Setel ulang point baca:\n" + readTime)
                    else:
                        arisys.sendMessage(msg.to, "Titik baca di atur")
                elif text.lower() == 'r':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nWaktu : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            arisys.sendMessage(receiver,"[ sider ]:\n")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = arisys.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Sider ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Waktu ]: \n" + readTime
                        try:
                            arisys.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        arisys.sendMessage(receiver,"Atur titik baca njerrr..")
#END OPERATIONS______________________________________________
#______________________________________________






#______________________________________________
#______________________________________________
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        arisys.log("[%s]"%(msg._from)+msg.text)
                    else:
                        arisys.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            print("[65] NOTIFIED_DESTROY_MESSAGE")
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            arisys.sendMessage(at,"[Terpidana unsend messaging]\n%s\n[Messages]\n%s"%(arisys.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["Ingat Pesan"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
#END OPERATIONS______________________________________________
#______________________________________________








#OP______________________________________________
#______________________________________________
        if op.type == 32:
            print("[32] NOTIFIED_CANCEL_INVITATION_GROUP")
            
        if op.type == 35:
            print("[35] NOTIFIED_REJECT_GROUP_INVITATION")
       
        if op.type == 40:
            print("[40] SEND_CHAT_CHECKED")
            
        if op.type == 55:
            print("[55] NOTIFIED_READ_MESSAGE")
       
        if op.type == 65:
            print("[65] NOTIFIED_DESTROY_MESSAGE")
            
        if op.type == 68:
            print("[68] NOTIFIED_BLOCK_CONTACT")
       
        if op.type == 69:
            print("[69] NOTIFIED_UNBLOCK_CONTACT")
            
        if op.type == 84:
            print("[84] NOTIFIED_ADD_FOLLOW")
        
        if op.type == 86:
            print("[86] NOTIFIED_DELETE_FOLLOW")
            
        if op.type == 88:
            print("[88] NOTIFIED_FRIEND_REQUEST")
        
#END OPERATIONS______________________________________________
#______________________________________________







#END OPERATIONS______________________________________________
#______________________________________________               
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != arisys.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    aryane.sendChatChecked(to, msg_id)
                    araragiayane.sendChatChecked(to, msg_id)
                    ayane.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in arisysMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if settings["detectMention"] == False:
                            contact = arisys.getContact(sender)
                            arname = contact.displayName
                            #respon = [arname + " ngapain sih tag tag mulu (╬ﾟ◥益◤ﾟ)", arname + " heh kutil kuda brisik paha gw getar nih lu tag mulu (┛◉Д◉)┛彡┻━┻ ",arname + " kampret lu ngapain tag, kurbel ??",arname + " cieee yang tag mulu cinta ya ⚈ ̫ ⚈"]
                            respon = ["[ Responded ]\n\n" + arname + " kenapa ngke ?"] 
                            ret_ = random.choice(respon)
                            name = re.findall(r'@(\w+)', text) 
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                if arisysMID in mention["M"]:
                                    arisys.sendMessage(to,ret_) 
                                    break
        if op.type == 55:
            print ("[55] READER ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e) 