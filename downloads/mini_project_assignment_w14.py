from github import Github
import random

""" cd2020 兩班的分組資料
"""
 # 2a Grouping list
cdaList = [['40723104', '40723107', '40723114', '40723115', '40723118', '40723122', '40723123', '40723140', '40723149', '40723151', '40723153', '40723154', '40723155'], ['40623143', '40723108', '40723127', '40723132', '40723133', '40723137', '40723141', '40723143', '40723144', '40723147', '40723148', '40723150'], ['40723103', '40723110', '40723112', '40723120', '40723125', '40723126', '40723128', '40723130', '40723139', '40723142', '40723145', '40723146'], ['40423155', '40723101', '40723102', '40723106', '40723111', '40723119', '40723121', '40723124', '40723134', '40723135', '40723136', '40723138']]
 
# 2b Grouping list
cdbList = [['40723201', '40723206', '40723213', '40723215', '40723216', '40723223', '40723226', '40723229', '40723230', '40723241', '40723242', '40723246', '40732319'], ['40523253', '40623117', '40623252', '40723221', '40723222', '40723228', '40723236', '40723237', '40723240', '40723243', '40723244', '40723249', '40732331'], ['40623114', '40623121', '40723203', '40723205', '40723207', '40723209', '40723218', '40723219', '40723227', '40723233', '40723239', '40723247', '40739214'], ['40623115', '40623144', '40623251', '40723204', '40723210', '40723212', '40723225', '40723232', '40723234', '40723238', '40723245', '40723250']]

"""定義 mini project 亂數分組
    studList: 班級分組數列, 例如: cdaList 或 cdbList
    prjTitle: 專案標題, 例如: cdaw14
    mbrNum: 每一組抽出人數 member number, 例如: 3
    prjNum: 總共建立的 mini project 組數, 例如: 3
"""

def miniProject(studList, prjTitle, mbrNum, prjNum):
    # 建立 miniProject 各分組組員數列
    # prjOrd: project order 專案序號
    # prjNum: 建立專案組數
    # 利用 for 迴圈執行指定專案次數
    # courseTitle: 課程名稱
    # prjDesp: project description 專案說明
    courseTitle = "cd2020"
    prjDesp = "mini project"
    webPrefix = "http://mde.tw/"
    repoPrefix = "https://github.com/mdecourse/"
    repoSuffix = ".git"
    nosExcept = ["40723153"]
    # 預計將各組抽選的學號放入 allGrp
    allGrp = []
    miniGrp = []
    # selStud 為各 mini project 抽選的學號數列
    # 先取出各大分組數列弄亂後共 mbrNum *prjNum 個數的分組組員
    grpNum = len(studList)
    for grp in range(grpNum):
        # 各組數列為 studList[grp]
        eachGrp = studList[grp]
        # 將各組數列放入 random.shuffle() 弄亂次序
        random.shuffle(eachGrp)
        # 將前面 mbrNum *prjNum 個學號納入
        allGrp.append(eachGrp[:mbrNum*prjNum])
        # 至此, 應該已經取得所需要的 allGrp
    print(allGrp)
    for grp in range(prjNum):
        tmpGrp = []
        for i in range(grpNum):
            # 各組待選數列 allGrp[i]
            for j in range(mbrNum):
                # 選到的組員為 allGrp[i][j]
                tmpGrp.append(allGrp[i][j])
        miniGrp.append(tmpGrp)
    print(miniGrp)        
    
    '''
    for prjOrd in range(prjNum):
        #mbrNum = 3
        # prjTitle = cdaw14
        #repoName = "cdbw14-3"
        repoName = prjTitle + "-" + prjOrd
        repoDesp = courseTitle + " " + repoName + " " + prjDesp
        #studList = cdbList

        selStud = []

        # 列出分組 Github Pages 與倉儲連結
        print(webPrefix + repoName)
        print()
        print(repoPrefix + repoName + repoSuffix)
        print()
        # random selection loop
        # i 為分組序號, 使用 for 迴圈逐組 shuffle 後, 按順序取出學號
        for i in range(len(studList)):
            random.shuffle(studList[i])
            print("group:" + str(i+1))
            print()
            # 
            for j in range(mbrNum):
                # 抽選的學號
                stud = studList[i][j]
                print(stud)
                
                # 405 and 407 with s
                #加上 "40723153" 例外判別
                #if (stud != "40723153") and (stud[2] == "5" or stud[2] == "7"):
                if (stud not in nosExcept) and (stud[2] == "5" or stud[2] == "7"):
                    selStud.append("s" + str(stud))
                else:
                    selStud.append(stud)
            print("----")
    '''

"""定義 createRepo 函式, 輸入 tokenPath 與 perm 變數
    tokenPath: 目前 token 位於 './../mdecourse_github_token.txt'
    perm: 目前授予用戶的權限為 'push'
"""
def createRepo(tokenPath, perm):
    # 讀取 github 中與帳號綁定的 token 值
    with open(tokenPath, 'r') as f:
        token = f.read().splitlines()
    #print(token[0])


    # 為抽出的各組組員建立協同倉儲
    # or using an access token
    github = Github(token[0])
    user = github.get_user()
    repo = user.create_repo(name=repoName, description=repoDesp, auto_init=True)

    # 將各組組員設為各分組倉儲的協同者, 具有倉儲推送權限
    # grand selected user permission to push
    for i in selStud:
        repo.add_to_collaborators(i, permission=perm)
        # 讓用戶擁有管理權
        #repo.add_to_collaborators(i, permission='admin')

studList = cdaList
prjTitle = "cd2020"
mbrNum = 3
prjNum = 3
miniProject(studList, prjTitle, mbrNum, prjNum)
