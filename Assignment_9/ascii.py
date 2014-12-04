import clusters
blognames,words,data=clusters.readfile('blogVectorResult.txt')
clust=clusters.hcluster(data)
#clusters.printclust(clust,labels=blognames)
reload(clusters)
#clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')
#kclust=clusters.kcluster(data,k=20)
coords=clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')
