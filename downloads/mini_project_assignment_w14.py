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
    # allGrp 為各組數列弄亂後, 取前 9 名學員所組成的大數列
    #print(allGrp)
    # 預計分成幾組專案迴圈
    for grp in range(prjNum):
        # 完成各專案組抽選人員之暫存數列
        tmpGrp = []
        # 每班各分幾組之組數迴圈
        for i in range(grpNum):
            # 各組待選數列 allGrp[i]
            #  每組抽出幾人迴圈
            for j in range(mbrNum):
                # 選到的組員為 allGrp[i][j]
                tmpGrp.append(allGrp[i][j + grp*mbrNum])
        miniGrp.append(tmpGrp)
    # miniGrp 則由 allGrp 中, 以
    #print(miniGrp)      
    return miniGrp    

# 根據已經完成的分組數列, 執行後續資料列印與倉儲新增設定
def finalStep(courseTitle, prjTitle, tokenPath, prjDesp, webPrefix, repoPrefix, repoSuffix, nosExcept, perm, miniGrp):
    #courseTitle = "cd2020"
    #prjTitle = "cdaw14"
    #repoName = "cdbw14-3"
    #tokenPath =  './../mdecourse_github_token.txt'
    #prjDesp = "mini project"
    #webPrefix = "http://mde.tw/"
    #repoPrefix = "https://github.com/mdecourse/"
    #repoSuffix = ".git"
    #nosExcept = ["40723153"]
    #perm = "push"
    with open(tokenPath, 'r') as f:
        token = f.read().splitlines()
        # 確認取得 token
        print("以下為 token:")
        print(token[0])
    github = Github(token[0])
    user = github.get_user()
    for i in range(len(miniGrp)):
        repoName = prjTitle + "-" + str(i+1)
        repoDesp = courseTitle + " " + repoName + " " + prjDesp
        subGrp = miniGrp[i]
        # 為抽出的各組組員建立協同倉儲
        # 測試時蓋掉 1/2
        #repo = user.create_repo(name=repoName, description=repoDesp, auto_init=True)
        print("根據 " + repoName + ", " + repoDesp + " 建立倉儲")
        print("第 " + str(i+1) + "組:")
        print()
        # 列出分組網站連結
        print(webPrefix + repoName)
        print()
        # 列出分組倉儲連結
        print(repoPrefix + repoName + repoSuffix)
        print()
        for j in range(len(miniGrp[i])):
            studNum = miniGrp[i][j]
            # 列出各組員學號 
            print(str(studNum))
            if (studNum not in nosExcept) and (studNum[2] == "5" or studNum[2] == "7"):
                studAccount = "s" + str(studNum)
            else:
                studAccount = str(studNum)
            # 依據學員 github 帳號, 設定權限
            # 測試時關閉 2/2
            #repo.add_to_collaborators(studAccount, permission=perm)
            #print("根據 " + studAccount + " 以及 permission: "+ perm + " 加為協同者")
        print()
            
 
 # -------------------------------------
# 專案名稱
prjTitle = "cdaw14"
# 選擇班級分組數列            
studList = cdaList
# 每組選出 3 人組成 mini project
mbrNum = 3
# 共組成 3 組 mini projects
prjNum = 3
# -------------------------------------
# 課程名稱
courseTitle = "cd2020"
# token 路徑
tokenPath =  './../mdecourse_github_token.txt'
# 專案說明
prjDesp = "mini project"
# 網站前綴
webPrefix = "http://mde.tw/"
# 倉儲前綴
repoPrefix = "https://github.com/mdecourse/"
# 倉儲後綴
repoSuffix = ".git"
# 帳號不以 s 開頭的例外學號數列
nosExcept = ["40723153"]
# 倉儲允許使用者 push
perm = "push"
# 呼叫 miniProject 進行分組, 完成後傳回分組人員數列
miniGrp = miniProject(studList, prjTitle, mbrNum, prjNum)
print(miniGrp)
# 準備根據分組結果, 進行資料列印與倉儲新增及設定
finalStep(courseTitle, prjTitle, tokenPath, prjDesp, webPrefix, repoPrefix, repoSuffix, nosExcept, perm, miniGrp)

