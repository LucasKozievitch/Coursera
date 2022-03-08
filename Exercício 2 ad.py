#Entrada de dados
x = int(input('Por favor, entre com o número de segundos que deseja converter: '))

#Cálculo para converter
a = (x//86400)
b = ((x%86400)//3600)
c = (((x%86400)%3600)//60)
d = (((x%86400)%3600)%60)

#Saída de dados
print(a,'dias,',b,'horas,',c,'minutos e',d,'segundos.')