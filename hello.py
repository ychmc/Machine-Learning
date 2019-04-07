from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    lable = ['A','A','B','B']
    return group, lable;

def classify(inX,dataSet,lable,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances**0.5
    print(distance)
    sortedDistance = distance.argsort()
    print(sortedDistance)
    classCount = {}
    for i in range(k):
        voteLable = lable[sortedDistance[i]]
        classCount[voteLable] = classCount.get(voteLable,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

group,lable = createDataSet()
print(group)
x = classify([0.7,0.7],group,lable,3)
print(x)