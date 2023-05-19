import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 350))
        pygame.display.set_caption("Fat Chicken Run")
        # setting the fps of the game
        self.framerate = pygame.time.Clock()
        # setting the background of the game window
        self.bg = pygame.image.load("resources/background_image.png").convert()

        # creating and resizing the character in our game (bird)
        # self.char = pygame.image.load("resources/char_1.png").convert_alpha()
        self.char = pygame.image.load(
            "resources/fat_chicken/chicken_frame4.png"
        ).convert_alpha()
        # self.new_char = pygame.transform.scale(self.char, (52, 38))
        self.new_char = pygame.transform.scale(self.char, (52, 52))
        self.char_width = 49
        # self.char_height = 34
        self.char_height = 49
        self.char_x = 100
        self.char_y = 288
        self.char_rect = pygame.Rect(
            self.char_x, self.char_y, self.char_width, self.char_height
        )

        self.char_gravity = 0

        # setting the name of our game
        self.game_font = pygame.font.Font(None, 30)
        self.text = self.game_font.render("Angy Iti Run", False, "black")
        self.text_rect = self.text.get_rect(center=(300, 100))

        # creating a running scoreboard
        # self.scoreboard = self.game_font.render("Your score: ", False, "black")

        # creating and resizing the obstacles (cactus)
        self.cactus = pygame.image.load("resources/cactus_image1.png").convert_alpha()
        self.new_cactus = pygame.transform.scale(self.cactus, (68, 62))
        # self.cactus_x_pos = 700
        self.cactus_width = 54
        self.cactus_height = 46
        self.cactus_x = 400
        self.cactus_y = 232
        self.new_cactus_rect = pygame.Rect(
            self.cactus_x, self.cactus_y, self.cactus_width, self.cactus_height
        )

        # setting the clock of the game
        self.start_time = 0

        # checking to see if game is active
        self.game_active = True

    def display_score(self):
        self.current_time = pygame.time.get_ticks() - self.start_time
        self.current_time_in_sec = self.current_time / 1000
        self.round_time = round(self.current_time_in_sec, 1)
        self.score_surf = self.game_font.render(
            f"time:{self.round_time}", False, "black"
        )
        self.score_rect = self.score_surf.get_rect(center=(550, 20))
        self.screen.blit(self.score_surf, self.score_rect)

    def game_over_screen(self):
        # background color
        self.screen.fill("lightblue")

        # selecting image when game over
        self.game_over_pic = pygame.image.load(
            "resources/grim_reaper.png"
        ).convert_alpha()
        self.new_game_over_pic = pygame.transform.scale(self.game_over_pic, (326, 163))
        self.game_over_rect = self.new_game_over_pic.get_rect(center=(300, 130))

        # game over message
        self.game_over_text = self.game_font.render("Game Over", True, "black")
        self.game_over_text_rect = self.game_over_text.get_rect(center=(300, 30))

        # the time the player survived message
        self.time_result = self.game_font.render(
            f"You survived for: {self.round_time} seconds", True, "black"
        )
        self.time_result_rect = self.time_result.get_rect(center=(300, 230))

        # game instructions
        self.instruction = self.game_font.render(
            "press 'Return' to replay                press 'Esc' to quit game",
            True,
            "black",
        )
        self.instruction_rect = self.instruction.get_rect(center=(300, 290))

        self.screen.blit(self.game_over_text, self.game_over_text_rect)
        self.screen.blit(self.new_game_over_pic, self.game_over_rect)
        self.screen.blit(self.time_result, self.time_result_rect)
        self.screen.blit(self.instruction, self.instruction_rect)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                if event.type == pygame.QUIT:
                    run = False
                if self.game_active == True:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE and self.char_rect.bottom == 288:
                            self.char_gravity = -17
                else:
                    if event.type == KEYDOWN and event.key == K_RETURN:
                        self.game_active = True
                        self.new_cactus_rect.left = 700
                        self.start_time = pygame.time.get_ticks()

            if self.game_active == True:
                self.screen.blit(self.bg, (0, 0))

                # player gravity
                self.char_gravity += 1
                self.char_rect.y += self.char_gravity
                if self.char_rect.bottom >= 288:
                    self.char_rect.bottom = 288
                self.screen.blit(self.new_char, self.char_rect)

                # pygame.draw.rect(self.screen, "white", self.text_rect)
                # pygame.draw.rect(self.screen, "white", self.text_rect, 10)
                # self.screen.blit(self.text, self.text_rect)
                self.display_score()

                self.new_cactus_rect.x -= 5
                if self.new_cactus_rect.right <= 0:
                    self.new_cactus_rect.left = 700

                self.screen.blit(self.new_cactus, self.new_cactus_rect)
                # self.new_char_rect.left += 1

                # checking to see if the two rectangles around bird and cactus are colliding with each other
                if self.char_rect.colliderect(self.new_cactus_rect):
                    self.game_active = False
            else:
                self.game_over_screen()

            pygame.display.update()
            self.framerate.tick(60)

    pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
