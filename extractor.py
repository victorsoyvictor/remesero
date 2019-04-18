import pandas as pd
import logging
import numpy as np


#read in the .xlsx file just created int to Pandas DataFrame
def extraerFilasExcel(ficheroExcel, hojaExcel):
    df_1 = pd.read_excel(io=ficheroExcel, sheet_name=hojaExcel, header=0)
    #Limpieza de columnas
    df_1.columns = df_1.columns.str.strip().str.replace('/', '_').str.replace(" ","")
    logging.info(df_1.columns)
    logging.info(df_1.isnull().any())
    #limpieza de campos vacios porque pandas pone NaN
    df_1 = df_1.fillna('')
    print(df_1.dtypes)
    #df_1 = df_1.round(decimals=20)
    for i in range(0, len(df_1)):
        logging.info(df_1.FACTURA.loc[i])
        logging.info(df_1.CLIENTE.loc[i])
        logging.info(df_1.SALUDO.loc[i])
        logging.info(df_1.NOMBRE.loc[i])
        logging.info(df_1.CONCEPTO.loc[i])
        logging.info(df_1.ENTIDAD.loc[i])
        logging.info(df_1.CUENTA.loc[i])
        logging.info(df_1.CIF.loc[i])
        logging.info(df_1.DIRECCION.loc[i])
        logging.info(df_1.CORRESPONDENCIA.loc[i])
        logging.info(df_1.POBLACION.loc[i])
        logging.info(df_1.CODIGOPOSTAL.loc[i])
        logging.info(df_1.PROVINCIA.loc[i])
        logging.info(df_1.RENTA.loc[i])
        logging.info(df_1.COMUNIDAD.loc[i])
        logging.info(df_1.MANCOMUNIDAD.loc[i])
        logging.info(df_1.LUZ.loc[i])
        logging.info(df_1.AGUA.loc[i])
        logging.info(df_1.IBI.loc[i])
        logging.info(df_1.TOTAL.loc[i])
        logging.info(df_1.IVA.loc[i])
        logging.info(df_1.TOTALFACTURA.loc[i])
    return df_1



