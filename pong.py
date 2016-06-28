import pygame, sys
FPS = 200
WindowWidth = 400
WindowHeight = 300

lineThickness = 10
paddleSize = 50
PaddleOffSet = 20
PaddleSpeed = 2

Black = (0, 0, 0)
White = (255,255,255)

def drawArena():
	DisplaySurf.fill((0,0,0))
	pygame.draw.rect(DisplaySurf,White, ((0,0),(WindowWidth,WindowHeight)),lineThickness*2)
	pygame.draw.line(DisplaySurf,White,((WindowWidth/2),0),((WindowWidth/2),WindowHeight),(lineThickness))

def drawPaddle(paddle, paddlerect):
	if paddlerect.bottom > WindowHeight - lineThickness:
		paddlerect.bottom = WindowHeight - lineThickness
	elif paddlerect.top < lineThickness:
		paddlerect.top = lineThickness
	DisplaySurf.blit(paddle,paddlerect)

def drawBall(bal,balrect):
	DisplaySurf.blit(bal,balrect)
	
def moveBall(ballrect, ballDirX, ballDirY):
	ballrect.x = ballrect.x+ballDirX
	ballrect.y = ballrect.y+ballDirY
	return ballrect
def checkEdgeCollision(ballrect, ballDirX, ballDirY):
	if ballrect.top ==lineThickness or ballrect.bottom == (WindowHeight-lineThickness):
		ballDirY = ballDirY*-1
	if ballrect.left == lineThickness or ballrect.right == (WindowWidth-lineThickness):
		ballDirX = ballDirX*-1
	return ballDirX, ballDirY\
def checkHitBall(ballrect, paddle1rect, paddle2rect, ballDirX):
	if ballDirX == -1 and paddle1rect.right == ballrect.left and paddle1rect.top < ballrect.top and paddle1rect.bottom > ballrect.bottom:
		return -1
	elif ballDirX == -1 and paddle1rect.right == ballrect.left and paddle1rect.top < ballrect.top and paddle1rect.bottom > ballrect.bottom:
		return -1
	else:
		return 1


def main():
	pygame.init()
	pygame.key.set_repeat(1,50)
	global DisplaySurf
	FPSCLOCK = pygame.time.Clock()
	DisplaySurf = pygame.display.set_mode((WindowWidth,WindowHeight))
	pygame.display.set_caption('Pongerango')

	ballX = WindowWidth/2 - lineThickness/2
	ballY = WindowHeight/2 - lineThickness/2
	playerOnePosition = (WindowHeight - paddleSize)/2
	playerTwoPosition = (WindowHeight - paddleSize)/2
	ballDirX = -1
	ballDirY = -1
##############################################################
	paddle1 = pygame.image.load("paddle.png")
	paddle2 = pygame.image.load("paddle2.png")
	ball = pygame.image.load("ball.png")

	paddle1 = pygame.transform.scale(paddle1, (lineThickness,paddleSize))
	paddle2 = pygame.transform.scale(paddle2, (lineThickness,paddleSize))
	ball = pygame.transform.scale(ball, (lineThickness, lineThickness))

	paddle1rect = paddle1.get_rect()
	paddle2rect = paddle2.get_rect()
	ballrect = ball.get_rect()

	paddle1rect = paddle1rect.move(PaddleOffSet,playerOnePosition)
	paddle2rect = paddle2rect.move(WindowWidth - PaddleOffSet - lineThickness, playerTwoPosition)
	ballrect = ballrect.move(ballX,ballY)

	drawArena()
	drawPaddle(paddle1,paddle1rect)
	drawPaddle(paddle2,paddle2rect)
	drawBall(ball,ballrect)



	

	while True:
		for event in pygame.event.get():
			#if event.type == QUIT:
			#	pygame.quit()
			#	sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					paddle2rect.y = paddle2rect.y - PaddleSpeed
				if event.key == pygame.K_DOWN:
					paddle2rect.y = paddle2rect.y + PaddleSpeed
				if event.key == pygame.K_w:
					paddle1rect.y = paddle1rect.y - PaddleSpeed
				if event.key == pygame.K_s:
					paddle1rect.y = paddle1rect.y + PaddleSpeed


		pygame.display.update()
		FPSCLOCK.tick(FPS)
		drawArena()
		drawPaddle(paddle1,paddle1rect)
		drawPaddle(paddle2,paddle2rect)
		drawBall(ball,ballrect)
		ballrect = moveBall(ballrect,ballDirX, ballDirY)
		ballDirX, ballDirY = checkEdgeCollision(ballrect, ballDirX, ballDirY)
		ballDirX = ballDirX* checkHitBall(ball,paddle1rect,paddle2rect, ballDirX)
if __name__=='__main__':
	main()
