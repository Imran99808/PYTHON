from pygame import mixer
pat=("C:\\Users\\Fuso\\Music\\pani.wav")
mixer.init()
mixer.music.load(pat)
mixer.music.play()
while 1:
    n=input("=")
    if n=="s":
        mixer.music.stop()
i=input("ssssssss")    