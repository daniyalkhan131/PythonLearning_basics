playlist={
	'title':'patagonia bus',
	'author': 'daniyal khan',
	'songs':[
		{'title':'song1','artist':['blue'],'duration':2.3},
		{'title':'song2','artist':['kitty','dj'],'duration':6.3},
		{'title':'song3','artist':['blue','perry'],'duration':2.9}]
}

for song in playlist['songs']:
	print(song['title'])

sum=0
for song in playlist['songs']:
	sum+=song['duration']
print(f"total length of playlist {sum}")