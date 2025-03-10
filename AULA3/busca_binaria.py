def busca_binaria(arr, low, high, x):
    mid = (low + high) // 2

    if arr[x] == mid:
        return f"O elemento está no meio: {mid}"
    elif x < mid:
        low = mid + 1
    else:
        high = mid - 1
    
    if x != -1:
        return f"Elemento presente no índice {mid}: {arr[x]}"
    else:
        return "Valor não encontrado."

print(busca_binaria([10,20,30,40,50,60], 10, len(arr)-1, 4))

