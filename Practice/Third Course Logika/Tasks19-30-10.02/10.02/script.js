function onScroll(event) {
    console.log(window.scrollY);
    console.log(document.querySelector('body').scrollHeight+'body');
    if (window.scrollY <= document.querySelector('body').scrollHeight/2) {
        document.getElementById("arrowDown").removeAttribute('hidden');
        document.getElementById("arrowTop").setAttribute('hidden','null');
        console.log("<="+document.querySelector('body').scrollHeight/2);
    }else{
        console.log(">="+document.querySelector('body').scrollHeight/2);
        document.getElementById("arrowTop").removeAttribute('hidden');
        document.getElementById("arrowDown").setAttribute('hidden','null');
    }
}
function onScrollDown(event) {
    window.scrollTo(0, document.querySelector('body').scrollHeight);
}
function onScrollUp(event) {
    window.scrollTo(0,0);
}
document.getElementById("arrowDown").addEventListener('click',onScrollDown);
document.getElementById("arrowTop").addEventListener('click',onScrollUp);
window.addEventListener('scroll',onScroll);