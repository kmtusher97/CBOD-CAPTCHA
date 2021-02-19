$(document).ready(function () {
    $.ajax({
        type: "get",
        url: "http://127.0.0.1:8000/boundary_colors",
        dataType: "json",
        success: function(data){
            colors = JSON.parse(data)["colors"];
            console.log(colors);
            shuffle(colors)
            console.log(colors);

        },
        error: function(){
            alert("failed to connect to the server");
        }
    });
});