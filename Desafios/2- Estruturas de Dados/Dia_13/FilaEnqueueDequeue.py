"""
Em Python, enqueue e dequeue são operações comuns em filas (queues).
Enqueue: Adiciona um elemento ao final da fila.
Dequeue: Remove um elemento do início da fila.
"""
from collections import deque

# Criando uma fila vazia
fila = deque()

# Enqueue - adicionando elementos
fila.append('a')  # Fila: ['a']
fila.append('b')  # Fila: ['a', 'b']
fila.append('c')  # Fila: ['a', 'b', 'c']
print("Fila após enqueue:", fila)

# Dequeue - removendo elementos
primeiro = fila.popleft()  # Remove 'a'
print("Elemento removido (dequeue):", primeiro)
print("Fila após dequeue:", fila)