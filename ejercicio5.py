class OperadorInvalidoError(Exception):
    def __init__(self, operador):
        self.operador = operador
        super().__init__(f"Operador inválido: '{operador}'. Debe ser uno de: + - * /")

def calcular_operacion(operacion):
    try:
        partes = operacion.split()
        numero1_str=partes[0]
        operador=partes[1]
        numero2_str = partes[2]

        numero1 = float(numero1_str)
        numero2 = float(numero2_str)
        if operador not in ['+', '-', '*', '/']:
            raise OperadorInvalidoError(operador)
        if operador == '+':
            resultado = numero1 + numero2
        elif operador == '-':
            resultado = numero1 - numero2
        elif operador == '*':
            resultado = numero1 * numero2
        elif operador == '/':
            resultado = numero1 / numero2
        return f"Resultado: {operacion} = {resultado}"

    except ValueError as e:
        return f"Error: Los números deben ser valores numéricos válidos"
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except OperadorInvalidoError as e:
        return str(e)
print(calcular_operacion("3 + 4"))
print(calcular_operacion("10 / 0"))
print(calcular_operacion("2 ** 5"))