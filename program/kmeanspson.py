from kmeans import kmeans
import collections

if __name__=="__main__":
    numberofclass=8
    dataset=[]
    realclass=[]
    with open("iris.data","r") as f:
        for line in f:
            dataset.append(line.split(",")[:-1])
            realclass.append(line.split(",")[-1])

    temp=[]
    counter=0
    for data in dataset:
        if data in temp:
            counter+=1
        else:
            temp.append(data)
    k=kmeans(dataset, 3)
    k.execute()