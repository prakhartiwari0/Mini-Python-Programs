import pafy 
  
url = input("Kindly the video link: ")
video = pafy.new(url) 
  
streams = video.streams 
for i in streams: 
    print(i) 
      
# get best resolution regardless of format 
best = video.getbest() 
  
print(best.resolution, best.extension) 
  
# Download the video 
best.download() 
