string = input("Digite:")
contagem = string.count('a') + string.count('A')
if contagem > 0:
  print(f'A letra a, maiúscula ou minúscula, está presente na string e aparece {contagem} vezes.')
else:
  print('A letra a, maiúscula ou minúscula, não está presente na string.')
