import pygame 
from sys import exit

pygame.init()
screen= pygame.display.set_mode((800,610))

pygame.display.set_caption('Farming Monkey')
clock=pygame.time.Clock()

MainSurface = pygame.image.load("FarmMonkey/Landscape/grass.jpg").convert_alpha()
MainSurface1= pygame.transform.scale (MainSurface,(800,610))

#When won
testFont = pygame.font.Font(None, 100)
textWin = testFont.render ("You Won", False,'GREEN')
textRect= textWin.get_rect(center = (400, 305))

#When lost
textLose = testFont.render ("You lose",False, 'RED')
textRect1=textLose.get_rect(center = (400,305))

#Barn to check your inventory
barn = pygame.image.load('FarmMonkey/barn.png').convert_alpha()
barn1 = pygame.transform.scale(barn,(150,150))
barn_rect= barn1.get_rect(bottomright=(790,600))
barn_menu_open=False

timeLeft = 300 #seconds

#When you try to unlock something and you cannot a message will popup
#At the moment we have no message nor do we need any time at the moment 
popupMessage = None
popupTimer = 0
popupXPos,popupYPos = 0,0

class Vegetable:
    '''
    The cost it takes to plant one (number of coins)
    The number of coins in produces when farmed
    The number of seconds it takes to 'grow'
    At how many seconds the plant was produced 
    Check if it is ready to produce 
    If it is available (unlocked)
    The materials needed to unlock the vegetable
    The image of the crop 
    '''
    def __init__ (self,vType,cost,produce,time,image,available,unlock = None):
        self.type= str(vType)
        self.cost= cost 
        self.produce_cost = produce
        self.growth_time = time
        self.available = available
        self.unlock = unlock
        self.image=image
      
wheat = Vegetable('wheat',1,2,5,pygame.image.load('FarmMonkey/Vegetables/wheat.png').convert_alpha(),True)
corn = Vegetable('corn',4,6,10,pygame.image.load('FarmMonkey/Vegetables/corn.png').convert_alpha(), False,{wheat:10} )
carrot = Vegetable('carrot',10,15,15,pygame.image.load('FarmMonkey/Vegetables/carrot.png').convert_alpha(), False,{wheat:10,corn:5})
potato=Vegetable('potato',12,18,30,pygame.image.load ('FarmMonkey/Vegetables/potato.png').convert_alpha(),False,{corn:5 ,carrot:10})
banana=Vegetable('banana', 20,30,40,pygame.image.load('FarmMonkey/Vegetables/banana.png').convert_alpha(),False,{carrot :10 , potato:10})
crop_options = [wheat, corn, carrot, potato, banana]  # Available crops
inventory = {wheat:0 ,corn:0,carrot:0,potato:0,banana:0}
coins = 10

