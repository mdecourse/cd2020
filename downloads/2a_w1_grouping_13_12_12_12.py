# read 2a_w1_grouping_13_12_12_12.txt
# and append student no in group into output list
# all 為已經分組後的全班成員名單
all = []
# output 為各組分割後的輸出數列
output = []
# 已知每組人數
grp_num = [13, 12, 12, 12]
# 將 2a.txt 資料讀出, 轉為數列
# 利用 strip() 去除每一行最後的 \n
with open('read 2a_w1_grouping_13_12_12_12.txt','r') as f: 
    # 逐一讀出學員, 轉入 all 數列 
    for row in f:
        all.append(row.strip())
# 檢查是否正確將檔案轉為數列
#print(all)
# 設計一個增量變數 inc
# 主要用來增量各組人數
grp = 0
inc = 0
for i in grp_num:
    gpList = []
    for j in range(i):
        gpList.append(all[j+inc])
    # 這裡與 c 及 dart 不同, 離開 for loop 時 j 為 i - 1
    # 因此 inc 除了加上 j, 還要加上 1
    inc = inc + j + 1
    grp = grp + 1
    print("group " + str(grp) + " has " + str(i) + "members")
    output.append(gpList)
print(output)
    