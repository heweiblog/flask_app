#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template
app = Flask(__name__)

name = '最新国内动漫'

movies = [
	{'title': '秦时明月', 'year': '1988'},
	{'title': '斗罗大陆', 'year': '1989'},
	{'title': '武庚纪', 'year': '1993'},
	{'title': '天行九歌', 'year': '1994'},
	{'title': '墓王之王', 'year': '1996'},
	{'title': '超神学院', 'year': '1996'},
	{'title': '星辰变', 'year': '1999'},
	{'title': '斗破苍穹', 'year': '1999'},
	{'title': '地灵曲', 'year': '2008'},
	{'title': '少年锦衣卫', 'year': '2012'},
]

@app.route('/')
def index():
	return render_template('index.html', name=name, movies=movies)

if __name__ == '__main__':
	app.run(host='192.168.5.41',port=18080,debug=True)
