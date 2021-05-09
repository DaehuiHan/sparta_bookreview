from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
# FIXME: POST 1.서버는 title, author, review를 받아야 한다.
@app.route('/review', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # FIXME: POST 2. db에 저장해주는 작업을 해준다.
    doc = {
        'title':title_receive,
        'author':author_receive,
        'review':review_receive
    }

    db.bookreview.insert_one(doc)

    # FIXME: POST 3. 이게 완료되면 어떤 동작을 해줄지 return에 적어준다.
    return jsonify({'msg': '저장 완료!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
