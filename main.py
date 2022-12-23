import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import math as m


def mess(Potok):
    messagebox.showinfo('Окно всплыло', f'Поток звезды {Potok}') #Создаёт окно, где записан результат.
def ok(): #Глобальная функция, внешняя, после двоеточия тело функции
    global scidata, x, y, Magnitude, R_vnut, R_vnesh, exp  # Переменные, доступ к которой можно получить из любого места в коде,
    def CO(exp, R_vnut, R_vnesh):  # Локальлная функция, после двоеточие тело функции
 # Переменная, доступ к которой можно получить из любого места в коде,
        Symm = 0
        R_st = 0
        for i in range(-R_vnesh, R_vnesh):
            for j in range(-R_vnesh, R_vnesh):
                if m.sqrt(i ** 2 + j ** 2) > R_vnut and m.sqrt(i ** 2 + j ** 2) <= R_vnesh:
                    p = scidata[y + j][x + i]
                    Symma.append(p)
                if m.sqrt(i ** 2 + j ** 2) <= R_vnut:
                    t = scidata[y + j][x + i]
                    R_star.append(t)
                    print(R_star)
        for k in range(0, len(Symma)):
            Symm += Symma[k]
        print(Symm / len(Symma))
        for star in range(0, len(R_star)):
            R_st += R_star[star]
        print(R_st)
        Potok = (R_st - Symm / len(Symma)) / exp
        return Potok

    hdulist = pyfits.open(txtS.get(1.0, END).replace('\n', '')) #открываем файл
    scidata = hdulist[0].data #Записывваем в scidata наши пиксели
    exp = hdulist[0].header['EXPTIME'] #Берем значение EXPTIME из файла
    hdulist.close() #закрываем файл
    x = int(txtX.get(1.0, END))# Для получения числа из поля ввода для текста
    y = int(txtY.get(1.0, END)) #Первая часть "1.0"означает, что входные данные должны считываться
    R = int(txtR.get(1.0, END)) # из первой строки с нулевым символом.
    R_vnut = int(txtR_vnut.get(1.0, END)) # END говорит программе прочитать до конца текста.
    R_vnesh = int(txtR_vnesh.get(1.0, END))
    #куча пустых списков
    Symma = []
    R_star=[]
    if selectedCO.get():
        Potok = CO(exp, R_vnut, R_vnesh)
        mess(Potok)

    if selectedX.get(): #get помогает понять нашей программе, что пользователь выбрал этот профиль. В роле передатчика
        X = []
        for i in range(x - R, x + R):
            X.append(i)
        fig = plt.figure()  # создали область Figure
        ax = fig.add_subplot(111)  # добавили к Figure область Axes. 111 - это первая строка, первый столбец и первая
        ax.plot(X, scidata[y][(x - R):(x + R)])                         # (единственная) ячейка на сетке Figure.
        '''
        scidata[y][(x - R):(x + R)]), берет соответствующее значение пикселя
        для соответствующего x, которые бегает в диапозоне x-R<x<x+R
                                                                        
                                                                         '''
        ax.set_title("Горизонтальный профиль")
        plt.show()
    if selectedY.get():
        Y = []
        for i in range(y - R, y + R):
            Y.append(i)
        scidata = np.transpose(scidata)
        fig1 = plt.figure() # создали область Figure1
        gr = fig1.add_subplot(111)
        gr.plot(Y, scidata[x][(y - R):(y + R)])
        '''
        scidata[x][(y - R):(y + R)]), берет соответствующее значение пикселя
        для соответствующего y, которые бегает в диапозоне y-R<y<y+R

                                                                         '''
        gr.set_title("Вертикальный профиль")
        plt.show() #Показать график
        scidata = np.transpose(scidata)
    if selected3D.get():
        prostranstvo = []
        for i in range(-R_vnesh, R_vnesh):
            for j in range(-R_vnesh, R_vnesh):
                prostranstvo.append([i + x, j + y, scidata[y + j][x + i]]) #Заполняем наш список в виде [x][y][z]
        plot_verticles(prostranstvo, color = 'GnBu_r') #Создаём поверхность


