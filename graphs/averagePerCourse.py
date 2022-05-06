import numpy as np
import matplotlib.pyplot as plt

def graphAveragePerCourse(df):
    x = ["MATE", "FISICA", "QUIMICA", "HISTORIA", "LITERATURA"]
    y = []

    for i in x: y.append(round(df[i].mean(), 2))
    
    plt.bar(x, y)
    plt.ylabel('Nota Promedio')
    plt.xlabel('Cursos')
    plt.title('Nota Pormedio por Curso')
    plt.show()