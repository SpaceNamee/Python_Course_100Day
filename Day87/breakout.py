import tkinter as tk
import random
import colors as clr

class Breakout:
    def __init__(self):
        self.change_direstion = None
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.resizable(False, False)

        blocks_frame = tk.Frame(self.root)
        blocks_frame.place(x=0, y=0, width=800)

        self.blocks=[]

        pad_y = 5
        for i in range(5):
            pad_x = random.randint(10,50)

            end_line = False
            while not end_line:
                block=tk.Label( bg=clr.COLORS[random.randint(0, len(clr.COLORS)-1)], relief='raised' )
                new_width = random.randint(30,70)

                if pad_x+new_width > 790:
                    end_line=True
                    break

                block.place(x=pad_x, y=pad_y,width=new_width, height=15)
                self.blocks.append(block)
                pad_x += int(block.place_info()['width'])           
                    
            pad_y += int(self.blocks[i].place_info()['height'])

        self.player = tk.Label(self.root, height=1, bg='red', relief='raised')
        self.player.place(x=350, y=760, width=100)

        self.root.bind("<Motion>", self.motion)
        
        self.photo = tk.PhotoImage(file="Bullet.png")
        self.label_photo = tk.Label(self.root, image=self.photo, )
        self.label_photo.place(x=350, y = 734)

        self.bullet(0, 5)

        self.root.mainloop()

    def direction_bullet(self):

        for block in self.blocks:

            block_width = int(block.place_info()['width'])
            block_height = int(block.place_info()['height'])
            block_y_top = int(block.place_info()['y'])
            
            block_y_bottom = block_y_top + block_height
            block_x_start = int(block.place_info()['x'])
            block_x_end = block_x_start + block_width

            bullet_x = int(self.label_photo.place_info()["x"])

            bullet_x_start = bullet_x
            bullet_x_center = bullet_x_start + (int(self.label_photo.place_info()['width'])/2)
            
            bullet_y = int(self.label_photo.place_info()['y'])

            if block_x_start <= bullet_x_center and block_x_end >= bullet_x_center and bullet_y <= block_y_bottom and bullet_y >= block_y_top:
                print("I am here")
                self.label_photo.after_cancel(self.change_direction)
                self.bullet(0, -5)



    def bullet(self, x_direction, y_direction):
        place_inf = self.label_photo.place_info()
        print(place_inf['y'])
        self.label_photo.place_configure(x=int(place_inf["x"])+x_direction, y=int(place_inf["y"])-y_direction)
        self.change_direction = self.label_photo.after(20,  self.bullet, x_direction, y_direction)
        self.direction_bullet()

    def motion(self, event):
        x, y = event.x, event.y
        self.player.place_configure(x=x)

        
