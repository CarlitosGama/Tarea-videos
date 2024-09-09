pesos = float(input("Cuantos pesos mexicanos tienes?: "))
valor_dolar = 19.97
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes \n $"+ dolares + " dolares" )
