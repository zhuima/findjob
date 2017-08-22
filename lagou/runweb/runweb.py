#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from collections import Counter
from os import sys
from os import path
sys.path.append(path.dirname(path.dirname( path.abspath(__file__))))
import db
import utils


app = Flask(__name__)
configweb = utils.get_config('web')
configdb = utils.get_config('common')
cursor = db.Cursor(configdb)


@app.route('/jobstocity')
def jobstocity():
    output = [
        'positionId', 'positionName', 'city', 'createTime', 'salary', 'companyId', 'companyName', 'companyFullName', 'minsalary', 'munsalary', 'maxsalary'
    ]
    result = cursor.get_results('jobinfo', output)
    city_list = [item.values()[1] for item in result]
    city_dict = Counter(city_list)

    return render_template('jobstocity.html', jobstocity=city_dict)


@app.route('/jobstomoney')
def jobstomoney():
    output = [
        'positionId', 'positionName', 'city', 'createTime', 'salary', 'companyId', 'companyName', 'companyFullName', 'minsalary', 'munsalary', 'maxsalary'
    ]
    result = cursor.get_results('jobinfo', output)
    money_list = [item.values()[4] for item in result]
    money_dict = Counter(money_list)
    _money_dict = [{'value': v, 'name': k.encode("utf-8")}for k, v in money_dict.items()]

    return render_template('jobstomoney.html', jobstomoney_dict=_money_dict, jobstomoney_list=money_list)


if __name__ == '__main__':
    app.run(host=configweb.get('bind', '0.0.0.0'), port=int(configweb.get('port', 8000)), debug=True)
