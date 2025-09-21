from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Разработка теста, Radiobutton")
root.geometry("550x450")

position = {"padx": 6, "pady": 6, "anchor": NW}

answer1 = "Ответ1"
answer2 = "Ответ2"
answer3 = "Ответ3"
answer4 = "Ни один из вариантов"

selected = StringVar(value=answer4)
res = StringVar()

def click_button():
    ''' Функция обработки ответов '''
    if selected.get() == answer1:
        res.set("Ответ верный")
    else:
        res.set("Ответ не верный")

header = ttk.Label(text="Вопрос")
header.pack(**position)

btn1 = ttk.Radiobutton(text=answer1, value=answer1, variable=selected)
btn1.pack(**position)

btn2 = ttk.Radiobutton(text=answer2, value=answer2, variable=selected)
btn2.pack(**position)

btn3 = ttk.Radiobutton(text=answer3, value=answer3, variable=selected)
btn3.pack(**position)

btn4 = ttk.Radiobutton(text=answer4, value=answer4, variable=selected)
btn4.pack(**position)

btn = ttk.Button(text="Ответить", command=click_button)
btn.pack(**position)

# Вывод результата
header = ttk.Label(textvariable=res)
header.pack(**position)

root.mainloop()