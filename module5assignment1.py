# Imports #

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Music Player Set-Up Code #

# I changed/tweaked a bit of the GUI by renaming the application as 'Music Player', increasing the height of the GUI
# window to reflect a more square interface between the controls and playlist information, and lastly changed both of
# the font and background color from yellow to white of the playlist for a more clean GUI output.

music_player = tkr.Tk()
# Beginning code to construct GUI for music player. #
music_player.title("Music Player")
# Displays title of application in GUI. #
music_player.geometry("350x450")
# Based dimensions of the GUI window. #
directory = askdirectory()
os.chdir(directory)
# Allows the search and selection for a music folder directory within the OS. #
song_list = os.listdir()
play_list = tkr.Listbox(music_player, font="Arial 12 bold", bg='white', selectmode=tkr.SINGLE)
# Pulls song information from selected directory and displays it as a list under player controls. #
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()
# For loop allows for continuous playback of music if there are multiple files in directory. #

# Defining Variables #

# I changed the unpause function to reflect the a 'RESUME' button as I feel that is more transparent than 'UNPAUSE'.
# No further changes were necessary to this section as these codes pertain to the overall functionality of the music
# player.

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
# Defining function to allow for music playback via a play command in the music player. #
def pause():
    pygame.mixer.music.pause()
# Defining function to allow for pausing music playback via a pause command in the music player. #
def resume():
    pygame.mixer.music.unpause()
# Defining function to allow for un-pausing music playback via an unpause command in the music player. #
def stop():
    pygame.mixer.music.stop()
# Defining function to allow for stopping/resetting music playback via a stop command in the music player. #

# Buttons For GUI #

# I changed all the buttons to have an Arial font and resized all button widths to 3 and all heights to 2. For the
# 'PLAY' button I changed the background from blue to green for more GUI transparency and ease of use under color
# association. For the 'PAUSE' button I changed the background from purple to orange for more GUI transparency and
# ease of use under color association. For the 'RESUME' button I changed the background from orange to blue for more
# GUI transparency and ease of use under color association, but I also changed the 'UNPAUSE' to 'RESUME' in both the
# text and command to reflect def function as well as having an easier user interface. Lastly, I moved the 'PAUSE' and
# 'RESUME' buttons from 3 & 4 to 2 & 3 while making the 'STOP' button from 2 to 4. This was done to make an
# easier/cleaner GUI.

Button1 = tkr.Button(music_player,width=3,height=2,font="Arial 12 bold",text="PLAY",command=play,bg="green",fg="white")
# Creates the GUI for the PLAY button such as text, background, foreground, and other custom visual output settings. #
Button2 = tkr.Button(music_player,width=3,height=2,font="Arial 12 bold",text="PAUSE",command=pause,bg="orange",fg="white")
# Creates the GUI for the PAUSE button such as text, background, foreground, and other custom visual output settings. #
Button3 = tkr.Button(music_player,width=3,height=2,font="Arial 12 bold",text="RESUME",command=resume,bg="blue",fg="white")
# Creates the GUI for the RESUME button such as text, background, foreground, and other custom visual output settings. #
Button4 = tkr.Button(music_player,width=3,height=2,font="Arial 12 bold",text="STOP",command=stop,bg="red",fg="white")
# Creates the GUI for the STOP button such as text, background, foreground, and other custom visual output settings. #
var = tkr.StringVar()
# Considers var as string values. #
song_title = tkr.Label(music_player, font="Arial 12 bold", textvariable=var)
# Creates the GUI for the current playing song such as text and other custom visual output settings #

# Packing Into The GUI #

# No changes were necessary to this section as these codes pertain to the overall functionality of the music player.

song_title.pack()
# Packs the currently playing song title and displays it in the GUI as text. #
Button1.pack(fill="x")
# Packs any executables and displays Button1, the 'PLAY' button, within the GUI. #
Button2.pack(fill="x")
# Packs any executables and displays Button2, the 'PAUSE' button, within the GUI. #
Button3.pack(fill="x")
# Packs any executables and displays Button3, the 'RESUME' button, within the GUI. #
Button4.pack(fill="x")
# Packs any executables and displays Button4, the 'STOP' button, within the GUI. #
play_list.pack(fill="both", expand="yes")
# Allows for GUI window resizing and expanding of contents within the GUI. #
music_player.mainloop()
# Loops the music player GUI to enable it as a continuous application. #

# Link to original code used #

# https://thecleverprogrammer.com/2020/12/27/music-player-gui-with-python/ #