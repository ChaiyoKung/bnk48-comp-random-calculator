from tkinter import *
from tkinter import messagebox
import random
import webbrowser




def official_web():
    webbrowser.open_new('https://www.bnk48.com/')
    



    
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
            def Aom():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=52')
            link = Aom
        elif Name == "Bamboo":
            Bamboo = PhotoImage(file="Member_Img_sng5/bamboo_sng5.png")
            img = Bamboo
            def Bamboo():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=51')
            link = Bamboo
        elif Name == "Cake":
            Cake = PhotoImage(file="Member_Img_sng5/cake_sng5.png")
            img = Cake
            def Cake():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=50')
            link = Cake
        elif Name == "Cherprang":
            Cherprang = PhotoImage(file="Member_Img_sng5/cherprang_sng5.png")
            img = Cherprang
            def Cherprang():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=4')
            link = Cherprang
        elif Name == "Deenee":
            Deenee = PhotoImage(file="Member_Img_sng5/deenee_sng5.png")
            img = Deenee
            def Deenee():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=49')
            link = Deenee
        elif Name == "Faii":
            Faii = PhotoImage(file="Member_Img_sng5/faii_sng5.png")
            img = Faii
            def Faii():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=48')
            link = Faii
        elif Name == "Fifa":
            Fifa = PhotoImage(file="Member_Img_sng5/fifa_sng5.png")
            img = Fifa
            def Fifa():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=47')
            link = Fifa
        elif Name == "Fond":
            Fond = PhotoImage(file="Member_Img_sng5/fond_sng5.png")
            img = Fond
            def Fond():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=46')
            link = Fond
        elif Name == "Gygee":
            Gygee = PhotoImage(file="Member_Img_sng5/gygee_sng5.png")
            img = Gygee
            def Gygee():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=45')
            link = Gygee
        elif Name == "Izurina":
            Izurina = PhotoImage(file="Member_Img_sng5/izurina_sng5.png")
            img = Izurina
            def Izurina():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=25')
            link = Izurina
        elif Name == "Jaa":
            Jaa = PhotoImage(file="Member_Img_sng5/jaa_sng5.png")
            img = Jaa
            def Jaa():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=23')
            link = Jaa
        elif Name == "Jane":
            Jane = PhotoImage(file="Member_Img_sng5/jane_sng5.png")
            img = Jane
            def Jane():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=24')
            link = Jane
        elif Name == "Jennis":
            Jennis = PhotoImage(file="Member_Img_sng5/jennis_sng5.png")
            img = Jennis
            def Jennis():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=2')
            link = Jennis
        elif Name == "Jib":
            Jib = PhotoImage(file="Member_Img_sng5/jib_sng5.png")
            img = Jib
            def Jib():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=22')
            link = Jib
        elif Name == "Juné":
            June = PhotoImage(file="Member_Img_sng5/june_sng5.png")
            img = June
            def June():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=44')
            link = June
        elif Name == "Kaew":
            Kaew = PhotoImage(file="Member_Img_sng5/kaew_sng5.png")
            img = Kaew
            def Kaew():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=21')
            link = Kaew
        elif Name == "Kaimook":
            Kaimook = PhotoImage(file="Member_Img_sng5/kaimook_sng5.png")
            img = Kaimook
            def Kaimook():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=20')
            link = Kaimook
        elif Name == "Kate":
            Kate = PhotoImage(file="Member_Img_sng5/kate_sng5.png")
            img = Kate
            def Kate():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=19')
            link = Kate
        elif Name == "Khamin":
            Khamin = PhotoImage(file="Member_Img_sng5/khamin_sng5.png")
            img = Khamin
            def Khamin():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=43')
            link = Khamin
        elif Name == "Kheng":
            Kheng = PhotoImage(file="Member_Img_sng5/kheng_sng5.png")
            img = Kheng
            def Kheng():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=42')
            link = Kheng
        elif Name == "Korn":
            Korn = PhotoImage(file="Member_Img_sng5/korn_sng5.png")
            img = Korn
            def Korn():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=18')
            link = Korn
        elif Name == "Maira":
            Maira = PhotoImage(file="Member_Img_sng5/maira_sng5.png")
            img = Maira
            def Maira():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=41')
            link = Maira
        elif Name == "Mewnich":
            Mewnich = PhotoImage(file="Member_Img_sng5/mewnich_sng5.png")
            img = Mewnich
            def Mewnich():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=40')
            link = Mewnich
        elif Name == "Mind":
            Mind = PhotoImage(file="Member_Img_sng5/mind_sng5.png")
            img = Mind
            def Mind():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=16')
            link = Mind
        elif Name == "Minmin":
            Minmin = PhotoImage(file="Member_Img_sng5/minmin_sng5.png")
            img = Minmin
            def Minmin():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=39')
            link = Minmin
        elif Name == "Miori":
            Miori = PhotoImage(file="Member_Img_sng5/miori_sng5.png")
            img = Miori
            def Miori():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=15')
            link = Miori
        elif Name == "Mobile":
            Mobile = PhotoImage(file="Member_Img_sng5/mobile_sng5.png")
            img = Mobile
            def Mobile():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=14')
            link = Mobile
        elif Name == "Music":
            Music = PhotoImage(file="Member_Img_sng5/music_sng5.png")
            img = Music
            def Music():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=13')
            link = Music
        elif Name == "Myyu":
            Myyu = PhotoImage(file="Member_Img_sng5/myyu_sng5.png")
            img = Myyu
            def Myyu():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=38')
            link = Myyu
        elif Name == "Namneung":
            Namneung = PhotoImage(file="Member_Img_sng5/namneung_sng5.png")
            img = Namneung
            def Namneung():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=12')
            link = Namneung
        elif Name == "Namsai":
            Namsai = PhotoImage(file="Member_Img_sng5/namsai_sng5.png")
            img = Namsai
            def Namsai():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=11')
            link = Namsai
        elif Name == "Natherine":
            Natherine = PhotoImage(file="Member_Img_sng5/natherine_sng5.png")
            img = Natherine
            def Natherine():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=37')
            link = Natherine
        elif Name == "New":
            New = PhotoImage(file="Member_Img_sng5/new_sng5.png")
            img = New
            def New():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=36')
            link = New
        elif Name == "Niky":
            Niky = PhotoImage(file="Member_Img_sng5/niky_sng5.png")
            img = Niky
            def Niky():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=35')
            link = Niky
        elif Name == "Nine":
            Nine = PhotoImage(file="Member_Img_sng5/nine_sng5.png")
            img = Nine
            def Nine():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=34')
            link = Nine
        elif Name == "Nink":
            Nink = PhotoImage(file="Member_Img_sng5/nink_sng5.png")
            img = Nink
            def Nink():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=10')
            link = Nink
        elif Name == "Noey":
            Noey = PhotoImage(file="Member_Img_sng5/noey_sng5.png")
            img = Noey
            def Noey():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=9')
            link = Noey
        elif Name == "Oom":
            Oom = PhotoImage(file="Member_Img_sng5/oom_sng5.png")
            img = Oom
            def Oom():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=33')
            link = Oom
        elif Name == "Orn":
            Orn = PhotoImage(file="Member_Img_sng5/orn_sng5.png")
            img = Orn
            def Orn():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=3')
            link = Orn
        elif Name == "Pakwan":
            Pakwan = PhotoImage(file="Member_Img_sng5/pakwan_sng5.png")
            img = Pakwan
            def Pakwan():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=32')
            link = Pakwan
        elif Name == "Panda":
            Panda = PhotoImage(file="Member_Img_sng5/panda_sng5.png")
            img = Panda
            def Panda():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=31')
            link = Panda
        elif Name == "Phukkom":
            Phukkom = PhotoImage(file="Member_Img_sng5/phukkom_sng5.png")
            img = Phukkom
            def Phukkom():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=30')
            link = Phukkom
        elif Name == "Piam":
            Piam = PhotoImage(file="Member_Img_sng5/piam_sng5.png")
            img = Piam
            def Piam():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=8')
            link = Piam
        elif Name == "Pun":
            Pun = PhotoImage(file="Member_Img_sng5/pun_sng5.png")
            img = Pun
            def Pun():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=1')
            link = Pun
        elif Name == "Pupé":
            Pupe = PhotoImage(file="Member_Img_sng5/pupe_sng5.png")
            img = Pupe
            def Pupe():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=7')
            link = Pupe
        elif Name == "Ratah":
            Ratah = PhotoImage(file="Member_Img_sng5/ratah_sng5.png")
            img = Ratah
            def Ratah():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=29')
            link = Ratah
        elif Name == "Satchan":
            Satchan = PhotoImage(file="Member_Img_sng5/satchan_sng5.png")
            img = Satchan
            def Satchan():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=6')
            link = Satchan
        elif Name == "Stang":
            Stang = PhotoImage(file="Member_Img_sng5/stang_sng5.png")
            img = Stang
            def Stang():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=28')
            link = Stang
        elif Name == "Tarwaan":
            Tarwaan = PhotoImage(file="Member_Img_sng5/tarwaan_sng5.png")
            img = Tarwaan
            def Tarwaan():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=5')
            link = Tarwaan
        elif Name == "View":
            View = PhotoImage(file="Member_Img_sng5/view_sng5.png")
            img = View
            def View():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=27')
            link = View
        elif Name == "Wee":
            Wee = PhotoImage(file="Member_Img_sng5/wee_sng5.png")
            img = Wee
            def Wee():
                webbrowser.open_new('https://www.bnk48.com/index.php?page=listMembers&memberId=26')
            link = Wee
        
        root2 = Toplevel(bg='#1a2c78')

        root2.title("YOU GET")
        root2.iconbitmap("Icon/BNK48_icon.ico")

        top2 = Frame(root2)
        top2.pack(side=TOP, fill=BOTH)

        run2 = Frame(root2, bg="#1a2c78")
        run2.pack()

        btimg = Button(top2, image=img, bd=0, command=link)
        btimg.pack(side=LEFT)

        '''Pic = Label(top2, image=img, bd='0')
        Pic.pack(side=LEFT)'''
        
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

