from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '0.0.1'
__author__ = 'Robert Navas'

from flask import Flask
from flask import render_template
from flask import request
from flask import *
from flask import redirect

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def main_function():

    return render_template('index.html')

@app.route('/jobs', methods=['GET', 'POST'])
def number_of_jobs():

    if request.method == 'POST':

        cpu = int(request.form['number'])
        print(cpu)
        return render_template('index.html', message=cpu, int=int())
    else:
        return "Bad Request"

@app.route('/fcfs/<int:message>', methods=['GET', 'POST'])
def fcfs(message):
    values = []
    sjf = []
    newval = []
    sjfval = []
    base = 0
    fcfs_sum = 0
    sjf_sum = 0
    if request.method == 'POST':
        for i in range(int(message)):
            value = int(request.form['job' + str(i)])
            values.append(value)
            sjf.append(value)
            
        for value in values:
            base += int(value)
            newval.append(base)

        for value in sorted(sjf):
            base += int(value)
            sjfval.append(base)
            
        # print(newval)
        return render_template('index.html', fcfs=newval, sjf = sjfval)
    else:
        return "Bad Request"


if __name__ == '__main__':

    app.run(debug=True, port = 5000)


