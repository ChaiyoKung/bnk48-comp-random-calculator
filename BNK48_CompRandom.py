import random

Mem = ["Cherprang","Izurina","Jaa","Jane","Jennis","Jib","Kaew","Kaimook",
       "Kate","Korn","Mind","Miori","Mobile","Music","Namneung","Namsai",
       "Noey","Orn","Pun","Pupe","Satchan","Tarwaan","Aom","Bamboo","Cake",
       "Deenee","Faii","Fifa","Fond","Gygee","June","Khamin","Kheng","Maira",
       "Mewnich","Minmin","Myyu","Natherine","New","Niky","Nine","Nink","Oom",
       "Pakwan","Panda","Phukkhom","Piam","Ratah","Stang","View","Wee"]

Type = ["(C)","(H)","(F)"]

while True:
    Set = 1
    Coll = []
    Name = input("Input member name : ")
    Name = Name.title()
    D = len("XXX"+Name+"Comp XXX")
    print("="*(D+2))
    if Name.isnumeric() == True:
        break
    elif Name in Mem:
        Box = []
        while True:
            for i in range(0,5):
                MEM = random.choice(Mem)
                TYPE = random.choice(Type)
                Photo = MEM + TYPE
                Box.append(Photo)
                if (Photo == Name+"(C)" or Photo == Name+"(H)" or
                    Photo == Name+"(F)"):
                    Coll.append(Photo)
            print("Set",Set,"|",Box[(Set*5)-5],Box[(Set*5)-4],Box[(Set*5)-3],Box[(Set*5)-2],Box[(Set*5)-1],end='\n\n')
            if Name+"(C)" in Coll and Name+"(H)" in Coll and Name+"(F)" in Coll:
                break
            Set += 1
        print("="*(D+2))
        print("List of",Name,"[",end=' ')
        for n in Coll:
            print(n,end=' ')
        print("]")
        print("="*(D+2)+"\nXXX",Name,"Comp XXX\n"+"="*(D+2))
        print("Total",Set,"Set")
        print("Total",Set*250,"Baht")
        print("="*(D+2),"\n\n")
    else:
        print("ERROR!")
        print("="*(D+2),"\n\n")
