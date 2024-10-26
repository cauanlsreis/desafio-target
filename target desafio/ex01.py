def fibonacci(n):
    if n <= 0:
        return 
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n = int(input())
lista = fibonacci(n)
print(lista)

if n in lista:
  print("Pertence a sequência de Fibonacci")
else:
  print("Não pertence a sequência de Fibonacci")