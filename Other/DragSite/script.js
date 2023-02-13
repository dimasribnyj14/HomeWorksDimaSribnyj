function startDrag(event) {
    const imgElem = event.target;
    if (imgElem.tagName != 'div') {
        imgElem.style.left = event.clientX;
        imgElem.style.top = event.clientY;
    }
}
function endDrag(event) {
    const imgElem = event.target;
    if (imgElem.tagName != 'div') {
        imgElem.style.left = event.clientX;
        imgElem.style.top = event.clientY;
    }
}
function overDrag(event) {
    event.preventDefault();
}
function dropDrag(event) {
    const imgElem = event.target;
    if (imgElem.tagName != 'div') {
        imgElem.style.left = event.clientX;
        imgElem.style.top = event.clientY;
    }
}
const imgNumbers = document.querySelectorAll('.img');
for (let img of imgNumbers) {
    img.addEventListener('dragstart', startDrag);
    img.addEventListener('dragend', endDrag);
    img.addEventListener('dragover', overDrag);
    img.addEventListener('drop', dropDrag);
}