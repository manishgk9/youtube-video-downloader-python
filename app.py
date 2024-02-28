import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
import os


def download_video():
    url = entry_url.get()
    resul = (resulution_box.get())

    if url and resul:
        progres_label.pack(pady=['10p', '5p'])
        progres_bar.pack(pady=["10px", "5px"])
        status_label.pack(pady=["10px", "5px"])
        try:
            print(url)
            yt = YouTube(url, on_progress_callback=progress_fun)
            stream = yt.streams.filter(res=resul).first()
            os.path.join("downloads", f"{yt.title}_{resul}.mp4")
            stream.download(output_path="downloads")
            status_label.configure(
                text="Downloaded video successfuly..", text_color="white", fg_color="green")
        except Exception as e:
            status_label.configure(
                text=f"Error:{str(e)}", text_color="white", fg_color="red")
            print("Exception is Occured", e)


def progress_fun(stream, chunk, bytes_remaining):
    totalsize = stream.filesize
    byte_downloaded = totalsize-bytes_remaining

    percentage = int(byte_downloaded/totalsize*100)
    print(percentage)
    progres_label.configure(text=f'{percentage} %')
    progres_label.update()
    progres_bar.set(float(percentage/100))


# root window
root = ctk.CTk()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# title of window

root.title("Youtube Downloader!")

root.geometry("720x480")
root.minsize(580, 480)
root.maxsize(580, 480)

content_frame = ctk.CTkFrame(master=root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here : ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=['10p', '5p'])
entry_url.pack(pady=['10p', '5p'])

download = ctk.CTkButton(
    content_frame, text='Download', command=download_video)
download.pack(pady=['10p', '5p'])

# resulutions
resulutions = ["720p", "360p"]
# resulutions_var = ctk.StringVar()
resulution_box = ctk.CTkComboBox(
    content_frame, values=resulutions)
resulution_box.pack(pady=['10p', '5p'])
resulution_box.set("720p")

# creating a label and progress
progres_label = ctk.CTkLabel(content_frame, text="0%")


progres_bar = ctk.CTkProgressBar(content_frame, width=400)
progres_bar.set(0)


# status label
status_label = ctk.CTkLabel(content_frame, text="")

root.mainloop()
