import random
import tkinter

###############################################
#MAIN MENU WINDOW

wts=open("settings.txt","r")
global fs
fs=int(wts.read())
print(fs)
wts.close()

def Iron_Man():
    global cclass
    cclass="Iron_Man"
    gameplay()
def Captain_America():
    global cclass
    cclass="Captain_America"
    gameplay()
def Thor():
    global cclass
    cclass="Thor"
    gameplay()

def menug():
    global menu
    menu=tkinter.Tk()
    menu.title("Marvel War")
    menu.geometry("500x500")
    menu.configure(background="DarkSlateGray2", cursor="dot")
    
    print("Game initialised.\n")

    def togglefullscreen():
        global fs
        if fs==1:
            fs-=1
            fsy.configure(text="Disabled")
            menu.attributes("-fullscreen",False)
            print("Fullscreen disabled")
            wts=open("settings.txt","w")
            wts.write("0")
            wts.close()
            
        elif fs==0:
            fs+=1
            fsy.configure(text="Enabled")
            menu.attributes("-fullscreen",True)
            print("Fullscreen enabled")
            wts=open("settings.txt","w")
            wts.write("1")
            wts.close()


    title=tkinter.Label(menu, text="Marvel War", font=("Courier", 28, "bold"), pady=20,bg="DarkSlateGray2", fg="white")
    char1t=tkinter.Button(menu, text="Iron Man", command=Iron_Man, pady=20, width=100)
    char2t=tkinter.Button(menu, text="Captain America",command=Captain_America, pady=20, width=100)
    char3t=tkinter.Button(menu, text="Thor",command=Thor, pady=20, width=100)
    mexit=tkinter.Button(menu, text="Exit", command=exit)
    settings=tkinter.Label(menu, text="Settings", font=("Courier", 20, "bold"),bg="DarkSlateGray4", fg="white")
    flscrn=tkinter.Label(menu, text="Fullscreen",font=("Courier", 14), bg="DarkSlateGray4", fg="white")
    fsy=tkinter.Button(menu, text="", command=togglefullscreen)
    if fs==0:
        menu.attributes("-fullscreen",False)
        fsy.configure(text="Disabled")
    elif fs==1:
        menu.attributes("-fullscreen",True)
        fsy.configure(text="Enabled")

    mexit.pack(fill=tkinter.X, side=tkinter.BOTTOM)    
    title.pack()
    char1t.pack()
    char2t.pack()
    char3t.pack()
    settings.pack()
    flscrn.pack()
    fsy.pack()
    menu.mainloop()
