### Проведение расчётов
import numpy as np

# Задание функции
def f(x):
    global A1, A2, T1, T2
    return A1 * np.exp(-x / T1) + A2 * np.exp(-x / T2)

### Настройки графика
import matplotlib.pyplot as plt
import locale
def plotting_settings():
    global x_min, x_max, A1, A2, T1, T2, fig, ax, linestyle

    # Настройки графика
    fig, ax = plt.subplots()
    locale.setlocale(locale.LC_NUMERIC, "de_RU")
    font = {'family': font_root,
            'size': fontsize_root}
    plt.rc('font', **font)
    ax.ticklabel_format(useLocale=True)
    ax.grid(linewidth = 0.5, color='#7b7b7b')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    # Настройка офомления графика
    ax_color = foreground_root
    ax.set_facecolor(background_root)
    fig.set_facecolor(background_root)
    ax.spines['bottom'].set_color(ax_color)
    ax.spines['left'].set_color(ax_color) 
    ax.tick_params(axis='x', colors=ax_color)
    ax.tick_params(axis='y', colors=ax_color)

### Построение нового графика поверх старого
def plotting_new():
    global x_min, x_max, A1, A2, T1, T2, fig, ax

    # Постройка графика
    x = np.linspace(x_min, x_max, 1000)
    ax.plot(x, f(x), color=bluecolor, linestyle=linestyle.get())

    plt.ylim(0)

    # Сохранение файла
    fig.set_size_inches(7.2, 7.2)
    fig.savefig('graph.png', dpi=100)


### Создание интерфейса
from tkinter import *
from tkinter import ttk
import re
# Костыль для того, чтобы интерфейс не был размытым
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# Создание окна программы
root = Tk()
root.title("Калькулятор")
root.geometry("1080x720")
root.resizable(False, False)

# Настройка оформления окна
background_root = '#181818'
foreground_root = '#cccccc'
bluecolor = '#66cc33'
fontsize_root = 16
font_root = 'Arial'
root.configure(bg=background_root)

# Настройка веса столбцов, т. е. какую часть окна занимает каждый столбец
root.columnconfigure(index=0, weight=4)
for column in range(1, 2+1): root.columnconfigure(index=column, weight=1)

# Вывод графика
initial_graph = PhotoImage(file="initial_graph.png")
canvas_graph = Canvas(width=720, height=720, background='white', highlightthickness=0)
canvas_graph.create_image(360, 360, image=initial_graph)
canvas_graph.grid(row=0, column=0, rowspan=12)

# Вывод функции
image_function = PhotoImage(file="function.png")
label_function = ttk.Label(image=image_function, background=background_root)
label_function.grid(row=0, column=1, columnspan=2)

## Ввод параметров
# Задание валидации
def is_valid(newval):
    return re.match("^[-]?\d*[.,]?\d*$", newval) is not None
check = (root.register(is_valid), "%P")

# Настройка оформления полей ввода
font_entry = 'Arial'
fontsize_entry = fontsize_root
background_entry = '#1f1f1f'
foreground_entry = foreground_root
insertbackground_entry = foreground_entry
highlightthickness_entry = 0
border_entry = 0
width_entry = 15

# A1
image_A1 = PhotoImage(file="A1.png")
label_A1 = ttk.Label(image=image_A1, background=background_root)
label_A1.grid(row=1, column=1)
entry_A1 = Entry(validate="key", 
                 validatecommand=check,
                 background=background_entry,
                 insertbackground=insertbackground_entry,
                 foreground=foreground_entry,
                 highlightthickness=highlightthickness_entry,
                 border=border_entry,
                 font=(font_entry, fontsize_entry, 'bold'),
                 width=width_entry
                 )
entry_A1.insert(0, "1")
entry_A1.grid(row=1, column=2)

# A2
image_A2 = PhotoImage(file="A2.png")
label_A2 = ttk.Label(image=image_A2, background=background_root)
label_A2.grid(row=2, column=1)
entry_A2 = Entry(validate="key", 
                 validatecommand=check,
                 background=background_entry,
                 insertbackground=insertbackground_entry,
                 foreground=foreground_entry,
                 highlightthickness=highlightthickness_entry,
                 border=border_entry,
                 font=(font_entry, fontsize_entry, 'bold'),
                 width=width_entry
                 )
entry_A2.insert(0, "1")
entry_A2.grid(row=2, column=2)

# T1
image_T1 = PhotoImage(file="T1.png")
label_T1 = ttk.Label(image=image_T1, background=background_root)
label_T1.grid(row=3, column=1)
entry_T1 = Entry(validate="key", 
                 validatecommand=check,
                 background=background_entry,
                 insertbackground=insertbackground_entry,
                 foreground=foreground_entry,
                 highlightthickness=highlightthickness_entry,
                 border=border_entry,
                 font=(font_entry, fontsize_entry, 'bold'),
                 width=width_entry
                 )
entry_T1.insert(0, "1")
entry_T1.grid(row=3, column=2)

# T2
image_T2 = PhotoImage(file="T2.png")
label_T2 = ttk.Label(image=image_T2, background=background_root)
label_T2.grid(row=4, column=1)
entry_T2 = Entry(validate="key", 
                 validatecommand=check,
                 background=background_entry,
                 insertbackground=insertbackground_entry,
                 foreground=foreground_entry,
                 highlightthickness=highlightthickness_entry,
                 border=border_entry,
                 font=(font_entry, fontsize_entry, 'bold'),
                 width=width_entry
                 )
