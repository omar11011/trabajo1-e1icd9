import pandas as pd

from operations.common import studentsInCommon
from operations.create import newDataFrame

if __name__ == "__main__":
    language = pd.read_csv('./database/IDIOMAS.csv', sep=";")
    software = pd.read_csv('./database/SOFTWARE.csv', sep=";")

    # Describir características cualitativas y cuantitativas
    print(language.describe())
    print(software.describe())

    # Número de alumnos que estudian en ambos institutos
    common = studentsInCommon(language, software)
    print('Número de alumnos que estudian en ambos institutos: ' + str(len(common)))

    # Nuevo DataFrame
    new_df = newDataFrame(common, language, software)
    print(new_df)

    # Número de Ingenieros Hombres que estudiaron Inglés
    ing_m_en = new_df.apply(
        lambda x: 
            ( (x['PROFESION'] == 'ING_SISTEMAS') or (x['PROFESION'] == 'ING_INDUSTRIAL') )
            and (x['IDIOMA'] == 'INGLES')
            and (x['GENERO'] == 'M')
        , axis=1).sum()
    print('Número de Ingenieros Hombres que estudiaron Inglés: ' + str(ing_m_en))

    # Número de Economistas Mujeres que estudiaron Francés
    ec_m_fr = new_df.apply(
        lambda x: 
            (x['PROFESION'] == 'ECONOMIA')
            and (x['IDIOMA'] == 'FRANCES')
            and (x['GENERO'] == 'F')
        , axis=1).sum()
    print('Número de Economistas Mujeres que estudiaron Francés: ' + str(ec_m_fr))