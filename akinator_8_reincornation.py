import tkinter
from tkinter import *
import akinator_7_genius


def TkinterApp():

    def eventHandler(event):

        global index
        index += 1

        question_string.set(akinator_7_genius.questions[index][0])
        input_form.delete(0, END)
        canvas.itemconfigure(color_indicator, fill='green')

    question_string = StringVar()
    input_string = StringVar()

    question_form = tkinter.Label(textvariable=question_string, height=5, font=50)
    question_string.set("Сыграем?")
    question_form.pack(fill='x', padx=(10, 10))

    input_form = tkinter.Entry(window, textvariable=input_string, font=50)
    input_form.pack(fill='x', padx=(50, 50), pady=(10, 50))

    game_description = tkinter.Label(text="Самый вероятный цвет", height=5, font=50)
    game_description.pack()

    canvas = tkinter.Canvas(window)
    canvas.pack()
    color_indicator = canvas.create_rectangle(15, 15, 355, 215, fill="blue")

    window.bind('<KeyRelease-Return>', eventHandler)


if __name__ == "__main__":
    window = Tk()
    window.geometry('400x700')
    window.title("Акинатор")

    global index
    index = 0
    TkinterApp()

    window.mainloop()