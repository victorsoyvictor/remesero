import pandas as pd
import logging

logging.basicConfig(filename='log',level=logging.INFO)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

#read in the .xlsx file just created int to Pandas DataFrame
#class Extractor:

def extraerFilasExcel(ficheroExcel, hojaExcel):
    df_1 = pd.read_excel(ficheroExcel, sheet_name=hojaExcel)
    #Limpieza de columnas
    df_1.columns = df_1.columns.str.strip().str.replace('/', '_').str.replace(" ","")
    logging.info(df_1.columns)
    logging.info(df_1.isnull().any())
    df_1 = df_1.fillna('')
    for i in range(0, len(df_1)):
        logging.info(str(df_1.FACTURA.loc[i]))
        logging.info(str(df_1.CLIENTE.loc[i]))
        logging.info(str(df_1.NOMBRE.loc[i]))
        logging.info(str(df_1.ENTIDAD.loc[i]))
        logging.info(str(df_1.CUENTA.loc[i]))
        logging.info(str(df_1.CIF.loc[i]))
        logging.info(str(df_1.DIRECCION.loc[i]))
        logging.info(str(df_1.CORRESPONDENCIA.loc[i]))
        logging.info(str(df_1.POBLACION.loc[i]))
        logging.info(str(df_1.CODIGOPOSTAL.loc[i]))
        logging.info(str(df_1.PROVINCIA.loc[i]))
        logging.info(str(df_1.ALQUILER.loc[i]))
        logging.info(str(df_1.RENTA.loc[i]))
        logging.info(str(df_1.COMUNIDAD.loc[i]))
        logging.info(str(df_1.MANCOMUNIDAD.loc[i]))
        logging.info(str(df_1.LUZAPTO.loc[i]))
        logging.info(str(df_1.AGUA.loc[i]))
        logging.info(str(df_1.IBI.loc[i]))
        logging.info(str(df_1.TOTAL.loc[i]))
        logging.info(str(df_1.IVA.loc[i]))
        logging.info(str(df_1.TOTALFACTURA.loc[i]))
    return df_1



