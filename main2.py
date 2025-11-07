import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
backgroundimg = pygame.transform.scale(pygame.image.load("bg.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
isagiimg =pygame.transform.scale(pygame.image.load("images.jpg").convert_alpha(), (200, 200))
isagirect = isagiimg.get_rect(center =(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 -30))
text = pygame.font.Font(None, 36).render("Isagi", True,pygame.Color("black"))
textrect = text.get_rect(center =(SCREEN_WIDTH//2, SCREEN_HEIGHT +110))

def game_loop():
                 
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(backgroundimg, (0, 0))
        screen.blit(isagiimg, isagirect)
        screen.blit(text, textrect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()
 
            
        
        
        