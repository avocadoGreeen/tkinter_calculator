from tkinter import *

value = ''
value1 = ''
before_e = ''
after_e = ''
operation_e = ''
value2 = ''
reset = 0

def add_num(number):
    global value2
    global reset

    value = entry_calc.get()

    if len(value) > 19:
        pass
    else:
        if value == 'Ошибка':
            clear()
            value = entry_calc.get()

        if reset == 1:
            clear()
            value = entry_calc.get()
            reset = 0

        if value[0] == "0" and len(value) == 1:
            value = value[1:]

        k = 0
        for i in value:
            if i in '+-÷×':
                value2 = value[k + 1:]
                break
            k += 1
        if '.' in value:
            if len(value) <= 9 or (
                    ('+' in value or '-' in value or '÷' in value or '×' in value) and (len(value2) < 9)):
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, value + number)
                entry_calc['state'] = DISABLED
        if '.' in value2:
            if len(value) < 9 or (
                    ('+' in value or '-' in value or '÷' in value or '×' in value) and (len(value2) <= 9)):
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, value + number)
                entry_calc['state'] = DISABLED
        if '.' in value and '.' in value2:
            if len(value) <= 9 or (
                    ('+' in value or '-' in value or '÷' in value or '×' in value) and (len(value2) <= 9)):
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, value + number)
                entry_calc['state'] = DISABLED
        else:
            if len(value) < 9 or (('+' in value or '-' in value or '÷' in value or '×' in value) and (len(value2) < 9)):
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, value + number)
                entry_calc['state'] = DISABLED


# знаки операций заменяются
def add_operation(operation):
    global before_e
    global after_e

    value = entry_calc.get()

    if len(value) > 19:
        pass
    else:
        if value[-1] == '.':
            value = value[:-1]

        if value[-1] in '-+÷×,':
            # сохраняем все, кроме последней операции
            value = value[:-1]

        if ',' in value:
            calculate()

        # Если уже есть операция, то вычисляем и затем выводим новое значение.
        elif '+' in value or '-' in value or '÷' in value or '×' in value:
            calculate()
            value = entry_calc.get()

        if value != "Ошибка":
            entry_calc['state'] = NORMAL
            entry_calc.delete(0, END)
            entry_calc.insert(0, value + operation)
            entry_calc['state'] = DISABLED


def calculate():
    global reset
    value = entry_calc.get()

    if value == "Ошибка":
        pass
    else:
        if 'e' in value:
            e = 0
            for i in value:
                if i == 'e':
                    before_e = value[:e]
                    after_e = value[e + 1:]
                    break
                e += 1
            value = str(before_e) + '*' + '10' + '**' + str(after_e)

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

        if (len(str(value)) - 1) > 8:
            try:
                res_value = eval(value)
                len_res_value = len(str(res_value))
                for_insert = res_value / 10 ** (len_res_value - 1)
                if for_insert >= 10:
                    while for_insert >= 10:
                        for_insert = for_insert / 10
                        len_res_value += 1
                if for_insert < 1:
                    while for_insert < 1:
                        for_insert *= 10
                        len_res_value -= 1
                for_insert = round(float(for_insert), 5)
                for_insert = str(for_insert)
                if for_insert[-2] == '.' and for_insert[-1] == '0':
                    for_insert = for_insert[:-2]
                    for_insert = int(for_insert)
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, for_insert)
                entry_calc.insert(END, 'e')
                entry_calc.insert(END, len_res_value - 1)
                reset = 1
                entry_calc['state'] = DISABLED
            except ZeroDivisionError:
                entry_calc['state'] = NORMAL
                entry_calc.insert(0, 'Ошибка')
                entry_calc['state'] = DISABLED
        else:
            entry_calc['state'] = NORMAL
            entry_calc.delete(0, END)
            try:
                plus = 0
                value = eval(value)
                value = str(value)
                if 'e' in str(value) and '+' in str(value):
                    for i in str(value):
                        if i == "+":
                            value = str(value[:plus]) + str(value[plus + 2:])
                            break
                        plus += 1

                entry_calc.insert(0, value)
                reset = 1
                entry_calc['state'] = DISABLED
            except ZeroDivisionError:
                entry_calc['state'] = NORMAL
                entry_calc.insert(0, 'Ошибка')
                entry_calc['state'] = DISABLED


