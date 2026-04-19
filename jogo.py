#!/usr/bin/env python3
"""Jogo de Pedra, Papel e Tesoura no terminal."""

from __future__ import annotations

import random

ESCOLHAS = ("pedra", "papel", "tesoura")


def normalizar_escolha(valor: str) -> str:
    escolha = valor.strip().lower()
    if escolha not in ESCOLHAS:
        raise ValueError("Escolha inválida. Use: pedra, papel ou tesoura.")
    return escolha


def determinar_vencedor(jogador: str, computador: str) -> str:
    if jogador == computador:
        return "empate"

    vitorias = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra",
    }

    if vitorias[jogador] == computador:
        return "jogador"
    return "computador"


def main() -> None:
    print("=== Pedra, Papel e Tesoura ===")
    print("Primeiro a vencer 3 rodadas ganha!")

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 3 and pontos_computador < 3:
        try:
            jogador = normalizar_escolha(input("Sua jogada (pedra/papel/tesoura): "))
        except ValueError as erro:
            print(f"Erro: {erro}")
            continue

        computador = random.choice(ESCOLHAS)
        resultado = determinar_vencedor(jogador, computador)

        print(f"Computador jogou: {computador}")

        if resultado == "empate":
            print("Empate na rodada!")
        elif resultado == "jogador":
            pontos_jogador += 1
            print("Você venceu a rodada!")
        else:
            pontos_computador += 1
            print("Computador venceu a rodada!")

        print(f"Placar: Você {pontos_jogador} x {pontos_computador} Computador\n")

    if pontos_jogador > pontos_computador:
        print("Parabéns! Você ganhou o jogo!")
    else:
        print("Fim de jogo! O computador venceu.")


if __name__ == "__main__":
    main()
