import tkinter
import random
import time
import os
import sys

# Definindo a qualidade HD da janela
hd_definition = '1280x720-300+100'
full_hd_definition = '1920x1080'


# Funcoes-Botoes

def destroy():
    main_window.destroy()


def button_1():
    global difficulty
    difficulty = 1
    label_explain.pack(side='top')
    label_start.pack(side='top')
    button_start.pack(side='top')


def button_2():
    global difficulty
    difficulty = 2
    label_explain.pack(side='top')
    label_start.pack(side='top')
    button_start.pack(side='top')


def button_3():
    global difficulty
    difficulty = 3
    label_explain.pack(side='top')
    label_start.pack(side='top')
    button_start.pack(side='top')


def button_start():
    destroy()


# Difinindo Variaveis

init_game = 0
difficulty = 0

###main_window


# Criando janela
main_window = tkinter.Tk()
main_window.attributes('-fullscreen', True)
main_window.title('Initialization')

# Criando label - janela inicial
label_inicial = tkinter.Label(main_window, text="Let's Play : How fast are you???")
label_question = tkinter.Label(main_window, text="How many times do you want to click ? ")
label_explain = tkinter.Label(main_window, text='Be ready... Click on the buttons as fast as possible!')
label_start = tkinter.Label(main_window, text='Start ?')

# definindo botões - janela inicial
button_times_1 = tkinter.Button(main_window, text='10 Times', bg='Steelblue1', padx='15', pady='5', command=button_1)
button_times_2 = tkinter.Button(main_window, text='30 Times', bg='green', padx='15', pady='5', command=button_2)
button_times_3 = tkinter.Button(main_window, text='50 Times', bg='red', padx='15', pady='5', command=button_3)
button_start = tkinter.Button(main_window, text='Start', padx='15', pady='5', command=button_start)

# Packing main_window
label_inicial.pack(side='top')
label_question.pack(side='top')
button_times_1.pack(side='top')
button_times_2.pack(side='top')
button_times_3.pack(side='top')

# Definindo loop da janela tkinter
main_window.mainloop()

# Game_window

# Criando Janela do jogo
game_window = tkinter.Tk()
game_window.attributes('-fullscreen', True)
game_window.title('Game')

# definindo variaveis - jogo
time_inicial = time.time()
lados = ['left', 'top', 'right', 'bottom']
clicks = difficulty * 20 - 10  # definindo numero de clicks no jogo
contagem = 1
record = 0


# definindo funções - jogo

def position_button():
    button_game.config(button_game.pack(side=random.choice(lados)))


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def stop():
    label_finished = tkinter.Label(text='Congrats... Yout time : {:.2f} sec'.format(record), fg="light green",
                                   font="Verdana 20 bold").pack(side='top')
    button_game.config(text='Restart', bg='green', fg='black', command=restart)
    button_game.config(button_game.pack(side='top'))


def finished():  # definindo o ultimo clique
    finish_time = time.time()
    game_time = finish_time - time_inicial  # verificando tempo de jogo

    def record_func():
        global record
        record = game_time
        label_record.config(text=('Record = {:.2f}seg'.format(record)))

    record_func()
    stop()


def button_game_func():
    def contagem_func():
        global contagem  # Definindo contagem
        contagem += 1
        label_contagem.config(text=str(contagem))
        if contagem == clicks:
            finished()

    position_button()
    contagem_func()


# definir label_contagem:
label_contagem = tkinter.Label(game_window, text=str(contagem))
label_record = tkinter.Label(game_window, text='Record = {:.2f} sec'.format(record))

# packing
label_contagem.pack(side='top')
#label_record.pack(side='bottom')

# definir botão
button_game = tkinter.Button(game_window, text='Click here!', padx='15', pady='5', bg='grey68',
                             command=button_game_func)
button_game.pack(side=random.choice(lados))

# Definindo loop da janela do game
game_window.mainloop()