def calculate_per():
    global value
    global value1
    global value2
    global before_e
    global after_e
    global operation_e
    global reset

    value = entry_calc.get()

    if 'e' in str(value):
        per = 0
        for i in str(value):
            if i == 'e':
                before_e = value[:per]
                after_e = value[per + 1:]
                break
            per += 1

        try:
            before_e = float(before_e)
            after_e = int(after_e)

            if after_e > 8:
                after_e -= 2
                if before_e < 1:
                    while before_e < 1:
                        before_e *= 10
                        after_e -= 1
                before_e = str(before_e)
                after_e = str(after_e)
                if before_e[-2] == '.' and before_e[-1] == '0':
                    before_e = before_e[:-2]
                value = before_e + 'e' + after_e

                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, value)
                reset = 1
                entry_calc['state'] = DISABLED

            elif after_e < 0 and after_e < -90:
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, "Ошибка")
                entry_calc['state'] = DISABLED

            else:
                after_e -= 2
                before_e = before_e
                value = str(before_e) + 'e' + str(after_e)
                if value[-2] == '0':
                    value = value[:-2] + value[-1]
                print(value, 'val')
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, value)
                reset = 1
                entry_calc['state'] = DISABLED

        except (ValueError, TypeError):
            pass

    else:
        if value[-1] in '-+÷×,':
            # сохраняем все, кроме последней операции
            value = value + value[:-1]

        if value[0] == "0" and len(value) == 1:
            clear()
        elif '+' in value or '-' in value:
            k = 0
            for i in value:
                if i in "+-":
                    value1 = value[:k]
                    value2 = value[k + 1:]
                    value_k = value[k]
                    break
                k += 1

            # изменяет тип на int/float обоих чисел
            n = 0
            for i in value1:
                if i == '.':
                    n += 1
            if n == 1:
                value1 = float(value1)
            else:
                value1 = int(value1)

            m = 0
            for j in value2:
                if j == '.':
                    m += 1
            if m == 1:
                value2 = float(value2)
            else:
                value2 = int(value2)

            result = str((value1 * value2) / 100)
            if result[-2] == '.' and value[-1] == '0':
                result = (value1 * value2) // 100
            value = str(value1) + str(value_k) + str(result)
            entry_calc['state'] = NORMAL
            entry_calc.delete(0, END)
            entry_calc.insert(0, round(eval(value), 6))
            reset = 1
            entry_calc['state'] = DISABLED

        elif '÷' in value or '×' in value:
            k = 0
            for i in value:
                if i in "×÷":
                    value1 = value[:k]
                    value2 = value[k + 1:]
                    value_k = value[k]
                    break
                k += 1

            if value_k == "×":
                value_k = '*'

            if value_k == '÷':
                value_k = '/'

            # изменяет тип на int/float обоих чисел
            n = 0
            for i in value1:
                if i == '.':
                    n += 1
            if n == 1:
                value1 = float(value1)
            else:
                value1 = int(value1)

            m = 0
            for j in value2:
                if j == '.':
                    m += 1
            if m == 1:
                value2 = float(value2)
            else:
                value2 = int(value2)

            result = str(value2 / 100)

            if result[-2] == '.' and value[-1] == '0':
                result = (value1 * value2) // 100

            value = str(value1) + str(value_k) + str(result)

            if value[-2] == '/' and value[-1] == '0':
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, 'Ошибка')
                entry_calc['state'] = DISABLED
            else:
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, round(eval(value), 6))
                reset = 1
                entry_calc['state'] = DISABLED
        else:
            if value == "Ошибка":
                pass
            else:
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, float(value) / 100)
                reset = 1
                entry_calc['state'] = DISABLED


def clear():
    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    entry_calc.insert(0, '0')
    entry_calc['state'] = DISABLED


def clear_last():
    value = entry_calc.get()

    if value == "Ошибка":
        clear()
    else:
        if value != "0":
            if len(value) == 1:
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, '0')
                entry_calc['state'] = DISABLED
            else:
                entry_calc['state'] = NORMAL
                entry_calc.delete(0, END)
                entry_calc.insert(0, value[:-1])
                entry_calc['state'] = DISABLED


def comma():
    value = entry_calc.get()

    if value == "Ошибка":
        pass
    else:
        if value[-1] in '+-×÷':
            value = value + '0'

        k = 0
        for comma in value:
            if comma == '.':
                k += 1

        if k < 1:
            value = value + '.'
        elif "+" in value or "-" in value or "×" in value or "÷" in value:
            n = 0
            for operation in value:
                n += 1
                if operation in '+-×÷':
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
        if event.char == '*':
            add_operation('×')
        elif event.char == '/':
            add_operation('÷')
        else:
            add_operation(event.char)

    elif event.char == '\b':
        clear_last()
    elif event.char == '\r':
        calculate()


calc = Tk()

calc.geometry('300x339')
calc.resizable(width=False, height=False)
calc['bg'] = '#CCCCFF'
calc.title('Калькулятор')

# Обработка событий.
calc.bind("<Key>", press_key)

entry_calc = Entry(calc, justify=RIGHT, font=('Franklin Gothic Medium', 18), width=15)

# значение по умолчанию-0.
entry_calc.insert(0, '0')
entry_calc['state'] = DISABLED

# расположения виджетов
# поле ввода
entry_calc.grid(row=0, column=0, columnspan=4, stick='we', padx=4, pady=3)

# цифры
make_button('1').grid(row=4, column=0, stick='wens', padx=2, pady=2)
make_button('2').grid(row=4, column=1, stick='wens', padx=2, pady=2)
make_button('3').grid(row=4, column=2, stick='wens', padx=2, pady=2)
make_button('4').grid(row=3, column=0, stick='wens', padx=2, pady=2)
make_button('5').grid(row=3, column=1, stick='wens', padx=2, pady=2)
make_button('6').grid(row=3, column=2, stick='wens', padx=2, pady=2)
make_button('7').grid(row=2, column=0, stick='wens', padx=2, pady=2)
make_button('8').grid(row=2, column=1, stick='wens', padx=2, pady=2)
make_button('9').grid(row=2, column=2, stick='wens', padx=2, pady=2)
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
calc.grid_columnconfigure(0, minsize=75)
calc.grid_columnconfigure(1, minsize=75)
calc.grid_columnconfigure(2, minsize=75)
calc.grid_columnconfigure(3, minsize=75)

calc.grid_rowconfigure(1, minsize=60)
calc.grid_rowconfigure(2, minsize=60)
calc.grid_rowconfigure(3, minsize=60)
calc.grid_rowconfigure(4, minsize=60)

calc.mainloop()
