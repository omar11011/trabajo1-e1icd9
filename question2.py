import pandas as pd

from graphs.scholarship import graphScholarship
from graphs.averagePerCourse import graphAveragePerCourse

if __name__ == "__main__":
    # Leemos el archivo CSV
    df = pd.read_csv('./database/BD_NOTAS_BECA.csv', sep=";")

    # Primer Gráfico
    graphAveragePerCourse(df)

    # Segundo Gráfico
    graphScholarship(df)