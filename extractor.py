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
    df_1 = pd.read_excel(io=ficheroExcel, sheet_name=hojaExcel, converters={'CP':str,'FACTURA':str,'CLIENTE':str}, skipfooter=2)
    #Limpieza de columnas en caso de contener espacios barras o espacios en blanco
    df_1.columns = df_1.columns.str.strip().str.replace('/', '_').str.replace(" ","")
    logging.info(df_1.columns)
    logging.info(df_1.isnull().any())
    #limpieza de campos vacios porque pandas pone NaN
    df_1 = df_1.fillna('')
    logging.info(df_1.dtypes)
    return df_1



