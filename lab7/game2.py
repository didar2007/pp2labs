import os
import sys
import pygame


music_path = "C:/Users/kalab/OneDrive/Рабочий стол/lab7"  
SUPPORTED = (".mp3", ".wav", ".ogg")

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

def gather_tracks(path):
    """Если path — файл, вернём [path]; если папка — все поддерж. файлы внутри; иначе []"""
    if os.path.isfile(path):
        if path.lower().endswith(SUPPORTED):
            return [path]
        return []
    if os.path.isdir(path):
        files = []
        for name in sorted(os.listdir(path)):
            if name.lower().endswith(SUPPORTED):
                files.append(os.path.join(path, name))
        return files
    return []

tracks = gather_tracks(music_path)
if not tracks:
    print("Нет музыкальных файлов по пути:", music_path)
    print("Положи .mp3/.wav/.ogg файл(ы) в папку или укажи путь к файлу в переменной music_path.")
    sys.exit(1)


pygame.init()
try:
    pygame.mixer.init()
except Exception as e:
    print("Ошибка инициализации звука:", e)
    sys.exit(1)

index = 0
status = "Stopped"  
volume = 0.8
pygame.mixer.music.set_volume(volume)


MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

def safe_print_track():
    name = os.path.basename(tracks[index])
    print(f"Playing: {name}  | status: {status} | vol:{int(volume*100)}%")

def load_and_play(i):
    global status, index
    index = i % len(tracks)
    path = tracks[index]
    try:
        pygame.mixer.music.load(path)
    except Exception as e:
        print("Не удалось загрузить:", path, " — пропускаем. Ошибка:", e)
        return False
    try:
        pygame.mixer.music.play()
        status = "Playing"
        safe_print_track()
        return True
    except Exception as e:
        print("Ошибка при воспроизведении:", e)
        return False

def play_pause_toggle():
    global status
    if status == "Stopped":
        load_and_play(index)
    elif status == "Playing":
        pygame.mixer.music.pause()
        status = "Paused"
        print("Paused")
    elif status == "Paused":
        pygame.mixer.music.unpause()
        status = "Playing"
        print("Resumed")

def stop():
    global status
    pygame.mixer.music.stop()
    status = "Stopped"
    print("Stopped")

def next_track():
    load_and_play(index + 1)

def prev_track():
    load_and_play(index - 1)

def change_volume(delta):
    global volume
    volume = max(0.0, min(1.0, volume + delta))
    pygame.mixer.music.set_volume(volume)
    print(f"Volume: {int(volume*100)}%")


load_and_play(index)


print("Controls: p - play/pause | s - stop | n - next | b - prev | + - vol up | - - vol down | q - quit")
try:
    while True:
        
        for ev in pygame.event.get():
            if ev.type == MUSIC_END:
                next_track()

        cmd = input(">>> ").strip().lower()
        if cmd == "p":
            play_pause_toggle()
        elif cmd == "s":
            stop()
        elif cmd == "n":
            next_track()
        elif cmd == "b":
            prev_track()
        elif cmd == "+":
            change_volume(0.05)
        elif cmd == "-":
            change_volume(-0.05)
        elif cmd == "q":
            stop()
            break
        elif cmd == "":
            
            continue
        else:
            print("Unknown command")
finally:
    pygame.mixer.music.stop()
    pygame.quit()
