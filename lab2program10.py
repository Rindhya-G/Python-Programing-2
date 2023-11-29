def rem_dup(sen1,sen2):
  com=[]
  sen1=list(sentence1.split())
  sen2=list(sentence2.split())
  for i in sen1:
    if i in sen2:
      sen1.remove(i)
      sen2.remove(i)
  print(*sen1)
  print(*sen2)
sentence1 = "sky is blue in color"
sentence2 = "raj likes sky blue color"
rem_dup(sentence1,sentence2)
            
