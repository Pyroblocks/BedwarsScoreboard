#import dependencies
import time
import PIL 
from kill_messages import kill_fd_msg,kill_bow_msg,kill_msg,kill_void_msg,bed_break_msg #list of kill/bed break messages
import pandas as pd

#setup logs reading
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.2)
            continue
        yield line

imglink = "https://cravatar.eu/helmavatar/{}/256.png"
print(imglink.format("Pyroblocks"))

#your Minecraft username
you = "Pyroblocks"
mode = "doubles" #solos, doubles, threes, fours, ranked

#Due to the limitations of the Minecraft chat logs (and my lackluster coding skills), I am unable to detect players in a game as it starts,
#and I am fully unable to detect what team specific players are on (kill/death/bed break messages are color coded by team, and not be color codes).
#Hopefully I can find a solution to this in the future.

#INPUT TEAM MEMBERS (Minecraft username)

#for solos input color1 for all colors
#for doubles input color1 & color2 for all colors
#for threes input color1, color2, & color3 for red, blue, green, & yellow
#for fours input color1, color2, color3, & color4 for red, blue, green, & yellow
#for ranked input color1, color2, color3, & color4 for red & green
red1 = "r"
red2 = "r2"
red3 = "r3"
red4 = "r4"
blue1 = "b"
blue2 = "b2"
blue3 = "b3"
blue4 = "b4"
green1 = "g"
green2 = "g2"
green3 = "g3"
green4 = "g4"
yellow1 = "y"
yellow2 = "y2"
yellow3 = "y3"
yellow4 = "y4"
white1 = "w"
white2 = "w2"
aqua1 = "a"
aqua2 = "a2"
pink1 = "p"
pink2 = "p2"
gray1 = "s"
gray2 = "s2"

#solos dataframe
if mode == "solos":
    d = {
        "Red" : ["N/A", "N/A", "N/A", False, False], red1: [0,0,0,False,0],
        "Blue" : ["N/A", "N/A", "N/A", False, False], blue1: [0,0,0,False,0],
        "Green" : ["N/A", "N/A", "N/A", False, False], green1: [0,0,0,False,0],
        "Yellow" : ["N/A", "N/A", "N/A", False, False], yellow1: [0,0,0,False,0],
        "Aqua" : ["N/A", "N/A", "N/A", False, False], aqua1: [0,0,0,False,0],
        "White" : ["N/A", "N/A", "N/A", False, False], white1: [0,0,0,False,0],
        "Pink" : ["N/A", "N/A", "N/A", False, False], pink1: [0,0,0,False,0],
        "Gray" : ["N/A", "N/A", "N/A", False, False], gray1: [0,0,0,False,0]
        }
    df = pd.DataFrame(data=d, index=["Kills", "Deaths", "Final Kills", "Eliminated", "Beds Broken/Bed Broken"])
    print(df.head(8))

#doubles dataframe
if mode == "doubles":
    d = {
        "Red" : ["N/A", "N/A", "N/A", False, False], red1: [0,0,0,False,0], red2: [0,0,0,False,0], 
        "Blue" : ["N/A", "N/A", "N/A", False, False], blue1: [0,0,0,False,0], blue2: [0,0,0,False,0],
        "Green" : ["N/A", "N/A", "N/A", False, False], green1: [0,0,0,False,0], green2: [0,0,0,False,0],
        "Yellow" : ["N/A", "N/A", "N/A", False, False], yellow1: [0,0,0,False,0], yellow2: [0,0,0,False,0],
        "Aqua" : ["N/A", "N/A", "N/A", False, False], aqua1: [0,0,0,False,0], aqua2: [0,0,0,False,0],
        "White" : ["N/A", "N/A", "N/A", False, False], white1: [0,0,0,False,0], white2: [0,0,0,False,0],
        "Pink" : ["N/A", "N/A", "N/A", False, False], pink1: [0,0,0,False,0], pink2: [0,0,0,False,0],
        "Gray" : ["N/A", "N/A", "N/A", False, False], gray1: [0,0,0,False,0], gray2: [0,0,0,False,0]
        }
    df = pd.DataFrame(data=d, index=["Kills", "Deaths", "Final Kills", "Eliminated", "Beds Broken/Bed Broken"])
    print(df.head(8))

