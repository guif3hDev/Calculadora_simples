def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def dividir(a, b):
    return a / b


def multiplicar(a, b):
    return a * b


operadores = {
    "+": somar,
    "-": subtrair,
    "/": dividir,
    "*": multiplicar
}

historico = []


def pergunta_saida():
    while True:
        sair = input("Deseja sair? (sim/não) ").strip().lower()

        if sair in ("sim", "s", "ss"):
            return True

        elif sair in ("não", "nao", "n", "nn"):
            return False

        else:
            print("Resposta inválida!")


def main():

    try:
        num1 = float(input("Digite um número: "))
        operador = input("Digite um operador (+, -, *, /): ")
        num2 = float(input("Digite outro número: "))

        if operador not in operadores:
            print("Operador inválido!")
            return

        resultado = operadores[operador](num1, num2)

        print(f"{num1:g} {operador} {num2:g} = {resultado:g}")

        historico.append(
            f"{num1:g} {operador} {num2:g} = {resultado:g}"
        )

    except ValueError:
        print("Digite apenas números!")
        return

    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
        return

    while True:

        if pergunta_saida():
            break

        operador_novo = input(
            "Digite um operador (+, -, *, /): "
        )

        if operador_novo not in operadores:
            print("Operador inválido!")
            continue

        try:
            numero_novo = float(
                input("Digite outro número: ")
            )

            resultado_anterior = resultado

            resultado = operadores[operador_novo](
                resultado,
                numero_novo
            )

            historico.append(
                f"{resultado_anterior:g} "
                f"{operador_novo} "
                f"{numero_novo:g} "
                f"= {resultado:g}"
            )

            print(f"Resultado atual: {resultado:g}")

            print("\nHistórico:")
            for conta in historico:
                print(conta)

        except ValueError:
            print("Digite apenas números!")

        except ZeroDivisionError:
            print("Não é possível dividir por zero!")


if __name__ == "__main__":
    main()