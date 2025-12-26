import arcade
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Hero Shooter"

PLAYER_SCALING = 0.4
ENEMY_SCALING = 0.4
BULLET_SCALING = 0.8

ENEMY_COUNT = 8
BULLET_SPEED = 10
ENEMY_SPEED = 2
PLAYER_SPEED = 5
PLAYER_LIVES = 3


class Bullet(arcade.Sprite):
    def update(self):
        self.center_y += BULLET_SPEED
        if self.bottom > SCREEN_HEIGHT:
            self.remove_from_sprite_lists()


class Enemy(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.angle_offset = random.uniform(0, 6.28)

    def update(self):
        self.center_y -= ENEMY_SPEED
        self.center_x += math.sin(self.angle_offset) * 2
        self.angle_offset += 0.05

        if self.top < 0:
            self.reset_pos()

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 50, SCREEN_HEIGHT + 200)
        self.center_x = random.randrange(50, SCREEN_WIDTH - 50)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player = None
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.lives = PLAYER_LIVES
        self.game_over = False

    def setup(self):
        self.player = arcade.Sprite(
            ":resources:images/space_shooter/playerShip1_blue.png",
            PLAYER_SCALING
        )
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 60

        self.enemy_list.clear()
        self.bullet_list.clear()

        for _ in range(ENEMY_COUNT):
            enemy = Enemy(
                ":resources:images/space_shooter/playerShip1_red.png",
                ENEMY_SCALING
            )
            enemy.reset_pos()
            self.enemy_list.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()

    def on_update(self, dt):
        if self.game_over:
            return

        self.player.center_x += self.player.change_x
        self.player.left = max(self.player.left, 0)
        self.player.right = min(self.player.right, SCREEN_WIDTH)

        self.bullet_list.update()
        self.enemy_list.update()

        for bullet in self.bullet_list:
            enemies_hit = arcade.check_for_collision_with_list(
                bullet, self.enemy_list
            )
            for enemy in enemies_hit:
                bullet.remove_from_sprite_lists()
                enemy.reset_pos()

        for enemy in arcade.check_for_collision_with_list(
            self.player, self.enemy_list
        ):
            enemy.reset_pos()
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        elif key == arcade.key.SPACE:
            bullet = Bullet(
                ":resources:images/space_shooter/laserBlue01.png",
                BULLET_SCALING
            )
            bullet.center_x = self.player.center_x
            bullet.bottom = self.player.top
            self.bullet_list.append(bullet)

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
