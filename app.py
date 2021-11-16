from flask import Flask,redirect,jsonify, render_template, request
import sys,os,json
import pandas as pd
app = Flask(__name__)
path='../wis-advanced-python-2021-2022/students'
@app.route("/")
def main():
 return '''
     <form action="/all" method="POST">
         <input name="text">
         <input type="submit" value="Search">
     </form>
     '''

@app.route("/all", methods=['POST'])
def all():
 name=request.form['text']
 return(list_pepole_sorted(path,name))
 
@app.route("/all/<username>")
def user(username):
 return (personal_details(path,username))


def list_pepole_sorted(path,name):
 students_page=""" """
 path_to_json=path
 name_list=[]
 json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

 for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        for i in json_text :     
         if json_text[i] is None:
           continue
         elif (name in json_text[i]):
            name_list.append(json_text['name'])
            break

 name_list.sort()

 
 for student in name_list:
        # get the details
       
        # create automatic redirection to flask web page 
            link="/all/"+student
            students_page += f'<li><a href="{link}">{student}</a></li></ul></div>'
 return students_page
 
def personal_details(path,username):
#function to redirect username link to his personal details information from his json file
 students_details=""" """
 path_to_json=path
 json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
 for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        if json_text['name']==username :
         for i in json_text :
          students_details +=f'<li>{i} : {json_text[i]}</li></ul></div>'
 return students_details
        



