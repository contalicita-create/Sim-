import random
import unittest

from passarinho import (
    ALTURA,
    EstadoJogo,
    atualizar_estado,
    colisao,
    criar_obstaculo,
    mover_obstaculos,
)


class PassarinhoTests(unittest.TestCase):
    def test_criar_obstaculo_dentro_dos_limites(self):
        obs = criar_obstaculo(random.Random(1))
        self.assertEqual(obs[0], 19)
        self.assertGreaterEqual(obs[1], 2)
        self.assertLessEqual(obs[1], ALTURA - 3)

    def test_mover_obstaculos_remove_fora_da_tela(self):
        obstaculos = [(1, 4), (0, 5)]
        self.assertEqual(mover_obstaculos(obstaculos), [(0, 4)])

    def test_colisao_no_cano(self):
        self.assertTrue(colisao(0, [(2, 5)]))
        self.assertFalse(colisao(5, [(2, 5)]))

    def test_atualizar_estado_incrementa_pontos(self):
        estado = EstadoJogo(altura_passarinho=5, velocidade=0, turno=0, pontos=0, obstaculos=[])
        atualizado = atualizar_estado(estado, "", random.Random(2))
        self.assertEqual(atualizado.pontos, 1)
        self.assertEqual(atualizado.turno, 1)


if __name__ == "__main__":
    unittest.main()
