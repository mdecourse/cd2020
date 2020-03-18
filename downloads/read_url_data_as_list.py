import requests
import ast
import random

link = "https://mdecourse.github.io/cd2020/downloads/2a_group_list.txt"
f = requests.get(link)
print(f.text)

# draw num of members from each group randomly
num = 1
x = ast.literal_eval(f.text)
print(type(x))
for i in range(len(x)):
    #print("group " + str(i+1) + ":", x[i])
    random.shuffle(x[i])
    print("-" * 20)
    for j in range(num):
        print("group " + str(i+1) + ":", x[i][j])