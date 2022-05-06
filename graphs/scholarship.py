import numpy as np
import matplotlib.pyplot as plt

def graphScholarship(df):
    df["NOTA"] = (df["MATE"] + df["FISICA"] + df["QUIMICA"] + df["HISTORIA"] + df["LITERATURA"]) / 5
    
    total_students = len(df)
    scholarship = (df[(df['BECA'] == 'SI')]['BECA']).count()
    current_scolarship = df.apply(lambda x: (x['BECA'] == "SI") and (x['NOTA'] >= 14), axis=1).sum()

    serie1 = [ scholarship, current_scolarship ]
    serie2 = [ total_students - scholarship, total_students - current_scolarship ]
    num_groups = len(serie1)
    bar_index = np.arange(num_groups)
    bar_width = 0.35

    plt.bar(bar_index, serie1, width=bar_width, label="Becados")
    plt.bar(bar_index + bar_width, serie2, width=bar_width, label="No Becados")
    plt.legend(loc='best')

    plt.xticks(bar_index + bar_width, ('Antes', 'Ahora'))
    plt.ylabel('Número de Alumnos')
    plt.show()