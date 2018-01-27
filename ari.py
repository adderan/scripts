import sys
import argparse

class Feature:
    def __init__(self, chrom, start, end, name):
        self.chrom = chrom
        self.start = start
        self.end = end
        self.name = name

class Element:
    def __init__(self, name, refName):
        self.name = name
        self.refName = refName

def readGff(gff):
    features = []
    for line in gff:
        info = line.split()
        if len(info) != 9:
            continue
        chrom, source, annotationType, start, end, score, strand, a, name = info
        features.append(Feature(chrom, start, end, name))
    return(features)

def readRmaskGff(gff):
    features = []
    for line in gff:
        info = line.split()
        if len(info) != 16:
            continue
        chrom, source, annotationType, start, end, score, strand, a, b, name, c, d, e, f, g, h = info
        features.append(Feature(chrom, start, end, name))
    return(features)

def overlap(f1, f2):
    left = (f1.start <= f2.start) and (f1.end >= f2.start)
    right = (f1.start >= f2.start) and (f1.start <= f2.end)
    if left or right:
        #Overlap
        return 0
    elif f1.start < f2.start:
        #No overlap and f1 occurs before f2
        return -1
    else:
        #No overlap and f1 occurs after f2
        return 1

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--rmask", type=file)
    parser.add_argument("--features", type=file)
    args = parser.parse_args()

    
    features = readGff(args.features)
    refFeatures = readRmaskGff(args.rmask)

    #sort by start position
    features.sort(key=lambda x: x.start)
    refFeatures.sort(key=lambda x: x.start)

    elements = []
    i = 0
    for feature in features:
        while overlap(feature, refFeatures[i]) > 0:
            i = i + 1
        if overlap(feature, refFeatures[i]) == 0:
            print "Found overlap betwen " + feature.name + " and " + refFeatures[i].name
            elements.append(Element(name=feature.name, refName=refFeatures[i].name))


    #Calculate rand index
    a = 0.0
    b = 0.0
    c = 0.0
    d = 0.0
    for i in range(len(elements)):
        for j in range(i):
            if (elements[i].name == elements[j].name) and (elements[i].refName == elements[j].refName):
                a += 1.0
            elif (elements[i].name != elements[j].name) and (elements[i].refName != elements[j].refName):
                b += 1.0
            elif (elements[i].name == elements[j].name) and (elements[i].refName != elements[j].refName):
                c += 1.0
            elif (elements[i].name != elements[j].name) and (elements[i].refName == elements[j].refName):
                d += 1.0

    print("Found %d elements" % len(elements))

    print("a = %f" % a)
    print("b = %f" % b)
    print("c = %f" % c)
    print("d = %f" % d)

    r = (a + b)/(a + b + c + d)

    print("Rand index = %f" % r)


if __name__ == "__main__":
    main()
