#!/usr/bin/env python

"""extractor.py: usando Pandas y tomando de input un fichero Excel, 
devuelve un dataframe con informacion de facturas para una PYME."""

__author__ = 'Victor Sanchez Alonso'
__email__ = "victorsoyvicto@gmail.com"

import pandas as pd
import logging


#read in the .xlsx file just created int to Pandas DataFrame
#Retoca las columnas CP, FACTURA y CLIENTE para no ser tratadas como numero
def extraerFilasExcel(ficheroExcel, hojaExcel):
    df_1 = pd.read_excel(io=ficheroExcel, sheet_name=hojaExcel, converters={'CP':str,'FACTURA':str,'CLIENTE':str})
    #Limpieza de columnas en caso de contener espacios barras o espacios en blanco
    #df_1.columns = df_1.columns.str.strip().str.replace('/', '_').str.replace(" ","")
    logging.info(df_1.columns)
    logging.info(df_1.isnull().any())
    #limpieza de campos vacios porque pandas pone NaN
    df_1 = df_1.fillna('')
    logging.info(df_1.dtypes)
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
        logging.info(df_1.CP.loc[i])
        logging.info(df_1.PROVINCIA.loc[i])
        logging.info(df_1.RENTA.loc[i])
        logging.info(df_1.COMUNIDAD.loc[i])
        logging.info(df_1.MANCOMUNIDAD.loc[i])
        logging.info(df_1.LUZ.loc[i])
        logging.info(df_1.AGUA.loc[i])
        logging.info(df_1.IBI.loc[i])
        logging.info(df_1.TOTAL.loc[i])
        logging.info(df_1.IVA.loc[i])
        logging.info(df_1.TOTAL_FACTURA.loc[i])
    return df_1