entry_T2.insert(0, "1")
entry_T2.grid(row=4, column=2)

# x_min
image_x_min = PhotoImage(file="x_min.png")
label_x_min = ttk.Label(image=image_x_min, background=background_root)
label_x_min.grid(row=5, column=1)
entry_x_min = Entry(validate="key", 
                    validatecommand=check,
                    background=background_entry,
                    insertbackground=insertbackground_entry,
                    foreground=foreground_entry,
                    highlightthickness=highlightthickness_entry,
                    border=border_entry,
                    font=(font_entry, fontsize_entry, 'bold'),
                    width=width_entry
                    )
entry_x_min.insert(0, "0")
entry_x_min.grid(row=5, column=2)

# x_max
image_x_max = PhotoImage(file="x_max.png")
label_x_max = ttk.Label(image=image_x_max, background=background_root)
label_x_max.grid(row=6, column=1)
entry_x_max = Entry(validate="key", 
                    validatecommand=check,
                    background=background_entry,
                    insertbackground=insertbackground_entry,
                    foreground=foreground_entry,
                    highlightthickness=highlightthickness_entry,
                    border=border_entry,
                    font=(font_entry, fontsize_entry, 'bold'),
                    width=width_entry
                    )
entry_x_max.insert(0, "1")
entry_x_max.grid(row=6, column=2)

## Вывод флажков
# Для построения нового графика поверх старого
enabled_checkbutton_new = IntVar()
checkbutton_new = Checkbutton(text='Не удалять предыдущий график', 
                              variable=enabled_checkbutton_new,
                              background=background_root,
                              foreground=foreground_root,
                              activebackground=background_root,
                              activeforeground=foreground_root,
                              font=('Arial', 12, 'bold'),
                              selectcolor=background_entry
                              )
checkbutton_new.grid(row=7, column=1, columnspan=2, sticky='w')

## Вывод радиокнопок
# Сплошная линия
solid = '-'
linestyle = StringVar(value=solid)
solid_radiobutton = Radiobutton(text='Сплошная линия', 
                                value=solid, 
                                variable=linestyle,
                                background=background_root,
                                foreground=foreground_root,
                                activebackground=background_root,
                                activeforeground=foreground_root,
                                font=('Arial', 12, 'bold'),
                                selectcolor=background_entry                                
                                )
solid_radiobutton.grid(row=8, column=1, columnspan=2, sticky='w')

# Пунктирная линия
dashed_radiobutton = Radiobutton(text='Пунктирная линия', 
                                value='--', 
                                variable=linestyle,
                                background=background_root,
                                foreground=foreground_root,
                                activebackground=background_root,
                                activeforeground=foreground_root,
                                font=('Arial', 12, 'bold'),
                                selectcolor=background_entry                                
                                )
dashed_radiobutton.grid(row=9, column=1, columnspan=2, sticky='w')

# Штрих-пунктирная линия
dasheddotted_radiobutton = Radiobutton(text='Штрих-пунктирная линия', 
                                       value='-.', 
                                       variable=linestyle,
                                       background=background_root,
                                       foreground=foreground_root,
                                       activebackground=background_root,
                                       activeforeground=foreground_root,
                                       font=('Arial', 12, 'bold'),
                                       selectcolor=background_entry                                
                                       )
dasheddotted_radiobutton.grid(row=10, column=1, columnspan=2, sticky='w')

## Вывод кнопок
# Для очищения полей ввода
def click_clear():
    entry_A1.delete(0, END)
    entry_A2.delete(0, END)
    entry_T1.delete(0, END)
    entry_T2.delete(0, END)
    entry_x_min.delete(0, END)
    entry_x_max.delete(0, END)
btn_clear = Button(text='C', 
                   command=click_clear,
                   background=bluecolor,
                   foreground=background_root,
                   activebackground=background_root,
                   activeforeground=bluecolor,                   
                   highlightthickness=0,
                   width=3,
                   height=1,
                   border=0,
                   cursor='hand2',
                   font=('Arial', 16, 'bold'),
                   relief=SUNKEN
                   )
btn_clear.grid(row=11, column=1)

# Для расчёта
def click_solve():
    global x_min, x_max, A1, A2, T1, T2, graph
    A1 = float(entry_A1.get())
    A2 = float(entry_A2.get())
    T1 = float(entry_T1.get())
    T2 = float(entry_T2.get())
    x_min = float(entry_x_min.get())
    x_max = float(entry_x_max.get())
    if enabled_checkbutton_new.get() == 0:
        plotting_settings()
    plotting_new()
    graph = PhotoImage(file="graph.png")
    canvas_graph.create_image(360, 360, image=graph)
btn_solve = Button(text="Построить",
                   command=click_solve,
                   background=bluecolor,
                   foreground=background_root,
                   activebackground=background_root,
                   activeforeground=bluecolor,
                   highlightthickness=0,
                   width=13,
                   height=1,
                   border=0,
                   cursor='hand2',
                   font=('Arial', 16, 'bold'),
                   relief=SUNKEN
                   )
btn_solve.grid(row=11, column=2)

# Вывод окна
plotting_settings()
root.mainloop()