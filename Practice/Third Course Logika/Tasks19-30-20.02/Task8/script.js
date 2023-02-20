const pText = document.querySelector('strong');
const font = document.querySelector('font');
const splittedText = pText.innerHTML.split('');
let count = 0;
function Type(event) {
    splittedText.forEach(function callback(currentValue, index, array) {
        if (event.key == splittedText.currentValue) {
            console.log(pText.innerHTML.length);
        }
    })
    if (event.key == "Delete" || event.key == "Backspace") {
        font.innerHTML = font.innerHTML.substring(0, font.innerHTML.length - 1);
        count -= 1;
    } else if (event.key == "CapsLock" || event.key == "Shift" || event.key == "Control" || event.key == "Alt" || event.key == "Meta" || event.key == "F1" || event.key == "F2" || event.key == "F3" || event.key == "F4" || event.key == "F5" || event.key == "F6" || event.key == "F7" || event.key == "F8" || event.key == "F9" || event.key == "F10" || event.key == "F11" || event.key == "F12" || event.key == "Enter" || event.key == "Tab" || event.key == "ContextMenu" || event.key == "PageUp" || event.key == "PageDown" || event.key == "ScrollLock" || event.key == "Pause" || event.key == "Home" || event.key == "Insert" || event.key == "End" || event.key == "NumLock" || event.key == "Escape") {
        return;
    } else {
        if (count != pText.innerHTML.length) {
            count += 1;
            console.log(count);
            font.innerHTML += event.key;
            pText.innerHTML = pText.innerHTML.substring(pText.innerHTML.length - 1, 0);
        }
    }
}
document.addEventListener('keydown', Type);