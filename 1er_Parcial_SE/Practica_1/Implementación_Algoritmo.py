import numpy as np
import matplotlib.pyplot as plt

# Objetivo:
# Este programa realiza un ajuste de regresión lineal sobre los gastos mensuales
# para analizar la tendencia de los gastos a lo largo del año y poder estimar o predecir gastos futuros.
# Esto es útil en la vida real para presupuestar, identificar patrones de consumo y tomar mejores decisiones financieras.

# Ejemplo de meses y gastos reales (enero a diciembre)
meses = np.arange(1, 13)  # Meses de enero (1) a diciembre (12)
gastos = np.array([1200, 1150, 1230, 1190, 1250, 1300, 1280, 1270, 1290, 1310, 1330, 1350])  # Gastos en cada mes

# Ajuste de regresión lineal usando numpy
coef = np.polyfit(meses, gastos, 1)  # coef[0]=pendiente (tendencia), coef[1]=intersección (valor inicial)
gastos_estimados = coef[0]*meses + coef[1]  # Calcula los gastos estimados según la recta ajustada

# Graficar datos reales y la recta ajustada
plt.scatter(meses, gastos, color='blue', label='Gastos reales')  # Puntos de datos reales
plt.plot(meses, gastos_estimados, color='red', label='Recta ajustada')  # Línea de tendencia (regresión)
plt.xlabel('Mes')
plt.ylabel('Gasto ($)')
plt.title('Regresión lineal de gastos mensuales')
plt.legend()
plt.grid(True)
plt.show()