import unittest
from types import SimpleNamespace

SCREEN_HEIGHT = 600
BULLET_SPEED = 10


class BulletMock:
    def __init__(self, y):
        self.center_y = y
        self.bottom = y - 5
        self.removed = False

    def remove_from_sprite_lists(self):
        self.removed = True

    def update(self):
        self.center_y += BULLET_SPEED
        self.bottom += BULLET_SPEED
        if self.bottom > SCREEN_HEIGHT:
            self.remove_from_sprite_lists()


class EnemyMock:
    def __init__(self):
        self.reset_called = False

    def reset_pos(self):
        self.reset_called = True


class GameLogicTest(unittest.TestCase):

    def test_bullet_moves_up(self):
        bullet = BulletMock(100)
        bullet.update()
        self.assertEqual(bullet.center_y, 110)

    def test_bullet_removed_when_off_screen(self):
        bullet = BulletMock(700)
        bullet.update()
        self.assertTrue(bullet.removed)

    def test_enemy_reset_called(self):
        enemy = EnemyMock()
        enemy.reset_pos()
        self.assertTrue(enemy.reset_called)

    def test_life_decrement(self):
        game = SimpleNamespace(lives=3)
        game.lives -= 1
        self.assertEqual(game.lives, 2)

    def test_game_over(self):
        game = SimpleNamespace(lives=1, game_over=False)
        game.lives -= 1
        if game.lives <= 0:
            game.game_over = True
        self.assertTrue(game.game_over)


if __name__ == "__main__":
    unittest.main()
