import os

url = input("Enter the link of the google drive video : ")
url = url.replace("view?usp=sharing", "preview")
code = f"""
<iframe src="{url}" width="1120" height="630"  frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
"""

html_code = f"""
<html>
<head>
<title>DRIVE VIDEO</title>
</head>

<style>
body{{
background-color: yellow;
text-align: center;
border: 10px black solid;
height:2000px;
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
