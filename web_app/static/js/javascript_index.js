$(document).ready(function () {
    selectedColors = new Set();

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
                button.click(function (e) { 
                    e.preventDefault();
                    selectedColors.add(e.target.id);
                });
                $("#color-button-div").append(button);

            });
        },
    });

    function selectColor(event) {
        console.log(event.target);
    }
});
