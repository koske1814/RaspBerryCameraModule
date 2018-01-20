from flask import Flask, render_template, request  # 追加

app = Flask(__name__)


@app.route('/')
def hello():
    name = "Hoge"
    # return name
    return render_template('hello.html', title='flask test', name=name) #変更

@app.route('/photo',methods=['GET'])
def photo():
    val = request.args.get("msg","Not defined")
    return 'Hello World' + val

# おまじない
if __name__ == "__main__":
    app.run(debug=True)
