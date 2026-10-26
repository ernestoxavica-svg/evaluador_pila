# Evaluador de expresiones posfijas y prefijas usando una Pila

class Pila:
    def __init__(self):
        self.items = []

    def push(self, x):          # meter un elemento
        self.items.append(x)

    def pop(self):              # sacar el de arriba
        return self.items.pop()

    def vacia(self):
        return len(self.items) == 0


def operar(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    if op == '^': return a ** b


def evaluar_posfija(expr):
    pila = Pila()
    for t in expr.split():              # leo de izquierda a derecha
        if t in "+-*/^":
            b = pila.pop()              # primero sale el segundo operando
            a = pila.pop()
            pila.push(operar(a, b, t))
        else:
            pila.push(float(t))         # numero: lo meto a la pila
    return pila.pop()


def evaluar_prefija(expr):
    pila = Pila()
    for t in reversed(expr.split()):    # leo de derecha a izquierda
        if t in "+-*/^":
            a = pila.pop()              # aqui sale primero el primer operando
            b = pila.pop()
            pila.push(operar(a, b, t))
        else:
            pila.push(float(t))
    return pila.pop()


while True:
    print("1) Posfija   2) Prefija")
    op = input("Elige: ")
    expr = input("Expresion (separada por espacios): ")
    try:
        if op == "1":
            print("Resultado:", evaluar_posfija(expr))
        else:
            print("Resultado:", evaluar_prefija(expr))
    except Exception:
        print("Expresion invalida")
    print()
    if input("Enter para otra prueba (s para salir): ").lower() == "s":
        break