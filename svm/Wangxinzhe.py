from svmutil import *

y, x = svm_read_problem('train.svm')
print "66666"
yt, xt = svm_read_problem('test.svm')
print "???????"

m = svm_train(y,x)
svm_predict(yt,xt,m)