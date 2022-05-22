#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import webbrowser
import json
from server.api.models import saveArticle, fetchArticle, executeSQL, openPath, fetchFilelist, createEz, renameArticle
from flask import Flask, render_template, request, redirect, url_for

app = Flask(
      import_name = __name__,
      static_folder = '/',
      static_url_path = '/static',
      template_folder = './'
    )
app.jinja_env.variable_start_string = '<<'
app.jinja_env.variable_end_string = '>>'

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/save_ez', methods=["POST"])
def saveEz():
  data = request.get_data()
  json_data = json.loads(data.decode("utf-8"))
  saveArticle(json_data)
  return {}

@app.route('/rename_ez', methods=["POST"])
def ajaxRenameEz():
  data = request.get_data()
  json_data = json.loads(data.decode("utf-8"))
  newName = renameArticle(json_data['path'], json_data['oldName'], json_data['newName'])
  return {'name':newName}

@app.route('/fetch_article', methods=["POST"])
def ajaxFetchArticle():
  json_data = json.loads(request.get_data().decode("utf-8"))
  ez, id, title = fetchArticle(json_data['path'], json_data['name'])
  return {'ez': ez, 'id': id, 'title': title}

@app.route('/sql', methods=["GET","POST"])
def ajaxSQL():
  data = request.get_data()
  json_data = json.loads(data.decode("utf-8"))
  sql = json_data['sql']
  config = json_data['config']
  result = executeSQL(sql, config)

  return result

@app.route('/openpath', methods=["POST"])
def ajaxOpenPath():
  data = request.get_data()
  json_data = json.loads(data.decode("utf-8"))
  path = openPath(json_data['path'])
  filelist = fetchFilelist(json_data['path'], "")
  return {'filelist': filelist, 'path':path}

@app.route('/create_ez', methods=["POST"])
def ajaxCreateEz():
  data = request.get_data()
  json_data = json.loads(data.decode("utf-8"))
  path = openPath(json_data['path'])
  ez, id, title = createEz(path)

  return {'ez': ez, 'id': None, 'title': title}

@app.route('/filelist', methods=["POST"])
def ajaxFilelist():
  data = request.get_data()
  json_data = json.loads(data.decode("utf-8"))
  filelist = fetchFilelist(json_data['path'], json_data['searchName'])
  return {'filelist': filelist}


if __name__ == '__main__':
  webbrowser.open('http://127.0.0.1:5000/', 0, autoraise=False)
  app.run(debug=False)
