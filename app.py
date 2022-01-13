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
if len(check) != 1:
    soup_happiness = BeautifulSoup(data.text, 'html.parser')
    soup_angry = BeautifulSoup(data2.text, 'html.parser')
    song_disgust = BeautifulSoup(data3.text, 'html.parser')
    song_fear = BeautifulSoup(data4.text, 'html.parser')
    song_neutral = BeautifulSoup(data5.text, 'html.parser')
    song_sad = BeautifulSoup(data6.text, 'html.parser')
    song_surprise = BeautifulSoup(data7.text, 'html.parser')


    # 데이터
    happiness = soup_happiness.select('#ESALBUM39691 > table > tbody > tr')
    for song_happiness in happiness:
        happiness_img = song_happiness.select_one('td > a > img')['src']
        happiness_title = song_happiness.select_one('th > p > a').text
        happiness_singer = song_happiness.select_one('td > p > a').text
        db.feeling_data.insert_one =({
            'feeing_num': 0,
            'color':'red',
            'img' :happiness_img,
            'title': happiness_title,
            'singer': happiness_singer,
            #'chicken': chicken
        })

        # print(happiness_img, happiness_title, happiness_singer)

    angry = soup_angry.select('#ESALBUM50746 > table > tbody > tr')
    for song_angry in angry:
        angry_img = song_angry.select_one('td > a > img')['src']
        angry_title = song_angry.select_one('th > p > a').text
        angry_singer = song_angry.select_one('td > p > a').text
        # print(angry_img, angry_title, angry_singer)
        db.feeling_data.insert_one = ({
            'feeing_num': 1,
            'color': 'red',
            'img': angry_img,
            'title': angry_title,
            'singer': angry_singer,
            # 'chicken': chicken
        })

    disgust = song_fear.select('#ESALBUM50519 > table > tbody > tr')
    for song_disgust in disgust:
        disgust_img = song_disgust.select_one('td > a > img')['src']
        disgust_title = song_disgust.select_one('th > p > a').text
        disgust_singer = song_disgust.select_one('td > p > a').text
        # print(disgust_img, disgust_title, disgust_singer)
        db.feeling_data.insert_one = ({
            'feeing_num': 2,
            'color': 'pink',
            'img': disgust_img,
            'title': disgust_title,
            'singer': disgust_singer,
            # 'chicken': chicken
        })

    fear = song_fear.select('#ESALBUM41409 > table > tbody > tr')
    for song_fear in fear:
        fear_img = song_fear.select_one('td > a > img')['src']
        fear_title = song_fear.select_one('th > p > a').text
        fear_singer = song_fear.select_one('td > p > a').text
        # print(fear_img, fear_title, fear_singer)
        db.feeling_data.insert_one = ({
            'feeing_num': 3,
            'color': 'black',
            'img': fear_img,
            'singer': fear_singer,
            'title': fear_title,
            # 'chicken': chicken
        })

    neutral = song_neutral.select('#ESALBUM50793 > table > tbody > tr')
    for song_neutral in neutral:
        neutral_img = song_neutral.select_one('td > a > img')['src']
        neutral_title = song_neutral.select_one('th > p > a').text
        neutral_singer = song_neutral.select_one('td > p > a').text
        # print(neutral_img, neutral_title, neutral_singer)
        db.feeling_data.insert_one = ({
            'feeing_num': 4,
            'color': 'gray',
            'img': neutral_img,
            'title': neutral_singer,
            'singer': neutral_singer,
            # 'chicken': chicken
        })

    sad = song_sad.select('#ESALBUM50839 > table > tbody > tr')
    for song_sad in sad:
        sad_img = song_sad.select_one('td > a > img')['src']
        sad_title = song_sad.select_one('th > p > a').text
        sad_singer = song_sad.select_one('td > p > a').text
        # print(sad_img, sad_title, sad_singer)
        db.feeling_data.insert_one = ({
            'feeing_num': 5,
            'color': 'purple',
            'img': sad_img,
            'title':sad_title,
            'singer':sad_singer,
            # 'chicken': chicken
        })

    surprise = song_surprise.select('#ESALBUM44402 > table > tbody > tr')
    for song_surprise in surprise:
        surprise_img = song_surprise.select_one('td > a > img')['src']
        surprise_title = song_surprise.select_one('th > p > a').text
        surprise_singer = song_surprise.select_one('td > p > a').text
        # print(surprise_img, surprise_title, surprise_singer)
        db.feeling_data.insert_one = ({
            'feeing_num': 6,
            'color': 'blue',
            'img': surprise_img,
            'title': surprise_title,
            'singer': surprise_singer
            # 'chicken': chicken
        })

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

