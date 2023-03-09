const buttonElem = document.querySelector('.button-readmore');
const textElem = document.querySelector('.text-content');
if (textElem.innerHTML.length >= 20) {
    textElem.innerHTML = 'Lorem ipsum dolor...'
}
function readmore() {
    if (textElem.innerHTML.length > 20) {
        textElem.innerHTML = 'Lorem ipsum dolor...'
        buttonElem.innerHTML = "Read More"
    } else {
        buttonElem.innerHTML = "Read Less"
        textElem.innerHTML = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    }

}