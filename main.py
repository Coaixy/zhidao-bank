import json,re

data = ""
question_list = list()
danxuan = list()
duoxuan = list()
panduan = list()
with open("100.txt",'r',encoding='UTF-8') as f:
    data = f.read()
a = re.compile('{"status":200(.*?)}}')
question_list =a.findall(data)
for index,value in enumerate(question_list):
    question_list[index] = '{"status":200'+value+'}}'
for index,value in enumerate(question_list):
    data = json.loads(value)
    question_list[index] = data['rt']
for i in question_list:
    result = "🎈("+i['questionName']+")"+i['content']+"\n"
    optionList = i['optionList']
    for j in optionList:
        if j['isCorrect'] == 1:
            result = result +j['content']+"  ✔"+"\n"
        else:
            result = result +j['content']+"\n"
    if i['questionName'] == "单选题":
        danxuan.append(result)
    elif i['questionName'] == "判断题":
        panduan.append(result)
    else:
        duoxuan.append(result)
result = ""
for i in danxuan:
    result = result+i+"\n"
for i in panduan:
    result = result+i+"\n"
for i in duoxuan:
    result = result+i+"\n"
print(result)
with open('result.txt',"w",encoding='UTF-8') as f:
    f.write(result)