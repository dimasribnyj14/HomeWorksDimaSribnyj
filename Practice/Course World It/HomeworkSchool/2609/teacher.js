class Teacher{
    constructor(name,surname,login,password){
        this.name = name
        this.surname = surname
        this.login = login
        this.password = password
    }
    auth(login,password){
        if(login == this.login && password == this.password){
            console.log(`Вітаємо, ${this.name} ${this.surname}`)
            return this
        } else {
            return null
        }
    }
}

const teachers = []

teachers.push(new Teacher('Dmytro', 'Dohonov', 'dima', '123456'))
teachers.push(new Teacher('Mykola', 'Skrypnyk', 'mykola', '126'))

module.exports = {
    teachers: teachers,
    Teacher: Teacher
}