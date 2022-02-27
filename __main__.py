# importing packages
from multiprocessing import pool
from pprint import pprint
from pytube import YouTube
from youtube_dl import YoutubeDL
import os
from multiprocessing.pool import Pool

def download(value):
    for count in range(0, 3):
        try:
            initial_list = YouTube(value)

            audio = initial_list.streams.filter(only_audio=True, file_extension='webm').first()

            audio.download("songs")
            
            return True
        
        except:
            pass

    return False


def main():
    with open("song_list.txt", "r") as f:
        songs = f.read()

    pool = Pool()
    song_list = songs.strip().split("\n")
    song_list = list(set(song_list))
    results = pool.map(download, song_list)

    for link, success in zip(song_list, results):
        print(f"Success - {success} ||| link - {link}")



if __name__ == "__main__":
    main()