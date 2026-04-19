#!/usr/bin/env python3
"""Calculadora simples de linha de comando."""


def calcular(operacao: str, a: float, b: float) -> float:
    """Executa uma operação matemática entre dois números."""
    if operacao == "+":
        return a + b
    if operacao == "-":
        return a - b
    if operacao == "*":
        return a * b
    if operacao == "/":
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b
    raise ValueError("Operação inválida. Use +, -, * ou /.")


def main() -> None:
    print("=== Calculadora ===")
    print("Operações disponíveis: +, -, *, /")

    operacao = input("Escolha a operação: ").strip()
    try:
        primeiro = float(input("Primeiro número: ").strip())
        segundo = float(input("Segundo número: ").strip())
        resultado = calcular(operacao, primeiro, segundo)
        print(f"Resultado: {resultado}")
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
