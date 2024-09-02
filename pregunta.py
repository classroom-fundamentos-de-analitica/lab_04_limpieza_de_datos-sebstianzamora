"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #

    # eliminar duplicados
    df = df.drop_duplicates()
    
    # eliminación de filas con valores faltantes
    df = df.dropna()
    
    # estandarizar
    # convertir texto a minúsculas y eliminar espacios adicionales en columnas de texto
    df.columns = df.columns.str.strip().str.lower()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip().str.lower()
    
    return df

#dtf = clean_data()
#print(dtf)
    
    