import sys, csv
hakka_lines = sys.stdin #教育部《臺灣客家語常用詞辭典》內容資料(1110429).xlsx - records.tsv 
csvreader = csv.reader(hakka_lines, delimiter="\t")
headers = next(csvreader)

from ArticutAPI_Taigi import ArticutTG
username = apikey = ""
articutTaigi = ArticutTG(username, apikey)

import re
tp = fn = 0
#for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in csvreader:
for 系統編號,詞目,詞性,詞目索引分類,四縣腔音讀,海陸腔音讀,大埔腔音讀,饒平腔音讀,詔安腔音讀,南四縣腔音讀,釋義,近義詞,反義詞,對應國語,大埔腔相關字詞,大埔腔相關字詞音讀,饒平腔相關字詞,饒平腔相關字詞音讀,詔安腔相關字詞,詔安腔相關字詞音讀,南四縣相關字詞,南四縣相關字詞音讀 in csvreader:
    try:
        example = 釋義.split("例")[1][1:]
        hakka_example_sent, Chinese_example_sent = example.split("（")[:2]
        Chinese_example_sent = Chinese_example_sent.split("）")[0]

        inputSTR = hakka_example_sent
        resultDICT = articutTaigi.parse(inputSTR=inputSTR, level="lv1", convert="TL")
        if 詞目 in resultDICT['result_segmentation']:
            print("O", end="\t")
            tp += 1
        else:
            print("X", end="\t")
            fn += 1
        print(詞性, 詞目, 系統編號, Chinese_example_sent, resultDICT['result_segmentation'])
    except: pass
recall = tp / (tp + fn)
print(f"recall = tp / (tp + fn) = {tp} / ({tp} + {fn}) = {recall}")
