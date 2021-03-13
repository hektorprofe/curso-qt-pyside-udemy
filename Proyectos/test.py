import sqlite3
import datetime


def insert():
    print("Introduce los 6 números")
    conexion = sqlite3.connect("variadonumeros.db")
    cursor = conexion.cursor()
    dt = datetime.date.today()
    lista = []
    try:
        for n in range(6):
            numeros = int(input("Introduce el numero:"))
            lista.append(numeros)
    except:
        print("Ha occurido un error")

    else:
        print("Se ha guardado los números correctamente")

    cursor.execute(
        '''INSERT INTO numeros_reps VALUES (datetime(),?,?,?,?,?,?)''', lista)
    cursor.execute('''SELECT * FROM numeros_reps''')

    numeros = cursor.fetchall()
    print(numeros)

    conexion.commit()
    conexion.close()


def apariciones():
    conexion = sqlite3.connect("variadonumeros.db")
    cursor = conexion.cursor()
    print("Los numeros evaluados son: ")
    cursor.execute("SELECT n2 FROM numeros_reps")
    listax = cursor.fetchall()

    total_numeros = []
    for tupla in listax:
        total_numeros.extend(tupla)
    print(total_numeros)

    # for n in range(50):
    #     print("El numero  se repite", listax.count(n))

    conexion.close()


# insert()
apariciones()


# Ah vale ya veo, es que fetchall no devuelve una lista, sino una lista con tuplas y las repeticio
