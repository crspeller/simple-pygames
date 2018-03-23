import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

if __name__ == "__main__":
    main()
