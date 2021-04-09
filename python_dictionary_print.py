dict = {
  "mathematics": "jiaoxue",
  "dog": "gou",
  "father" : "baba",
  "news" : "xinwen",
  "god" : "shen",
}

#find the longest string in dictionary
keyList = list(dict.keys())
longestKey = keyList[0]

for i in keyList:
    if len(i) > len(longestKey):
        longestKey = i


#printing the dictionary
for i in keyList:
    print('{0:>{x}}'.format(i ,x=str(len(longestKey))) + ' | ' + str(dict[i]))

