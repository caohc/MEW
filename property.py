import nltk

line = 'Plants need things to grow healthy and strong'
tokens = nltk.word_tokenize(line)

pos_tags = nltk.pos_tag(tokens)
l=len(pos_tags)

N_total=0
N_noun=0
N_verb=0
N_preposition=0

for i in range(0,l):
  N_total+=1
  if pos_tags[i][1]=="IN" or pos_tags[i][1]=="TO":
     N_preposition+=1
  elif pos_tags[i][1]=="NN" or pos_tags[i][1]=="NNS" or pos_tags[i][1]=="NNP" or pos_tags[i][1]=="NNPS":
     N_noun+=1
  elif pos_tags[i][1]=="VB" or pos_tags[i][1]=="VBD" or pos_tags[i][1]=="VBG" or pos_tags[i][1]=="VBN" or pos_tags[i][1]=="VBP" or pos_tags[i][1]=="VBZ":
     N_verb+=1
    
print(N_total, N_preposition, N_noun, N_verb)

#for word,pos in pos_tags:
#  if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
#     print(word,pos)


