# Description: Construction and computation of new features
# Category:    core
# Uses:        monks-1
# Referenced:  Orange.data.variable
# Classes:     Orange.data.variable.Discrete

import Orange

def checkE(inst, returnWhat):
    if inst["e"]=="1": 
        return e2("1")
    else:
        return e2("not 1") 

data = Orange.data.Table("monks-1")
e2 = Orange.data.variable.Discrete("e2", values=["not 1", "1"])    
e2.getValueFrom = checkE 

print Orange.core.MeasureAttribute_info(e2, data)

dist = Orange.core.Distribution(e2, data)
print dist 

# Split the data into training and testing set
indices = Orange.core.MakeRandomIndices2(data, p0=0.7)
trainData = data.select(indices, 0)
testData = data.select(indices, 1)

# Convert the training set to a new domain
newDomain = Orange.data.Domain([data.domain["a"], data.domain["b"], e2, data.domain.classVar])
newTrain = Orange.data.Table(newDomain, trainData)

# Construct a tree and classify unmodified instances
tree = Orange.core.TreeLearner(newTrain)
for ex in testData[:10]:
    print ex.getclass(), tree(ex)