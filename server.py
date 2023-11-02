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
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
db = SQLAlchemy(app)

class Upload(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   filname = db.Column(db.String(50))
   data = db.Column(db.LargeBinary)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      file = request.files['file']

      upload = Upload(filename = file.filename, data=file.read())
      db.session.add(upload)
      db.session.commit()

      return f'Uploaded: {file.filename}'
   return render_template('input.html')

@app.route('/download/<upload_id>')
def download(upload_id):
    upload = Upload.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=True)


if __name__ == '__main__':
   app.run()


token='cgi4Z9tmdUjP1rfvcjUmABUr4I9WmNb5NpupntBVvJDwJOjYwuW_tesvj1R8OWRDqCufKA.'
bard=Bard(token=token)

#image
image=open(r"C:\pythonProjects\TXsoftware\PPT\good\01.jpg","rb").read()
#image search
info=bard.ask_about_image("이 ppt에 대한 정보를 기술해 줘",image)['content']
print(info)