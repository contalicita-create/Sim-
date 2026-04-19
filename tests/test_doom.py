import math
import unittest

from doom import Jogador, cast_ray, mover, parede


class DoomTests(unittest.TestCase):
    def test_parede_identifica_bordas(self):
        self.assertTrue(parede(0, 0))
        self.assertFalse(parede(1.5, 1.5))

    def test_cast_ray_detecta_parede(self):
        distancia = cast_ray(2.5, 2.5, 0.0)
        self.assertGreater(distancia, 0)
        self.assertLess(distancia, 12.0)

    def test_mover_avanca_em_area_livre(self):
        jogador = Jogador(x=2.5, y=2.5, angulo=0.0)
        mover(jogador, frente=0.3, giro=0)
        self.assertGreater(jogador.x, 2.5)

    def test_mover_rotaciona_sem_quebrar_angulo(self):
        jogador = Jogador(x=2.5, y=2.5, angulo=0.0)
        mover(jogador, frente=0, giro=2 * math.pi + 0.2)
        self.assertAlmostEqual(jogador.angulo, 0.2, places=6)


if __name__ == "__main__":
    unittest.main()
