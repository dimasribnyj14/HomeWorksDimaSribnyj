// Функция которая изменяет цвет исходя из атрибута value у option
function changeColor(event) {
    const bodyElem = document.querySelector("body");
    bodyElem.style.backgroundColor = selectColorEvent;
    console.log(selectColor.value);
}
// Сюда пишите название события, которое должно произойти после смены option
const selectColor = document.getElementById('selectColor');
var selectColorEvent = `${selectColor.value}`;
// Создаем события на тег select.
selectColor.addEventListener(selectColorEvent, changeColor);
console.log(selectColor.value);
// Напишите, почему событие делаем на тег select, а работаем с тегом option?
// Здесь писать.
