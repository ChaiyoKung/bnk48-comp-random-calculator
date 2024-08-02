from tkinter import *
import random





def SelectMember():
    while True:
        Set = 1
        Coll = []
        #All = []
        Name = mylist.selection_get()

        if mylist.selection_get():
            okButton.destroy()
            mylist.destroy()
            scrollMember.destroy()

        D = len("♦ ♦ ♦ " + Name + " Comp ♦ ♦ ♦")
        Box = ["=" * (D-5)]
        #All.append("=" * (D+20))

        if Name in Mem:
            while True:
                #Box = [] #<<< off - Y list
                for i in range(0, 5):
                    MEM = random.choice(Mem)
                    TYPE = random.choice(Type)
                    Photo = MEM + TYPE
                    Box.append(Photo)

                    if (Photo == Name + " (C)" or Photo == Name + " (H)" or Photo == Name + " (F)"):
                        Coll.append(Photo)
                Box.append("=" * (D-5)) #<<< on - Y list
                #All.append(Box)
                #All.append("=" * (D+20))

                if Name + " (C)" in Coll and Name + " (H)" in Coll and Name + " (F)" in Coll:
                    break
                
                Set += 1
            break

    ShowBox = Label(top, text=("||\n||\n||\n||\n||\n||\n||\n||\n||\n\n"
                                 "YOU GET >>"
                                 "\n\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||"), fg="#cb96c2")
    ShowBox.pack(side=LEFT)

    scrollBox = Scrollbar(top)

    Boxlist = Listbox(top, yscrollcommand=scrollBox.set, heigh=21, width=21, fg="white", bg="#cb96c2")
    for PhoList in Box:
        Boxlist.insert(END, PhoList)
    Boxlist.pack(side=LEFT, fill=BOTH)

    scrollBox.config(command=Boxlist.yview)
    scrollBox.pack(side=LEFT, fill=Y)
    
    Label_5 = Label(run, text="=" * (D-5))
    Label_5.pack()
    Label_6 = Label(run, text=("♦ ♦ ♦ " + Name + " Comp ♦ ♦ ♦"))
    Label_6.pack()
    Label_7 = Label(run, text="=" * (D-5))
    Label_7.pack()
    Label_8 = Label(run, text=("Total", Set, "Set"))
    Label_8.pack()
    Label_9 = Label(run, text=("Total", Set * 250, "Baht"))
    Label_9.pack()
    Label_10 = Label(run, text="=" * (D-5))
    Label_10.pack()
    #break





root = Tk()

root.title("BNK48 Comp Random-Cal")
root.iconbitmap("Icon/BNK48_icon.ico")

### Photo ###
Allmemb = PhotoImage(file="Member_Img_sng4/bnk48_allmemb.png")


top = Frame(root)
top.pack(side=TOP, fill=BOTH)

Get = Frame(root)
Get.pack(side=RIGHT)

run = Frame(root)
run.pack()

Mem = ["Cherprang", "Izurina", "Jaa", "Jané", "Jennis", "Jib", "Keaw", "Kaimook",
       "Kate", "Korn", "Mind", "Miori", "Mobile", "Music", "Namneung", "Namsai",
       "Noey", "Orn", "Pun", "Pupé", "Satchan", "Tarwaan", "Aom", "Bamboo", "Cake",
       "Deenee", "Faii", "Fifa", "Fond", "Gygee", "June", "Khamin", "Kheng", "Maira",
       "Mewnich", "Minmin", "Myyu", "Natherine", "New", "Niky", "Nine", "Nink", "Oom",
       "Pakwan", "Panda", "Phukkom", "Piam", "Ratah", "Stang", "View", "Wee"]

Mem.sort()

Type = [" (C)", " (H)", " (F)"]

selectText = Label(top, text="♥  ♥  ♥   Select Member   ♥  ♥  ♥")
selectText.pack(side=TOP)

okButton = Button(top, text="0K", command=SelectMember, bg="#cb96c2", width=10)
okButton.pack(side=BOTTOM)

#dropdownMem = OptionMenu(root, tkvar, *memberList)
#dropdownMem.pack(side = BOTTOM)

AllmemberImg = Label(top, image=Allmemb, bd="0")
AllmemberImg.pack(side=LEFT)

scrollMember = Scrollbar(top)

mylist = Listbox(top, yscrollcommand=scrollMember.set, heigh=20)
for mList in Mem:
    mylist.insert(END, mList)
mylist.pack(side=LEFT, fill=BOTH)

scrollMember.config(command=mylist.yview)
scrollMember.pack(side=LEFT, fill=Y)

root.mainloop()
