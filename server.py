# from bardapi import Bard

# token='cgi4Z9tmdUjP1rfvcjUmABUr4I9WmNb5NpupntBVvJDwJOjYwuW_tesvj1R8OWRDqCufKA.'
# bard=Bard(token=token)

# #image
# image=open(Users/parkjunhyoung/Downloads/christian-VRbtz7PD40M-unsplash.jpg","rb").read()
# #image search
# im=bard.ask_about_image("how about this image?",image)['content']
# print(im)
from io import BytesIO
from bardapi import Bard
from flask import Flask, render_template,request, flash, redirect
from werkzeug.utils import secure_filename
import os
import time
app = Flask(__name__)

token='cwi4ZyN8maSsllIn9ZWOsG89nCVV56g17dg9NZ4jQ8gdFIhRaMvy_XA0tbiMJdL1euA9aA.'
bard=Bard(token=token)
UPLOAD_FOLDER="static/img/upload/"
app.secret_key="sada_gbshs_designdoctor"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
print('2')
num=0

# class Upload(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    filname = db.Column(db.String(50))
#    data = db.Column(db.LargeBinary)

@app.route('/uploader',methods=['GET','POST'])
def uploader():
      if request.method=="POST":
         print('3')
         if 'file' not in request.files:
               flash('No file part')
               return redirect(request.url)
         print('4')
         file=request.files['file']
         if file.filename=='':
               flash('No image selected')
               return redirect(request.url)
         else:
               print('5')
               filename=secure_filename(file.filename)
               file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
               image=open(os.path.join(app.config['UPLOAD_FOLDER'],filename),"rb").read()
               return render_template("index.html",file=filename)
      else:
             #문제 있음
            pass
@app.route('/')
def index():
       # if request.method == 'POST':
   #    file = request.files['file']

   #    upload = Upload(filename = file.filename, data=file.read())
   #    db.session.add(upload)
   #    db.session.commit()

   #    return f'Uploaded: {file.filename}'
   print("1")
   return render_template('index.html',filename="hello")

# @app.route('/download/<upload_id>')
# def download(upload_id):
#     upload = Upload.query.filter_by(id=upload_id).first()
#     return send_file(BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=True)


if __name__ == '__main__':
   app.run()

def barding(image):
   print('bard')
   return bard.ask_about_image("이 ppt에 대해서 분석하고 더 고칠만한 점을 알려줘",image)['content']