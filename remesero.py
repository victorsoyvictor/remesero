import plantilla
import extractor
import sys

#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print ("The arguments are: " , str(sys.argv))


print("Hello CHARO vamos a hacer remesas very quick!!")

#print("__name__ value: ", __name__) -> si se ejecuta por consola vale __main__


def main():
    print('Extrayendo información de la base de datos...')
    df = extractor.extraerFilasExcel(sys.argv[1], sys.argv[2])
    print('Generando PDFs...')
    plantilla.generarFacturasPDF(df)

    

if __name__ == '__main__':
    main()



