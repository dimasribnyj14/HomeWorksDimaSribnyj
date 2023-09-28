const authModule = require('./auth.js');
const studentsModule = require('./student.js');
// const readLine = require('readline')

// // const rl = readLine.createInterface({
// //     input: process.stdin,
// //     output: process.stdout
// // })

var studentUser
var teacherUser

const teacher = () => {
    authModule.rl.question('Меню вчителя: \n1: Список учнів; \n2: Додати оцінку; \n3: Список оцінок',(select)=>{
        switch(select){
            case '1':
                for (let i = 0; i <= studentsModule.students-1; i++){
                    console.log(`${i}: Ім'я: ${student.name}; Прізвище: ${student.surname}`)
                }
                main()
                break;
            case '2':
                authModule.rl.question('Додайте оцінку',(mark)=>{
                    authModule.rl.question('Оберіть учня',(number)=>{
                        for (let i = 0; i <= studentsModule.students-1; i++){
                            console.log(`${i}: Ім'я: ${student.name}; Прізвище: ${student.surname}`)
                        }
                        var studentIndex = studentsModule.students.at(number-1)
                        console.log()
                        authModule.rl.question('Оберіть урок',(lesson)=>{
                            for (let i = 0; i <= studentIndex.marks-1; i++){
                                console.log(`${i}: ${studentIndex.marks}`)
                            }
                            if (studentIndex.marks.hasOwnProperty(lesson)){
                                studentIndex.marks[lesson].push(mark)
                                console.log(`${lesson}: ${studentIndex.marks[lesson]} \n${studentIndex}`)
                                main()
                            } else {
                                console.log("Урока не знайдено :(")
                                main()
                            }

                        })

                    })
                })
                break;
            case '3':
                for (let i = 0; i <= studentsModule.students-1; i++){
                    for (let mark in student.marks) {
                        console.log(`${i}: ${student.name} ${student.surname} \nОцінки з ${mark}: ${student.marks[mark]}`)
                    }
                    main()
                }
        } 
    })
}

const student = (user) => {
    authModule.rl.question('Меню учня: \n1: Список оцінок',(select)=>{
        switch(select){
            case '1':
                console.log(user.marks)
                break;
        } 
    })
}

const main = () => {
    if (!studentUser && !teacherUser){
        console.log('Авторизація: \n1: Я вчитель\n2: Я учень')
        authModule.rl.question('',(select)=>{
            switch(select){
                case '1':
                    authModule.authTeacher((teacher) => {
                        teacherUser = teacher
                        main()
                    })
                    break;
                case '2':
                    authModule.authStudent((student) => {
                        studentUser = student
                        main()
                    })
                    break;
            } 
        })
        
    } else if (teacherUser){
        console.log('You are teacher ')
        console.log(teacherUser.name, teacherUser.surname)
        teacher()
    } else if (studentUser){
        console.log('You are student ')
        console.log(studentUser.name, studentUser.surname)
        student(studentUser)
    }
    
}

main()
