function updateTime() {
    // Здесь должен быть элемент hours 
    // Здесь должен быть элемент minutes 
    // Здесь должен быть элемент seconds
    const htmlHours = document.querySelector(".hours");
    const htmlMinutes = document.querySelector(".minutes");
    const htmlSeconds = document.querySelector(".seconds");

    const clock = new Date();
    console.log("Check");
    clock.getHours();
    clock.getMinutes();
    clock.getSeconds();
    htmlHours.innerHTML = clock.getHours();
    htmlMinutes.innerHTML = clock.getMinutes();
    htmlSeconds.innerHTML = clock.getSeconds();
}
// Здесь должен быть задан интервал
setInterval(updateTime, 1000)