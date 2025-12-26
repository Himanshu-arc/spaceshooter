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
        # Move downward
        self.center_y -= ENEMY_SPEED

        # Zig-zag movement
        self.center_x += math.sin(self.angle_offset) * 2
        self.angle_offset += 0.05

        if self.top < 0:
            self.reset_pos()

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 50, SCREEN_HEIGHT + 200)
        self.center_x = random.randrange(50, SCREEN_WIDTH - 50)


class Explosion(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(
            ":resources:images/spritesheets/explosion.png",
            scale=0.5,
            center_x=x,
            center_y=y
        )
        self.textures = arcade.load_spritesheet(
            ":resources:images/spritesheets/explosion.png",
            256, 256, 16, 60
        )
        self.current_texture = 0

    def update(self):
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.texture = self.textures[self.current_texture]
        else:
            self.remove_from_sprite_lists()


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background = arcade.load_texture("/mnt/data/space.jpg")

        self.player = None
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()

        self.lives = PLAYER_LIVES
        self.game_over = False

        # 🎵 Sounds
        self.shoot_sound = arcade.load_sound(":resources:sounds/laser1.wav")
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion1.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")

    def setup(self):
        self.player = arcade.Sprite("/mnt/data/monoplane.png", PLAYER_SCALING)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 60

        self.enemy_list.clear()

        for _ in range(ENEMY_COUNT):
            enemy = Enemy("/mnt/data/enemy image'.jpg", ENEMY_SCALING)
            enemy.reset_pos()
            self.enemy_list.append(enemy)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background
        )

        self.player.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.explosion_list.draw()

        # ❤️ Lives display
        arcade.draw_text(
            f"Lives: {self.lives}",
            10, SCREEN_HEIGHT - 30,
            arcade.color.WHITE, 18
        )

        if self.game_over:
            arcade.draw_text(
                "GAME OVER",
                SCREEN_WIDTH // 2 - 120,
                SCREEN_HEIGHT // 2,
                arcade.color.RED,
                36
            )

    def on_update(self, delta_time):
        if self.game_over:
            return

        self.player.center_x += self.player.change_x
        self.player.left = max(self.player.left, 0)
        self.player.right = min(self.player.right, SCREEN_WIDTH)

        self.bullet_list.update()
        self.enemy_list.update()
        self.explosion_list.update()

        # Bullet → Enemy
        for bullet in self.bullet_list:
            hits = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            for enemy in hits:
                bullet.remove_from_sprite_lists()
                enemy.remove_from_sprite_lists()

                explosion = Explosion(enemy.center_x, enemy.center_y)
                self.explosion_list.append(explosion)

                arcade.play_sound(self.explosion_sound)

        # Enemy → Player
        hits = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        for enemy in hits:
            enemy.reset_pos()
            self.lives -= 1
            arcade.play_sound(self.hit_sound)

            if self.lives <= 0:
                self.game_over = True

        # Respawn enemies
        while len(self.enemy_list) < ENEMY_COUNT:
            enemy = Enemy("/mnt/data/enemy image'.jpg", ENEMY_SCALING)
            enemy.reset_pos()
            self.enemy_list.append(enemy)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        elif key == arcade.key.SPACE and not self.game_over:
            bullet = Bullet(":resources:images/space_shooter/laserBlue01.png", BULLET_SCALING)
            bullet.center_x = self.player.center_x
            bullet.bottom = self.player.top
            self.bullet_list.append(bullet)
            arcade.play_sound(self.shoot_sound)

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0



# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Hero Shooter"

PLAYER_SCALING = 0.5
ENEMY_SCALING = 0.5
BULLET_SCALING = 0.8

ENEMY_COUNT = 10
BULLET_SPEED = 10
ENEMY_SPEED = 2

class Bullet(arcade.Sprite):
    def update(self):
        # Move bullet upward
        self.center_y += BULLET_SPEED
        # Remove if off screen
        if self.top > SCREEN_HEIGHT:
            self.remove_from_sprite_lists()

class Enemy(arcade.Sprite):
    def update(self):
        # Move enemy downward
        self.center_y -= ENEMY_SPEED
        # If enemy goes off screen, move to top again
        if self.bottom < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(50, SCREEN_WIDTH - 50)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.player = None
        self.enemy_list = None
        self.bullet_list = None

    def setup(self):
        # Create player sprite
        self.player = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", PLAYER_SCALING)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 50

        # Sprite lists
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Create enemies
        for i in range(ENEMY_COUNT):
            enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_red.png", ENEMY_SCALING)
            enemy.center_x = random.randrange(50, SCREEN_WIDTH - 50)
            enemy.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 150)
            self.enemy_list.append(enemy)

    def on_draw(self):
        arcade.start_render()
        # Draw background
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw sprites
        self.player.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()

    def on_update(self, delta_time):
        # Update bullets and enemies
        self.bullet_list.update()
        self.enemy_list.update()

        # Check for collisions
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                bullet.remove_from_sprite_lists()

        # Respawn enemies
        while len(self.enemy_list) < ENEMY_COUNT:
            enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_red.png", ENEMY_SCALING)
            enemy.center_x = random.randrange(50, SCREEN_WIDTH - 50)
            enemy.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 150)
            self.enemy_list.append(enemy)

    def on_key_press(self, key, modifiers):
        # Move player left/right
        if key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5
        # Shoot bullet
        elif key == arcade.key.SPACE:
            bullet = Bullet(":resources:images/space_shooter/laserBlue01.png", BULLET_SCALING)
            bullet.center_x = self.player.center_x
            bullet.bottom = self.player.top
            self.bullet_list.append(bullet)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_update(self, dt):
        # Update positions
        self.player.center_x += self.player.change_x
        self.bullet_list.update()
        self.enemy_list.update()

        # Keep player on screen
        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

        # Collision detection
        for bullet in self.bullet_list:
            enemies_hit = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if enemies_hit:
                bullet.remove_from_sprite_lists()
                for enemy in enemies_hit:
                    enemy.remove_from_sprite_lists()

        # Respawn enemies
        while len(self.enemy_list) < ENEMY_COUNT:
            new_enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_red.png", ENEMY_SCALING)
            new_enemy.center_x = random.randrange(50, SCREEN_WIDTH - 50)
            new_enemy.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 150)
            self.enemy_list.append(new_enemy)

if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
