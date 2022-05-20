#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import random
import time
import os
from webbrowser import Error
from pymysql import cursors
import pymysql.cursors


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


def saveArticle(ezJson):
  ez = ezJson['ez']
  article_id = ezJson['id']
  article_file = article_id + ".ez"
  article_path = os.path.join("./database/ezs", article_file)
  with open(article_path, 'w', encoding = 'utf-8') as file_obj:
    json.dump(ez, file_obj)

  fileIndex = getFileIndex()
  fileIndex[article_id] = ezJson['title'] 
  saveFileIndex(fileIndex)

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
  

def fetchArticles(name=''):
  articles = getFileIndex(name)

  return articles

def fetchArticle(id):
  idWithType = id
  if(id.endswith(".ez") == False):
    idWithType = id + '.ez'


  with open(os.path.join("./database/ezs", idWithType), 'r', encoding = 'utf-8') as file_obj:
    article = json.load(file_obj)

  return article, id, getFileIndex()[id]

def executeSQL(sql, config):
  connection = pymysql.connect(host=config['host'],
                             user=config['user'],
                             password=config['password'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
  try:
    with connection:
      with connection.cursor() as cursor:
          # Create a new record
          cursor.execute(sql)
      # connection.commit()
          desc = cursor.description
          fetch_result = cursor.fetchall()
          head = [x[0] for x in desc] 
          rows = list(map(lambda row: [row[col] for col in row], fetch_result))
          rows.insert(0, head)
    return {'result': rows}
  except pymysql.Error as e:
    err = str(e.args[1])
    return {'result':[['错误信息'], [err]]}

def serverDirectory():
  print(os.path.abspath(os.sep))