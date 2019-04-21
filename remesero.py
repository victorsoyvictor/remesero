import plantilla
import extractor
import sys
import datetime
import logging
import pandas as pd


logging.basicConfig(filename='log',level=logging.INFO)
#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print ("The arguments are: " , str(sys.argv))

print("Hello CHARO vamos a hacer remesas very quick!!")

x = datetime.datetime.now()
logging.info(x)
# La fecha para las remesas es el dia 1 del mes siguiente
x = datetime.datetime.now() + pd.offsets.MonthBegin(1)
# Ojo seteo una variable global de otro modulo, no se si es la mejor manera
plantilla.FECHA = "%s/%s/%s" % (x.day, x.month, x.year)
#print("__name__ value: ", __name__) -> si se ejecuta por consola vale __main__


def main():
	if len(sys.argv) == 3:
	    print('Extrayendo información de la base de datos...')
	    df = extractor.extraerFilasExcel(sys.argv[1], sys.argv[2])
	    print('Generando PDFs...')
	    plantilla.generarFacturasPDF(df)
	else:
		print ("FALTAN ARGUMENTOS DE ENTRADA (2): <BASE_DE_DATOS> <PESTAÑA>")

if __name__ == '__main__':
    main()



