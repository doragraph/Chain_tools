import json
import requests

f = open('targetAddress', 'r', encoding = 'UTF-8')
x = []
while True :
	i = f.readline()
	if i=='': break
	print(i,end='')
	if i not in x:
		x.append(i.rstrip())

x = set(x)
f = open("resultBalance.txt", "w")
final = 0
for y in x:

	r = requests.get('http://192.168.51.203:9006/getAccount?address='+y)

	data2 = json.loads(r.text)
	front = ""
	back = "TokenName:[]string{"
	back2 = "TokenBalance:[]string{"
	front = front + "{\n"
	front = front + 'Address:"'+y+'",\n'
	front = front + 'Amount:"'+data2["Balance"]+'",\n'

	try:
		for i,v in data2["Token"].items():
			back = back +'"'+ i+'",'+"\n"
			back2 = back2 +'"'+ str(v)+'",'+"\n"
			u = 1
	except:
		print("error")
	if(u==1):
		back = back + "},\n"+back2+"},\n"
		f.write(front + back + "},\n")
		f.write(front + "},\n")


f.close()
