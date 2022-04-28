import numpy as np

def solve_eq(A, b):
    inv_A = np.linalg.inv(A) #Aの逆行列
    h_A, w_A = inv_A.shape
    h_b = len(b)
    if(w_A != h_b):
        print("Aの逆行列の列数と行列bの行数が等しくありません")
        exit()
    answer = np.dot(inv_A, b)
    return answer

A = np.array([[1, 2], [3, 5]])
b = np.array([4, 6])
ans = solve_eq(A, b)
print(ans)
