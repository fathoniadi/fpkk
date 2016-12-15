import random

class pso:
    k=0

    def centroidOptimization(self, listParticle, listRataClusterParticle, rataGlobal):
        rand=[random.uniform(0.0, 1.0) for _ in xrange(3)]
        print rand
        for i in range(0, len(listParticle)):
            VDimen1 = listParticle[i].v.getVDimensi1() + 2 * rand[i] * (listRataClusterParticle[i][0] - listParticle[i].dimen.getDimensi1()) + 2 * rand[i] * (rataGlobal[0]-listParticle[i].dimen.getDimensi1())
            VDimen2 = listParticle[i].v.getVDimensi2() + 2 * rand[i] * (listRataClusterParticle[i][1] - listParticle[i].dimen.getDimensi2()) + 2 * rand[i] * (rataGlobal[1]-listParticle[i].dimen.getDimensi2())
            VDimen3 = listParticle[i].v.getVDimensi3() + 2 * rand[i] * (listRataClusterParticle[i][2] - listParticle[i].dimen.getDimensi3()) + 2 * rand[i] * (rataGlobal[2]-listParticle[i].dimen.getDimensi3())
            VDimen4 = listParticle[i].v.getVDimensi4() + 2 * rand[i] * (listRataClusterParticle[i][3] - listParticle[i].dimen.getDimensi4()) + 2 * rand[i] * (rataGlobal[3]-listParticle[i].dimen.getDimensi4())

            listParticle[i].v.setVDimensi1(VDimen1)
            listParticle[i].v.setVDimensi2(VDimen2)
            listParticle[i].v.setVDimensi3(VDimen3)
            listParticle[i].v.setVDimensi4(VDimen4)

            listParticle[i].dimen.setDimensi1(listParticle[i].dimen.getDimensi1() + VDimen1)
            listParticle[i].dimen.setDimensi2(listParticle[i].dimen.getDimensi2() + VDimen2)
            listParticle[i].dimen.setDimensi3(listParticle[i].dimen.getDimensi3() + VDimen3)
            listParticle[i].dimen.setDimensi4(listParticle[i].dimen.getDimensi4() + VDimen4)

        return listParticle

class dimension:
    dimensi1=0.0
    dimensi2=0.0
    dimensi3=0.0
    dimensi4=0.0

    def __init__(self, dimensi1, dimensi2, dimensi3, dimensi4):
        self.dimensi1 = dimensi1
        self.dimensi2 = dimensi2
        self.dimensi3 = dimensi3
        self.dimensi4 = dimensi4

    def setDimensi1(self, dimensi1):
        self.dimensi1=dimensi1

    def getDimensi1(self):
        return float(self.dimensi1)

    def setDimensi2(self, dimensi2):
        self.dimensi2=dimensi2

    def getDimensi2(self):
        return float(self.dimensi2)

    def setDimensi3(self, dimensi3):
        self.dimensi3=dimensi3

    def getDimensi3(self):
        return float(self.dimensi3)

    def setDimensi4(self, dimensi4):
        self.dimensi4=dimensi4

    def getDimensi4(self):
        return float(self.dimensi4)

class velocity:
    vdimensi1 = 0.0
    vdimensi2 = 0.0
    vdimensi3 = 0.0
    vdimensi4 = 0.0

    def __init__(self, vdimensi1, vdimensi2, vdimensi3, vdimensi4):
        self.vdimensi1 = vdimensi1
        self.vdimensi2 = vdimensi2
        self.vdimensi3 = vdimensi3
        self.vdimensi4 = vdimensi4

    def setVDimensi1(self, dimensi1):
        self.dimensi1 = dimensi1

    def getVDimensi1(self):
        return self.vdimensi1

    def setVDimensi2(self, dimensi2):
        self.vdimensi2 = dimensi2

    def getVDimensi2(self):
        return self.vdimensi2

    def setVDimensi3(self, dimensi3):
        self.vdimensi3 = dimensi3

    def getVDimensi3(self):
        return self.vdimensi3

    def setVDimensi4(self, dimensi4):
        self.vdimensi4 = dimensi4

    def getVDimensi4(self):
        return self.vdimensi4

class particle:
    dimen=None
    v=None
    SSE=0.

    def __init__(self, dimen, v, SSE):
        self.dimen=dimen
        self.v=v
        self.SSE=SSE

    def setSSE(self, SSE):
        return self.SSE

    def getSSE(self):
        return self.SSE

    def setVelocity(self, velocity):
        self.v=velocity

    def getVelocity(self):
        return self.v

    def setDimen(self, dimen):
        self.dimen=dimen

    def getDimen(self):
        return self.dimen