#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import webbrowser
import json
from server.api.models import saveArticle, fetchArticles, fetchArticle, newArticle, executeSQL, serverDirectory
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
  articles = fetchArticles('')
  context = {'articles':articles, 'searchName': ''}
  return render_template('index.html', **context)

@app.route('/<name>')
def indexName(name):
  articles = fetchArticles(name)
  context = {'articles':articles, 'searchName': name}
  return render_template('index.html', **context)

@app.route('/newArticle')
def indexNewArticle():
  article, id, title = newArticle()
  return redirect(url_for('indexArticle', id=id))

@app.route('/article/<id>')
def indexArticle(id):
  serverDirectory()
  articles = fetchArticles()
  context = {'articles':articles, 'id': id}
  return render_template('index.html', **context)

@app.route('/save_ez', methods=["POST"])
def saveEz():
  data = request.get_data()
  json_data = json.loads(data.decode("utf-8"))
  saveArticle(json_data)
  return {}

@app.route('/fetch_article', methods=["GET"])
def ajaxFetchArticle():
  id = request.args.get('id')
  ez, id, title = fetchArticle(id)

  return {'ez': ez, 'id': id, 'title': title}

@app.route('/sql', methods=["GET","POST"])
def ajaxSQL():
  data = request.get_data()
  json_data = json.loads(data.decode("utf-8"))
  sql = json_data['sql']
  config = json_data['config']
  result = executeSQL(sql, config)

  return result

if __name__ == '__main__':
  # webbrowser.open('http://127.0.0.1:5000/', 0, autoraise=False)
  app.run(debug=True)
