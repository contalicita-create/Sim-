#!/usr/bin/env python3
"""Jogo do passarinho (estilo Flappy Bird) em modo texto."""

from __future__ import annotations

from dataclasses import dataclass
import random

ALTURA = 10
LARGURA = 20
GRAVIDADE = 1
FORCA_PULO = -2
FREQUENCIA_OBSTACULO = 3


@dataclass
class EstadoJogo:
    altura_passarinho: int = ALTURA // 2
    velocidade: int = 0
    turno: int = 0
    pontos: int = 0
    obstaculos: list[tuple[int, int]] | None = None

    def __post_init__(self) -> None:
        if self.obstaculos is None:
            self.obstaculos = []


def criar_obstaculo(rng: random.Random) -> tuple[int, int]:
    """Cria um obstáculo com uma abertura vertical de 3 linhas."""
    abertura_centro = rng.randint(2, ALTURA - 3)
    return (LARGURA - 1, abertura_centro)


def mover_obstaculos(obstaculos: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Move todos os obstáculos uma coluna para a esquerda."""
    return [(x - 1, gap) for (x, gap) in obstaculos if x - 1 >= 0]


def colisao(altura_passarinho: int, obstaculos: list[tuple[int, int]]) -> bool:
    """Retorna True se o passarinho bater em um obstáculo na coluna 2."""
    for x, gap in obstaculos:
        if x == 2:
            if altura_passarinho not in (gap - 1, gap, gap + 1):
                return True
    return altura_passarinho < 0 or altura_passarinho >= ALTURA


def atualizar_estado(estado: EstadoJogo, comando: str, rng: random.Random) -> EstadoJogo:
    """Atualiza estado do jogo com base no comando do jogador (pular ou não)."""
    if comando.strip().lower() == "p":
        estado.velocidade = FORCA_PULO

    estado.velocidade += GRAVIDADE
    estado.altura_passarinho += estado.velocidade
    estado.turno += 1

    estado.obstaculos = mover_obstaculos(estado.obstaculos)

    if estado.turno % FREQUENCIA_OBSTACULO == 0:
        estado.obstaculos.append(criar_obstaculo(rng))

    estado.pontos += 1
    return estado


def desenhar(estado: EstadoJogo) -> str:
    """Gera uma representação textual do jogo."""
    grade = [[" " for _ in range(LARGURA)] for _ in range(ALTURA)]

    for x, gap in estado.obstaculos:
        if 0 <= x < LARGURA:
            for y in range(ALTURA):
                if y not in (gap - 1, gap, gap + 1):
                    grade[y][x] = "|"

    if 0 <= estado.altura_passarinho < ALTURA:
        grade[estado.altura_passarinho][2] = "@"

    linhas = ["+" + "-" * LARGURA + "+"]
    linhas.extend("|" + "".join(linha) + "|" for linha in grade)
    linhas.append("+" + "-" * LARGURA + "+")
    linhas.append(f"Pontos: {estado.pontos}")
    linhas.append("Comando: [p] para pular, [enter] para cair")
    return "\n".join(linhas)


def main() -> None:
    print("=== Jogo do Passarinho ===")
    print("Desvie dos canos! Você controla @ na coluna fixa 2.")

    estado = EstadoJogo()
    rng = random.Random()

    while True:
        print(desenhar(estado))
        comando = input("Sua jogada: ")
        estado = atualizar_estado(estado, comando, rng)

        if colisao(estado.altura_passarinho, estado.obstaculos):
            print(desenhar(estado))
            print(f"Game Over! Pontuação final: {estado.pontos}")
            break


if __name__ == "__main__":
    main()
