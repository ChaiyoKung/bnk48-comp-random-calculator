from tkinter import *
from tkinter import messagebox
import random





def SelectMember():
    try:
        while True:
            Set = 1
            Coll = []
            #All = []
            Name = mylist.selection_get()
            D = len("♦ ♦ ♦ " + Name + " Comp ♦ ♦ ♦")
            Box = ["=" * (D-5)]
            #All.append("=" * (D+20))

            if Name in Mem:
                while True:
                    #Box = []
                    for i in range(0, 5):
                        MEM = random.choice(Mem)
                        TYPE = random.choice(Type)
                        Photo = MEM + TYPE
                        Box.append(Photo)

                        if (Photo == Name + " (C)" or Photo == Name + " (H)" or Photo == Name + " (F)"):
                            Coll.append(Photo)
                    Box.append("=" * (D-5))
                    #All.append(Box)
                    #All.append("=" * (D+20))

                    if Name + " (C)" in Coll and Name + " (H)" in Coll and Name + " (F)" in Coll:
                        break
                    
                    Set += 1
            break
            
        if Name == "Aom":
            Aom = PhotoImage(file="Member_Img_sng5/aom_sng5.png")
            img = Aom
        elif Name == "Bamboo":
            Bamboo = PhotoImage(file="Member_Img_sng5/bamboo_sng5.png")
            img = Bamboo
        elif Name == "Cake":
            Cake = PhotoImage(file="Member_Img_sng5/cake_sng5.png")
            img = Cake
        elif Name == "Cherprang":
            Cherprang = PhotoImage(file="Member_Img_sng5/cherprang_sng5.png")
            img = Cherprang
        elif Name == "Deenee":
            Deenee = PhotoImage(file="Member_Img_sng5/deenee_sng5.png")
            img = Deenee
        elif Name == "Faii":
            Faii = PhotoImage(file="Member_Img_sng5/faii_sng5.png")
            img = Faii
        elif Name == "Fifa":
            Fifa = PhotoImage(file="Member_Img_sng5/fifa_sng5.png")
            img = Fifa
        elif Name == "Fond":
            Fond = PhotoImage(file="Member_Img_sng5/fond_sng5.png")
            img = Fond
        elif Name == "Gygee":
            Gygee = PhotoImage(file="Member_Img_sng5/gygee_sng5.png")
            img = Gygee
        elif Name == "Izurina":
            Izurina = PhotoImage(file="Member_Img_sng5/izurina_sng5.png")
            img = Izurina
        elif Name == "Jaa":
            Jaa = PhotoImage(file="Member_Img_sng5/jaa_sng5.png")
            img = Jaa
        elif Name == "Jané":
            Jane = PhotoImage(file="Member_Img_sng5/jane_sng5.png")
            img = Jane
        elif Name == "Jennis":
            Jennis = PhotoImage(file="Member_Img_sng5/jennis_sng5.png")
            img = Jennis
        elif Name == "Jib":
            Jib = PhotoImage(file="Member_Img_sng5/jib_sng5.png")
            img = Jib
        elif Name == "June":
            June = PhotoImage(file="Member_Img_sng5/june_sng5.png")
            img = June
        elif Name == "Kaew":
            Kaew = PhotoImage(file="Member_Img_sng5/kaew_sng5.png")
            img = Kaew
        elif Name == "Kaimook":
            Kaimook = PhotoImage(file="Member_Img_sng5/kaimook_sng5.png")
            img = Kaimook
        elif Name == "Kate":
            Kate = PhotoImage(file="Member_Img_sng5/kate_sng5.png")
            img = Kate
        elif Name == "Khamin":
            Khamin = PhotoImage(file="Member_Img_sng5/khamin_sng5.png")
            img = Khamin
        elif Name == "Kheng":
            Kheng = PhotoImage(file="Member_Img_sng5/kheng_sng5.png")
            img = Kheng
        elif Name == "Korn":
            Korn = PhotoImage(file="Member_Img_sng5/korn_sng5.png")
            img = Korn
        elif Name == "Maira":
            Maira = PhotoImage(file="Member_Img_sng5/maira_sng5.png")
            img = Maira
        elif Name == "Mewnich":
            Mewnich = PhotoImage(file="Member_Img_sng5/mewnich_sng5.png")
            img = Mewnich
        elif Name == "Mind":
            Mind = PhotoImage(file="Member_Img_sng5/mind_sng5.png")
            img = Mind
        elif Name == "Minmin":
            Minmin = PhotoImage(file="Member_Img_sng5/minmin_sng5.png")
            img = Minmin
        elif Name == "Miori":
            Miori = PhotoImage(file="Member_Img_sng5/miori_sng5.png")
            img = Miori
        elif Name == "Mobile":
            Mobile = PhotoImage(file="Member_Img_sng5/mobile_sng5.png")
            img = Mobile
        elif Name == "Music":
            Music = PhotoImage(file="Member_Img_sng5/music_sng5.png")
            img = Music
        elif Name == "Myyu":
            Myyu = PhotoImage(file="Member_Img_sng5/myyu_sng5.png")
            img = Myyu
        elif Name == "Namneung":
            Namneung = PhotoImage(file="Member_Img_sng5/namneung_sng5.png")
            img = Namneung
        elif Name == "Namsai":
            Namsai = PhotoImage(file="Member_Img_sng5/namsai_sng5.png")
            img = Namsai
        elif Name == "Natherine":
            Natherine = PhotoImage(file="Member_Img_sng5/natherine_sng5.png")
            img = Natherine
        elif Name == "New":
            New = PhotoImage(file="Member_Img_sng5/new_sng5.png")
            img = New
        elif Name == "Niky":
            Niky = PhotoImage(file="Member_Img_sng5/niky_sng5.png")
            img = Niky
        elif Name == "Nine":
            Nine = PhotoImage(file="Member_Img_sng5/nine_sng5.png")
            img = Nine
        elif Name == "Nink":
            Nink = PhotoImage(file="Member_Img_sng5/nink_sng5.png")
            img = Nink
        elif Name == "Noey":
            Noey = PhotoImage(file="Member_Img_sng5/noey_sng5.png")
            img = Noey
        elif Name == "Oom":
            Oom = PhotoImage(file="Member_Img_sng5/oom_sng5.png")
            img = Oom
        elif Name == "Orn":
            Orn = PhotoImage(file="Member_Img_sng5/orn_sng5.png")
            img = Orn
        elif Name == "Pakwan":
            Pakwan = PhotoImage(file="Member_Img_sng5/pakwan_sng5.png")
            img = Pakwan
        elif Name == "Panda":
            Panda = PhotoImage(file="Member_Img_sng5/panda_sng5.png")
            img = Panda
        elif Name == "Phukkom":
            Phukkom = PhotoImage(file="Member_Img_sng5/phukkom_sng5.png")
            img = Phukkom
        elif Name == "Piam":
            Paim = PhotoImage(file="Member_Img_sng5/paim_sng5.png")
            img = Paim
        elif Name == "Pun":
            Pun = PhotoImage(file="Member_Img_sng5/pun_sng5.png")
            img = Pun
        elif Name == "Pupé":
            Pupe = PhotoImage(file="Member_Img_sng5/pupe_sng5.png")
            img = Pupe
        elif Name == "Ratah":
            Ratah = PhotoImage(file="Member_Img_sng5/ratah_sng5.png")
            img = Ratah
        elif Name == "Satchan":
            Satchan = PhotoImage(file="Member_Img_sng5/satchan_sng5.png")
            img = Satchan
        elif Name == "Stang":
            Stang = PhotoImage(file="Member_Img_sng5/stang_sng5.png")
            img = Stang
        elif Name == "Tarwaan":
            Tarwaan = PhotoImage(file="Member_Img_sng5/tarwaan_sng5.png")
            img = Tarwaan
        elif Name == "View":
            View = PhotoImage(file="Member_Img_sng5/view_sng5.png")
            img = View
        elif Name == "Wee":
            Wee = PhotoImage(file="Member_Img_sng5/wee_sng5.png")
            img = Wee
        
        root2 = Toplevel(bg='#1a2c78')

        root2.title("YOU GET")
        root2.iconbitmap("Icon/BNK48_icon.ico")

        top2 = Frame(root2)
        top2.pack(side=TOP, fill=BOTH)

        run2 = Frame(root2, bg="#1a2c78")
        run2.pack()

        Pic = Label(top2, image=img, bd='0')
        Pic.pack(side=LEFT)
        
        scrollBox = Scrollbar(top2)

        Boxlist = Listbox(top2, yscrollcommand=scrollBox.set, heigh=21, width=21, fg="white", bg="#ffa6bc")
        for PhoList in Box:
            Boxlist.insert(END, PhoList)
        Boxlist.pack(side=LEFT, fill=BOTH)

        scrollBox.config(command=Boxlist.yview)
        scrollBox.pack(side=LEFT, fill=Y)
        
        Label_5 = Label(run2, text="=" * (D-5), fg='#fff81f' , bg="#1a2c78")
        Label_5.pack()
        Label_6 = Label(run2, text=("♦ ♦ ♦ " + Name + " Comp ♦ ♦ ♦"), fg='#fff81f' , bg="#1a2c78")
        Label_6.pack()
        Label_7 = Label(run2, text="=" * (D-5), fg='#fff81f' , bg="#1a2c78")
        Label_7.pack()
        Label_8 = Label(run2, text=("Total", Set, "Set"), fg='#fff81f' , bg="#1a2c78")
        Label_8.pack()
        Label_9 = Label(run2, text=("Total", Set * 250, "Baht"), fg='#fff81f' , bg="#1a2c78")
        Label_9.pack()
        Label_10 = Label(run2, text="=" * (D-5), fg='#fff81f' , bg="#1a2c78")
        Label_10.pack()

        root2.mainloop()
        
    except:
            messagebox.showerror("Error", "Please select member")
        



