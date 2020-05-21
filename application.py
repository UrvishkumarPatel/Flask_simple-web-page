
# Copyright 2013. Amazon Web Services, Inc. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.






#################################################################

# Most of the code is from https://github.com/aws-samples/eb-py-flask-signup


import os
import sys
import json
import config
import csv
import flask
from flask import request, Response

# Create the Flask app
application = flask.Flask(__name__)

# Load config values specified above
application.config.from_object(config)

# Only enable Flask debugging if an env var is set to true
application.debug = application.config['FLASK_DEBUG'] in ['true', 'True']


@application.route('/')
def welcome():
    theme = application.config['THEME']
    return flask.render_template('index.html', theme=theme, flask_debug=application.debug)


@application.route('/signup', methods=['POST'])
def signup():
    signup_data = dict()
    for item in request.form:
        signup_data[item] = request.form[item]
    print(signup_data)

    # signup_data is a dictionary 
    # add your code here to process the data


    path = os.getcwd()
    filename= 'data.csv'
    myFile = open(filename, 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(myFile, quotechar='"', quoting=csv.QUOTE_ALL)
    csv_writer.writerow([str(s) for s in signup_data.keys()])
    csv_writer.writerow([str(s) for s in list(signup_data.values())])
    myFile.close()
    file = filename

    print ('find your file here:    '+path+'\\'+file)
    return Response(json.dumps(signup_data), status=201, mimetype='application/json')


if __name__=='__main__':
    application.run()