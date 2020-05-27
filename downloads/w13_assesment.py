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
repoName = "cdaw13-3"
repoDesp = "cd2020 " + repoName + " mini project"
studList = cdaList

selStud = []
 
# random selection loop
 
for i in range(len(studList)):
    random.shuffle(studList[i])
    print("group:" + str(i+1))
    print()
    for j in range(num):
        stud = studList[i][j]
        print(stud)
        # 405 and 407 with s
        if stud[2] == "5" or stud[2] == "7":
            selStud.append("s" + str(stud))
        else:
            selStud.append(stud)
    print("----")
 
# got selected student list
 
#print(selStud)
 
with open('./../../mdecourse_github_token.txt', 'r') as f:
    token = f.read().splitlines()
#print(token[0])
 
# or using an access token
github = Github(token[0])
user = github.get_user()
repo = user.create_repo(name=repoName, description=repoDesp, auto_init=True)
 
# grand selected user permission to push
for i in selStud:
    repo.add_to_collaborators(i, permission='push')
    # 讓用戶擁有管理權
    #repo.add_to_collaborators(i, permission='admin')

'''
# list app repository of user
for repo in github.get_user().get_repos():
    print(repo.name)
'''