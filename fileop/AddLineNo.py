with open("fileop/AddLineNo.py", "rt") as f:
    lines = f.readlines()
#杨悦20245007
maxLength=len(max(lines,key=len))

newLines = [line.rstrip() .ljust(maxLength) +" # " + str(i+1) + "\n" for i, line in enumerate(lines)]

with open("fileop/AddLineNo2.py", "w") as f:
    f.writelines(newLines)