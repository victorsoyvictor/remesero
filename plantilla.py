import numpy as np
import os
from fpdf import FPDF
import extractor
import datetime
import math

x = datetime.datetime.now()#print ("Formato dd/mm/yyyy =  %s/%s/%s" % (x.day, x.month, x.year) ) 

#Globales
FECHA 				= "%s/%s/%s" % (datetime.datetime.now().day, 
	datetime.datetime.now().month,  
	datetime.datetime.now().year) 
EMPRESA 			= 'PROREYMON S.L.'
DIR_EMPRESA 		= 'C/ MORERAS 48 BJ'
DIR_EMPRESA2 		= '28300 Aranjuez, Madrid'
TELEFONO_EMPRESA 	= 'TLFO: 653675981'
CIF 				= 'CIF: B78561099'
FORMA_DE_PAGO 		= 'REMESA BANCARIA'
DOMICILIO_DE_COBRO 	= 'DOMICILIO DE COBRO'
IVA 				= '21%'
LUZ					= 'CONSUMO DE LUZ'
AGUA 				= 'CONSUMO DE AGUA'
MANCOMUNIDAD 		= 'MANCOMUNIDAD'	
COMUNIDAD 			= 'COMUNIDAD'
IBI 				= 'IBI'


def generarFacturasPDF(df_1):
	i = 0
	for i in range(0, len(df_1)):
		p_factura			= str(df_1.FACTURA.loc[i])
		p_cliente			= str(df_1.CLIENTE.loc[i])
		p_saludo			= df_1.SALUDO.loc[i]
		p_nombre 			= df_1.NOMBRE.loc[i]
		p_concepto 			= df_1.CONCEPTO.loc[i]
		p_entidad			= df_1.ENTIDAD.loc[i]
		p_cuenta			= df_1.CUENTA.loc[i]
		p_cif				= df_1.CIF.loc[i]
		p_direccion			= df_1.DIRECCION.loc[i]
		p_correspondencia	= df_1.CORRESPONDENCIA.loc[i]
		p_poblacion			= df_1.POBLACION.loc[i]
		p_codigopostal		= str(df_1.CODIGOPOSTAL.loc[i])
		p_provincia			= df_1.PROVINCIA.loc[i]
		p_renta 			= '{:.2f}'.format(df_1.RENTA.loc[i])
		p_comunidad 		= df_1.COMUNIDAD.loc[i]
		p_mancomunidad 		= df_1.MANCOMUNIDAD.loc[i]
		p_luz				= df_1.LUZ.loc[i]
		p_agua 				= df_1.AGUA.loc[i]
		p_ibi 				= df_1.IBI.loc[i]
		p_total 			= '{:.2f}'.format(df_1.TOTAL.loc[i])
		p_iva				= str(df_1.IVA.loc[i])
		p_facturatotal		= '{:.2f}'.format(df_1.TOTALFACTURA.loc[i])

		#creating a pdf in called test.pdf in the current directory
		pdf = FPDF()
		pdf.add_page()
		pdf.set_auto_page_break(True,10)
		pdf.set_margins(10, 10)
		pdf.set_xy(0, 0)
		pdf.set_font('times', 'B', 16)
		pdf.cell(20,10,'',0,1)
		pdf.cell(10)
		#pdf.cell(-70,10,'aaaaaaaa',1)
		pdf.cell(70, 6, EMPRESA, 0, 2, 'L')
		pdf.set_font('times', 'B', 12)
		pdf.cell(70, 6, DIR_EMPRESA, 0, 2, 'L')
		pdf.cell(70, 6, DIR_EMPRESA2, 0, 1, 'L')
		fat = 0.6
		pdf.cell(100,5,'',0,0)
		pdf.set_line_width(fat)
		pdf.cell(90, 5, '', 'TLR',1, 'L')
		pdf.cell(100,5,'',0,0)
		pdf.cell(90, 6, p_nombre, 'LR', 1, 'L')
		pdf.set_line_width(0.2)
		pdf.set_font('times', 'B', 12)
		pdf.cell(100, 6, TELEFONO_EMPRESA, 0, 0, 'L')
		pdf.set_line_width(fat)
		pdf.cell(90, 6, p_cif, 'LR', 1, 'L')
		pdf.set_line_width(0.2)
		pdf.cell(100, 6, CIF, 0, 0, 'L')
		pdf.set_font('times','B',12)
		pdf.set_line_width(fat)
		pdf.cell(90, 6, p_direccion, 'LR', 1, 'L')
		pdf.set_line_width(0.2)
		pdf.set_font('times','B',10)
		pdf.cell(25, 6, 'Fecha', 0, 0, 'C')
		pdf.cell(25, 6, 'N. Cliente', 0, 0, 'C')
		pdf.cell(25, 6, 'N. de Factura', 0, 0, 'C')
		pdf.cell(25)
		pdf.set_line_width(fat)
		pdf.cell(12, 6, p_codigopostal, 'L', 0, 'L')
		pdf.cell(39, 6, p_poblacion, 0, 0, 'C')
		pdf.cell(39, 6, p_provincia, 'R', 1, 'R')
		pdf.set_font('times', '', 10)
		pdf.set_line_width(0.2)
		pdf.cell(25, 6, FECHA, 'TBL', 0, 'C')
		pdf.cell(25, 6, p_cliente, 'TB', 0, 'C')
		pdf.cell(25, 6, p_factura, 'TBR', 0, 'C')
		pdf.cell(25)
		pdf.set_line_width(fat)
		pdf.cell(90, 5, '', 'BLR',1, 'L')
		pdf.set_line_width(0.2)


		pdf.ln(10)

		pdf.set_font('times', 'B', 10)

		pdf.cell(100, 10, 'CONCEPTO', 1, 0, 'C')
		pdf.cell(45, 10, 'CARGO', 1, 0, 'C')
		pdf.cell(45, 10, 'ABONO', 1, 1, 'C')
		#pdf.cell(-180)
		pdf.set_font('times', '', 10)

		#Itero sobre las 6 columnas de conceptos que pueden estar rellenos o no
		#RENTA COMUNIDAD MANCOMUNIDAD LUZ AGUA IBI
		abono = '' # campo por si se provee
		anch_concepto = 100
		anch_cargo = 45
		if p_renta:
			concepto = p_concepto
			cargo = p_renta
			pdf.cell(anch_concepto , 10, '%s' % (concepto), 'LR', 0, 'C')
			pdf.cell(anch_cargo , 10, '%s' % (cargo), 'R', 0, 'C')
			pdf.cell(0 , 10, abono, 'R', 1, 'C')
		if p_comunidad:
			concepto = COMUNIDAD
			cargo = p_comunidad
			pdf.cell(anch_concepto , 10, '%s' % (concepto), 'LR', 0, 'C')
			pdf.cell(anch_cargo , 10, '%s' % (cargo), 'R', 0, 'C')
			pdf.cell(0 , 10, abono, 'R', 1, 'C')
		if p_mancomunidad:
			concepto = MANCOMUNIDAD
			cargo = p_mancomunidad
			pdf.cell(anch_concepto , 10, '%s' % (concepto), 'LR', 0, 'C')
			pdf.cell(anch_cargo , 10, '%s' % (cargo), 'R', 0, 'C')
			pdf.cell(0 , 10, abono, 'R', 1, 'C')	
		if p_luz:
			concepto = LUZ
			cargo = p_luz
			pdf.cell(anch_concepto , 10, '%s' % (concepto), 'LR', 0, 'C')
			pdf.cell(anch_cargo , 10, '%s' % (cargo), 'R', 0, 'C')
			pdf.cell(0 , 10, abono, 'R', 1, 'C') 	
		if p_agua:
			concepto = AGUA
			cargo = p_agua
			pdf.cell(anch_concepto , 10, '%s' % (concepto), 'LR', 0, 'C')
			pdf.cell(anch_cargo , 10, '%s' % (cargo), 'R', 0, 'C')
			pdf.cell(0 , 10, abono, 'R', 1, 'C')
		if p_ibi:
			concepto = IBI
			cargo = p_ibi
			pdf.cell(anch_concepto , 10, '%s' % (concepto), 'LR', 0, 'C')
			pdf.cell(anch_cargo , 10, '%s' % (cargo), 'R', 0, 'C')
			pdf.cell(0 , 10, abono, 'R', 1, 'C')

		pdf.cell(100, 10, '', 'LB', 0, 'C')
		pdf.cell(45, 10, '', 'LRB', 0, 'C')
		pdf.cell(45, 10, '', 'RB', 1, 'C')
		pdf.ln(10)

		pdf.set_font('times', 'B', 10)
		pdf.cell(20, 10, 'BASE', 0, 0, 'C')
		pdf.cell(20, 10, '% IVA', 0, 0, 'C')
		pdf.cell(20, 10, 'IVA', 0, 0, 'C')
		pdf.cell(30, 10, '%REC IRPF', 0, 0, 'C')
		pdf.cell(20, 10, 'IRPF', 0, 0, 'C')
		pdf.cell(80, 10, 'IMPORTE LIQUIDO', 0, 1, 'C')

		pdf.set_font('times', '', 10)
		pdf.cell(20, 10, p_total, 'TLB', 0, 'C')
		pdf.cell(20, 10, IVA, 'TB', 0, 'C')
		pdf.cell(20, 10, p_iva, 'TB', 0, 'C')
		pdf.cell(30, 10, '0', 'TB', 0, 'C')
		pdf.cell(20, 10, '0', 'TB', 0, 'C')
		pdf.cell(80, 10, p_facturatotal, 'TBR', 1, 'C')

		pdf.ln(10)
		pdf.set_font('times', 'B', 10)
		pdf.cell(190, 10, 'FORMA DE PAGO', 'D', 1, 'L')
		pdf.set_font('times', '', 10)
		pdf.cell(190, 10, FORMA_DE_PAGO, 1, 1, 'L')

		pdf.ln(10)
		pdf.set_font('times', 'B', 10)
		pdf.cell(110, 10, DOMICILIO_DE_COBRO, 0, 0, 'L')
		pdf.cell(80, 10, 'CCC', 0, 1, 'L')
		pdf.set_font('times', '', 10)
		pdf.cell(110, 10, p_entidad, 'TBL',0, 'L')
		pdf.cell(80, 10, "ES**-****-****-**-******" + p_cuenta[20:], 'TBR', 0, 'L')
		#print(os.getcwd())
		pdf.output(os.getcwd()+ "/pdf/"+ p_cliente + ".pdf", 'F')
		#print("Creado: " + p_cliente + ".pdf")
	print('--------------------------')
	i = i + 1
	print ('Creadas %s facturas en PDF.' %i)