from flask import Flask, render_template, request
from os.path import join,relpath
from glob import glob
import takePhoto as tp
import useServo as us
app = Flask(__name__)


@app.route('/')
def hello():
    name = "Guest"
    # return name
    return render_template('hello.html', title='flask test', name=name)

@app.route('/photo', methods=['POST'])
def photo():
    tp.take_photo()
    name="Guest"
    title="photo_test"
    path = "./static/img"
    image_names = [relpath(x,path) for x in glob(join(path,'*.jpg'))]
    my_list = []
    for image in image_names:
        my_dic = {}
        my_dic['image_name'] = "static/img/" + image
        my_list.append(my_dic)
    return render_template('photo.html',title=title,name=name,message=my_list)


if __name__ == "__main__":
    app.run(host='192.168.100.201', debug=True)
