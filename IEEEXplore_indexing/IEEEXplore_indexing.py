import sys
import re
def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def rem_sm(lis):
    res = []
    for i in lis:
        if len(i)<4:
            continue
        else:
            res.append(i)
    return res


stopWords = input().split(';')
indexTerms = input().split(';')
complete_input = sys.stdin.read()
# get all text inside title tag
title = re.findall("<title>(\n|.*?)</title>","".join(complete_input.replace("\n"," ")))
title = remove_html_tags(title[0])
# remove all notations
title = title.replace("!","").replace("?","").replace(",","").replace(".","")
title = title.split()
#remove small words
title = rem_sm(title)
title = [i.lower() for i in title]
#repeat for the other tags
body = re.findall("<body>(\n|.*?)</body>","".join(complete_input.replace("\n"," ")))
body = remove_html_tags(body[0])
body = body.replace(".","").replace("!","").replace("?","").replace(",","")
body = body.split()
body = rem_sm(body)
body = [i.lower() for i in body]
abstract = re.findall("<abstract>(\n|.*?)</abstract>","".join(complete_input.replace("\n"," ")))
abstract = remove_html_tags(abstract[0])
abstract = abstract.replace(".","").replace("!","").replace("?","").replace(",","")
abstract = abstract.split()
abstract = rem_sm(abstract)
abstract = [i.lower() for i in abstract]

for i in stopWords:
    # filter out all stopWords
    title = list(filter((i).__ne__, title))
    body = list(filter((i).__ne__, body))
    abstract = list(filter((i).__ne__, abstract))

TotalWords = len(title) + len(body) + len(abstract)
indexes = {}
# calculate scores
for i in indexTerms:
    indexes[i] = (title.count(i)*5 + body.count(i) + abstract.count(i)*3)*100/TotalWords

indexes = {k: v for k, v in sorted(indexes.items(), key=lambda item: (-item[1],item[0]), reverse=False)}

flag = 0


for i in indexes:
    if flag >= 3:
        if indexes.get(i) == temp[1]:
            print(i +":" , indexes.get(i))
            temp = [i, indexes.get(i)]
            continue
        break
    else:
        temp = [i, indexes.get(i)]
        print(i +":" , indexes.get(i))
    flag += 1
