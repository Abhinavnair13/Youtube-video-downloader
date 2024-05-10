from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")#progressive-can be played while downloading
        highest_res_stream= streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully")
    except Exception as e:
        print(e)
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder : {folder}")
    return folder
if __name__== "__main__":
    root = tk.Tk()
    root.withdraw()
    video_url =input("Please enter a youtube url: ")
    root.deiconify()
    save_dir=select_folder()
    if save_dir:
        print("Download started ...")
        download_video(video_url,save_dir)
