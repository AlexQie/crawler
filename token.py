#-*-coding:utf-8-*-
import re
import os
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

dirs = os.listdir('/home/jy/src/python/stemming/ori_text/')
for f in dirs:
  query = open('/home/jy/src/python/stemming/ori_text/'+f,'r').read()
#query = open("2-Detective: \'Hero\' cop sought hit-man to cover up thefts - Yahoo News.txt","r").read()
  query1 = str.lower(query)
  query01 = query1.replace('\n',' ')
  query10 = query01.replace('.',' ')
  query11 = query10.replace(',',' ')
  query2 = query11.split()
  swords = open('stopword.txt','r').read()
  stopwords = swords.split()
  temp = open("temp.txt","w")
  qry=''

  for i in query2:
     if i in stopwords:
        continue
     m = re.search("\d+",i)
     n = re.search("\W+",i)
     if not m and not n:
        temp.write(i+"\n")
        qry=qry+' '+i       



  def is_noun(tag):
      return tag in ['NN', 'NNS', 'NNP', 'NNPS']

  def is_verb(tag):
      return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

  def is_adverb(tag):
      return tag in ['RB', 'RBR', 'RBS']

  def is_adjective(tag):
      return tag in ['JJ', 'JJR', 'JJS']

  def penn_to_wn(tag):
      if is_adjective(tag):
          return wn.ADJ
      elif is_noun(tag):
          return wn.NOUN
      elif is_adverb(tag):
          return wn.ADV
      elif is_verb(tag):
          return wn.VERB
      return wn.NOUN

  changed = ''
  tags = nltk.pos_tag(word_tokenize(qry))
  for tag in tags:
     wn_tag = penn_to_wn(tag[1])
     changed = changed + ' '+ WordNetLemmatizer().lemmatize(tag[0],wn_tag)
     
  dictionary ={}
  changed1 = changed.split()
  resltname = '/home/jy/src/python/stemming/classed_text/'+'_'+f
  result = open(resltname,"w")
  fdist = nltk.FreqDist(changed1)

  for localkey in fdist.keys():
     #localkey = 
     dictionary[localkey] = fdist[localkey]
  result.write(str(sorted(dictionary.items(), key = lambda x:x[1] ,reverse = True)))

