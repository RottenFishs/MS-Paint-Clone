import pygame
import os
import glob

class shortcut:
    def __init__(self,screen) -> None:
        self.counter = 0
        self.size = 1

        self.check = False
        blank_file = "canvas_stack/temp_image{}.png".format(0)
        pygame.image.save(screen,blank_file)

        pass

    def check_if_viable(self,current_tool):
        viable_tools = ["pencil","brush", "eraser", "fill"]
        if current_tool in viable_tools and pygame.mouse.get_pos()[1] > 50:
            self.check = True
        else:
            self.check = False

    
    def save(self,screen):
        if self.check == True:
            self.counter += 1 
            image_file = "canvas_stack/temp_image{}.png".format(self.counter)
            for i in range(self.counter+1,self.size):
                delete_file = "canvas_stack/temp_image{}.png".format(i)
                if os.path.exists(delete_file):
                    os.remove(delete_file)

            self.size = self.counter+1
            pygame.image.save(screen,image_file)
    
    def undo(self,canvas_obj):
        if self.counter > 0:
            self.counter -= 1
            image_file = "canvas_stack/temp_image{}.png".format(self.counter)
            undo_image = pygame.image.load(image_file)
            canvas_obj.surface.blit(undo_image,(0,0))
            pygame.display.flip()

    def redo(self,canvas_obj):
        if self.counter < self.size-1:
            self.counter +=1
            image_file = "canvas_stack/temp_image{}.png".format(self.counter)
            undo_image = pygame.image.load(image_file)
            canvas_obj.surface.blit(undo_image,(0,0))
            pygame.display.flip()

    def clearTemp(self):
        temp = glob.glob("canvas_stack/temp_image*.png")
        for file in temp:
            os.remove(file)