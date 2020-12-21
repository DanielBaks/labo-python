# Claviers Virtuels
import sys

from tkinter import *

def clavier_numerique() :
    fen = Tk()
    clavier = Canvas(fen, bg ="dark grey", width = 1024, height = 768)
    fen.title('Clavier Virtuel 3000')
    fen.geometry('600x260')
    fen.resizable(0, 0)

    def closeKeyboard():
        fen.destroy()

    bouton_1 = Button(fen, text = '1', command = "<1>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_1.grid()
    bouton_1.place(x = 10, y =10 )

    bouton_2 = Button(fen, text = '2', command = "<2>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_2.grid()
    bouton_2.place(x = 60, y = 10)

    bouton_3 = Button(fen, text = '3', command = "<3>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_3.grid()
    bouton_3.place(x = 110, y = 10)

    bouton_4 = Button(fen, text = '4', command = "<4>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_4.grid()
    bouton_4.place(x = 160, y = 10)

    bouton_5 = Button(fen, text = '5', command = "<5>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_5.grid()
    bouton_5.place(x = 210, y = 10)

    bouton_6 = Button(fen, text = '6', command = "<6>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_6.grid()
    bouton_6.place(x = 260, y = 10)

    bouton_7 = Button(fen, text = '7', command = "<7>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_7.grid()
    bouton_7.place(x = 310, y =  10)

    bouton_8 = Button(fen, text = '8', command = "<8>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_8.grid()
    bouton_8.place(x = 360, y = 10)

    bouton_9 = Button(fen, text = '9', command = "<9>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_9.grid()
    bouton_9.place(x = 410, y = 10)

    bouton_0 = Button(fen, text = '0', command = "<0>", bg = "black", fg = "white",
              height = 2, width = 2)
    bouton_0.grid()
    bouton_0.place(x = 460, y = 10)

    bouton_A = Button(fen, text = 'A', command = "<A>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_A.grid()
    bouton_A.place(x = 10, y =60 )

    bouton_Z = Button(fen, text = 'Z', command = "<Z>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_Z.grid()
    bouton_Z.place(x = 60, y =60 )

    bouton_E = Button(fen, text = 'E', command = "<E>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_E.grid()
    bouton_E.place(x = 110, y =60 )

    bouton_R = Button(fen, text = 'R', command = "<R>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_R.grid()
    bouton_R.place(x = 160, y =60 )

    bouton_T = Button(fen, text = 'T', command = "<T>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_T.grid()
    bouton_T.place(x = 210, y =60 )

    bouton_Y = Button(fen, text = 'Y', command = "<Y>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_Y.grid()
    bouton_Y.place(x = 260, y =60 )

    bouton_U = Button(fen, text = 'U', command = "<U>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_U.grid()
    bouton_U.place(x = 310, y =60 )

    bouton_I = Button(fen, text = 'I', command = "<I>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_I.grid()
    bouton_I.place(x = 360, y =60 )

    bouton_O = Button(fen, text = 'O', command = "<O>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_O.grid()
    bouton_O.place(x = 410, y =60 )

    bouton_P = Button(fen, text = 'P', command = "<P>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_P.grid()
    bouton_P.place(x = 460, y =60 )

    bouton_Q = Button(fen, text = 'Q', command = "<Q>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_Q.grid()
    bouton_Q.place(x = 10, y =110 )

    bouton_S = Button(fen, text = 'S', command = "<S>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_S.grid()
    bouton_S.place(x = 60, y =110 )

    bouton_D = Button(fen, text = 'D', command = "<D>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_D.grid()
    bouton_D.place(x = 110, y =110 )

    bouton_F = Button(fen, text = 'F', command = "<F>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_F.grid()
    bouton_F.place(x = 160, y =110 )

    bouton_G = Button(fen, text = 'G', command = "<G>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_G.grid()
    bouton_G.place(x = 210, y =110 )

    bouton_H = Button(fen, text = 'H', command = "<H>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_H.grid()
    bouton_H.place(x = 260, y =110 )

    bouton_J = Button(fen, text = 'J', command = "<J>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_J.grid()
    bouton_J.place(x = 310, y =110 )

    bouton_K = Button(fen, text = 'K', command = "<K>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_K.grid()
    bouton_K.place(x = 360, y =110 )

    bouton_L = Button(fen, text = 'L', command = "<L>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_L.grid()
    bouton_L.place(x = 410, y =110 )

    bouton_M = Button(fen, text = 'M', command = "<M>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_M.grid()
    bouton_M.place(x = 460, y =110 )

    bouton_W = Button(fen, text = 'W', command = "<W>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_W.grid()
    bouton_W.place(x = 10, y =160 )

    bouton_X = Button(fen, text = 'X', command = "<X>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_X.grid()
    bouton_X.place(x = 60, y =160 )

    bouton_C = Button(fen, text = 'C', command = "<C>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_C.grid()
    bouton_C.place(x = 110, y =160 )

    bouton_V = Button(fen, text = 'V', command = "<V>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_V.grid()
    bouton_V.place(x = 160, y =160 )

    bouton_B = Button(fen, text = 'B', command = "<B>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_B.grid()
    bouton_B.place(x = 210, y =160 )

    bouton_N = Button(fen, text = 'N', command = "<N>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_N.grid()
    bouton_N.place(x = 260, y =160 )

    bouton_Arobase = Button(fen, text = '@', command = "<@>", bg = "white", fg = "black",
              height = 2, width = 2)
    bouton_Arobase.grid()
    bouton_Arobase.place(x = 310, y =160 )

    bouton_Tiret = Button(fen, text = '-', command = "<->", bg = "white", fg = "black",
              height = 2, width = 2)
    bouton_Tiret.grid()
    bouton_Tiret.place(x = 360, y =160 )

    bouton_TiretBas = Button(fen, text = '_', command = "<_>", bg = "white", fg = "black",
              height = 2, width = 2)
    bouton_TiretBas.grid()
    bouton_TiretBas.place(x = 410, y =160 )

    bouton_Point = Button(fen, text = '.', command = "<.>", bg = "white", fg = "black",
              height = 2, width = 2)
    bouton_Point.grid()
    bouton_Point.place(x = 460, y =160)

    bouton_É = Button(fen, text = 'É', command = "<É>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_É.grid()
    bouton_É.place(x = 10, y =210)

    bouton_È = Button(fen, text = 'È', command = "<È>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_È.grid()
    bouton_È.place(x = 60, y =210)

    bouton_Ê = Button(fen, text = 'Ê', command = "<Ê>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_Ê.grid()
    bouton_Ê.place(x = 110, y =210)

    bouton_À = Button(fen, text = 'À', command = "<À>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_À.grid()
    bouton_À.place(x = 160, y =210)

    bouton_Ë = Button(fen, text = 'Ë', command = "<Ë>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_Ë.grid()
    bouton_Ë.place(x = 210, y =210)

    bouton_Ä = Button(fen, text = 'Ä', command = "<Ä>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_Ä.grid()
    bouton_Ä.place(x = 260, y =210)

    bouton_Ï = Button(fen, text = 'Ï', command = "<Ï>", bg = "white", fg = "blue",
              height = 2, width = 2)
    bouton_Ï.grid()
    bouton_Ï.place(x = 310, y =210)

    bouton_Suppr = Button(fen, text = u"\u00ab", command = "<<->", bg = "dark green", fg = "white",
              height = 2, width = 6)
    bouton_Suppr.grid()
    bouton_Suppr.place(x = 510, y = 10)

    bouton_Del = Button(fen, text = 'Delete', command = "<Del>", bg = "dark green", fg = "white",
              height = 2, width = 6)
    bouton_Del.grid()
    bouton_Del.place(x = 510, y = 60)

    bouton_Space = Button(fen, text = 'Space', command = "<Space>", bg = "dark green", fg = "white",
              height = 2, width = 6)
    bouton_Space.grid()
    bouton_Space.place(x = 510, y = 110)

    bouton_Maj = Button(fen, text = 'MAJ', command = "<MAJ>", bg = "dark green", fg = "white",
              height = 2, width = 6)
    bouton_Maj.grid()
    bouton_Maj.place(x = 510, y = 160)

    bouton_Quit = Button(fen, text = 'Close', command = closeKeyboard , bg = "red", fg = "black",
              height = 2, width = 10)
    bouton_Quit.grid()
    bouton_Quit.place(x = 360, y = 210)

    bouton_Confirm = Button(fen, text = 'Confirm', command = "<Confirm>", bg = "light blue", fg = "black",
              height = 2, width = 10)
    bouton_Confirm.grid()
    bouton_Confirm.place(x = 480, y = 210)
