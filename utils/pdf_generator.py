from fpdf import FPDF
def generar_liquidacion_pdf(fila, tasas):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="LIQUIDACION DE SUELDO", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Nombre: {fila['Nombre']}", ln=True)
    pdf.cell(200, 10, txt=f"RUT: {fila['RUT']}", ln=True)
    pdf.cell(200, 10, txt=f"AFP: {fila['AFP']} - ISAPRE: {fila['ISAPRE']}", ln=True)

    sueldo = fila['Sueldo Base']
    gratificacion = fila['Gratificación']
    bono = fila['Bono Producción']
    horas_extras = fila['Horas Extras']
    colacion = fila['Colación']
    movilizacion = fila['Movilización']

    imponible = sueldo + gratificacion + bono + horas_extras
    no_imponible = colacion + movilizacion

    afp = tasas[fila['AFP']] * imponible
    salud = tasas['SALUD'] * imponible

    total_descuentos = afp + salud
    liquido = imponible + no_imponible - total_descuentos

    pdf.cell(200, 10, txt=f"Total Imponible: {imponible:.0f}", ln=True)
    pdf.cell(200, 10, txt=f"Total No Imponible: {no_imponible:.0f}", ln=True)
    pdf.cell(200, 10, txt=f"Descuentos Legales: AFP {afp:.0f}, Salud {salud:.0f}", ln=True)
    pdf.cell(200, 10, txt=f"Total Descuentos: {total_descuentos:.0f}", ln=True)
    pdf.cell(200, 10, txt=f"Alcance Líquido: {liquido:.0f}", ln=True)

    nombre_archivo = f"liquidacion_{fila['Nombre'].replace(' ', '_')}.pdf"
    pdf.output(nombre_archivo)
    return nombre_archivo