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

                let temp_html = `<div class = "chicken_photo">
                                    <img src="${chicken_pic}">
                                </div>
                                <div class = "chicken_desc">
                                    <p>${chicken_desc}</p>
                                </div>`

            }
        })
    }