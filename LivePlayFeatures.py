import pygame

'''
Additional features for game (pygame)


1. Buttons for start / restart / hint 
    a. Type of hint? - give a number , or highlight a strategy/boxes??
    b. depending on strategy, dark highlight boxes to change, and their connecting rows/col/box??
    
2. Difficulty level 

3. Timer? 

4. Infinate loop for moving up/down left/right 

5. Longer Description


6. Show possible numbers in box? 
    a. Allow for active removal? or Automatic? 
    
7. Save name/score / accounts? 

'''

class Button(): 
    
    def __init__(self, x, y, width, height, buttonText = 'Button', onclickFunction = None, onePress = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed' :'#333333'
        }
        
        
        self.buttonSurvace = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font4.render(buttonText, True, (20,20,20))
        
        objects.append(self)
        
        
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
                
        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
        
def myFunction():
    print('Button pressed')