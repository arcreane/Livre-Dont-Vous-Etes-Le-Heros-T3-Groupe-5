#On importe les modules
import tkinter as tk

import pygame as pygame
from PIL import Image, ImageTk

def play():
    pygame.mixer.music.load('''Musiques/MusiqueAcceuil.mp3''')
    pygame.mixer.music.play(loops=0)#Musique de Fond

class MyText(tk.Text):

    def __init__(self, master=None, **kw):
        tk.Text.__init__(self, master, undo=False, **kw)
        self._undo_stack = []
        self._redo_stack = []
        # create proxy
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)


    def _proxy(self, *args):
        if args[0] in ["insert", "delete"]:
            if args[1] == "end":
                index = self.index("end-1c")
            else:
                index = self.index(args[1])
            if args[0] == "insert":
                undo_args = ("delete", index, "{}+{}c".format(index, len(args[2])))
            else:  # args[0] == "delete":
                undo_args = ("insert", index, self.get(*args[:1]))
            self._redo_stack.clear()
            self._undo_stack.append((undo_args, args))
        elif args[0] == "tag":
            if args[1] in ["add", "remove"] and args[2] != "sel":
                indexes = tuple(self.index(ind) for ind in args[3:])
                undo_args = ("tag", "remove" if args[1] == "add" else "add", args[2]) + indexes
                self._redo_stack.clear()
                self._undo_stack.append((undo_args, args))
        result = self.tk.call((self._orig,) + args)
        return result

    def undo(self):
        if not self._undo_stack:
            return
        undo_args, redo_args = self._undo_stack.pop()
        self._redo_stack.append((undo_args, redo_args))
        self.tk.call((self._orig,) + undo_args)

    def redo(self):
        if not self._redo_stack:
            return
        undo_args, redo_args = self._redo_stack.pop()
        self._undo_stack.append((undo_args, redo_args))
        self.tk.call((self._orig,) + redo_args)

        text = MyText(top, width=65, height=20, font="consolas 14")
        text.pack()

        undo_button = tk.Button(top, text="Undo", command=text.undo)
        undo_button.pack()

        redo_button = tk.Button(top, text="Redo", command=text.redo)
        redo_button.pack()

        text.insert('end', "Hello world")
        text.tag_add('test', '1.0', '1.5')
        text.tag_config('test', background='yellow')  #Essai d'ajout d'un Bouton Retour et Suivant mais ne fontionne pas




def reloadmenu():
    Label2.destroy()
    Button3.destroy()
    Button4.destroy()
    Button5.destroy()

    def createNewWindow():
        newWindow = tk.Toplevel()
        newWindow.title('Nouvelle Histoire')
        labelExample = tk.Label(newWindow, text="Nouvelle Histoire")
        buttonExample = tk.Button(newWindow, text="New Window button")  # Nouvelle Page

    def editer():
        Label2.destroy()
        Button3.destroy()
        Button4.destroy()
        Button5.destroy()

    def des2():
        Button1.destroy()
        Button2.destroy()

        Button6 = tk.Button(command=createNewWindow, borderwidth=0)
        Button6.configure(text='''Histoire 1''')
        Button6.place(relx=0.400, rely=0.375, height=55, width=340)  # Bouton Charger Histoire 1



    click_btn1 = tk.PhotoImage(file='Photos Informatique/NouvellePartie.png')
    img_label1 = tk.Label(image=click_btn1)
    Button1 = tk.Button(top,command=createNewWindow, borderwidth=0)
    Button1.place(relx=0.200, rely=0.375, height=94, width=187)
    Button1.configure(text='''Nouvelle partie''') #Bouton Nouvelle Partie

    Button2 = tk.Button(command=des2,borderwidth=0)
    Button2.place(relx=0.650, rely=0.375, height=94, width=187)
    Button2.configure(text='''Charger partie''')  #Bouton Charger Partie, Page après avoir appuyé sur "Jouer"



