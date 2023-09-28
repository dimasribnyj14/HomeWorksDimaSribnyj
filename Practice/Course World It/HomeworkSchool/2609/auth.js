const studentModule = require('./student.js')
const teacherModule = require('./teacher.js')
const readLine = require('readline')

const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
})

function authStudent(callback){
    var studentLoging
    rl.question("Введіть логін: ", (login) =>{
        rl.question("Введіть пароль: ", (password) => {
            let success = false
            for (let student of studentModule.students){
                studentLoging = student.auth(login, password)
                if (studentLoging){
                    success = true
                    break
                }
            }
            if (!success){
                console.log('Користувача не знайдено')
                return null
            }
            callback(studentLoging)
        })
    })
    // return studentLoging
}

function authTeacher(callback){
    var teacherLoging
    rl.question("Введіть логін: ", (login) =>{
        rl.question("Введіть пароль: ", (password) => {
            let success = false
            for (let teacher of teacherModule.teachers){
                teacherLoging = teacher.auth(login, password)
                if (teacherLoging){
                    success = true
                    break
                }
            }
            if (!success){
                console.log('Користувача не знайдено')
                return null
            }
            callback(teacherLoging)
        })
    })
    
}

module.exports = {
    authStudent : authStudent,
    authTeacher : authTeacher,
    rl: rl,
}