// 
let cart = document.querySelector('.cart');
let price = document.querySelector('#price');
let form = document.querySelector('#orderForm');
// 
form.addEventListener('submit',function(event){
    form.setAttribute('action',`?#order&count=`+count.innerHTML)
    form.submit();
});
function openModalWindow(event) {
    // показывает backgrount для модального окна
    function showCover() {
        // Создаем елемент div
        let coverDiv = document.createElement('div'); 
        // добавляем в 
        coverDiv.classList.add('cover-div'); 
        // добавляем Div в документ
        document.body.append(coverDiv);
    }
    // вызываем функцию
    showCover();

    modalWindow.style.display = "flex";
    // ставим задержку для смени прозрачности потому что браузер не может обработать одновревенно
    setTimeout(
        () =>  modalWindow.style.opacity = 1, 
        1
    )
    // центрирование модального окна
    let windowWidth = document.body.clientWidth;
    let windowHeight = document.body.clientHeight;
    let modalWindowWidth = modalWindow.clientWidth;
    let modalWindowHeight = modalWindow.clientHeight;
    let left = windowWidth / 2 - modalWindowWidth / 2;
    let top = windowHeight / 2 - modalWindowHeight / 2;
    modalWindow.style.top = top + "px"; 
    modalWindow.style.left = left + "px";
}
// 
plusButton.addEventListener('click', function(event) { //Делаем евент plusButton при нажатии на которий ми добавляем 1 к количеству покупок
   
    count.innerHTML = +count.innerHTML + 1;
    price.innerHTML = '42999' *count.innerHTML
    
})
minusButton.addEventListener('click', function (event) {//Делаем евент minusButton при нажатии на которий ми отнимаем 1 к количеству покупок
    if ( +count.innerHTML > 1) { // условие благодоря которому ми не можем в меню покупок виставить 0 или -1
        count.innerHTML = +count.innerHTML - 1;
        price.innerHTML = '42999' * count.innerHTML
    }else{
        count.innerHTML = 0
        price.innerHTML = '0'
    }
})
buttonClose.addEventListener('click', function(event) { // создаем кнопку buttonClose при нажатии на которую закривается модальное окно
    let coverdiv = document.querySelector('.cover-div');
    coverdiv.remove();
    modalWindow.style.display = 'none';
    modalWindow.style.opacity = 0;
})

cart.addEventListener('click',openModalWindow);// Делаем евент для функции openModalWindow 