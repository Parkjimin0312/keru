import pygame
import random
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("파이썬 공룡 게임")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)


current_path = os.path.dirname(__file__)
dino_image = pygame.image.load(os.path.join(current_path, 'dino.png'))
tree_image = pygame.image.load(os.path.join(current_path, 'tree.png'))

# 공룡 클래스
class Dino:
    def __init__(self):
        self.image = pygame.transform.scale(dino_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 60
        self.y_velocity = 0
        self.is_jumping = False
    
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = -25
            
    def update(self):
        if self.is_jumping:
            self.rect.y += self.y_velocity
            self.y_velocity += 2.0
            if self.rect.y >= SCREEN_HEIGHT - 60:
                self.rect.y = SCREEN_HEIGHT - 60
                self.is_jumping = False
                self.y_velocity = 0
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# 장애물 클래스
class tree:
    def __init__(self):
        self.image = pygame.transform.scale(tree_image, (40, 50))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(100, 300)
        self.rect.y = SCREEN_HEIGHT - 55
        self.x_velocity = -10
        
    def update(self):
        self.rect.x += self.x_velocity
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# 게임 클래스
class Game:
    def __init__(self):
        self.dino = Dino()
        self.obstacles = []
        self.score = 0
        self.is_game_over = False
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.is_game_over:
                        self.dino.jump()
                    if event.key == pygame.K_r and self.is_game_over:
                        self.__init__() # 게임 재시작

            if not self.is_game_over:
                # 게임 로직 업데이트
                self.dino.update()

                # 장애물 생성 및 업데이트
                if len(self.obstacles) < 3 and random.randint(0, 150) == 1:
                    self.obstacles.append(tree())

                for obstacle in self.obstacles[:]:
                    obstacle.update()
                    if obstacle.rect.right < 0:
                        self.obstacles.remove(obstacle)
                        self.score += 1

                # 충돌 감지
                for obstacle in self.obstacles:
                    if self.dino.rect.colliderect(obstacle.rect):
                        self.is_game_over = True

                # 화면 그리기
                screen.fill(WHITE)
                self.dino.draw(screen)
                for obstacle in self.obstacles:
                    obstacle.draw(screen)
                
                # 점수 표시
                score_text = font.render(f"Score: {self.score}", True, BLACK)
                screen.blit(score_text, (10, 10))

            else:
                # 게임 오버 화면
                game_over_text = font.render("gg", True, BLACK)
                restart_text = font.render("Restart click "R" ", True, BLACK)
                screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20))
                screen.blit(restart_text, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 20))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()