#threes dataframe
if mode == "threes":
    d = {
        "Red" : ["N/A", "N/A", "N/A", False, False], red1: [0,0,0,False,0], red2: [0,0,0,False,0], red3: [0,0,0,False,0],
        "Blue" : ["N/A", "N/A", "N/A", False, False], blue1: [0,0,0,False,0], blue2: [0,0,0,False,0], blue3: [0,0,0,False,0],
        "Green" : ["N/A", "N/A", "N/A", False, False], green1: [0,0,0,False,0], green2: [0,0,0,False,0], green3: [0,0,0,False,0],
        "Yellow" : ["N/A", "N/A", "N/A", False, False], yellow1: [0,0,0,False,0], yellow2: [0,0,0,False,0], yellow3: [0,0,0,False,0]
        }
    df = pd.DataFrame(data=d, index=["Kills", "Deaths", "Final Kills", "Eliminated", "Beds Broken/Bed Broken"])
    print(df.head(8))
    
#fours dataframe
if mode == "fours":
    d = {
        "Red" : ["N/A", "N/A", "N/A", False, False], red1: [0,0,0,False,0], red2: [0,0,0,False,0], red3: [0,0,0,False,0], red4: [0,0,0,False,0],
        "Blue" : ["N/A", "N/A", "N/A", False, False], blue1: [0,0,0,False,0], blue2: [0,0,0,False,0], blue3: [0,0,0,False,0], blue4: [0,0,0,False,0],
        "Green" : ["N/A", "N/A", "N/A", False, False], green1: [0,0,0,False,0], green2: [0,0,0,False,0], green3: [0,0,0,False,0], green4: [0,0,0,False,0],
        "Yellow" : ["N/A", "N/A", "N/A", False, False], yellow1: [0,0,0,False,0], yellow2: [0,0,0,False,0], yellow3: [0,0,0,False,0], yellow4: [0,0,0,False,0]
        }
    df = pd.DataFrame(data=d, index=["Kills", "Deaths", "Final Kills", "Eliminated", "Beds Broken/Bed Broken"])
    print(df.head(8))

#ranked dataframe
if mode == "ranked":
    d = {
        "Red" : ["N/A", "N/A", "N/A", False, False], red1: [0,0,0,False,0], red2: [0,0,0,False,0], red3: [0,0,0,False,0], red4: [0,0,0,False,0],
        "Green" : ["N/A", "N/A", "N/A", False, False], green1: [0,0,0,False,0], green2: [0,0,0,False,0], green3: [0,0,0,False,0], green4: [0,0,0,False,0]
        }
    df = pd.DataFrame(data=d, index=["Kills", "Deaths", "Final Kills", "Eliminated", "Beds Broken/Bed Broken"])
    print(df.head(8))

#event functions
def on_bed_break(msg):
    if "'s" in msg:
        msg = msg.replace("'s","",1)
    else:
        msg = msg
    #print(msg)
    if "holiday spirit" in msg:
        breaker = msg.split(" ")
        breaker = breaker[-3]
    else:
        breaker = msg.split(" ")
        breaker = breaker[-1]
        breaker = breaker[:-1]
    #print(breaker)
    bed = msg.split(" ")
    bed = bed[3]
    #print(bed)
    print(breaker + " broke " + bed + " Team's bed!")
    return(breaker, bed)

