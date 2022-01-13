
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from datetime import datetime
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import numpy as np
from PIL import Image
import os

model = tf.keras.models.load_model('static/model/first_training_data.h5')
print("model roaded")
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.i0lgb.mongodb.net/test')
db = client.dbprojects


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/result/recommend', methods=['GET'])
def result_recommend():
    # 이미지이기에, rescale 및 size 조정을 위해 ImageDataGenerator 활용
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_dir = 'static/img/'

    test_generator = test_datagen.flow_from_directory(  # test_dir에 폴더별로 저장을 해야함
        test_dir,
        target_size=(48, 48),
        shuffle=False,
        class_mode='categorical'
    )

    pred = model.predict(test_generator)[0].tolist()  # numpyarray를 list로 변환
    # 마지막으로 업로드한 사진에 대한 판별결과를 보여줌
    pred_sorted = []
    for idx, val in enumerate(pred):
        pred_sorted.append((idx, val))  # 인덱스번호 부여
    pred_sorted.sort(reverse=True, key=lambda x: x[1])  # 원래의 값을 기준으로 내림차순 정렬

    result = []
    fir_data = db.users.find_one({pred_sorted[0][0]})  # 1번째로 높은 값 가져오기
    result.append(fir_data)

    sec_data = db.users.find_one({pred_sorted[1][0]})  # 2번째로 높은 감정의 값들 가져오기
    result.append(sec_data)

    thd_data = db.users.find_one({pred_sorted[2][0]})  # 3번째로 높은 감정의 값들 가져오기
    result.append(thd_data)

    return result


@app.route('result/second')
def result_second():
    return render_template('second.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)



