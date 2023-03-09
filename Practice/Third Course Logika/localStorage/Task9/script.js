// Подключаем #reg и .input
const form = document.querySelector("#reg");
let inputed = document.querySelectorAll('.input');
// inputed[0].value равен твоему имя пользователя
// inputed[1].value равен твоей електронной почты
// inputed[2].value равен твоего пароля
// Добавляем LocalStorage
let myStorage = window.localStorage; // ВАЖНО! Создаем localStorage при помощи window
// Список запрещенных символов
const bannedSymbols = ['%', '^', '&', '*', ";", ':', '!', '@', '#', "$", '~', '`', '"', "'", "/", '?', '.', ',', '>', "<"]
// Сохраняем данные перед уходом
window.onbeforeunload = function () {
    myStorage.setItem('username', inputed[0].value); //Добавляем имя пользователя в localStorage
    myStorage.setItem('email', inputed[1].value); //Добавляем электронную почту в localStorage
    myStorage.setItem('password', inputed[2].value); //Добавляем пароль в localStorage
};
// Загружаем данные из localStorage при заходе на страницу 
window.onload = function () {
    inputed[0].value = myStorage.getItem('username'); // Вставляем имя пользователя из localStorage в input 
    inputed[1].value = myStorage.getItem('email'); // Вставляем электронную почту из localStorage в input
    inputed[2].value = myStorage.getItem('password'); // Вставляем пароль из localStorage в input
};
form.addEventListener("submit", (event) => {
    // Очищаем настройки элемента браузера
    event.preventDefault();
    // Подключаем все классы input
    let inputs = document.querySelectorAll('.input');
    // Подключаем все классы error
    let divErrors = document.querySelectorAll('.error');
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
        form.submit() //Потверждаем отправку формы
        inputs[0].value = '' //Очищаем input имя пользователя
        inputs[1].value = '' //Очищаем input электронной почты
        inputs[2].value = '' //Очищаем input пароля 
        myStorage.clear() //Очищаем все данные localStorage
    }
})
// Создание ошибки
function createError(text, elem) {
    // Создаем div
    let divError = document.createElement('div');
    // Создаем p
    let pError = document.createElement('p');
    // Добавляем p в div
    divError.append(pError);
    // Будет добавлен контент, возвращаемый функцией
    elem.after(divError);
    // Цвет ошибки текста
    pError.style.color = 'red';
    // Текст p
    pError.innerHTML = text;
    // Добавляем класс error к div'ам
    divError.classList.add('error');
}
// Функция валидации
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
            if (bannedSymbols.includes(symbol)) {
                // Отобразится текст, что введен недопустимый символ и символ который ты ввел
                createError(`Введен недопустимый символ: ${symbol}`, input);
                // Возращаемся с false
                return false;
                // Если в имени пользователя меньше 6 символов
            } else if (input.value.length < 6) {
                // Отобразится текст, что имя пользователя должен содержать не менее 6 символов
                createError('Ваше имя пользователя должен содержать не менее 6 символов', input);
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
            createError(`В вашем электроном почте отсутствует @`, input);
            // Возращаемся с false
            return false;
        }
    }
    // Если id у input'а равен паролю
    else if (input.id == "password") {
        for (let symbol of input.value) {
            // Если у пароля меньше 8 символов
            if (input.value.length < 8) {
                // Отобразится текст, что пароль должен содержать не менее 8 символов
                createError("Пароль должен содержать не менее 8 символов", input);
                // Возращаемся с false
                return false;
                // Если у пароля нету цифр (Не работает)
            } else if (input.value.includes(Number)) {
                // Отобразится текст, что пароль должен содержать как минимум 1 цифра
                createError('Ваш пароль должен содержать как минимум 1 цифра', input);
                // Возращаемся с false
                return false;
                // Если у пароля нету букв (Не работает)
            } else if (input.value.includes(Symbol)) {
                // Отобразится текст, что пароль должен содержать как минимум 1 буква
                createError('Ваш пароль должен содержать как минимум 1 буква', input);
                // Возращаемся с false
                return false;
            }
        }
    }
    // Возращаемся с true
    return true
}