root = Tk()

root.title("BNK48 Comp Random-Cal")
root.iconbitmap("Icon/BNK48_icon.ico")

Allmemb = PhotoImage(file="Member_Img_sng5/bnk48_allmemb.png")

'''''Color Code'''''
#3425c4 - Blue
#3affe2 - Light blue
#ffa6bc - Pink
#fff81f - Yellow
#21ff85 - Green
#1a2c78 - Purple

top = Frame(root, bg="#1a2c78")
top.pack(side=TOP, fill=BOTH)

Mem = ["Cherprang", "Izurina", "Jaa", "Jané", "Jennis", "Jib", "Kaew", "Kaimook",
       "Kate", "Korn", "Mind", "Miori", "Mobile", "Music", "Namneung", "Namsai",
       "Noey", "Orn", "Pun", "Pupé", "Satchan", "Tarwaan", "Aom", "Bamboo", "Cake",
       "Deenee", "Faii", "Fifa", "Fond", "Gygee", "June", "Khamin", "Kheng", "Maira",
       "Mewnich", "Minmin", "Myyu", "Natherine", "New", "Niky", "Nine", "Nink", "Oom",
       "Pakwan", "Panda", "Phukkom", "Paim", "Ratah", "Stang", "View", "Wee"]

Mem.sort()

Type = [" (C)", " (H)", " (F)"]

selectText = Label(top, text="♥  ♥  ♥   Select Member   ♥  ♥  ♥",fg="#fff81f", bg="#1a2c78")
selectText.pack(side=TOP)

okButton = Button(top, text="0K", command=SelectMember, bg="#ffa6bc", width=10, fg='#3425c4', bd='1')
okButton.pack(side=BOTTOM)

AllmemberImg = Label(top, image=Allmemb, bd="0")
AllmemberImg.pack(side=LEFT)

scrollMember = Scrollbar(top)

mylist = Listbox(top, yscrollcommand=scrollMember.set, heigh=20, bg='#3425c4', fg='#fff81f')
for mList in Mem:
    mylist.insert(END, mList)
mylist.pack(side=LEFT, fill=BOTH)

scrollMember.config(command=mylist.yview)
scrollMember.pack(side=LEFT, fill=Y)

root.mainloop()
