from tkinter import *
import webbrowser


def link():
    webbrowser.open_new("https://www.bnk48.com/index.php?page=listMembers&memberId=52")

root = Tk()

img1 = PhotoImage(file="Member_Img_sng5/pupe_sng5.png")
img2 = PhotoImage(file="Member_Img_sng5/noey_sng5.png")
img3 = PhotoImage(file="Member_Img_sng5/kaimook_sng5.png")

scr = Scrollbar(root)

cnv = Canvas(root, yscrollcommand=scr.set)
cnv.pack(side=LEFT, fill=BOTH)
cnv.create_image(0, 0, anchor=NW, image=img1)
cnv.create_image(50, 50, anchor=NW, image=img2)
cnv.create_image(100, 100, anchor=NW, image=img3)

bt1 = Button(root, text="link", command=link)
bt1.pack()

'''
lb1 = Label(cnv, image=img1)
lb1.pack()
lb2 = Label(cnv, image=img2)
lb2.pack()
lb3 = Label(cnv, image=img3)
lb3.pack()'''

scr.config(command=cnv.yview)
scr.pack(side=LEFT, fill=Y)

root.mainloop()
