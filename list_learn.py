import os, sys


#list learn
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print '$reverse list base on a[start:len:step]'
print  reversed(a)


#loop
for i in reversed(a):
    print i
    
print 'split learn'
print a[-1]
print a[0:5]
print a[1::2]
print a[5:]
print a[:5]
print len(a)
print a[::-1]
print 1 in a
print 22 in a

a=[1,2]
b=[3,4]
print a + b


for i in a:
    print i

#list,tuple
# list []
# tuple ()
# 'tuple' object does not support item assignment , save memory

t=(1,2,3,4,5,6,7,8)
for i in t:
    print i
print t[::-1]

b=[1,2,3,4]
b[0]=0
print b
#t[0]=0

c=(3,5,7,8,4,3)
for i in sorted(c):
    print i,

print




#print a[::-1]
#print reversed(a)
#
#print "$slice list"
#
#print a[0:5]
#print a[5:]
#print a[:5]
#
#print '$loop list'
#
#for i in a:
#    print i
#
#for i in reversed(a):
#    print i
#
#print "len list"
#len(a)
#
##print "find in list"
#print 1 in a



