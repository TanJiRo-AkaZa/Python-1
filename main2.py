dict_test={"a":1,"b":2,"c":2,"d":2,"e":2}
print("the original dictionary is:" + str(dict_test))
K=2
res=0
for key in dict_test:
    if dict_test[key]==K:
        res=res+1
print("the frequency of",K,"is:",res)