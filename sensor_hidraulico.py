
def evaluar_temperatura_aceite(temp):
    if temp<0:
        return("Error: Sensor congelado o falla de lectura")
    elif temp>=0 and temp<=85:
        return("normal")
    elif temp>85 and temp<=105:
        return("Alerta: Sobrecalentamiento")
    else:
        return("Peligro: Apagar Motor")
