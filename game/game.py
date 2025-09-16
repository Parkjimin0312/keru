import pygame
import random
import os

pygame.init()

#화면 구성
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game")

#현재 스크립터 파일경로 가져옴
current_path = os.path.dirname(__file__)

fps = pygame.time.Clock()

#이미지 파일 폴더 경로 탐색
BlueDragon_folder = os.path.join(current_path, 'BlueDragon')

#이미지 로드
BlueDragon_images = {
    'east':pygame.image.load(os.path.join(BlueDragon_folder,'east.png')).convert_alpha(),
    'west':pygame.image.load(os.path.join(BlueDragon_folder,'west.png')).convert_alpha(),
    'south':pygame.image.load(os.path.join(BlueDragon_folder,'south.png')).convert_alpha(),
    'north':pygame.image.load(os.path.join(BlueDragon_folder,'north.png')).convert_alpha()
} 

#초기 이미지와 시작 위치 설정
current_image = BlueDragon_images['south']
x_position = SCREEN_WIDTH // 2 - current_image.get_width() // 2
y_position = SCREEN_HEIGHT // 2 - current_image.get_height() // 2

#캐릭터 이동 속도 설정
movement_speed = 10

play = True
while play:
    fps.tick(60)
    ##게임 진행중일때 나타나는 이벤트를 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
        keys = pygame.key.get_pressed()

        #방향키를 눌렀을때 캐릭터 이미지랑 위치 변경
        if keys[pygame.K_UP]:
            current_image = BlueDragon_images['north']
            y_position -= movement_speed
        if keys[pygame.K_DOWN]:
            current_image = BlueDragon_images['south']
            y_position += movement_speed
        if keys[pygame.K_LEFT]:
            current_image = BlueDragon_images['west']
            x_position -= movement_speed
        if keys[pygame.K_RIGHT]:
            current_image = BlueDragon_images['east']
            x_position += movement_speed

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(current_image, (x_position, y_position))

    pygame.display.update()

pygame.quit()