const { stdin, stdout } = require('process')
const readline = require('readline')

const rl = readline.createInterface({
    input: stdin,
    output: stdout
})

function Perimetr(a,b){
    return (a+b)*2
}

rl.question('Введіть перше число', (a)=>{
    rl.question('Введіть друге число',(b)=>{
        const floatA = parseFloat(a);
        const floatB = parseFloat(b);
        console.log(Perimetr(floatA,floatB))
    })
});