from flask import Flask, request, render_template, redirect, url_for
from bs4 import BeautifulSoup
import requests
import urllib.parse
from urllib.parse import urljoin
import controller
import json
import html
import model

app = Flask(__name__)


@app.route('/',  methods=['GET','POST'])
def home():
    
    try:
        url = request.form['url']
        result = controller.main(url)
        output = result
    except:
        output = 'NA'

    return render_template('index.html', output=output)


@app.route('/preview', methods=['POST'])
def preview():
    try:
        url = request.form.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for link in soup.find_all('link'):
            if link.get('href'):
                link['href'] = urljoin(url, link['href'])
        
        for img in soup.find_all('img'):
            if img.get('src'):
                img['src'] = urljoin(url, img['src'])

        return render_template('preview.html', content=soup.prettify())
    except Exception as e:
        return  f"Error: {e}"


@app.route('/source-code', methods=['GET','POST'])
def view_source_code():

    try:
        url = request.form.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        formatted_html = soup.prettify()
        
        return render_template('source_code.html', formatted_html = formatted_html, url = url)
    
    except Exception as e:
        return  f"Error: {e}"


@app.route('/about', methods=['GET'])
def about():
    return render_template('dev.html')


if __name__ == '__main__':
    app.run(debug=True)