def plot_verticles(prostranstvo, color = None): #Функция, которая принимает 2 аргумента: координаты точек и градиент
    global R_vnut, R_vnesh
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    coorDx = [v[0] for v in prostranstvo]
    coorDy = [v[1] for v in prostranstvo]
    coorDz = [v[2] for v in prostranstvo]
    ax.plot_trisurf(coorDx, coorDy, coorDz, cmap = color) #cmap - используем градиент, trisurf строит 3D поверхность
    plt.show()










window = Tk() #Создание окна
window.title("Window") #Даём окну название
window.geometry('800x500') #Выбираем размер окна

lblS = Label(window, text="Путь к файлу:", font=("Arial Bold", 10))
lblS.grid(column=0, row=0) #Табличный способ размещения
lblX = Label(window, text="Координата X:", font=("Arial Bold", 10))
lblX.grid(column=0, row=1) #Табличный способ размещения
lblY = Label(window, text="Координата Y:", font=("Arial Bold", 10)) #Содержащие строку (или несколько строк) текста
lblY.grid(column=0, row=2) #Табличный способ размещения
lblR = Label(window, text="Радиус звезды:", font=("Arial Bold", 10)) #и служащие в основном для информирования пользователя
lblR.grid(column=0, row=3) #Табличный способ размещения
lblR_vnut = Label(window, text="Внутренний радиус:", font=("Arial Bold", 10))
lblR_vnut.grid(column=0, row=4) #Табличный способ размещения
lblR_vnesh = Label(window, text="Внешний радиус:", font=("Arial Bold", 10))
lblR_vnesh.grid(column=0, row=5) #Табличный способ размещения
txtS = Text(window,width=30,height=1) #Текстовое поле
txtS.insert(INSERT, 'C:/v523cas60s-001.fit') #Для добавления текста
txtS.grid(column=1, row=0) #Табличный способ размещения
txtX = Text(window,width=30,height=1)
txtX.insert(INSERT, '452') #Для добавления текста
txtX.grid(column=1, row=1) #Табличный способ размещения
txtY = Text(window,width=30,height=1)
txtY.insert(INSERT, '678') #Для добавления текста
txtY.grid(column=1, row=2) #Табличный способ размещения
txtR = Text(window,width=30,height=1)
txtR.insert(INSERT, '5') #Для добавления текста
txtR.grid(column=1, row=3) #Табличный способ размещения
txtR_vnut = Text(window,width=30,height=1)
txtR_vnut.insert(INSERT, '8') #Для добавления текста
txtR_vnut.grid(column=1, row=4) #Табличный способ размещения
txtR_vnesh = Text(window,width=30,height=1)
txtR_vnesh.insert(INSERT, '16') #Для добавления текста
txtR_vnesh.grid(column=1, row=5) #Табличный способ размещения
selectedX = IntVar()
selectedX.set(0)
selectedY =IntVar() #IntVar() - специальный класс библиотеки для работы с целыми числами.
selectedY.set(0)
selected3D =IntVar()
selectedCO=IntVar()

cknX = Checkbutton(window,text='Профиль по X',variable=selectedX) #виджет, который позволяет отметить
cknX.grid(column=2, row=1)                                        # „галочкой“ определенный пункт в окне
cknY = Checkbutton(window,text='Профиль по Y', variable=selectedY)
cknY.grid(column=2, row=2)
ckn3D = Checkbutton(window,text='3D\t', variable=selected3D)
ckn3D.grid(column=2, row=3)
cknCO = Checkbutton(window,text='Поток звезды', variable=selectedCO)
cknCO.grid(column=2, row=4)
btn = Button(window, text="Ок", command=ok) #Создаёт кнопку
btn.grid(column=5, row=2)



window.mainloop()








