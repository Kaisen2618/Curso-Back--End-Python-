#For: indica o inicio de um loop, em português, você poderia interpretar isso com "para cada".
#In: indica a relação entre a varíavel temporária (elemento) e a lista que estamos percorrendo. Em português, você poderia interpretar isso com "dentro".

 # soma += num : tem o mesmo significado de soma + num:
 #estou dizendo de uma maneira mais simples que o total recebe o proprio vlor de total + o conteudo de num(1).
 # as duas formas funcionam da mesma maneira, ms muitos consideram o uso de += algo maais elegante, enxuto.
 
def somar_numeros(lista):
     soma = 0 # inicializando a variavel soma com o valor zero antes de começar  adicionar os numeros da lista
     for num in lista:
         soma += num
     return soma
 
 # Teste de mesa
numeros = [1,2,3,4,5]
resultado = somar_numeros(numeros)
print("a soma dos numeros é ", resultado)