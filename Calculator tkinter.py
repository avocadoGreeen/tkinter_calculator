from tkinter import *


def add_num(number):
    value = entry_calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    entry_calc.insert(0, value + number)
    entry_calc['state'] = DISABLED


# знаки операций заменяются
def add_operation(operation):
    value = entry_calc.get()

    if value[-1] in '-+÷×,':
        # сохраняем все, кроме последней операции
        value = value[:-1]

    if ',' in value:
        calculate()

    # Если уже есть операция, то вычисляем и затем выводим новое значение.
    elif '+' in value or '-' in value or '÷' in value or '×' in value:
        calculate()
        value = entry_calc.get()

    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    entry_calc.insert(0, value + operation)
    entry_calc['state'] = DISABLED


def calculate():
    value = entry_calc.get()
    k = 0
    for i in value:
        if i == '÷':
            value = value[0:k] + '/' + value[k + 1:]
            break
        k += 1

    k = 0
    for i in value:
        if i == '×':
            value = value[0:k] + '*' + value[k + 1:]
            break
        k += 1

    if value[-1] in '+-/*':
        value = value + value[:-1]

    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    try:
        entry_calc.insert(0, eval(value))
        entry_calc['state'] = DISABLED
    except (NameError, SyntaxError, ZeroDivisionError):
        clear()
        entry_calc['state'] = DISABLED


def calculate_per():
    value = entry_calc.get()
    if value[0] == "0" and len(value) == 1:
        clear()
    elif '+' in value or '-' in value or '÷' in value or '×' in value:
        calculate()
        value = entry_calc.get()
        entry_calc['state'] = NORMAL
        entry_calc.delete(0, END)
        entry_calc.insert(0, float(value) / 100)
        entry_calc['state'] = DISABLED
    else:
        entry_calc['state'] = NORMAL
        entry_calc.delete(0, END)
        entry_calc.insert(0, float(value) / 100)
        entry_calc['state'] = DISABLED


def clear():
    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    entry_calc.insert(0, '0')
    entry_calc['state'] = DISABLED


def clear_last():
    value = entry_calc.get()
    print(value)
    if value != "0":
        if len(value) < 1:
            print('gg')
            entry_calc['state'] = NORMAL
            entry_calc.insert(0, '0')
            entry_calc['state'] = DISABLED
        else:
            entry_calc['state'] = NORMAL
            entry_calc.delete(0, END)
            entry_calc.insert(0, value[:-1])
            entry_calc['state'] = DISABLED


def comma():
    value = entry_calc.get()
    k = 0
    for comma in value:
        if comma == '.':
            k += 1

    if k < 1:
        value = value + '.'
    elif "+" in value or "-" in value or "*" in value or "/" in value:
        n = 0
        for operation in value:
            n += 1
            if operation in '+-*/':
                u = 0
                for comma in value[n:]:
                    if comma == '.':
                        u += 1
                if u < 1:
                    value = value + '.'
                break

    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    entry_calc.insert(0, value)
    entry_calc['state'] = DISABLED


# функции для создания кнопок

def make_button(number):
    return Button(text=number, font=('Franklin Gothic Medium', 15), command=lambda: add_num(number))


# кнопки операций
def make_operation(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='gray85',
                  command=lambda: add_operation(operation))


def make_calc(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), bg='SteelBlue2',
                  command=calculate)


def make_clear(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='gray85',
                  command=clear)


def make_percent(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='gray85',
                  command=calculate_per)


def make_clear_last(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='gray85',
                  command=clear_last)


def make_comma(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='gray85',
                  command=comma)


# метод .isdigit проверяет, цифра или нет
# функция для обработки нажатий на клавиши
def press_key(event):
    if event.char.isdigit():
        add_num(event.char)
    elif event.char in '+-*/.':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


calc = Tk()

calc.geometry('240x339')
calc.resizable(width=False, height=False)
calc['bg'] = '#CCCCFF'
calc.title('Калькулятор')

# Обработка событий.
calc.bind("<Key>", press_key)

# justify отвечает за то, с какой стороны будет появляться текст в строке ввода.
entry_calc = Entry(calc, justify=RIGHT, font=('Franklin Gothic Medium', 18), width=15)

# значение по умолчанию-0.
entry_calc.insert(0, '0')
entry_calc['state'] = DISABLED

# расположения виджетов
# поле ввода
entry_calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5, pady=3)

# цифры
make_button('1').grid(row=4, column=0, stick='wens', padx=3, pady=3)
make_button('2').grid(row=4, column=1, stick='wens', padx=3, pady=3)
make_button('3').grid(row=4, column=2, stick='wens', padx=3, pady=3)
make_button('4').grid(row=3, column=0, stick='wens', padx=3, pady=3)
make_button('5').grid(row=3, column=1, stick='wens', padx=3, pady=3)
make_button('6').grid(row=3, column=2, stick='wens', padx=3, pady=3)
make_button('7').grid(row=2, column=0, stick='wens', padx=3, pady=3)
make_button('8').grid(row=2, column=1, stick='wens', padx=3, pady=3)
make_button('9').grid(row=2, column=2, stick='wens', padx=3, pady=3)
make_button('0').grid(row=5, column=0, columnspan=2, stick='wens', padx=3, pady=3)

# операции
make_operation('+').grid(row=4, column=3, stick='wens', padx=3, pady=3)
make_operation('-').grid(row=3, column=3, stick='wens', padx=3, pady=3)
make_operation('÷').grid(row=1, column=3, stick='wens', padx=3, pady=3)
make_operation('×').grid(row=2, column=3, stick='wens', padx=3, pady=3)

make_comma(',').grid(row=5, column=2, stick='wens', padx=3, pady=3)
make_percent('%').grid(row=1, column=2, stick='wens', padx=3, pady=3)
make_calc('=').grid(row=5, column=3, stick='wens', padx=3, pady=3)
make_clear('C').grid(row=1, column=0, stick='wens', padx=3, pady=3)
make_clear_last('<-').grid(row=1, column=1, stick='wens', padx=3, pady=3)

# минимальный размер колонок(column) и строк(row).
calc.grid_columnconfigure(0, minsize=60)
calc.grid_columnconfigure(1, minsize=60)
calc.grid_columnconfigure(2, minsize=60)
calc.grid_columnconfigure(3, minsize=60)

calc.grid_rowconfigure(1, minsize=60)
calc.grid_rowconfigure(2, minsize=60)
calc.grid_rowconfigure(3, minsize=60)
calc.grid_rowconfigure(4, minsize=60)

calc.mainloop()
