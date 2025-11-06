import os
import pygame
import time


music_path = "C:/Users/kalab/OneDrive/Рабочий стол/lab7"

SUPPORTED = (".mp3", ".wav", ".ogg")

if os.path.isdir(music_path):
    tracks = []
    for file in os.listdir(music_path):
        if file.lower().endswith(SUPPORTED):
            tracks.append(os.path.join(music_path, file))
else:
    print("Указанный путь не существует!")
    tracks = []

if not tracks:
    print("Нет музыкальных файлов по пути:", music_path)
    exit()

pygame.init()
pygame.mixer.init()


volume = 0.5
pygame.mixer.music.set_volume(volume)


index = 0

def play_track(i):
    global index
    index = i % len(tracks) 
    path = tracks[index]
    print("Сейчас играет:", os.path.basename(path))
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

play_track(index)

print("Команды: n - следующий | b - предыдущий | + - громче | - - тише | q - выход")

while True:
    cmd = input(">>> ").strip().lower()
    if cmd == "n":
        play_track(index + 1)
    elif cmd == "b":
        play_track(index - 1)
    elif cmd == "+":
        volume = min(1.0, volume + 0.1)
        pygame.mixer.music.set_volume(volume)
        print("Громкость:", int(volume * 100), "%")
    elif cmd == "-":
        volume = max(0.0, volume - 0.1)
        pygame.mixer.music.set_volume(volume)
        print("Громкость:", int(volume * 100), "%")
    elif cmd == "q":
        print("Выход...")
        break
    else:
        print("Неизвестная команда!")

pygame.mixer.music.stop()
pygame.quit()
