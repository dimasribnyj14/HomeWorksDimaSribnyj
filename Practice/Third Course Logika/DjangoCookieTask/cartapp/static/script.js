$(document).ready(function () {
    $(".add-to-cart").on("submit", function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: $(".add-to-cart").action,
            data: $(this).serialize(),
            dataType: "json",
            success: function () {
            }
        })
    })
})

