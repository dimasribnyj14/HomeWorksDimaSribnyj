// Подключаем div .reg
const form = document.querySelector(".reg");
// Список запрещенных слов
const bannedWords = [
    '%',
    '^',
    '&',
]
// Отправляем запрос на форму
form.addEventListener("submit", (event) => {
    // Очищаем настройки элемента браузера
    event.preventDefault();
    // Подключаем все классы input
    let inputs = document.querySelectorAll('.input');
    // Подключаем все классы error
    let divErrors = document.querySelectorAll('.error')
    // Относимся к divErrors с именем error
    for (let error of divErrors) {
        error.remove(); //Удаляем елемент error
    }
    // Результат boolean
    let result = true;
    // Относимся к inputs с именем input
    for (let input of inputs) {
        // Если валидация не прошла успешно, результат ставим на false
        if (validation(input) == false) {
            result = false;
        }
    }
    // Если результат равен true то отправляем форму
    if (result == true) {
        form.submit()
    }


})
// Создание ошибки
function createError(text, elem) {
    // Создаем div
    let divError = document.createElement('div');
    // Создаем p
    let pError = document.createElement('p');
    // Создаем img
    let imgError = document.createElement('img');
    // Добавляем p в div
    divError.append(pError);
    // Добавляем p в div
    divError.append(imgError);
    // Будет добавлен контент, возвращаемый функцией
    elem.after(divError);
    // Местоположение картинки
    imgError.src = "error.svg";
    // Текст p
    pError.innerHTML = text;
    // Добавляем класс error к div'ам
    divError.classList.add('error');
}
// 
function validation(input) {
    // Если поле пустое
    if (input.value == '') {
        createError(`Поле пустое`, input);
        // Возращаемся с false
        return false;
        // Ну я хз, что тут написать, там и там, пустое поле
    }
    // Если id у input'a равен username
    if (input.id == 'username') {
        // Относимся к input.value с именем symbol
        for (let symbol of input.value) {
            // Если в symbol содержится запрещенные символы
            if (bannedWords.includes(symbol)) {
                // Отобразится текст, что введен недопустимый символ и символ который ты ввел
                createError(`Введен недопустимый символ: ${symbol}`, input);
                // Возращаемся с false
                return false;
            }
        }
    }
    // Если id у input'a равен email
    else if (input.id == "email") {
        // Если в input.value нету @
        if (!input.value.includes("@")) {
            // То ошибка нам уведомит что в value отсутствует @
            createError(`Нету @`, input);
            // Возращаемся с false
            return false;
        }
    }
    // Возращаемся с true
    return true
}