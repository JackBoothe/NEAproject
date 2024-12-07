import pygame as pg

#IMPORTANT: THE MAJORITY OF THE CODE FOR THIS DYNAMIC BUTTON WAS COPIED - SEE BIBLIOGRAPHY FOR REFERENCE 
#although some of it has still been altered which is explained in development section 

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):

		#initialising button attributes 
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.selected = False 
		self.selectedIMG = pg.image.load("textures/assets/Selected Rect.png")
		

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)

		#if selected then, blit the highlighted box 
		if self.selected == True: 
			screen.blit(self.selectedIMG, (self.x_pos-67, self.y_pos+27))

		screen.blit(self.text, self.text_rect)
	
	#checking if mouse position overlaps with box of button 
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.selected = not self.selected 
			
			return True
		return False
	
	#when actively hovering over, change the colour of the box.
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and self.selected == False:
			self.text = self.font.render(self.text_input, True, self.hovering_color)

		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
            