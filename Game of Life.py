# game of life SYNC
# region Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import random
import sys
# endregion
#region initial variables
fps=15
shape_x=64
shape_y=32
ani=None
im=None
right_to_plot=1
ones=25
random_min=0
random_max=100
game_array=[]
T=1000/fps
size=shape_x*shape_y
#endregion
# region colors
# default
light_gray_color = "#333333"  # 333333
dark_gray_color = "#1e1e1e"  # 1e1e1e
white_color = "#f1f1f1"  # f1f1f1
accent_color = "#007acc"  # 007acc
connect_color = "#eaa100"  # eaa100
start_color = "#ff830f"  # ff830f
selected_color = "#252526"  # 252526
#endregion
# region Root declaration and config
def shut_down():
    sys.exit()  
root = Tk()
root.title("Game of Life")  # assign a title to the window
root.configure(background="#000000")
root.config(highlightbackground=dark_gray_color)
fontStyle = tkFont.Font(family="sans-serif", size=16)
root.protocol('WM_DELETE_WINDOW', shut_down)
if("win" in sys.platform):
    root.state('zoomed')
else:
    root.attributes('-zoomed', True)
# endregion
#region frames
ploting_frame = LabelFrame(root, padx=0, pady=0, bd=0)
ploting_frame.configure(background=dark_gray_color, fg='#f1f1f1',
                        highlightbackground=dark_gray_color, highlightcolor=dark_gray_color)
ploting_frame.grid(row=0, column=0, sticky=N+E+W+S)

configuration_frame = LabelFrame(root, padx=0, pady=0, bd=1)
configuration_frame.configure(background=dark_gray_color, fg='#f1f1f1',
                              highlightbackground=dark_gray_color, highlightcolor=dark_gray_color)
configuration_frame.grid(row=1, column=0, sticky=N+E+W+S)
#endregion
# region plotting canvas INIT
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
ratio=w/h
default_size=h/108
fig = plt.figure(figsize=(ratio*default_size, default_size), facecolor='#000000')
fig.suptitle('Game of Life',  fontsize=16, family="sans-serif",
             color='#f1f1f1', fontweight="bold")
canvas = FigureCanvasTkAgg(fig, master=ploting_frame)
canvas._tkcanvas.pack(side="top", fill="both", expand=1)
# endregion
# region Size Text And Entry
size_y_text = Label(configuration_frame, text="size : ", bg=dark_gray_color, fg=white_color,
                  justify='center').grid(row=0, column=2, sticky=W)  # put text on the window
size_y_entry = Entry(configuration_frame, bg=light_gray_color, width=7, fg=accent_color,
                   justify='center', highlightbackground="#2d2d30", highlightcolor=selected_color, bd=0)
size_y_entry.grid(row=0, column=3, sticky=W+E)
size_y_entry.insert('end', shape_y)
# endregion
# region ones Text And Entry
ones_text = Label(configuration_frame, text="ones %: ", bg=dark_gray_color, fg=white_color,
                       justify='center').grid(row=0, column=6, sticky=W)  # put text on the window
ones_entry = Entry(configuration_frame, bg=light_gray_color, width=7, fg=accent_color,
                        justify='center', highlightbackground="#2d2d30", highlightcolor=selected_color, bd=0)
ones_entry.grid(row=0, column=7, sticky=W+E)
ones_entry.insert('end', ones)

filler1=Label(configuration_frame, text="____", bg=dark_gray_color, fg=dark_gray_color,
                       justify='center').grid(row=0, column=8, sticky=W+E)  # put text on the window
filler2=Label(configuration_frame, text="_", bg=dark_gray_color, fg=dark_gray_color,
                       justify='center').grid(row=0, column=10, sticky=W+E)  # put text on the window
credits_text = Label(configuration_frame, text="credits to Adrianos SIDIRAS GALANTE ", bg=dark_gray_color, fg=accent_color,
                       justify='right').grid(row=0, column=15, sticky=E)  # put text on the window
#endregion
# region pause
def pause():
    global right_to_plot
    right_to_plot = not right_to_plot
    if (right_to_plot != 0):
        pause_button.configure(bg=light_gray_color)
        size_y_entry.configure(state='disabled')
        ones_entry.configure(state='disabled')
    else:
        pause_button.configure(bg="#222222")
        pause_button.configure(bg=light_gray_color)
        size_y_entry.configure(state='normal')
        ones_entry.configure(state='normal')


pause_button = Button(configuration_frame, width=8, text="Pause", padx=0, pady=0, fg=white_color, bg=light_gray_color,
                      bd=1, highlightbackground=dark_gray_color, highlightcolor=selected_color, command=pause)
