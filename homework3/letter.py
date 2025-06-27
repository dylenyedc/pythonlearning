letter=input()
nun=int(input())
print("{}是字母表中第{}个字母.".format(letter,ord(letter)-ord('A')+1))
print("字母表中第{}个字母是{}.".format(nun,chr(ord('A')-1+nun)),end="")