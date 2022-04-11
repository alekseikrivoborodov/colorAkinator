# TODO need a full list of HEX colors
# TODO need a akinator's img
# TODO need a magic lamp, color we will be changed by code
# TODO need a buttons yes, no
# TODO need a communicate tkinter and logic
# TODO need a error message with yes no and amazing rainbow in lamp


import tkinter
from tkinter import *
import akinator_7_genius

import aggdraw
from PIL import Image, ImageSequence, ImageTk
import random
import imageio


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

        for i in range(4):
            image = generationImg((color[0] + random.randint(0, 30),
                                   color[1] - random.randint(0, 30),
                                   color[2] - random.randint(0, 30)))

            gif_frames.append(image)

        imageio.mimwrite("result.gif", gif_frames, 'GIF', fps=5)

    def eventHandler(event):

        global index
        index += 1

        question_string.set(akinator_7_genius.questions[index][0])
        input_form.delete(0, END)

    question_string = StringVar()
    input_string = StringVar()

    question_form = tkinter.Label(textvariable=question_string, height=5, font=50)
    question_string.set("Сыграем?")
    question_form.pack(fill='x', padx=(10, 10))

    input_form = tkinter.Entry(window, textvariable=input_string, font=50)
    input_form.pack(fill='x', padx=(50, 50), pady=(10, 50))

    game_description = tkinter.Label(text="Самый вероятный цвет", height=5, font=50)
    game_description.pack()

    # canvas = Canvas(window, width=320, height=320)
    # canvas.pack()
    generationGif((0, 0, 0))

    # magic_lamp = tkinter.PhotoImage(file="result.gif", format="gif -index 2")
    # canvas.create_image(0, 0, anchor='nw', image=magic_lamp)

    # def gif_animation():
    #     pass

    def animation():
        global magic_lamp
        magic_lamp = Image.open('result.gif')
        gif_label = Label(window)
        gif_label.pack()

        for img in ImageSequence.Iterator(magic_lamp):
            img = ImageTk.PhotoImage(img)
            gif_label.config(image=img)
            window.update()
        window.after(0, animation())

    animation()

    window.bind('<KeyRelease-Return>', eventHandler)



if __name__ == "__main__":
    window = Tk()
    window.geometry('400x700')
    window.title("Акинатор")

    global index
    index = 0

    TkinterApp()
    window.mainloop()



