import math
import random
import psoOptimization

class kmeans():
    cluster1 = []
    centroidcluster1 = 0.0
    cluster2 = []
    centroidcluster2 = 0.0
    cluster3 = []
    centroidcluster3 = 0.0
    dataset=[]
    centercluster1=[]
    centercluster2 = []
    centercluster3 = []
    k=0
    MAXITER=10

    def __init__(self, dataset, k):
        self.dataset=dataset
        self.k=k

    def euclideandistance(self, list1, list2):
        if len(list1)!=len(list2):
            return 100000
        else:
            total=0
            for i in range(0,len(list2)):
                total=total+math.pow(float(list1[i])-float(list2[i]),2)
            return math.sqrt(total)

    def countcentroid(self, cluster):
        newcentroid=[]
        for i in range(0, len(cluster[0])):
            newcentroid.append(0.0)
        for record in cluster:
            for i in range(0, len(record)):
                newcentroid[i]+=float(record[i])
        for i in range(0, len(cluster[0])):
            newcentroid[i]=newcentroid[i]/len(cluster)
        return newcentroid

    def execute(self):
        psoobj=psoOptimization.pso()
        indexcentroidcluster1=random.randint(0,149)
        indexcentroidcluster2 = random.randint(0, 149)
        indexcentroidcluster3 = random.randint(0, 149)

        self.centercluster1 = self.dataset[indexcentroidcluster1]
        self.centercluster2 = self.dataset[indexcentroidcluster2]
        self.centercluster3 = self.dataset[indexcentroidcluster3]

        print "cluster1 awal: ",self.centercluster1
        print "cluster2 awal: ", self.centercluster2
        print "cluster3 awal: ", self.centercluster3
        #print self.dataset

        iterator=1
        while iterator<=self.MAXITER:
            print iterator
            self.cluster1.append(self.centercluster1)
            self.cluster2.append(self.centercluster2)
            self.cluster3.append(self.centercluster3)
            print self.dataset
            print "==========================================="

            self.centroidcluster1 = self.countcentroid(self.cluster1)
            self.centroidcluster2 = self.countcentroid(self.cluster2)
            self.centroidcluster3 = self.countcentroid(self.cluster3)

            self.dataset.pop(indexcentroidcluster1);
            self.dataset.pop(indexcentroidcluster2);
            self.dataset.pop(indexcentroidcluster3);

            counter=0
            for data in self.dataset:
                counter+=1
                print type(data)
                print data
                print type(self.centercluster1)
                distancetocluster1 = self.euclideandistance(data,self.centercluster1)
                distancetocluster2 = self.euclideandistance(data,self.centercluster2)
                distancetocluster3 = self.euclideandistance(data,self.centercluster3)
                closest =min(distancetocluster1, distancetocluster2, distancetocluster3)
                #print "memilih cluster"
                if closest==distancetocluster1:
                    self.cluster1.append(data)
                    self.centroidcluster1=self.countcentroid(self.cluster1)
                    '''if data not in self.cluster1:
                        #print "masuk ke cluster 1"
                        self.cluster1.append(data)
                        centroidcluster1=self.countcentroid(self.cluster1)
                    else:
                        print data," tidak masuk karena ada duplikat"
                        print "============================================="'''
                elif closest==distancetocluster2:
                    self.cluster2.append(data)
                    self.centroidcluster2 = self.countcentroid(self.cluster2)
                    '''if data not in self.cluster2:
                        #print "masuk ke cluster 2"
                        self.cluster2.append(data)
                        centroidcluster2=self.countcentroid(self.cluster2)
                    else:
                        print data," tidak masuk karena ada duplikat"
                        print "============================================="'''
                elif closest==distancetocluster3:
                    self.cluster3.append(data)
                    self.centroidcluster3 = self.countcentroid(self.cluster3)
                    '''if data not in self.cluster3:
                        #print "masuk ke cluster 3"
                        self.cluster3.append(data)
                        centroidcluster3=self.countcentroid(self.cluster3)
                    else:
                        print data," tidak masuk karena ada duplikat"
                        print "============================================="'''
                else:
                    print data," tidak berhasil diklasifikasikan"
                    print "closest: ", closest
                    print "distancetocluster1: ", distancetocluster1
                    print "distancetocluster2: ", distancetocluster2
                    print "distancetocluster3: ", distancetocluster3
                    print "============================================="

            listSSE=self.countSSE()
            particlecentroid1=psoOptimization.particle(psoOptimization.dimension(self.centercluster1[0],self.centercluster1[1],self.centercluster1[2],self.centercluster1[3]), psoOptimization.velocity(0.0,0.0,0.0,0.0),listSSE[0])
            particlecentroid2=psoOptimization.particle(psoOptimization.dimension(self.centercluster2[0],self.centercluster2[1],self.centercluster2[2],self.centercluster2[3]), psoOptimization.velocity(0.0,0.0,0.0,0.0),listSSE[1])
            particlecentroid3=psoOptimization.particle(psoOptimization.dimension(self.centercluster3[0],self.centercluster3[1],self.centercluster3[2],self.centercluster3[3]), psoOptimization.velocity(0.0,0.0,0.0,0.0),listSSE[2])

            listCenterCluster=psoobj.centroidOptimization([particlecentroid1,particlecentroid2,particlecentroid3],[self.ratarata(self.cluster1),self.ratarata(self.cluster2),self.ratarata(self.cluster3)],self.ratarata(self.dataset))

            self.centercluster1[0]=listCenterCluster[0].dimen.getDimensi1()
            self.centercluster1[1] = listCenterCluster[0].dimen.getDimensi2()
            self.centercluster1[2] = listCenterCluster[0].dimen.getDimensi3()
            self.centercluster1[3] = listCenterCluster[0].dimen.getDimensi4()

            self.centercluster2[0] = listCenterCluster[1].dimen.getDimensi1()
            self.centercluster2[1] = listCenterCluster[1].dimen.getDimensi2()
            self.centercluster2[2] = listCenterCluster[1].dimen.getDimensi3()
            self.centercluster2[3] = listCenterCluster[1].dimen.getDimensi4()

            self.centercluster3[0] = listCenterCluster[2].dimen.getDimensi1()
            self.centercluster3[1] = listCenterCluster[2].dimen.getDimensi2()
            self.centercluster3[2] = listCenterCluster[2].dimen.getDimensi3()
            self.centercluster3[3] = listCenterCluster[2].dimen.getDimensi4()

            print "cluster 1 akhir: ", self.centercluster1
            print "cluster 2 akhir: ", self.centercluster2
            print "cluster 3 akhir: ", self.centercluster3

            self.dataset.append(self.centercluster1);
            self.dataset.append(self.centercluster2);
            self.dataset.append(self.centercluster3);

            iterator+=1

        print "cluster1: ", self.cluster1
        print "cluster2: ", self.cluster2
        print "cluster3: ", self.cluster3
        print "banyaknya dataset: ", len(self.dataset)
        print counter
        print "banyaknya cluster 1:", len(self.cluster1)
        print "banyaknya cluster 2:", len(self.cluster2)
        print "banyaknya cluster 3:", len(self.cluster3)
        print "jumlah setelah clustering: ", len(self.cluster1)+len(self.cluster2)+len(self.cluster3)

    def countSSE(self):
        SSECluster1=0.0
        for data in self.cluster1:
            SSECluster1 += self.euclideandistance(data, self.centercluster1) ** 2
        SSECluster2=0.0
        for data in self.cluster2:
            SSECluster2 += self.euclideandistance(data, self.centercluster2) ** 2
        SSECluster3 = 0.0
        for data in self.cluster3:
            SSECluster3 += self.euclideandistance(data, self.centercluster3) ** 2
        return [SSECluster1,SSECluster2,SSECluster3]

    def ratarata(self, list):
        result=[0.0,0.0,0.0,0.0]
        for data in list:
            for i in range(0, len(data)):
                result[i]+=float(data[i])
        for i in range(0, len(result)):
            result[i]=result[i]/len(list)
        return result