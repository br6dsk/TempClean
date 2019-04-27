#Author: Braian D. Jesus
#Este programa exclui pra você todos os arquivos temporários do seu Windows!
#Se quiser usar esse programa, modifique os arquivos de Lote (.bat) com os seus próprios diretórios.
#Usando windows+r, digita o %temp% da enter e copia o caminho da barra de endereços e mude no arquivo file_tt.bat.
#Criado apenas para testes no meu computador, não me garanto que funcione em todos os sistemas windows.
#Faça o teste por mim :)
#Obrigado xD


import os
from time import sleep
print("""

\t\tL I M P E Z A    D E    R E S Í D U O S    T E M P O R Á R I O S 
\n\t\t\t\t[+] T e m p C l e a n [+]
""")

print(" \n\t\t\t[+] Vamo fazer uma limpezinha? Sim! [+]")

menu = """

[*] Menu, escolha o que deseja deletar [*]
[*] Deletar tudo é a melhor opção, numero 5! [*]

[1] - TEMP
[2] - PREFETCH
[3] - %TEMP%
[4] - Limpar Cache DNS
[5] - ALL 
[0] - Pra fechar o programa 
"""
print(menu)
pergunta = input("\nEscolha um numero equivalente a pasta!: ")
while(pergunta.isdigit()!=True):
	print(" \n[*] Apenas numeros!")
	pergunta=input(" \nDigite novamente um numero da lista: ")
pergunta=int(pergunta)


if pergunta == 1:
	sleep(0.3)
	print(" \n\t\t\tApagando...")
	os.system("start file_t.bat")
	sleep(0.3)
	print(" \n\t\t\tTemp apagado!")
	print(" \n\t\t\tObrigado por usar! by Braian D. Jesus.")
elif pergunta ==2:
	sleep(0.3)
	print(" \n\t\t\tApagando...")
	os.system("start file_p.bat")
	sleep(0.3)
	print(" \n\t\t\tPrefetch apagado!")
	print(" \n\t\t\tObrigado por usar! by Braian D. Jesus.")

elif pergunta ==3:
	sleep(0.3)
	print(" \n\t\t\tApagando...")
	os.system("start file_tt.bat")
	sleep(0.3)
	print(" \n\t\t\t%Temp% apagado!")
	print(" \n\t\t\tObrigado por usar! by Braian D. Jesus.")
elif pergunta ==4:
	sleep(0.3)
	print(" \n\t\t\tApagando...")
	os.system("start file_d.bat")
	sleep(0.3)
	print(" \n\t\t\tLiberação do Cache do DNS Resolver bem-sucedida.")
	print(" \n\t\t\tObrigado por usar! by Braian D. Jesus.")
elif pergunta ==5:
	sleep(0.3)
	print(" \n\t\t\tApagando...")
	os.system("start file_t.bat")
	os.system("start file_tt.bat")
	os.system("start file_d.bat")
	os.system("start file_p.bat")
	sleep(0.3)
	print(" \n\t\t\tA maioria dos arquivos temporários do sistema, foram apagados!")
	print(" \n\t\t\tLiberação do Cache do DNS Resolver bem-sucedida.")
	print(" \n\t\t\tObrigado por usar! by Braian D. Jesus.")	
elif pergunta==0:
	print(" \n\t\t\tObrigado por usar! by Braian D. Jesus.")
	quit()
else:
	print("\n\t\t\tNumero inválido")
	print("\t\t\tFechando...")









