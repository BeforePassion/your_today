var data_cart;


function loadFile(input) {
    // 인풋 태그에 파일이 있는 경우
    if (input.files && input.files[0]) {
        // 이미지 파일인지 검사 (생략)
        // FileReader 인스턴스 생성
        const reader = new FileReader()
        // 이미지가 로드가 된 경우
        reader.onload = e => {
            const previewImage = document.getElementById("preview-image")
            previewImage.src = e.target.result
        }
        // reader가 이미지 읽도록 하기
        reader.readAsDataURL(input.files[0])
    }
}

// input file에 change 이벤트 부여
const inputImage = document.getElementById("chooseFile")
inputImage.addEventListener("change", e => {
    readImage(e.target)
})

function posting() {
    let file = $('#chooseFile')[0].files[0]
    let form_data = new FormData()

    form_data.append("file_give", file)
    console.log(file.give)

    $.ajax({
        type: "POST",
        url: "/result/api",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            console.log(response["result"])
            data_cart = response["result"]
            let recon = data_cart.replace(/\[/g, '').replace(/\]/g, '').split(',')
            let first_feeling = recon[0]
            let second_feeling = recon[2]
            let third_feeling = recon[4]
            let feeling = [first_feeling, second_feeling, third_feeling]

            let feel = []
            for (i = 0; i < feeling.length; i++) {
                console.log(feeling[i])
                if (feeling[i] == 0) {
                    let happiness = '행복'
                    feel.push(happiness)
                }
                else if (feeling[i] == 1) {
                    let angry = '분노'
                    feel.push(angry)
                }
                else if (feeling[i] == 2) {
                    let disgust = '짜증'
                    feel.push(disgust)
                }
                else if (feeling[i] == 3) {
                    let fear = '공포'
                    feel.push(fear)
                }
                else if (feeling[i] == 4) {
                    let neutral = '무념'
                    feel.push(neutral)
                }
                else if (feeling[i] == 5) {
                    let sad = '슬픔'
                    feel.push(sad)
                }
                else if (feeling[i] == 6) {
                    let surprise = '놀람'
                    feel.push(surprise)
                }
            }
            let temp_html = `<p>${feel}</p>`
            $('#feeling_text').append(temp_html);

        }
    });
}

function preview() {
    let frame = $('#frame');
    frame.src = URL.createObjectURL(event.target.files[0]);
    frame.style.display = 'block';
}

function test() {
    $.redirect('/result/api', {msg: data_cart});
}