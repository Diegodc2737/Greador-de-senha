#criar um gegerador de senha simples
# Agora utilizando o random de moodo randonico

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "#@$%^&*()!"

for_pass = lower_case + upper_case + numbers + symbols

# tamanho da senha
tamanho_sennha = 12

password = "".join(random.sample(for_pass, tamanho_sennha))

print('\n')
print("Geador de senhas com Python\n")
print(f'Minha senha: {password}')
print('\n')
