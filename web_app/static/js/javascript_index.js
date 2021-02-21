const baseURL = "http://127.0.0.1:8000";
const categoryImagesUrl = "static/captcha/category_images/";
const captchaImageUrl = "static/captcha/captcha.jpeg";

$(document).ready(function () {
    selectedColors = new Set();
    function leadCAPTCHA() {
        $.ajax({
            type: "get",
            url: baseURL + "/generate_captcha",
            dataType: "json",
            success: function (response) {
                let data = JSON.parse(response);
                $("#category-name").text(data.category);
                $("#img-category").attr("src", categoryImagesUrl + data.category + ".jpg" + "?timestamp=" + new Date().getTime());
                $("#img-captcha").attr("src", captchaImageUrl + "?timestamp=" + new Date().getTime());
                $.ajax({
                    type: "get",
                    url: baseURL + "/boundary_colors",
                    dataType: "json",
                    success: function (response) {
                        $("#color-button-div").empty();
                        JSON.parse(response)["colors"].forEach(color => {
                            let button = $("<button>", {
                                id: color,
                                class: "button",
                                css: {
                                    "background-color": color,
                                    "margin": "1px"
                                }
                            });
                            button.click(function (e) {
                                e.preventDefault();
                                selectedColors.add(e.target.id);
                            });
                            $("#color-button-div").append(button);
                        });
                    },
                });
            }
        });
    }
    leadCAPTCHA();
    $("#page-reload-btn").click(function (e) {
        e.preventDefault();
        leadCAPTCHA();
    });
});
