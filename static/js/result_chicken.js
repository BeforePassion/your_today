function get_chicken() {
        $.ajax({
            type: "GET",
            url: "",
            data: {},
            success: function (data) {

                let chicken = data['result']
                console.log(data)
                let chicken_pic = chicken['pic']
                let chicken_desc = chicken['desc']

                let temp_html = `<div class="chicken-container_img">
                                    <img style="max-width: 500px; max-height: 500px; width: 60vw; height: 60vw; border-radius: 20px; border: 3px solid black; margin-bottom: 20px; padding: 30px" id="preview-image" src="${chicken_pic}">
                                </div>
                                <div class="chicken-container-desc">
                                    <p>${chicken_desc}</p>
                                </div>`

            }
        })
    }