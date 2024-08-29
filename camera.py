from MathLib import *

class Camera(object):
    def __init__(self):
        self.translate = [0, 0, 0]
        self.rotate = [0, 0, 0]

    def GetViewMatrix(self):
        translateMat = TranslationMatrix(self.translate[0],
                                         self.translate[1],
                                         self.translate[2])

        rotateMat = RotationMatrix(self.rotate[0],
                                   self.rotate[1],
                                   self.rotate[2])

        camMatrix = self.matrix_multiply(translateMat, rotateMat)

        return self.inverse_matrix(camMatrix)

    def matrix_multiply(self, A, B):
        # Multiplicación de matrices de 4x4
        result = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result[i][j] = sum(A[i][k] * B[k][j] for k in range(4))
        return result

    def inverse_matrix(self, mat):
        # Método de Gauss-Jordan para invertir una matriz 4x4
        size = len(mat)
        identity = [[float(i == j) for i in range(size)] for j in range(size)]

        # Crear una copia de la matriz original para no modificarla directamente
        augmented_matrix = [row[:] + identity_row[:] for row, identity_row in zip(mat, identity)]

        # Aplicar eliminación de Gauss-Jordan
        for i in range(size):
            # Asegurarse de que el pivote no sea 0
            if augmented_matrix[i][i] == 0:
                for j in range(i+1, size):
                    if augmented_matrix[j][i] != 0:
                        # Intercambiar filas
                        augmented_matrix[i], augmented_matrix[j] = augmented_matrix[j], augmented_matrix[i]
                        break

            # Hacer el pivote igual a 1
            pivot = augmented_matrix[i][i]
            for j in range(2*size):
                augmented_matrix[i][j] /= pivot

            # Hacer que los demás elementos en la columna i sean 0
            for j in range(size):
                if i != j:
                    factor = augmented_matrix[j][i]
                    for k in range(2*size):
                        augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

        # Extraer la matriz inversa de la matriz aumentada
        inverse = [row[size:] for row in augmented_matrix]
        return inverse

