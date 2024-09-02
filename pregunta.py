"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    #
    # Inserte su código aquí
    #

    # separaciones por espacios
    df.replace({"-": " ", "_": " "}, regex=True, inplace=True)

    # mayusculas y minusculas

    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["barrio"] = df["barrio"].str.lower()

    df["idea_negocio"] = df["idea_negocio"].str.lower().str.strip()
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip()

    df["comuna_ciudadano"] = pd.to_numeric(df["comuna_ciudadano"], errors='coerce').fillna(0).astype(int)

    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.replace(r"[,$]", "", regex=True)
        .str.replace(r"\.00$", "", regex=True)
        .astype(float)
    )

    

    # eliminar duplicados
    df = df.drop_duplicates()
    
    # eliminación de filas con valores faltantes
    df = df.dropna()

    
    # estandarizar
    # convertir texto a minúsculas y eliminar espacios adicionales en columnas de texto
    # df.columns = df.columns.str.strip().str.lower()
    # for col in df.select_dtypes(include=['object']).columns:
    #     df[col] = df[col].str.strip().str.lower()

    
    
    return df

barrio = clean_data().barrio.value_counts()
print(barrio)
#sex = clean_data().sexo.value_counts().to_list()
#print(sex)

#estrato = clean_data().estrato.value_counts().to_list()
#print(estrato)

#dtf = clean_data()
#print(dtf)
    
    