# Imgur-Speedrunner
"Speedrun" your bulk image uploads and get public links instantly


<img src="https://i.imgur.com/vOhqU3w.png"></img>


<em>Intro:</em> I wanted to build a wallpaper app, with imgur hosting all the pngs/jpgs behind the scenes <br>

<em>Problem:</em> cropping wallpapers to mobile resolution, generating thumbnails, uploading to imgur & generating its url in bulk was time consuming <br>

<em>Solution:</em> Enter Imgur-Speedrunner, two <strong>simple</strong> .py scripts to automate the problem statement above. <br>

# Step 1: put your images in one folder

<img src="https://i.imgur.com/iHzZaEc.jpg"></img>

# Step 2: Crop images and generate thumbnails

thumb_generator.py crops the images to mobile resolution in bulk in .png, generates thumbnails in .jpg keeps both cropped images and thumbs in one folder

<img src="https://i.imgur.com/xL2L3m5.jpg"></img>

# Step 3: upload & get public image urls

imgur_uploader.py uploads the images to imgur in bulk, and then returns a list of all the image urls in the same order it was uploaded

<img src="https://i.imgur.com/C0WuMcm.jpg"></img>

Thank you for reading, here's a cookie :) 
Feel free to play around and use it, Note that imgur allows only ~50 uploads max per hour


