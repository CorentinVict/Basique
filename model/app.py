# -*- coding: utf-8 -*-

"""
 * @author : Corentin Vincent
 * @email : corentin.vincent@cpe.fr
 * @date : 11/03/2024, lundi
 * TODO : Game viewer
 * writing preset : snake_case
"""

import tkinter as tk

class app(tk.Tk):
    def __init__(self):

        #Initialisation de la fênetre de jeu
        super().__init__()
        self.title("Game")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(background='White')

        # Création et positionnement du bouton Quitter
        quit_button = tk.Button(self, text="Quitter", command=self.quit, bg="White")  
        quit_button.pack(side='left', padx=10, pady=10)

    def quit(self):
        """Fonction pour fermer l'application."""
        self.destroy()
