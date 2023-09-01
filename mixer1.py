from pygame import mixer
import playsound
# Starting the mixer
song="C:\\Users\\Fuso\\Music\\khachar_pakhi__খাচঁার_পাখি__bangla_lyrics_song__samz_vai_song_2019_#iccha_diary(256k).mp3"
mixer.init()
  
# Loading the song
mixer.music.load(song)
  
# Setting the volume
mixer.music.set_volume(0.7)
  
# Start playing the song
mixer.music.play()
  
# infinite loop
while True:
      
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
  
        # Pausing the music
        mixer.music.pause()     
    elif query == 'r':
  
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
  
        # Stop the mixer
        mixer.music.stop()
        break