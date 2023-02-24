from tkinter import *
from os import system as cmd
import time as t
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

packed = True
first = True
root = Tk()
version = "1.10"
root.title(" ")
frame = Frame(root)
frame.pack()
icon = PhotoImage(file = r"./logo.png") #IMPORTANT, CHANGE THIS TO IMAGE LOCATION
main = Label(frame, image = icon, height = "200")
title = Label(frame, text = "RaspiPanel", font =(
  "URW Gothic", 45))
times = Label(frame, text = str(t.asctime(t.localtime())), font =("Quicksand", 10))
v3_3 = "1 17".split(" ")
v5 = "2 4".split(" ")
GND = "6 9 14 20 25 30 34 39".split(" ")
DNC = "27 28".split(" ")
SERIAL = "8 10".split(" ")
DATA = "3"
CLOCK = "5"
SPI = "19 21 23 24 26".split(" ")
gpio_trans = {7:4,
              11:17,
              12:18,
              13:27,
              15:22,
              16:23,
              18:24,
              22:25,
              29:5,
              31:6,
              32:12,
              33:13,
              35:19,
              36:16,
              37:26,
              38:20,
              40:21}

def base():
    global manual_gpio
    global Version
    global InitialTitle
    global InitialLogo
    global times
    global title
    global gpio
    global tools
    global media
    global first
    global main
    global packed
    global extr1
    global extr2

    def manual_gpio():
        global gpio_trans
        for number in gpio_trans:
            GPIO.setup(number, GPIO.OUT)
            GPIO.output(number, 0)

    def logo_clean():
        global packed
        global Version
        global times
        global title
        global main
        global gpio
        global media
        global tools
        global first
        global InitialTitle
        global InitialLogo
        Version.destroy()
        InitialTitle.destroy()
        InitialLogo.destroy()
        main.pack(side = TOP, pady = 10)
        title.pack(side = TOP)
        times.pack(side = TOP)
        gpio.pack(side = RIGHT, fill = BOTH, padx = 2, pady = 2)
        tools.pack(side = BOTTOM, fill = BOTH, padx = 2, pady = 2)
        media.pack(side = TOP, fill = BOTH, padx = 2, pady = 2)
        first = False

    def off(port):
        global media
        GPIO.output(int(port), 0)
        media.configure(background = "grey", command = lambda: on(port))
        
    def on(port):
        global media
        GPIO.output(int(port), 1)
        media.configure(background = "#bc1142", command = lambda: off(port))
    
    def boxcmd():
        global media
        port = (extr1.get())
        if port in v3_3:
            media.configure(text = "3V", state = DISABLED, disabledforeground = "orange", background = "grey")
        elif port in v5:
            media.configure(text = "5V", state = DISABLED, disabledforeground = "red", background = "grey")
        elif port in GND:
            media.configure(text = "Ground", state = DISABLED, disabledforeground = "black", background = "grey")
        elif port in DNC:
            media.configure(text = "DNC", state = DISABLED, disabledforeground = "white", background = "grey")
        elif port in SERIAL:
            media.configure(text = "Serial", state = DISABLED, disabledforeground = "white", background = "grey")
        elif port in DATA:
            media.configure(text = "Data", state = DISABLED, disabledforeground = "blue", background = "grey")
        elif port in CLOCK:
            media.configure(text = "Clock", state = DISABLED, disabledforeground = "blue", background = "grey")
        elif port in SPI:
            media.configure(text = "SPI", state = DISABLED, disabledforeground = "white", background = "grey")
        else:
            GPIO.setup(int(port), GPIO.OUT)
            media.configure(text = f"GPIO {gpio_trans[int(port)]}",state = NORMAL, foreground = "green")
            if GPIO.input((int(port))) == 0:
                media.configure(background = "dark grey", command = lambda: on(port))
            else:
                media.configure(background = "#bc1142", command = lambda: off(port))
            
    
    def time_update():
        global times
        times.configure(text = str(t.asctime(t.localtime())))
    
    def gpio_back():
        global extr1
        extr1.pack_forget()
        base()
    
    def BackButton():
        global gpio
        gpio.configure(text = "    Back    ", command = base,activebackground = "black",activeforeground = "#bc1142",background = "#75a928")
    
    def toolcmd():
        global tools
        global media
        time_update()
        BackButton()
        tools.configure(text = "Shutdown", command = lambda: cmd("sudo shutdown now"))
        media.configure(text = "Restart", command = lambda: cmd("sudo reboot"))
        
    def gpiocmd():
        global packed
        global gpio
        global tools
        global media
        global extr1
        packed = False
        time_update()
        tools.pack_forget()
        media.configure(text = "Updating...", state = DISABLED)
        gpio.configure(text = "    Back    ", command = gpio_back,activebackground = "black",activeforeground = "#bc1142",background = "#75a928")
        extr1.pack(side = BOTTOM, fill = BOTH, padx = 2, pady = 2)
        
    def mediacmd():
        manual_gpio()
        exit()
    
    if packed == False:
        title.pack_forget()
        times.pack_forget()
        gpio.pack_forget()
        tools.pack_forget()
        media.pack_forget()
        main.pack(side = TOP)
        title.pack(side = TOP)
        times.pack(side = TOP)
        gpio.pack(side = RIGHT, fill = BOTH, padx = 2, pady = 2)
        tools.pack(side = BOTTOM, fill = BOTH, padx = 2, pady = 2)
        media.pack(side = TOP, fill = BOTH, padx = 2, pady = 2)
        packed = True
    if first == True:
        
        gpio = Button(frame, text = "GPIO PINS", command = gpiocmd, height = 2,activebackground = "black",activeforeground = "#bc1142", background = "#75a928",foreground = "white", disabledforeground = "white")
        
        tools = Button(frame, text = "Tools", command = toolcmd, activebackground = "black",activeforeground = "#bc1142",background = "#bc1142",foreground = "white", disabledforeground = "white")

        media = Button(frame, text = "Exit", command = mediacmd, activebackground = "black",activeforeground = "#bc1142",background = "#bc1142",foreground = "white", disabledforeground = "white")
        
        extr1 = Spinbox(frame, from_ = 1, to = 40, command = boxcmd, background = "#bc1142",foreground = "white", justify = CENTER, width = 2, wrap = True, buttonbackground = "#75a928")

        InitialLogo = Label(frame, text = "\nTitanc3", font = (
        "URW Gothic", 80))
        InitialLogo.pack(side = TOP)
        Version = Label(frame, text = "Version "+version, font = ("Quicksand", 20))
        Version.pack(side = BOTTOM)
        InitialTitle = Label(frame, text = "<Studios>", font = ("Quicksand", 45))
        InitialTitle.pack(side = BOTTOM)
        
        frame.after(4000, logo_clean)
        
    
    else:
        gpio.configure(text = "GPIO PINS", state = NORMAL, command = gpiocmd, height = 2,activebackground = "black",activeforeground = "#bc1142", background = "#75a928",foreground = "white", disabledforeground = "white")
        tools.configure(text = "Tools", state = NORMAL, command = toolcmd, activebackground = "black",activeforeground = "#bc1142",background = "#bc1142",foreground = "white", disabledforeground = "white")
        media.configure(text = "Exit", state = NORMAL, command = mediacmd, activebackground = "black",activeforeground = "#bc1142",background = "#bc1142",foreground = "white", disabledforeground = "white")
try:
    base()
except KeyboardInterrupt:
    print("Program Interrupted, ending...")
    manual_gpio()
except:
    print("Error, Review Code")
