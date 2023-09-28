const teacherModule = require('./teacher.js')


class Student extends teacherModule.Teacher{
    constructor(name, surname, login, password){
        super(name, surname, login, password)
        this.marks = {
            "Математика":[],
            "Українська мова":[],
            "Англійська мова":[],
            "Історія України":[]
        }
    }
    printMarks() {
        for (let subdject in this.marks){
            console.log(`Оцінки з предмету ${subdject}:`)
            console.log(this.marks[subdject])
        }
        
    }
}

const students = []
students.push(new Student('Dmitry','Sribnyj','doc85','qqww'));
let MaksV = new Student("Maks","Voloshin","mvolosin","coolPASSWOrd31")
students.push(MaksV)
students.push(new Student('Данил', 'Андросов', 'dandrosov', '12345678'))
students.push(new Student("Владислав", "Злидар", "vzlydar", "2134"))
students.push(new Student("Roman","Babai", "rbabai", "0072"))
let pavlo = new Student('Кокора', 'Павло', 'pablo', 'cool_pa$$word')
students.push(pavlo)
students.push(new Student("Serhiy", "Vahnyuk", "svahnyuk", "qwerty123"))
students.push(new Student('Daniil', 'Makhno', 'hz', 'da'))
students.push(new Student ('Артем', 'Мулько', 'amulko','8732'));
students.push(new Student("Алксей", 'Беляев', 'alexb', '22812'))

module.exports = {
    students: students,
    Student: Student
}