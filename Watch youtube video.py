import os

link = input("Write the link of the youtube video - \n")



if "youtu.be" in link:
    a = link.index("t=")
    b = len(link)
    time = link[a+2:b]
    link = link.replace(f"?t={time}", "")
    link = link.replace("https://youtu.be/", "")
    link = f"https://www.youtube.com/embed/{link}?start={time}"
    code = f"""<iframe width="1120" height="630" src="{link}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""

else:
    link = link.replace("https://www.youtube.com/watch?v=", "")
    link = f"https://www.youtube.com/embed/{link}"
    code = f"""<iframe width="1120" height="630" src="{link}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""

html_code = f"""
<html>
<head>
<title>YOUTUBE VIDEO</title>
</head>

<style>
body{{
background-color: yellow;
text-align: center;
border: 10px black solid;
height:1000px;
}}
div{{background-color: black;}}
</style>

<body>
<div>
{code}
</div>
</body>


</html>"""

f = open("Video.html", "w")
f.write(html_code)
f.close()

os.startfile("Video.html")



