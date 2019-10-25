
import re


with open("tweets.csv", "w", encoding="utf-8") as result:
    with open("stockerbot-export.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        res_lines = []
        for line in lines:
            if ",http" in line:
                line = line[:20] + line[20:].replace(",http", ',"http')\
                    .replace(",True",'",True')\
                    .replace(",False",'",False')
            res_lines.append(line)
        result.writelines(res_lines)

# try:
#     f = open("stockerbot-export.csv", "r", encoding="utf-8")
# except:
#     pass
# finally:
#     f.close()
