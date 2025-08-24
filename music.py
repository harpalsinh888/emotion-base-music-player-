import tkinter as tk
from tkinter import messagebox
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Songs folders (create these folders and put songs inside)
MUSIC_DIR = {
    "happy": "songs/happy",
    "sad": "songs/sad",
    "angry": "songs/angry",
    "surprise": "songs/surprise",
    "neutral": "songs/neutral"
}

current_song = None

def play_song(song_path):
    """Play the selected song"""
    global current_song
    if os.path.exists(song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        current_song = song_path
        messagebox.showinfo("Now Playing", f"🎵 {os.path.basename(song_path)}")
    else:
        messagebox.showerror("Error", "Song file not found!")

def show_songs(emotion):
    """Show song list for a particular emotion"""
    folder = MUSIC_DIR.get(emotion)
    if not folder or not os.path.exists(folder):
        messagebox.showerror("Error", f"No folder found for {emotion}")
        return
    
    songs = os.listdir(folder)
    if not songs:
        messagebox.showwarning("No Songs", f"No songs available in {emotion} folder")
        return
    
    # New window for song list
    list_win = tk.Toplevel(root)
    list_win.title(f"{emotion.capitalize()} Songs 🎶")
    list_win.geometry("350x350")
    
    for song in songs:
        song_path = os.path.join(folder, song)
        btn = tk.Button(list_win, text=song, width=40, command=lambda s=song_path: play_song(s))
        btn.pack(pady=5)

# Tkinter GUI
root = tk.Tk()
root.title("Emotion Based Music Player 🎵")
root.geometry("400x450")

tk.Label(root, text="Select Emotion", font=("Arial", 16, "bold")).pack(pady=20)

# Emoji buttons
emotions = {
    "happy": "😀",
    "sad": "😢",
    "angry": "😡",
    "surprise": "😲",
    "neutral": "😐"
}

for emotion, emoji in emotions.items():
    btn = tk.Button(root, text=emoji, font=("Arial", 22), width=5, command=lambda e=emotion: show_songs(e))
    btn.pack(pady=10)

# Run main loop
root.mainloop()
