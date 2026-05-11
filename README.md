# Calculadora em Python

Projeto simples de calculadora desenvolvido em Python para praticar lógica de programação.

## O que foi praticado

- Funções
- `while`
- `try/except`
- Dicionários
- Validação de entrada
- Reutilização de código

---

# Lógica do projeto

## 1. Funções matemáticas

Cada operação foi separada em uma função:

```python
def somar(a, b):
    return a + b
```

Isso deixa o código mais organizado.

---

## 2. Dicionário de operadores

Ao invés de vários `if/elif`, foi utilizado um dicionário:

```python
operadores = {
    "+": somar,
    "-": subtrair,
    "/": dividir,
    "*": multiplicar
}
```

Assim o operador escolhe automaticamente a função correta.

---

## 3. Tratamento de erros

Foi utilizado `try/except` para evitar erros quando o usuário digita valores inválidos.

Exemplos:
- letras no lugar de números
- divisão por zero

---

## 4. Resultado acumulado

O resultado da conta fica salvo:

```python
resultado = operadores[operador](num1, num2)
```

Depois disso, o usuário pode continuar calculando usando o resultado anterior.

Exemplo:

```text
5 + 5 = 10
10 * 2 = 20
20 - 5 = 15
```

---

## 5. Função de saída

Foi criada uma função para perguntar se o usuário deseja sair do programa.

Isso ajudou a evitar repetição de código.

---

# Possíveis melhorias

- Potência e raiz quadrada
- Interface gráfica
- Mais operadores

---