top = tk.Tk()
top.title(" Livre dont vous êtes le héros") #TitreDeLaPage

Theme = tk.PhotoImage(file='Themes/ThemePrincipalGrand.png') #Fond d'ecran

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo #resize des photos


image = Image.open('Themes/ThemePrincipalGrand.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tk.Label(image=Theme)
label.bind('<Configure>', resize_image)
label.pack(fill=tk.BOTH, expand=tk.YES) #resize photo menu principal


click_btn = tk.PhotoImage(file='Photos Informatique/Jouer.png')
img_label = tk.Label(image=click_btn)#Creation d'un label pour le button
Button3 = tk.Button(top, image=click_btn,command= reloadmenu,borderwidth=0)
Button3.place(relx=0.150, rely=0.375, height=55, width=300) #Bouton Jouer

def editer():
    Button3.destroy()
    Button4.destroy()
    Label2.destroy()
    Button5.destroy() #Page Apres Editer

    def createNewWindow1():
        newWindow1 = tk.Toplevel()
        newWindow1.title('Nouvelle Histoire')
        labelExample = tk.Label(newWindow1, text="Nouvelle Histoire")
        buttonExample = tk.Button(newWindow1, text="New Window button")  # Nouvelle Page1

    def createNewWindow2():
        newWindow2 = tk.Toplevel()
        newWindow2.title('Histoire 1')
        labelExample = tk.Label(newWindow2, text="Histoire 1")
        buttonExample = tk.Button(newWindow2, text="New Window button")  # Nouvelle Page1

    click_btn3 = tk.PhotoImage(file='Photos Informatique/NouvelleHistoire.png')
    img_label3 = tk.Label(image=click_btn3)
    Button6 = tk.Button(command=createNewWindow1, borderwidth=0)#Normalement ajout de image=click_btn2 mais bug dans l'application
    Button6.configure(text='''Nouvelle Histoire''')
    Button6.place(relx=0.600, rely=0.375, height=55, width=300)# Bouton Nouvelle Histoire Apres avoir cliqué sur editer

    Button7 = tk.Button(top, command=createNewWindow2, borderwidth=0)
    Button7.configure(text='''Histoire 1''')
    Button7.place(relx=0.200, rely=0.375, height=55, width=300)    # Bouton Histoire 1 Apres avoir cliqué sur editer


click_btn2 = tk.PhotoImage(file='Photos Informatique/Editer.png')
img_label2 = tk.Label(image=click_btn2)
Button5 = tk.Button(top, image=click_btn2,command=editer, borderwidth=0)
Button5.place(relx=0.400, rely=0.375, height=55, width=340) #Bouton Editer


click_btn3 = tk.PhotoImage(file='Photos Informatique/Quitter.png')
img_label3 = tk.Label(image=click_btn3)
Button4 = tk.Button(top, image=click_btn3,command=top.quit,borderwidth=0)
Button4.place(relx=0.700, rely=0.375,height=55, width=340) #Bouton Quitter


click_btn4 = tk.PhotoImage(file='Photos Informatique/logoTeam.png')
img_label4 = tk.Label(image=click_btn4)
Label2 = tk.Label(top, image=click_btn4, borderwidth=0)
Label2.place(relx=0.719, rely=0.9, height=75, width=375) #LogoTeam

menu_bar = tk.Menu(top)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quitter", command=top.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
top.config(menu=menu_bar) #creation du menu en haut de la page


Theme2 = tk.PhotoImage(file='Themes/foret-medievale-2.png') #Fond d'ecran

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image2 = copy_of_image2.resize((new_width, new_height))
    photo2 = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo #resize des photos

image = Image.open('Themes/foret-medievale-2.png')
copy_of_image2 = image.copy()
photo2 = ImageTk.PhotoImage(image)
label = tk.Label(image=Theme2)
label.bind('<Configure>', resize_image)
label.pack(fill=tk.BOTH, expand=tk.YES) #resize photo menu principal

top.mainloop()