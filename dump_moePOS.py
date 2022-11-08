import sys, csv
hakka_lines = sys.stdin #教育部《臺灣客家語常用詞辭典》內容資料(1110429).xlsx - records.tsv 
csvreader = csv.reader(hakka_lines, delimiter="\t")
headers = next(csvreader)

targetPOSs = sys.argv[1:]
POSlist = []
#for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in csvreader:
for 系統編號,詞目,詞性,詞目索引分類,四縣腔音讀,海陸腔音讀,大埔腔音讀,饒平腔音讀,詔安腔音讀,南四縣腔音讀,釋義,近義詞,反義詞,對應國語,大埔腔相關字詞,大埔腔相關字詞音讀,饒平腔相關字詞,饒平腔相關字詞音讀,詔安腔相關字詞,詔安腔相關字詞音讀,南四縣相關字詞,南四縣相關字詞音讀 in csvreader:
    if 詞性 in targetPOSs:
        print(詞性, 系統編號, 詞目, 釋義)
        POSlist.append(詞目)
print(sorted(POSlist))

moe2articutPOS = {
        "名":"ENTITY",
        "熟":"IDIOM",
        "時":"TIME",
        "形":"MODIFIER",
        "副":"MODIFIER",
        "動":"ACTION",
        }

import json
targetPOS = targetPOSs[0]
articutPOS = moe2articutPOS[targetPOS]
fp = open(file="moe_dict/"+articutPOS+".json", mode="w")
json.dump(obj=POSlist, fp=fp, ensure_ascii=False)
