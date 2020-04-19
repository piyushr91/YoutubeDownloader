import tkinter as tk
import pprint
from pytube import YouTube
from PIL import ImageTk, Image

HEIGHT = 300
WIDTH = 450

def downloadVideos():
    global entry
    downloadLink = entry.get()
    yt = YouTube(str(downloadLink))
    # videos = yt.streams.filter(subtype='mp4', progressive=True).order_by('resolution').all()
    # index = 1
    # for v in videos:
    #     print(str(index) + '.' + str(v))
    #     index += 1
    # n = int(input("Enter your choice: "))
    # print()
    # vid = videos[n-1]
    # destLoc = str(input("Destination Folder: "))
    # print()
    # vid.download(destLoc)
    videos = yt.streams.filter(subtype='mp4', progressive=True).order_by('resolution').first()
    print(videos)
    destLoc = "C:\\Users\\prajesh\\Desktop\\VideoTest"
    videos.download(str(destLoc))
    print("Video has been downloaded successfully")

root = tk.Tk(className="Youtube Downloader")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('youtube-downloader.jpg'))
background_label = tk.Label(canvas, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

label = tk.Label(canvas, justify = 'left', bd = 2, font=('Ubuntu', 20), text="Youtube Downloader")
label.place(relwidth = 1, relheight = 0.2)

entry = tk.Entry(root, justify='left', font=('Ubuntu', 12))
entry.pack(side=tk.TOP, ipadx=110, ipady=8)

button = tk.Button(root, text="Download", fg="black", command=downloadVideos)
button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()     


