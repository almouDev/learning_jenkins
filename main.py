def tri_par_selection(A):
    n = len(A)
    B=[]
    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if A[j] < A[indice_min]:
                indice_min = j
        B.append(A[indice_min])
        A[i], A[indice_min] = A[indice_min], A[i]
    return B

# Exemple d'utilisation
A = [64, 25, 12, 22, 11]
tri_par_selection(A)
print("Tableau trié par sélection : ", A)
