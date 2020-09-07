#Sorting Algorithm Visualizer
#Created by Hamzah Shahid

import pygame
from random import randint
import pygame_widgets
from sys import exit

#initialize pygame
pygame.init()

#initial array size
arraySize = 10
data = []
progress = []

#initial bool
isSorted = False
done = False

#define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0,0,0)

#create screen
size = (900, 600)
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption("Sorting Algorithm Visualizer")

#create sorting visualizer surface
barSurface = pygame.Surface((900, 400))
barSurface.fill((50,50,50))
gameDisplay.blit(barSurface, (0, 200))
barSurfaceUpdateRect = pygame.Rect(50, 200,800, 400)

#create slider used to adjust the array size
slider = pygame_widgets.Slider(gameDisplay, 650, 100, 200, 50, min=10, max=100, step=10, initial = 10)

# create a clock to control how fast the screen updates
clock = pygame.time.Clock()

#fixes the size of the data when adjusting the slider
def fixSize(newSize):
    data = arrayInit(newSize, 20)
    return data

#draws the bars after each step in the sorting algorithm
def drawRect(data, progress):
    #clears the screen 
    barSurface.fill((50,50,50))

    #title 
    titleCenter = ((450), (50))
    textSurf, textRect = text_objects("Sorting Algorithm Visualizer", largeText, BLACK, titleCenter)
    gameDisplay.blit(textSurf, textRect)
    
    #determines which color to make the bars
    for i in range(arraySize):
        color = BLACK
        if progress[i] == 1:
            color = WHITE
        elif progress[i] == 2:
            color = RED
        else:
            color = GREEN
        
        #draws the rectangle
        pygame.draw.rect(barSurface, color, pygame.Rect((50 + (750/arraySize)*i, 350 - 15*data[i], (300/arraySize), 15*data[i])))
    
    #pushes the update to the screen
    gameDisplay.blit(barSurface, (0, 200))
    pygame.display.update(barSurfaceUpdateRect)

#code for selection sort algorithm    
def selectionSort():
    for i in range(arraySize): 

        #find the smallest element in the array from the unsorted elements
        smallestNumIndex = i 
        for j in range(i+1, arraySize): 
            if data[j] < data[smallestNumIndex]: 
                smallestNumIndex = j 
            
        progress[j] = 2
        progress[i] = 2
        drawRect(data, progress)
        pygame.time.delay(int(2500/arraySize))

        # Swap the found minimum element with the element at the beggining  
        data[i], data[smallestNumIndex] = data[smallestNumIndex], data[i]
        progress[j] = 1
        progress[i] = 3 
        drawRect(data, progress)
        pygame.time.delay(int(2500/arraySize))

        #code to allow the user to exit the program midway through sorting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

#code for bubble sort algorithm
def bubbleSort():
    for i in range(arraySize - 1):
        for j in range(0, arraySize - i - 1):
            if data[j] > data[j+1]:
                progress[j] = 2
                progress[j+1] = 2
                drawRect(data, progress)
                
                pygame.time.delay(int(2500/arraySize))

                t = data[j]
                data[j] = data[j+1]
                data[j+1] = t

                progress[j] = 1
                progress[j+1] = 1
                drawRect(data, progress)
                
                pygame.time.delay(int(2500/arraySize))

                #code to allow the user to exit the program midway through sorting
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                
        if arraySize - i >= 0:
            progress[arraySize -1  - i] = 3            
                
        drawRect(data, progress)
    progress[0] = 3

#code for insertion sort algorithm
def insertSort():
    for i in range(1, arraySize): 
        key = data[i] 

        j = i-1
        while j >=0 and key < data[j] : 
            progress[j+1] = 2
            progress[j] = 2
            drawRect(data, progress)
            pygame.time.delay(int(2500/arraySize))

            data[j+1] = data[j] 

            progress[j] = 1
            progress[j+1] = 1
            drawRect(data, progress)
            pygame.time.delay(int(2500/arraySize))

            j -= 1

            data[j+1] = key     
            drawRect(data, progress)
            pygame.time.delay(int(2500/arraySize))

            #code to allow the user to exit the program midway through sorting
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
    
    #colors the bars green after the sorting is complete
    for i in range(arraySize):
        progress[i] = 3
        drawRect(data, progress)
        pygame.time.delay(50)

#initialize the array used for sorting
def arrayInit(size, maxNum):
    newData = []
    for i in range(size):
        value = randint(0, maxNum)
        newData.insert(i, value)
        progress.insert(i, 1)
    #return the new data
    return newData

