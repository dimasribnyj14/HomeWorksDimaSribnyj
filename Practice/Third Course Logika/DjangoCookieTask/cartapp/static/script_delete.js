$(document).ready(function () {
    $(".delet-to-cart").on("submit", function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: $(".delet-to-cart").action,
            data: $(this).serialize(),
            dataType: "json",
            success: function () {
            }
        })
    })
})

