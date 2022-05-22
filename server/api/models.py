#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import random
import time
import os
from webbrowser import Error
from pymysql import cursors
import pymysql.cursors
import copy

def fixPathName(path, nname):
  name = copy.deepcopy(nname)
  dPath = copy.deepcopy(path)
  nameWith = name
  if((len(dPath) == 1 and dPath[0] == '根目录') or len(dPath) == 0):
    currentPath = os.getcwd() + "\database\ezs"
    dPath = currentPath.split(os.sep)
  else:
    dPath[0] = os.path.abspath(os.sep)

  pathStr = '\\'.join(dPath)

  if(name.endswith(".ez") == False):
    nameWith = name + '.ez'
  else:
    name = os.path.splitext(name)[0]

  if(nname != None and nname.strip() != ""):
    pathStr = os.path.join(pathStr, nameWith)
  
  return dPath, name, nameWith, pathStr
  

def saveArticle(ezJson):
  ez = ezJson['ez']
  name = ezJson['title']
  path = ezJson['path']

  dPath, nname, nnameWith, filePathStr = fixPathName(path, name)

  with open(filePathStr, 'w', encoding = 'utf-8') as file_obj:
    json.dump(ez, file_obj)

def renameArticle(path, oldName, newName):
  oPath, oName, oNameWith, oPathStr = fixPathName(path, oldName)
  nPath, nName, nNameWith, nPathStr = fixPathName(path, newName)
  try:
    os.rename(oPathStr,nPathStr)
    return nName
  except:
    return oName  

def fetchArticle(path, name):
  dPath, nname, nnameWith, filePathStr = fixPathName(path, name)

  with open(os.path.join(filePathStr), 'r', encoding = 'utf-8') as file_obj:
    article = json.load(file_obj)

  return article, None, name

def executeSQL(sql, config):
  connection = pymysql.connect(host=config['host'],
                             user=config['user'],
                             password=config['password'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
  try:
    with connection:
      with connection.cursor() as cursor:
          cursor.execute(sql)
          desc = cursor.description
          fetch_result = cursor.fetchall()
          head = [x[0] for x in desc] 
          rows = list(map(lambda row: [row[col] for col in row], fetch_result))
          rows.insert(0, head)
    return {'result': rows}
  except pymysql.Error as e:
    err = str(e.args[1])
    return {'result':[['错误信息'], [err]]}

def openPath(path):
  dPath, name, nameWith, pathStr = fixPathName(path, "")
  return dPath

def fetchFilelist(path, name):
  dPath, nname, nnameWith, pathStr = fixPathName(path, "")

  filelist = []
  files = os.listdir(pathStr)
  if(name != None):
    name = name.strip()
  else:
    name = ""

  for file in files:
    if os.path.isdir(os.path.join(pathStr, file)):
      filelist.append({'filename': str(file), 'type':'folder'})
    

  if(name == ""):
    for file in files:
      if(file.endswith(".ez")):
        filelist.append({'filename': os.path.splitext(file)[0], 'type':'file'})
  else:
    for file in files:
      if(file.endswith(".ez") and os.path.splitext(file)[0].find(name) != -1):
        filelist.append({'filename': os.path.splitext(file)[0], 'type':'file'})

  return filelist

def createEz(path):
  if(path[0] == '根目录'):
    path[0] = os.path.abspath(os.sep)
  pathStr = '\\'.join(path)
  filePathStr = os.path.join(pathStr, "新建笔记")
  filneName = "新建笔记"
  i=0
  while i < 10000:
    if i == 0:
      if(os.path.isfile(filePathStr+".ez")):
        i+=1
        continue
      else:
        break
    else:
      if(os.path.isfile(filePathStr+str(i)+".ez")):
        i+=1
        continue
      else:
        filePathStr = filePathStr + str(i)
        filneName = filneName+str(i)
        break
  
  filePathStr = filePathStr + ".ez"

  ez = {
    "editor":{
      "id":"editor",
      "parentID":"root",
      "name":"BaseEditor",
      "data":{
      },
      "children":["default_block"]
      },
    "default_block":{
      "id":"default_block",
      "parentID":"editor",
      "name":"BaseBlock",
      "data":{
      },
      "children":["default_text"]
      },
    "default_text":{
      "id":"default_text",
      "parentID":"default_block",
      "name":"BaseText",
      "text":"",
      "data":{
        "style":{}
      },
    },
  }

  with open(filePathStr, 'w', encoding = 'utf-8') as file_obj:
    json.dump(ez, file_obj)

  return ez, None, filneName



# abandon
def fetchArticles(name=''):
  articles = getFileIndex(name)

  return articles

def getFileIndex(name=''):
  fileIndex = {}
  with open("./database/ezs/_fileindex.json", 'r', encoding = 'utf-8') as file_obj:
    fileIndex = json.load(file_obj)

  if(name.lstrip() == ''):  
    return fileIndex
  else:
    filterObj = {}
    for key in fileIndex:
      n = fileIndex[key]
      if name in n:
        filterObj[key] = n
    return filterObj

def saveFileIndex(fileIndex):
  with open("./database/ezs/_fileindex.json", 'w', encoding = 'utf-8') as file_obj:
    json.dump(fileIndex, file_obj)

def newArticle():
  fileIndex = getFileIndex()
  article_id = time.strftime('%Y%m%d%H%M%S') + '_' + str(random.randint(0,1000))

  article_file = article_id + ".ez"
  article_path = os.path.join("./database/ezs", article_file)

  ez = {
    "editor":{
      "id":"editor",
      "parentID":"root",
      "name":"BaseEditor",
      "data":{
      },
      "children":["default_block"]
      },
    "default_block":{
      "id":"default_block",
      "parentID":"editor",
      "name":"BaseBlock",
      "data":{
      },
      "children":["default_text"]
      },
    "default_text":{
      "id":"default_text",
      "parentID":"default_block",
      "name":"BaseText",
      "text":"",
      "data":{
        "style":{}
      },
    },
  }

  with open(article_path, 'w', encoding = 'utf-8') as file_obj:
    json.dump(ez, file_obj)

  fileIndex[article_id] = "标题"
  saveFileIndex(fileIndex)

  return ez,article_id,"标题"