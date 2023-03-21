from leb import *

class App():
    def Buttons(self):
        def Open():
            global file
            file = filedialog.askopenfilename(filetypes =[('PNG IMAGES','*.png'),('JPG IMAGES', '*.jpg'),('BMP IMAGE','*.bmp')])
        def convert():
            new_name = filedialog.asksaveasfilename()
            ext = '.png'
            if to_ == 'JPG':
                ext = '.jpg'
            elif to_ == 'ICON':
                ext ='.ico'
            elif to_ == 'PNG':
                ext = '.png'
            elif to_ == 'ASCII':
                ext = '.txt'
                img = PIL.Image.open(file)
                width, height = img.size
                aspect_ratio = height/width
                new_width = 80
                new_height = aspect_ratio * new_width * 0.55
                img = img.resize((new_width, int(new_height)))
                img = img.convert('L')
                chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
                pixels = img.getdata()
                new_pixels = [chars[pixel//25] for pixel in pixels]
                new_pixels = ''.join(new_pixels)
                
                # split string of chars into multiple strings of length equal to new width and create a list
                new_pixels_count = len(new_pixels)
                ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
                ascii_image = "\n".join(ascii_image)
                
                # write to a text file.
                with open(new_name+ext,'w') as f:
                    f.write(ascii_image)
                messagebox.showinfo('Done','The image extension has been saved and changed. You will find it with the name and path that you chose')
            if ext != '.txt':
                if '.jpg' in file and ext == '.ico':
                    messagebox.showerror('Error','sorry you can\'t convert jpg to icon try png to icon')
                else:
                    image = PIL.Image.open(file)
                    if ext == '.jpg':
                        rgb = image.convert('RGB')
                        rgb.save(new_name+ext)
                    else:
                        image.save(new_name+ext)
                    messagebox.showinfo('Done','The image extension has been saved and changed. You will find it with the name and path that you chose')
        Main_menu = Frame(self.window,bg='#262626')
        def open_main_menu():
            i = -150
            Main_menu_button_open.place_configure(x=-50,y=-50)
            while True:
                self.window.update()
                Main_menu.place(x=i,y=0,width=150,height=300)
                self.window.update()
                i+=1
                if i == 0:
                    break
                else:
                    continue
        def close_main_menu():
            i = 0
            while True:
                self.window.update()
                Main_menu.place(x=i,y=0,width=150,height=300)
                self.window.update()
                i-=1
                if i == -150:
                    Main_menu_button_open.place_configure(x=10,y=3)
                    break
                else:
                    continue
        def social():
            open_new_tab('https://www.facebook.com/toxiccode12')
            open_new_tab('https://www.youtube.com/@Toxic_Code')
            open_new_tab('https://t.me/toxiccode12')
            open_new_tab('https://toxiccode12.blogspot.com')
        def apout_us():
            messagebox.showinfo('who am I','Freelance programmer, I work on my own, born in 2004, I am now 19, from Iraq. I have a YouTube channel and several Telegram channels, and I have a blog.')
        def mode_light():
            set_appearance_mode('light')
            mode.configure(text='Dark Mode',command=mode_dark)
            self.window.update()
        def mode_dark():
            set_appearance_mode('dark')
            mode.configure(text='Light Mode',command=mode_light)
            self.window.update()
        def E():
            exit()
        Select = CTkButton(self.window,text='Select File',command=Open)
        Convert = CTkButton(self.window,text='Convert To',command=convert)
        Main_menu_image = PhotoImage(file='src/main-menu.png').subsample(15,15)
        Main_menu_button_open = CTkButton(self.window,image=Main_menu_image,text='',width=10,command=open_main_menu)
        Main_menu_image = PhotoImage(file='src/close.png').subsample(20,20)
        Main_menu_button_close = CTkButton(master=Main_menu,image=Main_menu_image,text='',width=10,command=close_main_menu)
        apout = CTkButton(master=Main_menu,text='Apout Us',command=apout_us)
        myaccounts = CTkButton(master=Main_menu,text='social media sites',command=social)
        mode = CTkButton(master=Main_menu,text='Dark Mode',command=mode_dark)
        Exit = CTkButton(master=Main_menu,text='Exit',command=E)
        Select.place(x=160,y=180)
        Convert.place(x=320,y=180)
        Main_menu_button_open.place(x=10,y=3)
        Main_menu_button_close.place(x=100,y=10)
        apout.place(x=6,y=60)
        myaccounts.place(x=6,y=120)
        mode.place(x=6,y=180)
        Exit.place(x=6,y=240)
    def cyperight(self):
        cr = CTkLabel(master=self.window,text='Cyperight By Toxic Code')
        cr.pack(side=BOTTOM)
    def Com(self):
        global to_
        to_ = 'PNG'
        def cho(e):
            global to_
            to_ = e
        exta = CTkComboBox(master=self.window,values=['PNG','JPG','ASCII','ICON'],state='readonly',command=cho)
        exta.set('PNG')
        exta.place(x=480,y=180)
    def __init__(self,window=CTk):
        super().__init__()
        self.window = window
        set_appearance_mode('light')
        set_default_color_theme('dark-blue')
        self.window.title('Convert To')
        self.window.resizable(0,0)
        ICON = PhotoImage(file='src/image-files.png')
        ICON = ICON.subsample(4,4)
        self.window.iconbitmap('src/Icon.ico')
        Logo = CTkLabel(master=self.window,image=ICON,text='')
        Logo.pack(pady=20)
        self.window.geometry('750x300')

if __name__ == "__main__":
    app = CTk()
    gui = App(window=app)
    gui.Buttons()
    gui.Com()
    gui.cyperight()
    app.mainloop()