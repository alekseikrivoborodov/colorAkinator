# TODO need a full list of HEX colors
# TODO need a akinator's img
# TODO need a magic lamp, color we will be changed by code
# TODO need a buttons yes, no
# TODO need a communicate tkinter and logic
# TODO need a error message with yes no and amazing rainbow in lamp


import random
import tkinter
from tkinter import *

import aggdraw
import imageio
from PIL import Image

import akinator_7_genius


def TkinterApp():
    def generationGif(color):
        gif_frames = []

        def generationImg(simple_color):
            image = Image.new("RGB", (320, 320), (255, 255, 255))
            draw = aggdraw.Draw(image)
            draw.ellipse((10, 10, 300, 300), aggdraw.Pen(simple_color, 0.5), aggdraw.Brush(simple_color))
            draw.ellipse((8, 8, 302, 302), aggdraw.Pen("black", 0.5))
            draw.rectangle((10, 298, 300, 356), aggdraw.Pen((92, 42, 9), 0.5), aggdraw.Brush((92, 42, 9)))
            draw.flush()
            return image

        for _ in range(4):
            for solo_frame in range(30):
                gradient_start = 1.05
                gradient_end = 1.20

                multi_frame = generationImg((
                    round(color[0] * random.uniform(gradient_start, gradient_end)),
                    round(color[1] * random.uniform(gradient_start, gradient_end)),
                    round(color[2] * random.uniform(gradient_start, gradient_end))
                ))

                gif_frames.append(multi_frame)

            imageio.mimwrite("result.gif", gif_frames, 'GIF', fps=5)


    def eventHandler(event):

        print("Нажатие на кнопку")

        global index
        index += 1
        question_string.set(akinator_7_genius.questions[index][0])

        generationGif((50, 100, 50))
        global frames
        frames = [PhotoImage(file='result.gif', format='gif -index %i' % (i)) for i in range(frameCount)]
        window.after(0, update, 0)

    question_string = StringVar()

    question_form = tkinter.Label(textvariable=question_string, height=5, font=50)
    question_string.set("Сыграем?")
    question_form.pack(fill='x', padx=(10, 10))

    button_frame = tkinter.Frame(window)
    yes_btn = tkinter.Button(master=button_frame, text="ДА", width=5, height=3, padx=10, pady=10, bg="green")
    yes_btn.grid(row=0, column=0)
    no_btn = tkinter.Button(master=button_frame, text="НЕТ", width=5, height=3, padx=10, pady=10, bg="red")
    no_btn.grid(row=0, column=1)
    button_frame.pack(side=TOP)

    game_description = tkinter.Label(text="Самый вероятный цвет", height=5, font=50, bg="white")
    game_description.pack()

    generationGif((50, 100, 50))
    frameCount = 30

    global frames
    frames = [PhotoImage(file='result.gif', format='gif -index %i' % (i)) for i in range(frameCount)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCount:
            ind = 0
        label.configure(image=frame)
        window.after(100, update, ind)

    label = Label(window)
    label.pack()
    window.after(0, update, 0)

    yes_btn.bind('<Button-1>', eventHandler)
    no_btn.bind('<Button-1>', eventHandler)


if __name__ == "__main__":
    window = Tk()
    window.geometry('400x700')
    window['bg'] = "white"
    window.title("Акинатор")

    global index
    index = 0

    TkinterApp()
    window.mainloop()
