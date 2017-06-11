#!/usr/bin/python
# -*- coding: utf-8 -*-

#######################################
#  _  _   _     ___ _   _ _   ___  __ #
# | || | | |   |_ _| \ | | | | \ \/ / #
# | || |_| |    | ||  \| | | | |\  /  #
# |__   _| |___ | || |\  | |_| |/  \  #
#    |_| |_____|___|_| \_|\___//_/\_\ #
#                                     #
#######################################

# DEXTER COURIER !
# LINUX IS OPEN SOURCE ^-^
# LINUX IS FREE . . . ^-^

#SCRIPT CRIADO POR SAMUEL RODRIGUES! ;)
# ESTE SCRIPT TEM COMO FUNÇÃO MAPEAR O SERVIDOR DE FORMA AUTOMATICA!

try:
	import os
	import platform
except ImportError:
	print("[-] Erro: O script nessecita do módulo os e do platform para funcionar!")
	exit()
def banner():
	print(" __  __    _    ____  _____    _    __  __ _____ _   _ _____ ___  ")
	print("|  \/  |  / \  |  _ \| ____|  / \  |  \/  | ____| \ | |_   _/ _ \ ")
	print("| |\/| | / _ \ | |_) |  _|   / _ \ | |\/| |  _| |  \| | | || | | |")
	print("| |  | |/ ___ \|  __/| |___ / ___ \| |  | | |___| |\  | | || |_| |")
	print("|_|  |_/_/   \_\_|   |_____/_/   \_\_|  |_|_____|_| \_| |_| \___/  4Linux:V.0.1 ")
	print("\nLocal do Script: ")
	os.system("pwd")
	print("\nMapeamento de servidor by Samuel Rodrigues da Silva.")
	print("Email: samueldrs1@outlook.com")
os.system("clear")
banner()
def infos():
	try:
		os.system("sleep 3")
		print("\n[+] SUCESSO: Uptime capturado com sucesso: ")
		os.system("uptime")
	except:
		print("[-] ERRO: Não foi possivel capturar o uptime!")
	try:
		hostname = platform.node()
		os.system("sleep 1")
		print("\n[+] SUCESSO: hostname capturado com sucesso: \n" + hostname)
		os.system("sleep 1")
	except:
		print("[-] ERRO: Não foi possivel capturar o hostname!")
	try:
		
		print("\n[+] SUCESSO: Memória capturada com sucesso: \n")
		
		os.system("free -h ")
	except:
		print("[+] ERRO: Não foi possivel capturar a memória.")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Arquitetura capturada com sucesso: ")
		os.system("uname -m")
	except:
		print("[-] ERRO: Arquitetura não encontrada!")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Sistema encontrado com sucesso!: ")
		os.system("cat /etc/*-release | grep PRETTY_NAME")
	except:
		print("[-] ERRO: Sistema não encontrado!")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Versão do Kernel encontrada com sucesso: ")
		os.system("uname -r")
	except:
		print("[-] ERRO: Versão do Kernel não encontrada!")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Usuários existentes encontrados: ")
		os.system("awk -F: '$3 > 999 {print $0}' /etc/passwd") 
	except:
		print("[-] ERRO: Usuários não encontrados!")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Processor capturado com sucesso: ")
		os.system("cat /proc/cpuinfo | grep GHz")
	except:
		print("[-] ERRO: Processador não encontrado!")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Nucleo(s) encontrado(s) com sucesso: \n")
		nucleos = os.system("cat /proc/cpuinfo | grep processor")
		#print("%s Nucleo(s)."%nucleos)
	except:
		print("[-] ERRO: Processador não encontrado!")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Partições, espaço livre, espaço usado etc... econtrado: ")
		os.system("df -h")
	except:
		print("[-] ERRO: Não foi possivel capturar partições, espaço livre, espaço usado etc...")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Tamanho da pasta /var/log capturado: ")
		os.system("du -sh /var/log")
	except:
		print("[-] ERRO: Tamanho da pasta /var/log não capturado!")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Serviços rodando capturados: ")
		os.system("ss -nltp")
	except:
		print("[-] ERRO: Serviços rodando não capturados!")
	try:
		os.system("sleep 1")
		print("\n[+] SUCESSO: Pacotes instalados capturados")

		if "Debian" in platform.platform():
			os.system("dpkg -l >> pacotes.txt")
			print("Salvo em pacotes.txt")

		elif "Ubuntu" in platform.platform():
			os.system("dpkg -l >> pacotes.txt")
			print("Salvo em pacotes.txt")


		elif "Kali" in platform.platform():
			os.system("dpkg -l >> pacotes.txt")
			print("Salvo em pacotes.txt")

		elif "debian" in platform.platform():
			os.system("dpkg -l >> pacotes.txt")
			print("Salvo em pacotes.txt")

		elif "ubuntu" in platform.platform():
			os.system("dpkg -l >> pacotes.txt")
			print("Salvo em pacotes.txt")

		else:
			os.system("rpm -qa > pacotes.txt")
	except:
		print("[-] ERRO: Pacotes não encontrados!")



infos()


print("\nByee ;) \nBy Samuel Rodrigues!")
exit()

# FIM DO SRCIPT
# CRIADO POR : SAMUEL RODRIGUES
# DATA: DOM, 03:06 11/07/2017
