import pandas as pd

if __name__ == "__main__":
    # Leemos el archivo CSV
    df = pd.read_csv('./database/BD_NOTAS_BECA.csv', sep=";")

    # Creamos una nueva columna llamada "NOTA"
    df["NOTA"] = (df["MATE"] + df["FISICA"] + df["QUIMICA"] + df["HISTORIA"] + df["LITERATURA"]) / 5

    # Contamos cuantos estudiantes aprobados hay y su promedio
    approved = df[(df['NOTA'] >= 11)]['NOTA']
    count_approved = approved.count()
    mean_approved = round(approved.mean(), 2)
    print('Aprobaron ' + str(count_approved) + ' alumnos.')
    print('Nota promedio de los alumnos que aprobaron: ' + str(mean_approved))

    # Número de alumnos que mantendrán la beca
    num_scholarship = df.apply(lambda x: (x['BECA'] == "SI") and (x['NOTA'] >= 14), axis=1).sum()
    print('Alumnos que siguen manteniendo la beca: ' + str(num_scholarship))