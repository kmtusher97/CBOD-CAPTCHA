$(document).ready(function () {
    $.ajax({
        type: "get",
        url: "http://127.0.0.1:8000/boundary_colors",
        dataType: "json",
        success: function (data) {
            JSON.parse(data)["colors"].forEach(color => {
                let button = $("<button>", {
                    id: color,
                    class: "button",
                    css: {
                        "background-color": color,
                        "margin": "1px"
                    }
                });
                $("#color-button-div").append(button);

            });
        },
        error: function () {
            alert("failed to connect to the server");
        }
    });
});
