n=int(input())
sentences=[]
static={}
for i in range(0,n):
    a=input()
    sentences.append(a)
#97-122 65-90
def transentence(sentence):
    sentence=sentence.lower()
    result=[]
    for letter in sentence:
        if 'a' <= letter <= 'z':
            result.append(letter)
        else:
            result.append(" ")
    trueresult="".join(result)
    words=trueresult.split()
    return words
for sentence in sentences:
    words=transentence(sentence)
    for word in words:
        if(static.get(word,-1)==-1):
            static[word]=0
        static[word]+=1

for word in sorted(static):
    print(word, static[word])