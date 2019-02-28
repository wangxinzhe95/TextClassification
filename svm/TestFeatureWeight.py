# -*- coding:utf-8 -*-
import math
import sys
import os
ClassCode = ['aoyun', 'fangchan', 'hulianwang', 'jiankang', 'jiaoyu', 'junshi', 'lvyou', 'qiche', 'shangye', 'shishang', 'tiyu', 'wenhua', 'yule']
# ClassCode = ['aoyun', 'fangchan', 'jiankang', 'jiaoyu', 'lvyou', 'shangye', 'tiyu']
# textCutBasePath = "G:\\ChineseTextClassify\\SogouCCut\\"
# textCutBasePath = sys.path[0] + "\\SogouCCut\\"
textCutBasePath = "/Users/wangxinzhe/PycharmProjects/result_final/"
# 读取特征
def readFeature(featureName):
    featureFile = open(featureName, 'r')
    featureContent = featureFile.read().split('\n')
    featureFile.close()
    feature = list()
    for eachfeature in featureContent:
        eachfeature = eachfeature.split(" ")
        if (len(eachfeature)==2):
            feature.append(eachfeature[1])
    return feature


# 读取特征的文档计数
def readDfFeature(dffilename):
    dffeaturedic = dict()
    dffile = open(dffilename, "r")
    dffilecontent = dffile.read().split("\n")
    dffile.close()
    for eachline in dffilecontent:
        eachline = eachline.split(" ")
        if len(eachline) == 2:
            dffeaturedic[eachline[0]] = eachline[1]
            # print(eachline[0] + ":"+eachline[1])
    # print(len(dffeaturedic))
    return dffeaturedic

# 对测试集进行特征向量表示
def readFileToList(textCutBasePath):
    dic = dict()
    TrainDocumentCountTemp = 0
    for root, dirs, files in os.walk(textCutBasePath):
    # for eachclass in ClassCode:
        eachclass = root.split('/')[-1]
        if eachclass == "":
            continue
        eachclasslist = list()
        flag = -1
        for f in files:
            flag = flag + 1
            if (flag < len(files)/2):
                continue
        # for i in range(DocumentCount, DocumentCount+TestDocumentCount):
            #print(currClassPath+str(i)+".cut")
            # eachfile = open(currClassPath+str(i)+".txt")
            TrainDocumentCountTemp = TrainDocumentCountTemp + 1
            eachfile = open(root + '/' + f, 'r')
            eachfilecontent = eachfile.read()
            eachfilewords = eachfilecontent.split(" ")
            eachclasslist.append(eachfilewords)
            # print(eachfilewords)
        dic[eachclass] = eachclasslist
    return dic, TrainDocumentCountTemp

def TFIDFCal(feature, dic,dffeaturedic,filename,TrainDocumentCount):
    file = open(filename, 'w')
    file.close()
    file = open(filename, 'a')
    # classid = 0
    for key in dic:
        print key
        classFiles = dic[key]
        classid = ClassCode.index(key)
        for eachfile in classFiles:
            # 对每个文件进行特征向量转化
            file.write(str(classid)+" ")
            for i in range(len(feature)):
                if feature[i] in eachfile:
                    currentfeature = feature[i]
                    featurecount = eachfile.count(feature[i])
                    tf = float(featurecount)/(len(eachfile))
                    # 计算逆文档频率
                    idffeature = math.log(float(TrainDocumentCount + 1)/(int(dffeaturedic[currentfeature])+ 2))
                    featurevalue = idffeature * tf
                    file.write(str(i+1)+":"+str(featurevalue) + " ")
            file.write("\n")

# 对另一半文档作为测试集
feature = readFeature("SVMFeature.txt")
dffeaturedic = readDfFeature("dffeature.txt")
dic, TrainDocumentCount = readFileToList(textCutBasePath)
print TrainDocumentCount
TFIDFCal(feature, dic, dffeaturedic, "test.svm", TrainDocumentCount)