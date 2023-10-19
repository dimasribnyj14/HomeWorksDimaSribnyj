const { Telegraf } = require('telegraf') // Імпортуємо Telegraf
const sqlite3 = require('sqlite3').verbose() // Імпортуємо SQLITE3

const bot = new Telegraf('') // Створюємо telegram бот

const db = new sqlite3.Database('db.sqlite3') // Створюємо базу даних



function createUserTable(){ //Функція створення таблиці у базу даних, у яких буде мати id, status, friend
    const query = `CREATE TABLE Users(
        id INTEGER PRIMARY KEY,
        status varchar(255),
        friend int
    );`
    db.run(query)
}


function addUser(id){ //Функція додавання користувача до базу даних, у яких буде мати значення id та status
    const query = `INSERT INTO Users (id, status) VALUES(?,?)`
    db.run(query, [id,"in_search"])
}

function getUser(id, callback){ // Функція отримання інформації користувача
    const query = `SELECT status, friend FROM Users WHERE id = ${id}` // Обираємо значення status кліенту
    db.get(query, (err, res) => {
        callback(res)
    } )
}

function updateStatus(id, status){ // Оновляємо статус користувача
    const query = `UPDATE Users SET status = '${status}' WHERE id = ${id}` // Змінююємо значення status кліенту
    db.run(query)
}

function updateFriend(id, friend){ // Оновляємо дружину (точніше його id) користувача
    const query = `UPDATE Users SET friend = ${friend} WHERE id = ${id}` // Змінююємо значення friend кліенту
    db.run(query)
}

function getInSearchUsers(id, callback){ //Отримаємо усі користувачі
    const query = `SELECT id FROM Users WHERE status = 'in_search' AND id <> ${id}` // Обираємо значення id інших користувачів, у яких є status "in_search" й який не дорівнює id кліенту
    db.all(query, (err, res) => {
        callback(res)
    })
}


function findFriend(id){ // Шукаємо дружини
    getInSearchUsers(id,(res)=>{
        if (res.length > 0){
            const index = Math.floor(Math.random()*res.length) // Обираємо рандомний index й оновляємо status та friend кожного з них на "meet" й [id,randomUser.id]
            const randomUser = res[index]
            updateStatus(id, 'meet')
            updateStatus(randomUser.id, 'meet')
            updateFriend(id, randomUser.id)
            updateFriend(randomUser.id, id)
            bot.telegram.sendMessage(randomUser.id,"Співрозмовника знайдено. Можете спілкуватись")
            bot.telegram.sendMessage(id,"Співрозмовника знайдено. Можете спілкуватись")
        }
    })
}

bot.start((ctx) =>{ // Починаємо шукати, якщо користувача немає у базу даних або якщо у користувача статус standart, у інших випадках (наприклад статус meet або in_search) не буде шукати
    getUser(ctx.from.id, (res) => {
        if (res){
            if(res.status == "standart"){
                updateStatus(ctx.from.id, "in_search");
                ctx.reply('Шукаємо співрозмовника')
                findFriend(ctx.from.id)
            } else if(res.status == "in_search"){
                ctx.reply('Ми вже шукаємо співрозмовника')
            } else if(res.status == "meet"){
                ctx.reply('У вас вже є співрозмовник напишіть /stop щоб зупинити бесіду')
            }
        } else{
            addUser(ctx.from.id)
            ctx.reply('Шукаємо співрозмовника')
            findFriend(ctx.from.id)
        }
    })
})

bot.command("stop", (ctx)=>{ // Зупиняємо спілкування один з одним, якщо у них стоїть статус meet
    getUser(ctx.from.id, (res)=>{
        if (res){
            if (res.status == "meet"){
                updateStatus(ctx.from.id, "standart") //Змінююємо значення status й friend кожного з них на "standart" й null
                updateFriend(ctx.from.id, null)
                updateStatus(res.friend, 'standart')
                updateFriend(res.friend, null)
                ctx.reply('Розмову закінчено.')
                bot.telegram.sendMessage(res.friend,'Співрозмовник завершив бесіду.')
            } else{
                ctx.reply("У вас немає співрозмовника.")
            }
        }
    })
})

bot.on('text',(ctx)=>{ // Спілкуватись між собою, якщо вони мають статус meet
    getUser(ctx.from.id,(res)=>{
        if (res){
            if (res.status == 'meet'){
                bot.telegram.sendMessage(res.friend,ctx.message.text)
            } else {
                ctx.reply('З ким ви спілкуєтесь?')
            }
        } else {
            ctx.reply('Напишіть /start щоб знайти співрозмовника.')
        }
    })
})

bot.launch()  // Запускаємо бот

