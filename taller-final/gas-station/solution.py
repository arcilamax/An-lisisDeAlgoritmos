# 134. Gas Station
# Familia: greedy. Una pasada acumulando gas[i] - cost[i].
# Si el tanque queda negativo en i, ninguna estación entre el inicio candidato e i
# sirve de salida (cada una llega a i con igual o menos combustible que el inicio),
# así que se descarta el tramo completo y el nuevo candidato es i + 1. No se vuelve atrás.
# Si sum(gas) >= sum(cost), el candidato final es la respuesta (única).
# Tiempo Θ(n), espacio extra Θ(1). n = len(gas).

class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0    # balance de toda la vuelta
        tanque = 0   # balance desde el inicio candidato
        inicio = 0
        for i in range(len(gas)):
            diferencia = gas[i] - cost[i]
            total += diferencia
            tanque += diferencia
            if tanque < 0:
                inicio = i + 1   # se descarta el tramo [inicio..i]
                tanque = 0
        return inicio if total >= 0 else -1


if __name__ == "__main__":
    s = Solution()
    assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert s.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    assert s.canCompleteCircuit([5], [4]) == 0
    print("134 OK")
