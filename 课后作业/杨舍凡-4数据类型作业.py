# st1 = 'Hello pYthon'

# --------去重过度---------pass
# s1 = set(st1)
# s1.remove(' ')
# s2 = set(st1.lower())
# s3 = set(st1.upper())
# print('大写字母有',len(s1&s3),'个',s1&s3)
# print('小写字母有',len(s1&s2),'个',s1&s2)


import re
st1 = 'Hello pYthon'

Lower = re.compile('[a-z]')
Capitalize = re.compile('[A-Z]')

Lr = Lower.findall(st1)
Ce = Capitalize.findall(st1)

print('小写字母有',len(Lr),'个:',Lr)
print('大写字母有',len(Ce),'个:',Ce)
