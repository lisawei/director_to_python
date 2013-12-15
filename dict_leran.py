import os, sys
import json

dic = {'a':1,"b":2,"c":3,"d":4,"e":5,1:'f',2:'g'}
print dic['a']
print dic['b'],dic[2],dic['c']
for key,value in sorted(dic.iteritems()):
    print key, value

print 'g' in dic
print 'a' in dic
print 4 in dic

#list learn
#dic = {"a": 1, "b": 2, "c": 3}
#
#
#print "$key in dict"
#print dic.has_key("a")
#print dic.has_key("e")
#
#
#print '$loop list'
#for key,value in dic.iteritems():
#    print key , value


    



