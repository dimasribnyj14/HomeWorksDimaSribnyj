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
    if (clock.getHours() <= 9) {
        htmlHours.innerHTML = '0'+clock.getHours();
    }else{
        htmlHours.innerHTML = clock.getHours();
    }
    if (clock.getMinutes() <= 9) {
        htmlMinutes.innerHTML = '0'+clock.getMinutes();
    }else{
        htmlMinutes.innerHTML = clock.getMinutes();
    }
    if (clock.getSeconds() <= 9) {
        htmlSeconds.innerHTML = '0'+clock.getSeconds();
    }else {
        htmlSeconds.innerHTML = clock.getSeconds();
    }
    
}
// Здесь должен быть задан интервал
setInterval(updateTime, 1000)