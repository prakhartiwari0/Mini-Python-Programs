import pafy  
  
url = input("Kindly the video link: ")
video = pafy.new(url) 
  
bestaudio = video.getbestaudio() 
bestaudio.download() 
