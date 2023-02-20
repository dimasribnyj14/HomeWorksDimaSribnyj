const pText = document.querySelector('strong');
const font = document.querySelector('font');
const splittedText = pText.innerHTML.split('');
const main = document.querySelector('.wrapper');
let count = 0;
const error = document.createElement("h1");
error.style.color = 'red';
error.innerHTML = "Неправильно написано! Исправь!";
error.style.display = 'none';
main.append(error);
let activatedError = 0;
function Type(event) {
    if (event.key == "Delete" || event.key == "Backspace") {
        font.innerHTML = font.innerHTML.substring(0, font.innerHTML.length - 1);
        if (count != 0) {
            count -= 1;
            pText.innerHTML = splittedText[count]+pText.innerHTML;
        }
        // let undoOriginal = pText.innerHTML.substring(pText.innerHTML.length - 1, 0);
    } else if (event.key == "CapsLock" || event.key == "Shift" || event.key == "Control" || event.key == "Alt" || event.key == "Meta" || event.key == "F1" || event.key == "F2" || event.key == "F3" || event.key == "F4" || event.key == "F5" || event.key == "F6" || event.key == "F7" || event.key == "F8" || event.key == "F9" || event.key == "F10" || event.key == "F11" || event.key == "F12" || event.key == "Enter" || event.key == "Tab" || event.key == "ContextMenu" || event.key == "PageUp" || event.key == "PageDown" || event.key == "ScrollLock" || event.key == "Pause" || event.key == "Home" || event.key == "Insert" || event.key == "End" || event.key == "NumLock" || event.key == "Escape") {
        return;
    } else if (event.key == splittedText[count]) {
        if (count != pText.innerHTML.length) {
            count += 1;
            console.log(count);
            font.style.color = 'green';
            font.innerHTML += event.key;
            pText.innerHTML = pText.innerHTML.slice(1);
            error.style.display = 'none';
            activatedError = 0;
        }
    } else if (event.key == "Control" && event.key == "a") {
        if (event.key == "Delete" || event.key == "Backspace") {
            font.innerHTML = "";
            count = 0
        }
    } else {
        font.innerHTML += event.key;    
        count += 1;
        console.warn(count+"CurrentCount;"+pText.innerHTML.length+"LengthText;")
        console.error(splittedText[count]+'CurrentValue')
        font.style.color = 'firebrick';
        if (activatedError == 0) {
            activatedError = 1
            error.style.display = 'block';
        }
    }
    if (font.innerHTML == "") {
        font.style.color = 'green';
        activatedError == 0;
        error.style.display = 'none';
    }
}
document.addEventListener('keydown', Type);