#method used to create text
def text_objects(text, font, color, text_center):
    rendered = font.render(text, True, color)
    return rendered, rendered.get_rect(center = text_center)

#creates the interactive buttons found at the top of the screen
def create_buttons():
        #steup the text components
        bbSortCenter = ((50 + (100/2)), (100 + (50/2)))
        insertSortCenter = ((200 + (100/2), (100 + (50/2))))
        selectionSortCenter = ((350 + (100/2), (100 + (50/2))))
        randomCenter = ((500 + (100/2), (100 + (50/2))))
        arraySizeCenter = ((650 + 100), 75)

        #static buttons
        pygame.draw.rect(gameDisplay, GREEN, (50, 100, 100, 50))
        pygame.draw.rect(gameDisplay, GREEN, (200, 100, 100, 50))
        pygame.draw.rect(gameDisplay, GREEN, (350, 100, 100, 50))
        pygame.draw.rect(gameDisplay, GREEN, (500, 100, 100, 50))

        #bubble sort button

        #if user is rolling over the button
        if 50 + 100 > mouse[0] > 50 and 100 + 50 > mouse[1] > 50: 
            pygame.draw.rect(gameDisplay, RED, (50, 100, 100, 50))
            textSurf, textRect = text_objects("Bubble Sort", smallText, BLACK, bbSortCenter)
            gameDisplay.blit(textSurf, textRect)
            if click[0] == 1 and not isSorted:
                return 1

        #insert sort button

        #if user is rolling over the button
        if 200 + 100 > mouse[0] > 200 and 100 + 50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, RED, (200, 100, 100, 50))
            textSurf, textRect = text_objects("Insert Sort", smallText, BLACK, insertSortCenter)
            gameDisplay.blit(textSurf, textRect)
            if click[0] == 1 and not isSorted:
                return 2 
        
        #selection sort button

        #if user is rolling over the button
        if 350 + 100 > mouse[0] > 350 and 100 + 50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, RED, (350, 100, 100, 50))
            textSurf, textRect = text_objects("Selection Sort", superSmallText, BLACK, selectionSortCenter)
            gameDisplay.blit(textSurf, textRect)
            if click[0] == 1 and not isSorted:
                return 3 
        
        #randomize button

        #if user is rolling over the button
        if 500 + 100 > mouse[0] > 500 and 100 + 50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, RED, (500, 100, 100, 50))
            textSurf, textRect = text_objects("New Data", smallText, BLACK, randomCenter)
            gameDisplay.blit(textSurf, textRect)
            if click[0] == 1:
                return 4 

        #button text
        textSurf, textRect = text_objects("Bubble Sort", smallText, BLACK, bbSortCenter)
        gameDisplay.blit(textSurf, textRect)
        textSurf, textRect = text_objects("Insert Sort", smallText, BLACK, insertSortCenter)
        gameDisplay.blit(textSurf, textRect)
        textSurf, textRect = text_objects("Selection Sort", superSmallText, BLACK, selectionSortCenter)
        gameDisplay.blit(textSurf, textRect)
        textSurf, textRect = text_objects("New Data", smallText, BLACK, randomCenter)
        gameDisplay.blit(textSurf, textRect)
        textSurf, textRect = text_objects("Set Size", largeText, BLACK, arraySizeCenter)
        gameDisplay.blit(textSurf, textRect)


#initialize arrays
data = arrayInit(arraySize, 20)  

# loop until the user exits the program

while not done:
    # loop for every event that occurs in the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            exit()
    
        # fill display
        gameDisplay.fill(WHITE)

        # event listeners
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        slider.listen(event)
        slider.draw()

        # fonts
        largeText = pygame.font.SysFont('comicsansms', 25)
        smallText = pygame.font.SysFont('comicsansms', 15)
        superSmallText = pygame.font.SysFont('comicsansms', 12)

        # code to draw objects
        flag = create_buttons()
        drawRect(data, progress)

        # program logic

        #updates the array as soon as the value is changed
        newSize = slider.getValue()
        if newSize != arraySize:
            data = fixSize(newSize)
            arraySize = newSize
            isSorted = False
        
        #code to handle button presses
        if flag == 1:
            bubbleSort()
            isSorted = True
        if flag == 2:
            insertSort()
            isSorted = True
        if flag == 3:
            selectionSort()
            isSorted = True
        if flag == 4:
            data = arrayInit(arraySize, 20)
            isSorted = False

        # set the clock speed to 60 times per second 
        clock.tick(60)     

        # update the screen
        pygame.display.flip()

#needed to quit game correctly
pygame.quit()
exit()