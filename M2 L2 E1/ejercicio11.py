temperatura=float(input("Digite temperatura: "))
deporte=""
#Caja negra
if(temperatura>85):
    deporte="Natación"
elif(temperatura>70 and temperatura<=85):
    deporte="Tenis"
elif(temperatura>=33 and temperatura<=70):
    deporte="Golf"
elif(temperatura>10 and temperatura<=32):
    deporte="Esquí"
elif(temperatura<10):
    deporte="Marcha"   
else:
    deporte="No está en el rango"     
#Salidas
print(deporte)               
