#Declarando uma função
def saudacoes(hora_do_dia): #Exibir a saudação conrrespodente a hora do dia
    if (hora_do_dia >= 0) and (hora_do_dia <= 12):
        print("Bom Dia!")
    elif (hora_do_dia >= 12) and (hora_do_dia <= 18):
        print("Boa Noite!")
    

#Fora da Função
resposta = int(input("digite que horas são: "))

saudacoes(resposta)