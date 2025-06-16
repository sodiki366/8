# Задание сделать так что бы можно было отвязать тонкую линию
# Что бы рисковать не связанные между собой физуры

import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование линий")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)

LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)

points = []
drawing_mode = True # Режим рисования (вып/выкл)

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and drawing_mode: # Левая кнопка + режим рисования
                points.append(event.pos)
            elif event.button == 3: # Правая кнопка – переключить режим
                drawing_mode = not drawing_mode

    # Отрисовка
    screen.fill(BACKGROUND)

    # Рисуем уже добавленные линии
    for i in range(len(points) - 1):
        start_point = points[i]
        end_point = points[i + 1]
        pygame.draw.line(screen, LINE_COLOR, start_point, end_point, 3)

    # Рисуем линию предпроектора (если есть точки и режим включён)
    if len(points) > 0 and drawing_mode:
        last_point = points[-1]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos, 3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()