def on_kill(msg):
    if "'s" in msg:
        msg = msg.replace("'s","",1)
    else:
        msg = msg
    #print(msg)
    if "FINAL" in msg:
        isfinal = True
        if "final" in msg:
            killer = msg.split(" ")
            #print(killer)
            killer = killer[-5]
        else:
            killer = msg.split(" ")
            #print(killer)
            killer = killer[-3]
            killer = killer[:-1]
        #print(killer)
        dead = msg.split(" ")
        dead = dead[0]
        #print(dead)
        print(killer + " killed " + dead + " (FINAL KILL)")
    else:
        isfinal = False
        killer = msg.rpartition(' ')[-1]
        killer = killer[:-1]
        #print(killer)
        dead = msg.split(" ")
        dead = dead[0]
        #print(dead)
        print(killer + " killed " + dead)
    return(killer, dead, isfinal)

def on_void_kill(msg):
    if "'s" in msg:
        msg = msg.replace("'s","",1)
    else:
        msg = msg
    if "FINAL" in msg:
        isfinal = True
        if "holiday spirit" in msg:
            killer = msg.split(" ")
            killer = killer[-5]
        else:
            killer = msg.split(" ")
            killer = killer[-3]
            killer = killer[:-1]
        #print(killer)
        dead = msg.split(" ")
        dead = dead[0]
        #print(dead)
        print(killer + " voided " + dead + " (FINAL KILL)")
    else:
        isfinal = False
        if "holiday spirit" in msg:
            killer = msg.split(" ")
            killer = killer[-3]
        else:
            killer = msg.split(" ")
            killer = killer[-1]
            killer = killer[:-1]
        #print(killer)
        dead = msg.split(" ")
        dead = dead[0]
        #print(dead)
        print(killer + " voided " + dead)
    return(killer, dead, isfinal)

def on_bow_kill(msg):
    if "'s" in msg:
        msg = msg.replace("'s","",1)
    else:
        msg = msg
    #print(msg)
    if "FINAL" in msg:
        isfinal = True
        killer = msg.split(" ")
        #print(killer)
        killer = killer[-3]
        killer = killer[:-1]
        #print(killer)
        dead = msg.split(" ")
        dead = dead[0]
        #print(dead)
        print(killer + " killed " + dead + " with a bow (FINAL KILL)")
    else:
        isfinal = False
        killer = msg.rpartition(' ')[-1]
        killer = killer[:-1]
        #print(killer)
        dead = msg.split(" ")
        dead = dead[0]
        #print(dead)
        print(killer + " killed " + dead + " with a bow")
    return(killer, dead, isfinal)

def on_fd_kill(msg):
    if "'s" in msg:
        msg = msg.replace("'s","",1)
    else:
        msg = msg
    #print(msg)
    if "FINAL" in msg:
        isfinal = True
        if "holiday spirit" in msg:
            killer = msg.split(" ")
            killer = killer[-5]
        else:
            killer = msg.split(" ")
            killer = killer[-3]
            killer = killer[:-1]
        #print(killer)
        dead = msg.split(" ")
        dead = dead[0]
        #print(dead)
        print(killer + " killed " + dead + " via fall damage (FINAL KILL)")
    else:
        isfinal = False
        if "holiday spirit" in msg:
            killer = msg.split(" ")
            killer = killer[-5]
        else:
            killer = msg.rpartition(' ')[-1]
            killer = killer[:-1]
        #print(killer)
        dead = msg.split(" ")
        dead = dead[0]
        #print(dead)
        print(killer + " killed " + dead + " via fall damage")
    return(killer, dead, isfinal)

def on_void(msg):
    user = msg.rpartition(' fell into the void.')[0]
    #print(user)
    if "FINAL" in msg:
        isfinal = True
        print(user + " voided (FINAL KILL)")
    else:
        isfinal = False
        print(user + " voided")
    return(user, isfinal)

def on_disconnect(msg):
    user = msg.rpartition(' disconnected.')[0]
    #print(user)
    if "FINAL" in msg:
        isfinal = True
        print(user + " DCed (FINAL KILL)")
    else:
        isfinal = False
        print(user + " DCed")
    return(user, isfinal)

