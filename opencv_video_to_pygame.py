from pygame.locals import KEYDOWN, K_ESCAPE, K_q
import pygame
import cv2
import sys

camera = cv2.VideoCapture(1)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([1280, 720])

try:
    while True:

        ret, frame = camera.read()

        screen.fill([0, 0, 0])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame.swapaxes(0, 1)
        pygame.surfarray.blit_array(screen, frame)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit(0)

except (KeyboardInterrupt, SystemExit):
    pygame.quit()
    cv2.destroyAllWindows()