###############################################
#GAME WINDOW
def gameplay():
    global menu
    menu.destroy()
    window=tkinter.Tk()
    window.title("Avenger War")
    window.geometry("640x480")
    window.configure(background="firebrick1", cursor="dot")
    if fs==0:
        window.attributes("-fullscreen",False)
    elif fs==1:
        window.attributes("-fullscreen",True)


    global basehp
    global health
    global cclass
    global tdmgp
    global tdmg
    tdmg=0
    tdmgp=0
    if cclass=="Iron_Man":
        m1mod=1.5
        m2mod=0.5
        m3mod=0.25
        health=150
        basehp=150
    elif cclass=="Captain_America":
        m1mod=0.75
        m2mod=1.59
        m3mod=0.25
        health=125
        basehp=125
    elif cclass=="Thor":
        m1mod=0.5
        m2mod=0.5
        m3mod=2
        health=200
        basehp=200

    global ehealth
    ehealth=int(round(health*1.2))
    global emodifier
    emodifier=1.25
    global ebasehp
    ebasehp=ehealth

    global pwin
    pwin=0

    def pwin():
        global ehealth
        if ehealth<=0:
            ehealthl.configure(text="Health: 0"+"/"+str(ebasehp))
            print("Player has won")
            global pwin
            pwin=1
            winner.configure(text="Player has won")

    def ewin():
        global health
        if health<=0:
            healthl.configure(text="Health: 0"+"/"+str(basehp))
            print("Enemy has won")
            global pwin
            pwin=1
            winner.configure(text="Enemy has won")

    def echance():
        global pwin
        global tdmg
        
        if pwin!=1:
            global health
            missche=random.randint(0,15)
            echance=random.randint(0,15)
            if echance>=5:
                if missche>=12:
                    print("Enemy attack missed!")
                    enemymove.configure(text="Enemy attack missed")
                else:
                    global ehealth
                    dmgdealt=int(round(random.randint(12,20)*emodifier))
                    health-=dmgdealt
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(int(round(health)))+"/"+str(basehp))
                    enemymove.configure(text="Enemy used: Fury Attack(Damage dealt: "+(str(dmgdealt))+")")
                    
            elif echance>=10:
                if missche>=10:
                    print("Enemy attack missed!")
                    enemymove.configure(text="Enemy attack missed")
                else:
                    global ehealth
                    dmgdealt=int(round(random.randint(14,26)*emodifier))
                    health-=dmgdealt
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(health)+"/"+str(basehp))
                    enemymove.configure(text="Enemy used: Flurry of Punches(Damage dealt: "+(str(dmgdealt))+")")
            
            elif echance<=4:
                global tdmg
                chance=1
                while chance<7:
                    dmgdealt=random.randint(2,7)*emodifier
                    tdmg+=int(round(dmgdealt))
                    health-=dmgdealt
                    chance=int(round(random.randint(0,11)))
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(int(round(health)))+"/"+str(basehp))
                enemymove.configure(text="Enemy used: Full Power Sword Attack(Damage dealt: "+(str(tdmg))+")")           
            tdmg=0
    
    def move1p():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=11:
                print("Player attack missed!")
            else:
                global dmgdealtp
                dmgdealtp=int(round(random.randint(9,21)*m1mod))
                ehealth-=dmgdealtp
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Damage dealt to enemy: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()


    def move2p():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=10:
                print("Player attack missed!")
            else:
                global dmgdealtp
                dmgdealtp==int(round(random.randint(14,26)*m2mod))
                ehealth-=dmgdealtp
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Damage dealt to enemy: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()

    def move3p():
        if pwin!=1:
            global ehealth
            global tdmgp
            chance=1
            while chance<7:
                dmgdealtp=random.randint(2,7)*m3mod
                tdmgp+=dmgdealtp
                ehealth-=dmgdealtp
                chance=int(round(random.randint(0,11)))
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
            playerddealt.configure(text="Damage dealt to enemy: "+str(tdmgp))
            tdmgp=0                
            pwin()
            echance()
            ewin()
    def move4p():
        if pwin!=1:
            global ehealth
            global tdmgp
            chance=1
            while chance<7:
                dmgdealtp=random.randint(2,25)
                tdmgp+=dmgdealtp
                ehealth-=dmgdealtp
                chance=int(round(random.randint(0,11)))
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
            playerddealt.configure(text="Damage dealt to enemy: "+str(tdmgp))
            tdmgp=0                
            pwin()
            echance()
            ewin()
    def restart():
        print("\nNew game loaded\n")
        window.destroy()
        menug()
		
        
    if cclass=="Iron_Man":
        player=tkinter.Label(window, text="Iron Man", font=("Courier", 24, "bold"))
        healthl=tkinter.Label(window, text=("Health: "+str(health)+"/"+str(basehp)), font=("Courier", 18))
        enemy=tkinter.Label(window, text="Thanos", font=("Courier", 24, "bold"))
        ehealthl=tkinter.Label(window, text=("Health: "+str(ehealth)+"/"+str(ebasehp)), font=("Courier", 18))
        move1=tkinter.Button(window, text="Laser Sword",background="gold3", command=move1p)
        move2=tkinter.Button(window, text="Missile Blast",background="gold3", command =move2p)
        move3=tkinter.Button(window, text="EMP",background="gold3", command=move3p)
        move4=tkinter.Button(window, text="Plasma Pulse",background="gold3", command=move4p)
        restart=tkinter.Button(window, text="Restart", command=restart)
        texit=tkinter.Button(window, text="Exit", command=exit)
        enemymove=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404",fg="white")
        playerddealt=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404", fg="white")
        winner=tkinter.Label(window, text="", font=("Courier", 14, "bold"), bg="#7F0404", fg="white")
    
        texit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
        player.pack(pady=10, padx=20, fill=tkinter.X)
        healthl.pack()
        move1.pack(pady=5)
        move2.pack(pady=5)
        move3.pack(pady=5)
        move4.pack(pady=5)
        playerddealt.pack()
        enemy.pack(pady=10, padx=20, fill=tkinter.X)
        ehealthl.pack()
        enemymove.pack()
        restart.pack(fill=tkinter.X, side=tkinter.BOTTOM)
        winner.pack(side=tkinter.BOTTOM)
        window.mainloop()
        
    if cclass=="Captain_America":
        
        
        player=tkinter.Label(window, text="Captain America", font=("Courier", 24, "bold"))
        healthl=tkinter.Label(window, text=("Health: "+str(health)+"/"+str(basehp)), font=("Courier", 18))
        enemy=tkinter.Label(window, text="Thanos", font=("Courier", 24, "bold"))
        ehealthl=tkinter.Label(window, text=("Health: "+str(ehealth)+"/"+str(ebasehp)), font=("Courier", 18))
        move1=tkinter.Button(window, text="Shield throw",background="RoyalBlue3",command=move1p)
        move2=tkinter.Button(window, text="Kick Combo",background="RoyalBlue3", command =move2p)
        move3=tkinter.Button(window, text="Justice Lock",background="RoyalBlue3", command=move3p)
        move4=tkinter.Button(window, text="Mjolnir attack",background="RoyalBlue3", command=move4p)
        restart=tkinter.Button(window, text="Restart", command=restart)
        texit=tkinter.Button(window, text="Exit", command=exit)
        enemymove=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404",fg="white")
        playerddealt=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404", fg="white")
        winner=tkinter.Label(window, text="", font=("Courier", 14, "bold"), bg="#7F0404", fg="white")
    
        texit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
        player.pack(pady=10, padx=20, fill=tkinter.X)
        healthl.pack()
        move1.pack(pady=5)
        move2.pack(pady=5)
        move3.pack(pady=5)
        move4.pack(pady=5)
        playerddealt.pack()
        enemy.pack(pady=10, padx=20, fill=tkinter.X)
        ehealthl.pack()
        enemymove.pack()
        restart.pack(fill=tkinter.X, side=tkinter.BOTTOM)
        winner.pack(side=tkinter.BOTTOM)
        window.mainloop()
 
    if cclass=="Thor":
        player=tkinter.Label(window, text="Thor", font=("Courier", 24, "bold"))
        healthl=tkinter.Label(window, text=("Health: "+str(health)+"/"+str(basehp)), font=("Courier", 18))
        enemy=tkinter.Label(window, text="Thanos", font=("Courier", 24, "bold"))
        ehealthl=tkinter.Label(window, text=("Health: "+str(ehealth)+"/"+str(ebasehp)), font=("Courier", 18))
        move1=tkinter.Button(window, text="Mjolnir attack",command=move1p)
        move2=tkinter.Button(window, text="Thunder blast", command =move2p)
        move3=tkinter.Button(window, text="Flight Attack", command=move3p)
        move4=tkinter.Button(window, text="Rain of Thunder", command=move4p)
        restart=tkinter.Button(window, text="Restart", command=restart)
        texit=tkinter.Button(window, text="Exit", command=exit)
        enemymove=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404",fg="white")
        playerddealt=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404", fg="white")
        winner=tkinter.Label(window, text="", font=("Courier", 14, "bold"), bg="#7F0404", fg="white")
    
        texit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
        player.pack(pady=10, padx=20, fill=tkinter.X)
        healthl.pack()
        move1.pack(pady=5)
        move2.pack(pady=5)
        move3.pack(pady=5)
        move4.pack(pady=5)
        playerddealt.pack()
        enemy.pack(pady=10, padx=20, fill=tkinter.X)
        ehealthl.pack()
        enemymove.pack()
        restart.pack(fill=tkinter.X, side=tkinter.BOTTOM)
        winner.pack(side=tkinter.BOTTOM)
        window.mainloop()
 
           

#Initialises the game
menug()

