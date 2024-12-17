import tkinter as tk
from tkinter import messagebox 
import yt_dlp as youtube_dl
import threading
import re  

download_thread = None



def is_valid_youtube_url(url):
    youtube_regex = r"^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$"
    return re.match(youtube_regex, url) is not None


def download_video_high():
    global download_thread
    link = url_entry.get()

    if not is_valid_youtube_url(link):
        messagebox.showerror("Error", "Invalid YouTube URL. Please enter a valid link.")
        return

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }

    def download():
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                status_label.config(text="The video has been uploaded in high quality!!")
        except Exception as e:
            status_label.config(text=f"An error occurred: {str(e)}")

    download_thread = threading.Thread(target=download)
    download_thread.start()


def download_video_low():
    global download_thread
    link = url_entry.get()

    
    if not is_valid_youtube_url(link):
        messagebox.showerror("Error", "Invalid YouTube URL. Please enter a valid link.")
        return

    ydl_opts = {
        'format': 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }

    def download():
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                status_label.config(text="The video has been uploaded in low quality!!")
        except Exception as e:
            status_label.config(text=f"An error occurred: {str(e)}")

    download_thread = threading.Thread(target=download)
    download_thread.start()


def download_audio():
    global download_thread
    link = url_entry.get()

    if not is_valid_youtube_url(link):
        messagebox.showerror("Error", "Invalid YouTube URL. Please enter a valid link.")
        return

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': '%(title)s.%(ext)s',
    }

    def download():
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                status_label.config(text="Only audio has been uploaded!")
        except Exception as e:
            status_label.config(text=f"An error occurred: {str(e)}")

    download_thread = threading.Thread(target=download)
    download_thread.start()


def stop_download():
    global download_thread
    if download_thread and download_thread.is_alive():
        download_thread.join()  
        status_label.config(text="Download has been stopped.")


root = tk.Tk()
root.geometry("500x300")
root.title("Videos Downloader")
root.configure(bg="light gray")

url_label = tk.Label(root, text="Enter The Video URL: ", font="bold" ,bg=root["bg"])
url_label.grid(row=0, column=0, columnspan=3, pady=10)

url_entry = tk.Entry(root, width=60)
url_entry.grid(row=1, column=0, columnspan=2, pady=20)

high_button = tk.Button(root, text="Download High Quality", bg="gray", command=download_video_high,font="bold",activeforeground="green")
high_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

low_button = tk.Button(root, text="Download Low Quality", bg="gray", command=download_video_low,font="bold",activeforeground="green")
low_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

audio_button = tk.Button(root, text="Download Audio Only", bg="gray", command=download_audio,font="bold",activeforeground="green")
audio_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

stop_button = tk.Button(root, text="Stop Download", bg="red", command=stop_download)
stop_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