def on_reconnect(msg):
    user = msg.rpartition(' reconnected.')[0]
    #print(user)
    print(user + " RCed")
    return(user)

def on_death(msg):
    user = msg.rpartition(' died.')[0]
    #print(user)
    if "FINAL" in msg:
        isfinal = True
        print(user + " died (FINAL KILL)")
    else:
        isfinal = False
        print(user + " died")
    return(user, isfinal)

def on_win(msg):
    team = msg.rpartition(' - ')[0]
    team = team.replace(" ","")
    user = msg.rpartition(' - ')[-1]
    user = user.replace("[YT] ", "", 1)
    user = user.replace("[MVP++] ", "", 1)
    user = user.replace("[MVP+] ", "", 1)
    user = user.replace("[MVP] ", "", 1)
    user = user.replace("[VIP+] ", "", 1)
    user = user.replace("[VIP] ", "", 1)
    print(user + " wins! (" + team + ")")
    return(user, team)

def on_map(msg):
    map = msg.rpartition('You are currently playing on ')[-1]
    print("The map is " + map)
    return(map)

def on_1k(msg):
    kills = msg.rpartition(' - ')[-1]
    user = msg.rpartition(' - ')[-3]
    user = user.rpartition(' ')[-1]
    print(user + " was the top killer with " + kills + " kills.")
    return(user,kills)

def on_2k(msg):
    kills = msg.rpartition(' - ')[-1]
    user = msg.rpartition(' - ')[-3]
    user = user.rpartition(' ')[-1]
    print(user + " was the second killer with " + kills + " kills.")
    return(user,kills)

def on_3k(msg):
    kills = msg.rpartition(' - ')[-1]
    user = msg.rpartition(' - ')[-3]
    user = user.rpartition(' ')[-1]
    print(user + " was the third killer with " + kills + " kills.")
    return(user,kills)

def on_elimination(msg):
    for i in range (4):
        msg = msg.rpartition(' ')[0]
    team = msg.rpartition(' ')[-1]
    #print(team)
    print(team + " Team was eliminated!")
    return(team)

