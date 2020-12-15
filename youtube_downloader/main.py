import pytube

link = pytube.YouTube('https://www.youtube.com/watch?v=OJG3zTso4WI')
test = link.streams.filter(res='1080p', mime_type='video/mp4')
print(test)

