
saveFile = open('feedlink.txt','a')		
with open("blogs.txt", "r") as f:
  for line in f:
	newline =line.strip()
	newline =newline+'feeds/posts/default?max-results=500'
	saveFile.write(newline)
	saveFile.write('\n')
saveFile.close()