#main function
if __name__ == "__main__":
    #read chat
    logfile = open("C:/Users/gemki/.lunarclient/offline/1.8.9/logs/latest.log", "r")
    loglines = follow(logfile)
    for line in loglines:
        if "[Client thread/INFO]: [CHAT]" in line:
            #print(line)
            #filter to just messages
            lineedit = line.rpartition('[CHAT]')[2]
            lineedit = lineedit.replace('\n','',1)
            lineedit = lineedit[1:]
            #print(lineedit)
            #check for events
            if "died." in lineedit:
                death = on_death(lineedit)
                col = df.columns.get_loc(death[0])
                if death[1] == True:
                    df.iloc[3, col] = True
                df.iloc[col, 1] += 1
                #print(df.head())
            elif ("fell into the void." in lineedit) and (":" not in lineedit):
                void = on_void(lineedit)
                col = df.columns.get_loc(void[0])
                if void[1] == True:
                    df.iloc[3, col] = True
                df.iloc[col, 1] += 1
                #print(df.head())
            elif ("disconnected." in lineedit) and (":" not in lineedit):
                dc = on_disconnect(lineedit)
                col = df.columns.get_loc(dc[0])
                if dc[1] == True:
                    df.iloc[3, col] = True
                #print(df.head())
            elif ("reconnected." in lineedit) and (":" not in lineedit):
                rc = on_reconnect(lineedit)
            elif any(item in lineedit for item in kill_msg) and (":" not in lineedit):
                kill = on_kill(lineedit)
                kcol = df.columns.get_loc(kill[0])
                dcol = df.columns.get_loc(kill[1])
                if kill[2] == True:
                    df.iloc[3, dcol] = True
                    df.iloc[2, kcol] += 1
                df.iloc[1, dcol] += 1
                df.iloc[0,kcol] += 1
                #print(df.head())
            elif any(item in lineedit for item in kill_void_msg) and (":" not in lineedit):
                vk = on_void_kill(lineedit)
                vkkcol = df.columns.get_loc(vk[0])
                vkdcol = df.columns.get_loc(vk[1])
                if vk[2] == True:
                    df.iloc[3, vkdcol] = True
                    df.iloc[2, vkkcol] += 1
                df.iloc[1, vkdcol] += 1
                df.iloc[0,vkkcol] += 1
                #print(df.head())
            elif any(item in lineedit for item in bed_break_msg) and (":" not in lineedit):
                bb = on_bed_break(lineedit)
                if bb[1] == "Your":
                    lst = list(bb)
                    if (red1 or red2 or red3 or red4 == you):
                        lst[1] = "Red"
                    if (blue1 or blue2 or blue3 or blue4 == you):
                        lst[1] = "Blue"
                    if (green1 or green2 or green3 or green4 == you):
                        lst[1] = "Green"
                    if (yellow1 or yellow2 or yellow3 or yellow4 == you):
                        lst[1] = "Yellow"
                    if (aqua1 or aqua2 == you):
                        lst[1] = "Aqua"
                    if (white1 or white2 == you):
                        lst[1] = "White"
                    if (pink1 or pink2 == you):
                        lst[1] = "Pink"
                    if (gray1 or gray2 == you):
                        lst[1] = "Gray"
                    bb = tuple(lst)
                tcol = df.columns.get_loc(bb[1])
                bcol = df.columns.get_loc(bb[0])
                df.iloc[4, bcol] += 1
                df.iloc[4, tcol] = True
                #print(df.head())
            elif any(item in lineedit for item in kill_bow_msg) and (":" not in lineedit):
                bk = on_bow_kill(lineedit)
                bkkcol = df.columns.get_loc(bk[0])
                bkdcol = df.columns.get_loc(bk[1])
                if bk[2] == True:
                    df.iloc[3, bkdcol] = True
                    df.iloc[2, bkkcol] += 1
                df.iloc[1, bkdcol] += 1
                df.iloc[0,bkkcol] += 1
                #print(df.head())
            elif any(item in lineedit for item in kill_fd_msg) and (":" not in lineedit):
                fdk = on_fd_kill(lineedit)
                fdkkcol = df.columns.get_loc(fdk[0])
                fdkdcol = df.columns.get_loc(fdk[1])
                if fdk[2] == True:
                    df.iloc[3, fdkdcol] = True
                    df.iloc[2, fdkkcol] += 1
                df.iloc[1, fdkdcol] += 1
                df.iloc[0,fdkkcol] += 1
                #print(df.head())
            elif ("Red - " in lineedit) or ("Blue - " in lineedit) or ("Green - " in lineedit) or ("Yellow - " in lineedit) or ("Aqua - " in lineedit) or ("White - " in lineedit) or ("Pink - " in lineedit) or ("Gray - " in lineedit) and (":" not in lineedit):
                win = on_win(lineedit)
                print(df.head(8))
            elif ("You are currently playing on") in lineedit and (":" not in lineedit):
                map = on_map(lineedit)
            elif ("1st Killer - " in lineedit) and (":" not in lineedit):
                _1k = on_1k(lineedit)
            elif ("2nd Killer - " in lineedit) and (":" not in lineedit):
                _2k = on_2k(lineedit)
            elif ("3rd Killer" in lineedit) and (":" not in lineedit):
                _3k = on_3k(lineedit)
            elif ("TEAM ELIMINATED > " in lineedit) and (":" not in lineedit):
                elim = on_elimination(lineedit)
                try:
                    col = df.columns.get_loc(elim)
                    df.iloc[3, col] = True
                except KeyError:
                    print("Team not found")
                print(df.head())