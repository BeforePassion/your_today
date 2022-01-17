
var data_cart;


function loadFile(input) {
    // 인풋 태그에 파일이 있는 경우
    if(input.files && input.files[0]) {
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
            // 아래처럼 하지 않아도, 백엔드(app.py)에서 바로 판별 함수를 실행한 뒤에
            // render_template 을 해서 바로 결과 페이지로 넘어가도 됨

        }
    });
  }

  function preview() {
    let frame = $('#frame');
    frame.src=URL.createObjectURL(event.target.files[0]);
    frame.style.display = 'block';
  }

  function post_data(){

    $.ajax({
        type: "POST",
        url: "/result/toss",
        data: {'result':data_cart},
        success: function (response) {
            console.log(response["result"])
            // 아래처럼 하지 않아도, 백엔드(app.py)에서 바로 판별 함수를 실행한 뒤에
            // render_template 을 해서 바로 결과 페이지로 넘어가도 됨

        }
    });
  }
