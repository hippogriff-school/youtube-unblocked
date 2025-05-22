import os
import webbrowser

# Ask for YouTube URL
youtube_url = input("Enter a YouTube video URL: ")

# Extract the video ID
if "v=" in youtube_url:
    video_id = youtube_url.split("v=")[1].split("&")[0]
elif "youtu.be/" in youtube_url:
    video_id = youtube_url.split("youtu.be/")[1].split("?")[0]
else:
    print("Invalid YouTube link.")
    exit()

# Create folder
folder = "youtube_embed"
os.makedirs(folder, exist_ok=True)

# HTML content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Video</title>
</head>
<body>
    <h1>Embedded YouTube Video</h1>
    <iframe width="560" height="315" 
            src="https://www.youtube.com/embed/{video_id}" 
            frameborder="0" allowfullscreen></iframe>
</body>
</html>
"""

# Write HTML file
html_path = os.path.join(folder, "index.html")
with open(html_path, "w") as f:
    f.write(html_content)

# Open in default browser
webbrowser.open(f"file://{os.path.abspath(html_path)}")

print(f"HTML file created and opened: {html_path}")
