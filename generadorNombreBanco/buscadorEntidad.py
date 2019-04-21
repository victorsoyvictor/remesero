file1 = open('bancoEntidad')
file2 = open('CUENTAS')
file1line = file1.readlines()
file2line = file2.readlines()


nolist = []
encontrado = False
for IBAN in file2line:
    for numnombre in file1line:
        #print(IBAN[4:8]+"-"+numnombre[0:4])
        if IBAN[4:8] == numnombre[0:4]:
           print numnombre[5:len(numnombre) - 1]
           encontrado = True
    if not encontrado:
        print(IBAN)
        if IBAN not in nolist:
            nolist.append(IBAN[:len(IBAN) - 1])
    encontrado = False
print("no list -------------")
print nolist