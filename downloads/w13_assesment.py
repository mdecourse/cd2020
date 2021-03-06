# 每週上完進度後, 以亂數抽選出 mini project 組員, 然後在既有先前的協同內容之外, 加上當週的進度協同實習結果
# 1. 分別選定班別, 以及分組別後, 執行亂數抽選, 程序會自動新增倉儲, 並將各組組員設為可推送版本的權限組員
# 2. 目前採手動設定各倉儲的 Github Pages (隨後嘗試改為自動設定)
# 3. 目前必須手動將亂數抽選結果, 加入對應倉儲內容 (隨後嘗試透過分頁程序與組合程序, 將結果納入靜態與動態網站中)
# 4. 目前必須採手動新增提交與推送 (隨後嘗試以自動流程進行)

from github import Github
import random
 
 # 2a Grouping list
cdaList = [['40723104', '40723107', '40723114', '40723115', '40723118', '40723122', '40723123', '40723140', '40723149', '40723151', '40723153', '40723154', '40723155'], ['40623143', '40723108', '40723127', '40723132', '40723133', '40723137', '40723141', '40723143', '40723144', '40723147', '40723148', '40723150'], ['40723103', '40723110', '40723112', '40723120', '40723125', '40723126', '40723128', '40723130', '40723139', '40723142', '40723145', '40723146'], ['40423155', '40723101', '40723102', '40723106', '40723111', '40723119', '40723121', '40723124', '40723134', '40723135', '40723136', '40723138']]
 
# 2b Grouping list
cdbList = [['40723201', '40723206', '40723213', '40723215', '40723216', '40723223', '40723226', '40723229', '40723230', '40723241', '40723242', '40723246', '40732319'], ['40523253', '40623117', '40623252', '40723221', '40723222', '40723228', '40723236', '40723237', '40723240', '40723243', '40723244', '40723249', '40732331'], ['40623114', '40623121', '40723203', '40723205', '40723207', '40723209', '40723218', '40723219', '40723227', '40723233', '40723239', '40723247', '40739214'], ['40623115', '40623144', '40623251', '40723204', '40723210', '40723212', '40723225', '40723232', '40723234', '40723238', '40723245', '40723250']]

'''
for i in cdbList:
    for j in range(len(i)):
        print(i[j])
'''
 
# every group select num of student
num = 3
repoName = "cdaw13-30"
repoDesp = "cd2020 " + repoName + " mini project"
studList = cdaList

selStud = []

# 列出分組 Github Pages 與倉儲連結
print("http://mde.tw/" + repoName)
print()
print("https://github.com/mdecourse/" + repoName + ".git")
print()
# random selection loop
for i in range(len(studList)):
    random.shuffle(studList[i])
    print("group:" + str(i+1))
    print()
    for j in range(num):
        stud = studList[i][j]
        print(stud)
        # 405 and 407 with s
        #加上 "40723153" 例外判別
        if (stud != "40723153") and (stud[2] == "5" or stud[2] == "7"):
            selStud.append("s" + str(stud))
        else:
            selStud.append(stud)
    print("----")
 
# got selected student list
 
#print(selStud)
 
with open('./../mdecourse_github_token.txt', 'r') as f:
    token = f.read().splitlines()
#print(token[0])

'''
# 為抽出的各組組員建立協同倉儲
# or using an access token
github = Github(token[0])
user = github.get_user()
repo = user.create_repo(name=repoName, description=repoDesp, auto_init=True)

# 將各組組員設為各分組倉儲的協同者, 具有倉儲推送權限
# grand selected user permission to push
for i in selStud:
    repo.add_to_collaborators(i, permission='push')
    # 讓用戶擁有管理權
    #repo.add_to_collaborators(i, permission='admin')
'''

'''
# list app repository of user
for repo in github.get_user().get_repos():
    print(repo.name)
'''