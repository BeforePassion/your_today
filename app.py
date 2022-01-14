from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from datetime import datetime
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import certifi
import numpy as np
from PIL import Image
import os




#model = tf.keras.models.load_model('static/model/first_training_data.h5')
#print("model roaded")




app = Flask(__name__)

from pymongo import MongoClient



from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.i0lgb.mongodb.net/test')
db = client.dbprojects


#SY db 테스트용
client = MongoClient('mongodb+srv://test:sparta@cluster0.g1cco.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsidepj


import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://music.bugs.co.kr/musicpd/albumview/39691',headers=headers) # 기쁠 때
data2 = requests.get('https://music.bugs.co.kr/musicpd/albumview/50746',headers=headers) # 화날 때
data3 = requests.get('https://music.bugs.co.kr/musicpd/albumview/50519',headers=headers) # 짜증날 때
data4 = requests.get('https://music.bugs.co.kr/musicpd/albumview/41409',headers=headers) # 무서울 때
data5 = requests.get('https://music.bugs.co.kr/musicpd/albumview/50793',headers=headers) # 무표정일 때
data6 = requests.get('https://music.bugs.co.kr/musicpd/albumview/50839',headers=headers) # 슬플 때
data7 = requests.get('https://music.bugs.co.kr/musicpd/albumview/44402?wl_ref=list_mab_01',headers=headers) # 놀랄 때


check = list(db.userinfo.find({'feeling_num':0},{'_id':False}))
if len(check) == 0:
    soup_happiness = BeautifulSoup(data.text, 'html.parser')
    soup_angry = BeautifulSoup(data2.text, 'html.parser')
    song_disgust = BeautifulSoup(data3.text, 'html.parser')
    song_fear = BeautifulSoup(data4.text, 'html.parser')
    song_neutral = BeautifulSoup(data5.text, 'html.parser')
    song_sad = BeautifulSoup(data6.text, 'html.parser')
    song_surprise = BeautifulSoup(data7.text, 'html.parser')


    # 데이터
    emotion_musics = [soup_happiness.select('#ESALBUM39691 > table > tbody > tr'),
                      soup_angry.select('#ESALBUM50746 > table > tbody > tr'),
                      song_fear.select('#ESALBUM50519 > table > tbody > tr'),
                      song_fear.select('#ESALBUM41409 > table > tbody > tr'),
                      song_neutral.select('#ESALBUM50793 > table > tbody > tr'),
                      song_sad.select('#ESALBUM50839 > table > tbody > tr'),
                      song_surprise.select('#ESALBUM44402 > table > tbody > tr'),
                      ]

    color = ['yellow', 'red', 'pink', 'black', 'gray', 'purple', 'blue']
    for idx, emotion in enumerate(emotion_musics):  # emotion == happiness // detail_song == song_happiness
        img_list = []
        title_list = []
        singer_list = []

        for detail_song in emotion:
            img = detail_song.select_one('td > a > img')['src']
            title = detail_song.select_one('th > p > a').text
            singer = detail_song.select_one('td > p > a').text

            img_list.append(img)
            title_list.append(title)
            singer_list.append(singer)

        db.feeling_data.insert_one({
            'feeing_num': idx,
            'color': color[idx],
            'img': img_list,
            'title': title_list,
            'singer': singer_list,
            # 'chicken': chicken
            #'movie' : movie
        })
        #print("db넣었다!")


@app.route('/first')
def home():
    return render_template('first.html')


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/result/api', methods=['GET'])
def result_api():
    # 이미지이기에, rescale 및 size 조정을 위해 ImageDataGenerator 활용
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_dir = 'static/img/'

    test_generator = test_datagen.flow_from_directory( # test_dir에 폴더별로 저장을 해야함
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
    fir_data = db.feeling_data.find_one({'feeling_num':pred_sorted[0][0]})  # 1번째로 높은 값 가져오기
    result.append(fir_data)

    sec_data = db.feeling_data.find_one({'feeling_num':pred_sorted[1][0]})  # 2번째로 높은 감정의 값들 가져오기
    result.append(sec_data)

    thd_data = db.feeling_data.find_one({'feeling_num':pred_sorted[2][0]})  # 3번째로 높은 감정의 값들 가져오기
    result.append(thd_data)

    print(result)
    return result


@app.route('result/second')
def result_second():
    return render_template('second.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)

