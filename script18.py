from flask import Flask, render_template

app = Flask(__name__)

# 1. Trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# 2. Kho từ vựng tổng hợp
@app.route('/vocab')
def vocab():
    return render_template('vocab.html')

# 3. Trang bài học số 1 mới thêm
@app.route('/lesson-sc1')
def lesson_sc1():
    return render_template('lesson_sc1.html')

# 4. Khối chạy server luôn nằm dưới cùng của file và viết sát lề trái
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)