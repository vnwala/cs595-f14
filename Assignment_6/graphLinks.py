from igraph import *
karate = load("karate.GraphML")
karate.vs["label"] = karate.vs["name"]
karate.vs["Faction"] = ["1","1","1","1","1","1","1","1", "2", "2","1","1","1","1", "2", "2","1","1", 
"2","1", "2","1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
color_dict = {"1": "blue", "2": "pink"}
karate.vs["color"] = [color_dict[Faction] for Faction in karate.vs["Faction"]]
layout = karate.layout("kamada_kawai")
plot(karate, "original.pdf", layout = layout, bbox = (600, 600), margin = 40)

while len(karate.clusters()) <= 6:
  
  ebs = karate.edge_betweenness()
  # determines the edge betweenness
  max_idx = max(xrange(len(ebs)), key = ebs.__getitem__)
  # find the index of the edge with the maximum betweenness
  karate.delete_edges(max_idx)
  # remove that edge
  print "cluster is equal to" +' '+ str(len(karate.clusters()))
  # prints the number of clusters after an edge is removed
  if len(karate.clusters()) == 2:
	layout = karate.layout("kamada_kawai")	
	plot(karate, "final_2.pdf", layout = layout,bbox = (600, 600), margin = 40)
	#saves plot when 2 clusters are reached 
  if len(karate.clusters()) == 3:
	layout = karate.layout("kamada_kawai")
	plot(karate, "final_3.pdf", layout = layout,bbox = (600, 600), margin = 40)
	# saves plot when 3 clusters are reached
  if len(karate.clusters()) == 4:
	layout = karate.layout("kamada_kawai")
	plot(karate, "final_4.pdf", layout = layout,bbox = (600, 600), margin = 40)
	# saves plot when 4 clusters are reached
  if len(karate.clusters()) == 5:
	layout = karate.layout("kamada_kawai")
	plot(karate, "final_5.pdf", layout = layout,bbox = (600, 600), margin = 40)
	# saves plot when 5 clusters are reached


	
	     

 

