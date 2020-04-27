import pygame
from random import randint, choice

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Фрактал Серпинского')
done = False
pygame.init()

a = pygame.Rect(350, 100, 2, 2)
b = pygame.Rect(200, 350, 2, 2)
c = pygame.Rect(500, 350, 2, 2)

amount_of_points = 1
i = pygame.Rect(randint(292, 411), randint(200, 350), 2, 2)
vertexs = [a,b,c]

while not done:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	text_time = pygame.font.Font(None, 18)
	text_time = text_time.render('i = ' + str(amount_of_points), True, (255,255,255))
	win.blit(text_time, (30, 20))
	random_vertex = randint(0,2)
	vertex = vertexs[random_vertex]
	middle = pygame.Rect((vertex.x + i.x) / 2, (vertex.y + i.y) / 2, 2, 2)
	i = middle
	pygame.draw.rect(win, (255,255,255), a) 
	pygame.draw.rect(win, (255,255,255), b) 
	pygame.draw.rect(win, (255,255,255), c) 
	pygame.draw.rect(win, (255,255,255), i) 
	pygame.display.update()
	text_time = pygame.font.Font(None, 18)
	text_time = text_time.render('i = ' + str(amount_of_points), True, (0,0,0))
	win.blit(text_time, (30, 20))
	amount_of_points += 1
  

pygame.quit()