Mem = ["Cherprang", "Izurina", "Jaa", "Jane", "Jennis", "Jib", "Kaew", "Kaimook",
       "Kate", "Korn", "Mind", "Miori", "Mobile", "Music", "Namneung", "Namsai",
       "Noey", "Orn", "Pun", "Pupé", "Satchan", "Tarwaan", "Aom", "Bamboo", "Cake",
       "Deenee", "Faii", "Fifa", "Fond", "Gygee", "Juné", "Khamin", "Kheng", "Maira",
       "Mewnich", "Minmin", "Myyu", "Natherine", "New", "Niky", "Nine", "Nink", "Oom",
       "Pakwan", "Panda", "Phukkom", "Piam", "Ratah", "Stang", "View", "Wee"]

Mem.sort()

Type = [" (C)", " (H)", " (F)"]

selectText = Label(top, text="♥  ♥  ♥   Select Member   ♥  ♥  ♥",fg="#fff81f", bg="#1a2c78")
selectText.pack(side=TOP)

okButton = Button(top, text="0K", command=SelectMember, bg="#ffa6bc", width=10, fg='#3425c4', bd='1')
okButton.pack(side=BOTTOM)

AllmemberImg = Button(top, image=Allmemb, bd=0, command=official_web, bg="#1a2c78")
AllmemberImg.pack(side=LEFT)

scrollMember = Scrollbar(top)

mylist = Listbox(top, yscrollcommand=scrollMember.set, heigh=20, bg='#3425c4', fg='#fff81f')
for mList in Mem:
    mylist.insert(END, mList)
mylist.pack(side=LEFT, fill=BOTH)

scrollMember.config(command=mylist.yview)
scrollMember.pack(side=LEFT, fill=Y)

root.mainloop()
