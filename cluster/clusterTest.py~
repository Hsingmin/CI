
# clusterTest.py

import cluster

blognames, words, data = cluster.readfile('blogdata.txt')

'''
clust = cluster.hcluster(data)

# cluster.printclust(clust, labels = blognames)

cluster.drawdendrogram(clust, blognames, jpeg = 'blogclust.jpg')
'''

kclust = cluster.kcluster(data, k = 10)

print([blognames[r] for r in kclust[2]])





















