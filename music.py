import os
from tkinter import *
from pygame import mixer
from tkinter import filedialog
import fnmatch
import time
from mutagen.mp3 import MP3

root = Tk()
#Musicplayer(root)
  
root.geometry("1000x700+200+200")
root.title("Music Player")
root.resizable(False,False)
icon = PhotoImage(file=r"C:\Users\WK. BRANDON\Desktop\python projects\Music player\play-button-transparent.png")
root.iconphoto(True,icon)


#function to play song
def playsong():
    #displaying selected song title
    #track.set(listbox.get("anchor"))
    song = listbox.get(ACTIVE)
    track.set(song)
    #displaying status
    status.set("Playing")
    #loading selected song
    mixer.music.load(rootpath + '\\' + song) 
    #playing selected song
    mixer.music.play() 
    
    #play_time()

#function to pause the song which is currently playing
def pause():
    #displaying status
    
    #paused song
    if pausebtn["text"] == "Pause":
        status.set("Pause")
        mixer.music.pause()
        pausebtn["text"] = "Resume"
      
        
    else:
        status.set("playing")
        mixer.music.unpause()
        pausebtn["text"] = "Pause"
     
#function to stop the song which is currently playing
def stop():
    #displaying status
    status.set("Stopped")
    #stopped song
    
    mixer.music.stop()
    listbox.select_clear(0,'end')
    
def back():
    status.set("playing")
    mixer.music.rewind()

def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listbox.get(next_song)
    
    track.set(next_song_name)
    
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)
    
    status.set("Playing")
    mixer.music.load(rootpath + '\\' + next_song_name )
    mixer.music.play()   

#displaying status
def previous_song():
    next_song = listbox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listbox.get(next_song)
    
    track.set(next_song_name)
    
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)
    
    #displaying status
    
    status.set("Playing")
    mixer.music.load(rootpath + '\\' + next_song_name )
    mixer.music.play()   
#function to delete a song
def delete_song():
    listbox.delete(ACTIVE)
    mixer.music.stop()

#function to delete many songs
def delete_many_songs():
    listbox.delete(0,END)
    mixer.music.stop()
    

def add_song():
    song  = filedialog.askopenfilename(initialdir="Songs/",title="Choose A Song",filetypes=(("mp3 Files", "*.mp3"),))
    #remove the directory info and .mp3 extension from the song title
    song = song.replace("C:/Users/WK. BRANDON/Desktop/python projects/Music player/Songs/","")
    song = song.replace(".mp3","")
    #add song to listbox
    listbox.insert(1,song)   
    
def add_many_song():
    songs  = filedialog.askopenfilenames(initialdir="Songs/",title="Choose Many Songs",filetypes=(("mp3 Files", "*.mp3"),))
    #loop through list of songs and replacing directory info and mp3 extension
    for song in songs:
        song = song.replace("C:/Users/WK. BRANDON/Desktop/python projects/Music player/Songs/","")
        song = song.replace(".mp3","")
        #insert into song playlist
        listbox.insert(1,song)

#getting the song length info     
def play_time():
    #grab current song elapsed time
    current_time  = mixer.music.get_pos() / 1000
    #convert to time format
    converted_current_time = time.strftime("%M:%S", time.gmtime(current_time))
   
   
    #get current song playing
    current_song = listbox.curselection()
    #get song title from playlist
    
    song = listbox.get(current_song)
    song =  f"C:\\Users\WK. BRANDON\Desktop\python projects\Music player\Songs {song}"
    #load song with mutagen

    song_mut = MP3(song)
    #get song length
    song_length = song_mut.info.length()
    #convert to time format
    converted_song_length = time.strftime("%M:%S", time.gmtime(song_length))
    time_bar.config(text=f'Time Elapsed: {converted_current_time} of  {converted_song_length} ' )
    print(converted_current_time)
#update the song length
    time_bar.after(1000,play_time)
    
#initilizing the mixer module
mixer.init()

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)
#add the add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add song",menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist",command=add_song)
#add many songs to playlist
add_song_menu.add_command(label="Add many songs to playlist",command=add_many_song)

delete_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Delete song",menu=delete_song_menu)
delete_song_menu.add_command(label="Delete one song from playlist",command=delete_song)
#add many songs to playlist
delete_song_menu.add_command(label="Delete many songs from playlist",command=delete_many_songs)

#declaring track variable
track = StringVar()
#declaring status variable
status  = StringVar()
#creating the track frame for song label and status label
trackframe = LabelFrame(root,text="Song Track",font=("times new roman",15,'bold'),bg="navyblue",fg="white",bd=5,relief=GROOVE)
trackframe.place(x=0,y=0,width=600,height=450)

songtrack = Label(trackframe,textvariable=track,width=20,font=("times new roman",20,'bold'),bg="black",fg="cyan")
songtrack.grid(row=0,column=0,padx=10,pady=5)

time_bar = Label(root,text='',bg='cyan',fg='black',width=90,bd=0,anchor=E)
time_bar.pack(ipady=2,fill=X)
time_bar.place(x=5,y=100)

trackstatus = Label(trackframe,textvariable=status,width=10,font=("times new roman",20,'bold'),bg="black",fg="white")
trackstatus.grid(row=0,column=1,padx=10,pady=5)

#Creating button frame
buttonframe = LabelFrame(root,text="Control Panel",font=("times new roman",15,'bold'),bg="black",fg="white",bd=5,relief=GROOVE)
buttonframe.place(x=0,y=450,width=1000,height=250)

#inserting play button
playbtn = Button(buttonframe,text="Play",width=5,height=4,font=("times new roman",12,'bold'),bg="navyblue",fg="white",command=playsong)
playbtn.grid(row=0,column=0)

pausebtn = Button(buttonframe,text="Pause",width=5,height=4,font=("times new roman",12,'bold'),bg="navyblue",fg="white",command=pause)
pausebtn.grid(row=0,column=1)

stopbtn = Button(buttonframe,text="Stop",bg="navyblue",font=("times new roman",12,'bold'),fg="white",width=5,height=4,command=stop)
stopbtn.grid(row=0,column=3)

rewindbtn = Button(buttonframe,text="Restart",bg="navyblue",font=("times new roman",12,'bold'),fg="white",width=5,height=4,command=back)
rewindbtn.grid(row=0,column=4)

nextbtn = Button(buttonframe,text="Next",bg="navyblue",font=("times new roman",12,'bold'),fg="white",width=5,height=4,command=play_next)
nextbtn.grid(row=0,column=5)

previousbtn = Button(buttonframe,text="Previous",bg="navyblue",font=("times new roman",12,'bold'),fg="white",width=5,height=4,command=previous_song)
previousbtn.grid(row=0,column=6)
#creating playlist frame
songsframe = LabelFrame(root,text="Song Playlist",font=("times new roman",20,'bold'),bg="black",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=530,y=0,width=470,height=450)
#inserting scrollbar
scrol_y = Scrollbar(songsframe,orient=VERTICAL)

listbox = Listbox(root,fg='cyan',bg='black',selectmode=SINGLE,width=30,height=20,font=('ariel',20))
#listbox.pack(padx=15,pady=15,expand=True)
listbox.place(x=530,y=30)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=listbox.yview)

rootpath = "C:\\Users\WK. BRANDON\Desktop\python projects\Music player\Songs"
pattern = '*.mp3'
#inserting songs into playlist
for pathroot,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end',filename)
  
root.mainloop()