with open("fileop/AddLineNo.py", "rt") as f:                                                           # 1
    lines = f.readlines()                                                                              # 2
#杨悦20245007                                                                                           # 3
maxLength=len(max(lines,key=len))                                                                      # 4
                                                                                                       # 5
newLines = [line.rstrip() .ljust(maxLength) +" # " + str(i+1) + "\n" for i, line in enumerate(lines)]  # 6
                                                                                                       # 7
with open("fileop/AddLineNo2.py", "w") as f:                                                           # 8
    f.writelines(newLines)                                                                             # 9
