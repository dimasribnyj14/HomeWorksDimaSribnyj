// Функция которая изменяет цвет исходя из атрибута value у option
function changeColor(event) {
    const bodyElem = document.querySelector("body");
    bodyElem.style.backgroundColor = selectColor.value;
    console.log(selectColor.value);
}
// Сюда пишите название события, которое должно произойти после смены option
const selectColor = document.querySelector('select');
const selectColorEvent = "change";
// Создаем события на тег select.
selectColor.addEventListener(selectColorEvent, changeColor);
// Напишите, почему событие делаем на тег select, а работаем с тегом option?
// Здесь писать.
