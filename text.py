from pytube import YouTube
from sys import argv

def main():

 link =input('enter the link of the vedio')
 yt =YouTube(link)

 print("title:",yt.title)

 print("vies:",yt.views)

 yd =yt.streams.get_highest_resolution()
 yd.download("/Users/fazal/Desktop/new")


 a=input("downloaded")







 
 repeat=True
 if repeat==True:
  main()
 else :
    exit()
main()