pause_button.grid(row=0, column=9, sticky=W+N+E)
# endregion
# region Relaude
def reload():
    global ones, random_min, random_max, shape_x, shape_y, game_array, year, alive, dead, spread, size
    
    
    shape_y=int(size_y_entry.get())
    shape_x=shape_y*2
    size=shape_y*shape_x
    game_array=generate_random(int(ones_entry.get()), random_min, random_max, shape_x, shape_y, game_array)
    year=0
    alive=0
    dead=0
    spread=0
    
reload_button = Button(configuration_frame, width=8, text="reload", padx=0, pady=0, fg=white_color, bg=light_gray_color,
                      bd=1, highlightbackground=dark_gray_color, highlightcolor=selected_color, command=reload)
reload_button.grid(row=0, column=11, sticky=W+N+E)
# endregion
#region RANDOM generation
def generate_random(ones, random_min, random_max, shape_x, shape_y, game_array):
    lenght=shape_x*shape_y
    threshold=random_max-ones
    random_array=[]
    rand_one=0
    rand_zero=0
    for cell in range(0, lenght):
        random_number=random.randint(random_min,random_max)
        if random_number>(threshold):
            random_array.append(random.randint(1,10))
            rand_one+=1
        else:
            random_array.append(0)
            rand_zero+=1
    game_array=np.reshape(random_array,(shape_y, shape_x))
    return game_array
game_array=generate_random(ones, random_min, random_max, shape_x, shape_y, game_array)
#endregion
#region Rules
def simulate_state(shape_x, shape_y):
    global game_array
    futur_game_array= np.empty(shape=(shape_y, shape_x))
    for x in range (0, shape_x):
        for y in range (0,shape_y):
            neighbours_offset=[-1,0,1]
            neighbours=[]
            live_neighbours=0
            dead_neighbours=0
            cell=game_array[y][x]
            for offset_x in neighbours_offset:
                neighbour_x=x+offset_x
                if neighbour_x<0:
                    neighbour_x=shape_x-1
                elif neighbour_x>(shape_x-1):
                    neighbour_x=0
                for offset_y in neighbours_offset:
                    neighbour_y=y+offset_y
                    if neighbour_y<0:
                        neighbour_y=shape_y-1
                    elif neighbour_y>(shape_y-1):
                        neighbour_y=0
                    if ((offset_x!=0)or(offset_y!=0)):
                        neighbours.append(game_array[neighbour_y][neighbour_x])
            for neighbour in neighbours:
                if neighbour:
                    live_neighbours+=1
                else:
                    dead_neighbours+=1
            if (cell) and (live_neighbours>1) and (live_neighbours<4):
                pass
            elif (not(cell)) and (live_neighbours==3):
                cell=random.randint(1,10)
            else:
                cell=0
            futur_game_array[y][x]=cell
    return futur_game_array  
#endregion
#region PLotting
year=0
alive=0
dead=0
spread=0
threads=[]
def population(game_array, size):
    global alive, dead, spread
    dead=np.count_nonzero(game_array==0)
    alive=size-dead
    spread=(alive/(dead+alive))*100


stat_text=Label(configuration_frame, text="",width=150, bg=dark_gray_color, fg='#ffab40',justify='left') # put text on the window
stat_text.grid(row=0, column=12, sticky=W) 
#endregion
#region animate
def animate(i):
    global game_array, next_game_array, T, right_to_plot, year, size, shape_x, shape_y, frames
    
    if right_to_plot: 
        futur_game_array=simulate_state(shape_x, shape_y)
        game_array=futur_game_array
        text="Alive : {}   Dead : {}   Spread : {:.2f}%   Hours : {}".format(alive, dead, spread, year)
        stat_text.configure(text=text)
        year=year+1
    population(game_array, size)
    im.set_data(game_array)
    
    #print(end-start)
    
#endregion
#region start
fig.tight_layout(pad=3)
fig.set_tight_layout(True)
right_to_plot=0
ax = fig.add_subplot(111)
ax.tick_params(axis='x', colors='#000000')
ax.tick_params(axis='y', colors='#000000')
ax.spines['bottom'].set_color('#000000')
ax.spines['top'].set_color('#000000')
ax.spines['right'].set_color('#000000')
ax.spines['left'].set_color('#000000')
im= plt.imshow(game_array, cmap='inferno', interpolation='none')
ani= animation.FuncAnimation(plt.gcf(), animate, interval=T)
size_y_entry.configure(state='disabled')
ones_entry.configure(state='disabled')
right_to_plot=1
root.mainloop()
#"viridis", "inferno", "hot", "cool", "coolwarm", "tab20", "jet"
#endregion


