import pandas as pd

def newDataFrame(students, df1, df2):
    dni = students
    gender = []
    cost_i = []
    cost_s = []
    profession = []
    language = []

    df = pd.DataFrame()

    for i in range(len(dni)):
        row1 = df1[df1['DNI'] == dni[i]]
        row2 = df2[df2['DNI'] == dni[i]]
        
        gender.append(row1['GENERO'].values[0])
        cost_i.append(row1['COSTO_I'].values[0])
        cost_s.append(row2['COSTO_S'].values[0])
        profession.append(row2['PROFESION'].values[0])
        language.append(row1['IDIOMA'].values[0])
    
    df['DNI'] = dni
    df['GENERO'] = gender
    df['COSTO_I'] = cost_i
    df['COSTO_S'] = cost_s
    df['PROFESION'] = profession
    df['IDIOMA'] = language
    df['INVERSION'] = df['COSTO_I'] + df['COSTO_S']

    return df