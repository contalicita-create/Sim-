#!/usr/bin/env python3
"""Mini DOOM em ASCII no terminal (estilo raycasting)."""

from __future__ import annotations

import math
from dataclasses import dataclass

MAPA = [
    "###########",
    "#.........#",
    "#..##.....#",
    "#.........#",
    "#.....##..#",
    "#.........#",
    "###########",
]

LARGURA_TELA = 50
ALTURA_TELA = 20
FOV = math.pi / 3
PROFUNDIDADE_MAX = 12.0


@dataclass
class Jogador:
    x: float = 2.5
    y: float = 2.5
    angulo: float = 0.0


def parede(x: float, y: float) -> bool:
    xi = int(x)
    yi = int(y)
    if yi < 0 or yi >= len(MAPA) or xi < 0 or xi >= len(MAPA[0]):
        return True
    return MAPA[yi][xi] == "#"


def cast_ray(px: float, py: float, angulo: float, passo: float = 0.05) -> float:
    distancia = 0.0
    while distancia < PROFUNDIDADE_MAX:
        tx = px + math.cos(angulo) * distancia
        ty = py + math.sin(angulo) * distancia
        if parede(tx, ty):
            return distancia
        distancia += passo
    return PROFUNDIDADE_MAX


def mover(jogador: Jogador, frente: float, giro: float) -> Jogador:
    novo_angulo = (jogador.angulo + giro) % (2 * math.pi)
    nx = jogador.x + math.cos(novo_angulo) * frente
    ny = jogador.y + math.sin(novo_angulo) * frente

    if not parede(nx, ny):
        jogador.x = nx
        jogador.y = ny
    jogador.angulo = novo_angulo
    return jogador


def caractere_parede(distancia: float) -> str:
    if distancia < PROFUNDIDADE_MAX * 0.2:
        return "█"
    if distancia < PROFUNDIDADE_MAX * 0.4:
        return "▓"
    if distancia < PROFUNDIDADE_MAX * 0.6:
        return "▒"
    if distancia < PROFUNDIDADE_MAX * 0.8:
        return "░"
    return "."


def renderizar(jogador: Jogador) -> str:
    colunas = []
    for coluna in range(LARGURA_TELA):
        angulo_raio = jogador.angulo - FOV / 2 + (coluna / LARGURA_TELA) * FOV
        distancia = cast_ray(jogador.x, jogador.y, angulo_raio)

        altura_parede = int(ALTURA_TELA / max(0.1, distancia))
        teto = max(0, ALTURA_TELA // 2 - altura_parede)
        chao = min(ALTURA_TELA, ALTURA_TELA // 2 + altura_parede)

        pixels = []
        for y in range(ALTURA_TELA):
            if y < teto:
                pixels.append(" ")
            elif y <= chao:
                pixels.append(caractere_parede(distancia))
            else:
                pixels.append("_")
        colunas.append(pixels)

    linhas = []
    for y in range(ALTURA_TELA):
        linhas.append("".join(colunas[x][y] for x in range(LARGURA_TELA)))

    hud = f"X:{jogador.x:.2f} Y:{jogador.y:.2f} Ângulo:{jogador.angulo:.2f}"
    ajuda = "Comandos: [w] frente, [s] ré, [a]/[d] gira, [q] sair"
    mini = mini_mapa(jogador)
    return "\n".join(linhas + [hud, ajuda, mini])


def mini_mapa(jogador: Jogador) -> str:
    linhas = []
    for y, linha in enumerate(MAPA):
        chars = list(linha)
        if y == int(jogador.y) and 0 <= int(jogador.x) < len(chars):
            chars[int(jogador.x)] = "P"
        linhas.append("".join(chars))
    return "\n".join(linhas)


def main() -> None:
    jogador = Jogador()
    print("=== MINI DOOM ASCII ===")

    while True:
        print(renderizar(jogador))
        cmd = input("> ").strip().lower()
        if cmd == "q":
            print("Até a próxima!")
            break
        if cmd == "w":
            mover(jogador, frente=0.3, giro=0)
        elif cmd == "s":
            mover(jogador, frente=-0.3, giro=0)
        elif cmd == "a":
            mover(jogador, frente=0, giro=-0.2)
        elif cmd == "d":
            mover(jogador, frente=0, giro=0.2)


if __name__ == "__main__":
    main()
