const { stdin, stdout } = require('process')
const readline = require('readline')

const rl = readline.createInterface({
    input: stdin,
    output: stdout
})

function Quadratic(a,b,c){
    const quadratic = (b*b) - (4 * a * c)
    var result;
    if (quadratic > 0) {
        var equalPlus = (-b + Math.sqrt(quadratic))/(2*a)
        var equalMinus = (-b - Math.sqrt(quadratic))/(2*a)
        result = `PLUS: ${equalPlus} and MINUS: ${equalMinus}`
    } else if (quadratic == 0) {
        result = -b/(2*a)
    } else {
		result = "Розв'язків немає"
	}
    return result;
}

rl.question('Введіть перше число', (a)=>{
    rl.question('Введіть друге число',(b)=>{
        rl.question('Введіть третє число',(c)=>{
            const floatA = parseFloat(a);
            const floatB = parseFloat(b);
            const floatC = parseFloat(c);
            console.log(Quadratic(floatA,floatB,floatC));
        })
    })
});