class Dirt:
    def __init__(self, x, y, unlocked):
        self.xPos = x
        self.yPos = y 
        self.unlocked = unlocked 
        self.empty= True
        self.cost = 10
        self.crop = None
        self.planted_time = None
        self.harvest_ready=False
        self.menu_open = False 
        self.set_image()
    
    def plant(self):
        global timeLeft
        '''
        Setting the time at which the crop was planted
        '''
        self.planted_time = timeLeft

    def update_growth(self):
        global timeLeft
        '''
        Checking if the time needed for the crop to grow has passed. 
        Does so by checking if the time planted - the current time is greater than or equal to the time needed to grow 
        if it is then it changes ready to harvest to True so the played can harvest said crop 
        '''
        if self.planted_time and self.planted_time - timeLeft >= self.crop.growth_time:
            self.harvest_ready = True
        
    def set_image(self):
        if self.crop: 
            if self.harvest_ready :
                self.image = self.crop.image
            else:
                self.image = pygame.image.load('FarmMonkey/Vegetables/seedling.png').convert_alpha()
        elif self.unlocked:
            self.image = pygame.image.load('FarmMonkey/Landscape/dirt.png').convert_alpha()
        else:
            self.image = pygame.image.load('FarmMonkey/Unlocking/dirtPlus.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # Correctly store the image
        self.rect = self.image.get_rect(topleft=(self.xPos, self.yPos))  # Store Rect separately for position tracking
    
    def is_clicked(self, mouse_x, mouse_y):
        clicked = self.rect.collidepoint(mouse_x, mouse_y)
        return clicked  # Check if the mouse clicked inside the patch    
        
dirts = []
for x in range (10 , 380, 80):
    for y in range (10, 400, 80):
        unlocked =  len(dirts)<6
        currect_dirt = Dirt (x,y,unlocked)
        dirts.append (currect_dirt)

# Keeping Track
def tracker ():
    ''' 
    keeps track of all the important stuff on the side of the screen to ensure the played is aware of 
    time and his materials 
    '''
    font = pygame.font.Font(None,20)
    timer_text = font.render(f"Time Left: {timeLeft}s", True, (0, 0, 0))
    coins_text = font.render(f"Coins: {coins}", True, (0, 0, 0))
    banana_text = font.render(f"Bananas: {inventory[banana]}/5", True, (0, 0, 0))

    return screen.blit(timer_text, (700,20)), screen.blit(coins_text, (700, 40)) , screen.blit(banana_text, (700, 60))

def secondTracker (a):
    global timeLeft
    '''
    The game runs a frame thirty times every second, so for every thity runs a second passes 
    and the time left will be ruduced by one
    '''
    if a==30:
        timeLeft -=1
        return timeLeft 
    else:
        return timeLeft

def draw_crop_menu(screen, x, y, crop_options):
    menu_width, menu_height = 200, 270
    menu_x = x + 40  
    menu_y = y 
    pygame.draw.rect(screen, (220, 220, 220), (menu_x, menu_y, menu_width, menu_height), border_radius=10) 

    font = pygame.font.Font(None, 22) 

    for index, crop in enumerate(crop_options):
        crop_x = menu_x + 10 
        crop_y = menu_y + 10 + (index *50)  

        if crop.available:
            crop_image_scaled = pygame.transform.scale(crop.image, (40, 40)) 
            screen.blit(crop_image_scaled, (crop_x, crop_y))
            cost_text = font.render (f": {crop.cost} coin",True, (0,0,0))
            screen.blit (cost_text, (crop_x + 60, crop_y + 10))

        else:
            locked_image = pygame.Surface((40, 40))  # Smaller, cleaner gray box
            locked_image.fill((100, 100, 100))  
            screen.blit(locked_image, (crop_x, crop_y))   
            unlocked = font.render(f":locked", True, (0, 0, 0))  
            screen.blit(unlocked, (crop_x + 60, crop_y + 10))   
    
def draw_barn_inventory():
    global crop_options,inventory
    menu_x,menu_y =  410,250
    pygame.draw.rect(screen, (220, 220, 220), (menu_x, menu_y,300, 270), border_radius=10)
    for index, crop in enumerate(crop_options):
        crop_x = menu_x + 10 
        crop_y = menu_y + 10 + (index *50) 

        font = pygame.font.Font(None, 22) 
        if crop.available:
            crop_image_scaled = pygame.transform.scale(crop.image, (40, 40)) 
            screen.blit(crop_image_scaled, (crop_x, crop_y))
            amount_text = font.render (f": {inventory[crop]}",True, (0,0,0))
            screen.blit (amount_text, (crop_x + 60, crop_y +10))
        else:
            locked_image = pygame.Surface((40, 40))  # Smaller, cleaner gray box
            locked_image.fill((100, 100, 100))  
            screen.blit(locked_image, (crop_x, crop_y)) 
            needed = {}  
            for crop,amount in crop.unlock.items():
                needed[crop.type] = amount
            unlock_text = font.render(f": {needed}", True, (0, 0, 0))  
            screen.blit(unlock_text, (crop_x + 60, crop_y + 10)) 
            
def get_clicked_crop (dirt, mouse_x,mouse_y):
    crop = None
    wheat_rect = pygame.Rect(dirt.xPos + 30 , dirt.yPos , 50, 50)
    corn_rect = pygame.Rect ( dirt.xPos + 30 ,dirt.yPos + 60,50,50)
    carrot_rect = pygame.Rect (dirt.xPos + 30 , dirt.yPos + 110 , 50,50)
    potato_rect = pygame.Rect (dirt.xPos + 30 , dirt.yPos + 160 , 50,50)
    banana_rect = pygame.Rect ( dirt.xPos + 30, dirt.yPos + 210, 50,50)
    if wheat_rect.collidepoint (mouse_x,mouse_y):
        crop = wheat
    elif corn_rect.collidepoint (mouse_x,mouse_y) and corn.available:
        crop = corn 
    elif carrot_rect.collidepoint (mouse_x,mouse_y) and carrot.available:
        crop = carrot
    elif potato_rect.collidepoint (mouse_x,mouse_y) and potato.available:
        crop = potato 
    elif banana_rect.collidepoint(mouse_x,mouse_y) and banana.available:
        crop = banana
    return crop

def find_clicked_barn(mouse_x,mouse_y):
    crop =None
    corn_rect=pygame.Rect(420,310,40,40)
    carrot_rect=pygame.Rect(420,360,40,40)
    potato_rect=pygame.Rect(420,410,40,40)
    banana_rect=pygame.Rect(420,460,40,40)
    if corn_rect.collidepoint(mouse_x,mouse_y):
        crop = corn
    elif carrot_rect.collidepoint(mouse_x,mouse_y):
        crop = carrot
    elif potato_rect.collidepoint(mouse_x,mouse_y):
        crop =potato
    elif banana_rect.collidepoint(mouse_x,mouse_y):
        crop = banana
    return crop

def handle_cant_unlock (x,y,message):
    global popupMessage,popupTimer,popupXPos,popupYPos
    popupMessage=message
    popupTimer=120 #frames
    popupXPos,popupYPos = x,y
    
def handle_cant_unlock_menu(x,y):
    global popupMessage,popupTimer
    pygame.draw.rect(screen,(255,200,200),(x,y,150,30),border_radius=10)
    font= pygame.font.Font(None,20)
    text=font.render(popupMessage,True,(0,0,0))
    screen.blit(text,(x + 5,y + 5))
    popupTimer -= 1

def unlock_new_crops(unlocking_crop):
    unlock = True
    for item,amount in unlocking_crop.unlock.items():
        if not inventory[item] >= amount:
            unlock = False
            handle_cant_unlock(420,385,f"NOT ENOUGH {item.type}")

    if unlock:
        unlocking_crop.available=True
        for item,amount in unlocking_crop.unlock.items():
            inventory[item]-=amount

def find_dirt_with_open_menu():
    for dirt in dirts:
        if dirt.menu_open:
            return dirt

    return None    

def find_clicked_dirt(mouse_x, mouse_y):
    for dirt in dirts:
        if dirt.is_clicked(mouse_x, mouse_y):
            return dirt
    return None    

def handle_clicked_dirt(dirt):
    global coins,inventory
    if dirt.unlocked:
        if dirt.empty:
            dirt.menu_open = not dirt.menu_open # Toggle the menu
        else:
            if dirt.harvest_ready:
                coins += dirt.crop.produce_cost
                inventory[dirt.crop] += 1
                dirt.empty = True
                dirt.planted_time= None 
                dirt.harvest_ready=False
                dirt.crop=None
                dirt.set_image()
            else:
                handle_cant_unlock(dirt.xPos,dirt.yPos,"NOT DONE HARVEST")

    elif not dirt.unlocked:
        if coins >= 10: 
            dirt.unlocked = True  
            dirt.set_image()
            coins -= 10 
        else:
            handle_cant_unlock(dirt.xPos,dirt.yPos,"NOT ENOUGHT COINS") 
  
def plant_crop(dirt, selected_crop):
    global coins

    if dirt.unlocked and dirt.empty: 
        if coins >= selected_crop.cost:
            dirt.crop = selected_crop
            coins -= selected_crop.cost  
            dirt.empty = False  
            dirt.set_image()  
        else:
            handle_cant_unlock(dirt.xPos,dirt.yPos,"NOT ENOUGHT COINS")

def handle_mouse_down(mouse_x, mouse_y):
    global barn_menu_open
    dirt_with_open_menu = find_dirt_with_open_menu()
    if dirt_with_open_menu:
        clicked_crop = get_clicked_crop(dirt_with_open_menu, mouse_x, mouse_y)
        if clicked_crop:
            plant_crop(dirt_with_open_menu, clicked_crop)
            dirt_with_open_menu.plant()
        
        dirt_with_open_menu.menu_open = False   
    elif barn_rect.collidepoint(mouse_x,mouse_y):
        barn_menu_open= not barn_menu_open 

    elif not dirt_with_open_menu:
        clicked_dirt = find_clicked_dirt(mouse_x, mouse_y)
        if clicked_dirt:
            handle_clicked_dirt(clicked_dirt)
        elif barn_menu_open:
            if find_clicked_barn(mouse_x,mouse_y):
                unlocking_crop = find_clicked_barn(mouse_x,mouse_y)
                unlock_new_crops(unlocking_crop)

a=0 
running=True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            handle_mouse_down(mouse_x, mouse_y)
    
    screen.blit(MainSurface1,(0,0))
    tracker()
    screen.blit(barn1,barn_rect)
    if barn_menu_open:
        draw_barn_inventory()

    for dirt in dirts:
        if dirt.crop:
            dirt.update_growth()
            if dirt.harvest_ready:
                dirt.set_image()
        screen.blit(dirt.image, (dirt.xPos, dirt.yPos))        
        
    for dirt in dirts:
        if dirt.menu_open:
            draw_crop_menu(screen, dirt.xPos, dirt.yPos, crop_options)
    
    if popupMessage and popupTimer:
        handle_cant_unlock_menu(popupXPos,popupYPos)
    
    #Win
    if inventory[banana]==5:
        screen.fill('White')
        screen.blit(textWin,textRect)
    #loose
    if timeLeft <= 0 and inventory[banana] < 5:
        screen.fill('white')
        screen.blit (textLose,textRect1)
    
    pygame.display.update()
    clock.tick(30)
    a+=1
    timeLeft = secondTracker(a)
    if a==30:
        a=0

