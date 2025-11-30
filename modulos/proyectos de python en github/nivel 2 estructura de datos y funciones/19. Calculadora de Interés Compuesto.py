#proyecto de calculadora de interes compuesto
class CalculadoraInteresCompuesto:

    def __init__(self, monto_inicial,tasa_interes,periodo):
        self.monto_inicial = monto_inicial
        self.tasa_interes = tasa_interes
        self.periodo = periodo

    def calcular_monto_final(self):
        monto_final = self.monto_inicial * (1 + self.tasa_interes) ** self.periodo
        return monto_final

# Ejemplo de uso

if __name__ == "__main__":

    
    try:
       monto = int(input("Ingresa el monto inicial: "))
    except ValueError:
       print("Por favor ingresa un valor numérico válido para el monto inicial.")
    try:
       tasa = float(input("Ingresa la tasa de interés (en decimal, por ejemplo 0.05 para 5%): "))
    except ValueError:
       print("Por favor ingresa un valor numérico válido para la tasa de interés.")
    try:
       periodo = int(input("Ingresa el número de años: "))
    except ValueError:
       print("Por favor ingresa un valor numérico válido para el número de períodos.")

    calculadora = CalculadoraInteresCompuesto(monto,tasa,periodo)
    monto_final = calculadora.calcular_monto_final()

    print(f"El monto final después de {periodo} años es: {monto_final:.2f}")    