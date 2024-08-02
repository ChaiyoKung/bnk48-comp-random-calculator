Mem = ["Cherprang", "Izurina", "Jaa", "Jane", "Jennis", "Jib", "Kaew", "Kaimook",
       "Kate", "Korn", "Mind", "Miori", "Mobile", "Music", "Namneung", "Namsai",
       "Noey", "Orn", "Pun", "Pupe", "Satchan", "Tarwaan", "Aom", "Bamboo", "Cake",
       "Deenee", "Faii", "Fifa", "Fond", "Gygee", "June", "Khamin", "Kheng", "Maira",
       "Mewnich", "Minmin", "Myyu", "Natherine", "New", "Niky", "Nine", "Nink", "Oom",
       "Pakwan", "Panda", "Phukkom", "Piam", "Ratah", "Stang", "View", "Wee"]
Mem.sort()

for i in Mem:
    j = i.lower()
    print('elif Name == "',i,'":',sep='')
    print("    ",i,' = PhotoImage(file="Member_Img_sng5/',j,'_sng5.png")',sep='')
    print("    img = ",i,sep='')
    print("    def ",i,"():",sep='')
    print("        webbrowser.open_new('')")
    print("    link =",i)
