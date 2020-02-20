import pandas as pd 
import SimpSOM as sps

df = pd.read_csv("H1_MLP Data label.csv")
H1Data = df[['Feature 1','Feature 2','Feature 3','Feature 4','Feature 5']]

print(H1Data)
H1Data = H1Data.dropna()

H1Data = H1Data.to_numpy()

print(H1Data)
print (len(H1Data))



# initializing and traning the model
# import SimpSOM as sps

#Build a network 20x20 with a weights format taken from the raw_data and activate Periodic Boundary Conditions. 
net = sps.somNet(20, 20, H1Data, PBC=True)

#Train the network for 10000 epochs and with initial learning rate of 0.01. 
net.train(0.01, 10000)

#Save the weights to file
net.save('filename_weights')

#Print a map of the network nodes and colour them according to the first feature (column number 0) of the dataset
#and then according to the distance between each node and its neighbours.
net.nodes_graph(colnum=0)
net.diff_graph()

#Project the datapoints on the new 2D network map.
# net.project(clean_data, labels=Surface attribute)

#Cluster the datapoints according to the Quality Threshold algorithm.
# net.cluster(clean_data, type='qthresh')	
