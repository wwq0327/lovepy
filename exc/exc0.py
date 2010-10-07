#coding:utf-8

f = open('test.txt','r')
result = []
for line in f.readlines():
    line = line.strip()
    if not len(line) or line.startswith('#'):
        continue
    result.append(line)
result.sort()
print result
open('test-new.txt','w').write('%s' % '\n'.join(result))
