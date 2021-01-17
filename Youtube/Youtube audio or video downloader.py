import pafy


a = input("Enter the url of Youtube Video - ")
b = input("Do you want to download the whole video or only audio(A/V) - ")


if b=="A":
    url = a
    video = pafy.new(url) 
  
    bestaudio = video.getbestaudio() 
    bestaudio.download()

if b=="V": 
  
    url = a
    video = pafy.new(url) 
      
    streams = video.streams 
    for i in streams: 
        print(i) 
          
    # get best resolution regardless of format 
    best = video.getbest() 
      
    print(best.resolution, best.extension) 
      
    # Download the video 
    best.download()
