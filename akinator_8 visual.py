import tkinter
from tkinter import *
import akinator_7_genius
from PIL import Image, ImageDraw, ImageTk



# Пустой желтый фон.
# image = Image.new('RGB', (500, 300), (219, 193, 27))
# draw = ImageDraw.Draw(image)
# image.save('draw-smile.jpg')




# def img():
#     img = ImageTk.(file="draw-smile.jpg")
#     label = Label(window, image=img)
#     label.image_ref = img
#     label.pack()
#
# img()




# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)


# # canvas.grid(row=2, column=3)
#
# msg = Message(window, text = "whatever_you_do")
# msg.config(bg='lightgreen', font=('times', 24, 'italic'))
# # msg.grid(row=2, column=3)
# msg.bind('<Return>', print(1))
#
#
# msg.pack()



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

    # canvas = Canvas(window, width=200, height=200, bg='#000000')
    # canvas.pack()

    window.bind('<KeyRelease-Return>', eventHandler)


if __name__ == "__main__":
    window = Tk()
    window.geometry('400x700')
    window.title("Акинатор")



    global index
    index = 0
    TkinterApp()

    window.mainloop()