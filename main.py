# -*- coding: utf-8 -*-

"""
 * @author : Corentin Vincent
 * @email : corentin.vincent@cpe.fr
 * @date : 11/03/2024, lundi
 * TODO : 
 * writing preset : snake_case
"""

from model.app import app

if __name__ == "__main__":
    game = app()
    game.mainloop()


