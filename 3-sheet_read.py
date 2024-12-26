from openpyxl import load_workbook

#- Lê pasta de trabalho e planilha
wb = load_workbook("data/pivot_table.xlsx")
sheet = wb["Relatorio"]

# 2-Acessando um valor específico
print(sheet["A3"].value)
print(sheet["B3"].value)

# 3-Iterando valorespor meio de loop
for i in range(2, 6):
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value 
    bt = sheet["C%s" %i].value
    print(
        "{1} o Aston martin vendeu e o Bentley vendeu {2}".format(ano, am, bt)
    )
