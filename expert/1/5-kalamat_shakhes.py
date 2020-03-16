
def shakhes(word):
    if word[0].isupper():
        return True
    else:
        return False

def dot_virgool(ls,word):
    tool = len(word)
    if shakhes(word)==True and (word[-1]=="." or word[-1]==","):
        return word[: tool-1]
    else: return word

jomle = str(input())
jomle_list = jomle.split()
list_word=list()
length = len(jomle_list)

for i in range(0,length):
    if jomle_list[i][0].isupper() and jomle_list[i]!= jomle_list[0] and jomle_list[i-1][-1]!=".":
        list_word.append(i+1)
        list_word.append(dot_virgool(jomle_list,jomle_list[i]))

if len(list_word) == 0:
    print(None)

tool = len(list_word)
for i in range(0,tool//2):
    print("%i:%s"%(list_word[(2*i)],list_word[(2*i)+1]))
