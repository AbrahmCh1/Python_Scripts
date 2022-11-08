#ACY 26/08/22
#Programa 1/ sin ciclo while
#Ultima Modificación 26/08/2022
#ITESM
import calendar
from datetime import date

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

d = date.today() #OBTENEMOS FECHA DE HOY
print(colored(122,144,152,"Date is:"), d)

x = calendar.day_name[d.weekday()] #Obtenemos nombre del día de hoy
print(colored(141, 123, 25,"Hola a todos, hoy es"), x)
