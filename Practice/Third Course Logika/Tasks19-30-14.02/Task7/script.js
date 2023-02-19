// Variables
let point = 0;
// Map
let matrix = [
    ['P', '0', "0", '1', "1", '1', "1", '1', "1", '1'],
    ['0', '1', "0", '0', "0", '1', "0", '0', "0", '1'],
    ['0', '1', "0", '1', "0", '1', "1", '1', "1", '1'],
    ['0', '1', "0", '1', "0", '0', "0", '0', "1", '1'],
    ['0', '1', "1", '1', "1", '1', "1", '0', "1", '1'],
    ['0', '1', "0", '0', "0", '0', "1", '0', "1", '1'],
    ['0', '1', "0", '0', "0", '0', "1", '0', "1", '1'],
    ['0', '1', "0", '0', "0", '0', "1", '0', "1", '1'],
    ['0', '1', "0", '0', "0", '0', "0", '0', "1", '1'],
    ['0', '0', "0", '1', "1", '0', "1", '1', "1", '1'],
    ['0', '1', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '1', "0", '1', "1", '1', "1", '1', "1", '0'],
    ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
    ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
    ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
    ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
    ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
    ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
    ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "1", 'W'],
]
// Official Modules
function sleep(ms) {
    return new Promise(
        resolve => setTimeout(resolve, ms)
    );
}
// Custom Modules
function Win() {
    let pointEl = document.querySelector('h1');
    let warper = document.querySelector('.wrapper');
    let wonEl = document.createElement('strong');
    wonEl.style.color = 'red';
    wonEl.innerHTML = 'You Won! Restart page to play again!';
    warper.append(wonEl);
    point += 1;
    pointEl.innerHTML = "Points " + point;
    document.removeEventListener('keydown', onMove);
}

function onMove(event) {
    const coordsPlayer = document.getElementById('player');
    if (event.code == "KeyW") {
        if (coordsPlayer.style.top != '0px') {
            console.log(matrix)
            coordsPlayer.style.top = (parseInt(coordsPlayer.style.top || getComputedStyle(coordsPlayer)['left'], 10) - 25) + 'px';
        }
    } else if (event.code == 'KeyD') {
        if (coordsPlayer.style.left != '475px') {
            coordsPlayer.style.left = (parseInt(coordsPlayer.style.left || getComputedStyle(coordsPlayer)['left'], 10) + 25) + 'px';
            if (coordsPlayer.style.left == '475px' && coordsPlayer.style.top == '475px') {
                Win();
            }
        }
    } else if (event.code == 'KeyA') {
        if (coordsPlayer.style.left != '0px') {
            coordsPlayer.style.left = (parseInt(coordsPlayer.style.left || getComputedStyle(coordsPlayer)['left'], 10) - 25) + 'px';
        }
    } else if (event.code == 'KeyS') {
        if (coordsPlayer.style.top != '475px') {
            matrix.unshift(matrix.pop('P'));
            console.log(matrix);
            coordsPlayer.style.top = (parseInt(coordsPlayer.style.top || getComputedStyle(coordsPlayer)['left'], 10) + 25) + 'px';
            if (coordsPlayer.style.left == '475px' && coordsPlayer.style.top == '475px') {
                Win();
            }
        }
    }
}
function drawMatrix() {
    const divElQ = document.querySelector(".maze-field");
    const coordsPlayer = document.getElementById('player');
    let x = -25
    let y = -25
    let count = -1
    for (let i = 0; i < matrix.length; i++) {
        count += 1
        console.error(count)
        // if (y <= 475) {
        y += 25
        // } else {
        //     y = 0
        // }
        console.log(y + "Y")
        const wallEl = document.createElement('div');
        wallEl.style.width = '25px';
        wallEl.style.height = '25px';
        wallEl.style.position = 'absolute';
        wallEl.className = 'wall';
        wallEl.style.backgroundColor = 'black';
        wallEl.style.top = y + 'px';
        const winEl = document.createElement('div');
        winEl.style.width = '25px';
        winEl.style.height = '25px';
        winEl.style.position = 'absolute';
        winEl.className = 'win';
        winEl.style.backgroundColor = 'green';
        winEl.style.left = '475px';
        winEl.style.top = '475px';
        const playerEl = document.createElement('div');
        playerEl.style.width = '25px';
        playerEl.style.height = '25px';
        playerEl.style.position = 'absolute';
        playerEl.className = 'player';
        playerEl.style.left = coordsPlayer.style.left;
        playerEl.style.top = coordsPlayer.style.top;
        for (let o = 0; o < matrix[i].length; o++) {
            if (x <= 475) {
                x += 2.5
                console.log(x + 'X')
            } else {
                x = 0
            }
            wallEl.style.left = x + 'px';
            matrix.forEach(function callback(currentValue, index, array) {
                console.log(currentValue[count])
                switch (currentValue[count]) {
                    case '1':
                        divElQ.append(wallEl)
                        break;
                    case 'W':
                        divElQ.append(winEl)
                        break;
                    case "P":
                        divElQ.append(playerEl)
                        break;
                    case 'undefined':
                        break;
                    default:
                        // console.error(currentValue[y]);
                        break;
                }
            });
        }
    }
}
drawMatrix()
// function draw() {
//     for (let i = 0; i < matrix.length; i++) {
//         const each = matrix.forEach(element => element)
//         console.log(each.element[0])
//         switch (matrix.forEach(element => element[0])) {
//             case 1:
//                 console.log("done")
//                 break;
//             default:
//                 console.error('error')
//                 break;
//         }
//     }
// }

// Call Modules
// draw();
// Events
document.addEventListener('keydown', onMove);
//Trash
// divEl.style.opacity = 0;

// function onCheck() {
//     const coordsPlayer = document.getElementById('player');
//     const whileBool = true;
//     while (whileBool) {
//         window.setTimeout(onCheck, 1000);
//         if (coordsPlayer.style.left == '475px' && coordsPlayer.style.top == '475px') {
//             Win();
//             whileBool = false;
//         }
//     }
// }

// onCheck()

// function Ban() {
//     let divElQ = document.querySelector(".wrapper");
//     const text = document.createElement('h1');
//     text.style.color = 'red';
//     text.innerHTML = 'Тебя забанили за читы, перезагрузите страницу!';
//     divElQ.append(text);
//     document.removeEventListener('keydown',onMove);
// }

// function checkCollision(event) {
//     let divElP = document.getElementById('player');
//     if (divElP.style.left > 500) {
//         Ban();
//     }else if (divElP.style.left < 0) {
//         Ban();
//     }else if (divElP.style.top < 0) {
//         Ban();
//     }else if (divElP.style.top > 500) {
//         Ban();
//     }
// }

// document.addEventListener('keydown',checkCollision);

// function draw() {
//     let divElQ = document.querySelector('.maze-field');
//     for (let i = 0; i < matrix.length; i++) {
//         const chunk = matrix.slice();
//         console.log(chunk);
//         let divEl = document.createElement("div");
//         divEl.style.width = '25px';
//         divEl.style.height = '25px';
//         switch (matrix[0][2]) {
//             case '1':
//                 divEl.style.backgroundColor = 'black';
//                 divEl.style.left;
//                 divEl.style.top;
//                 divElQ.append(divEl);
//                 break;
//             default:
//                 break;
//         }

//     }
// }
// draw()

//const drawMaze = (maze) => {

// if (maze) {
    // let divElQ = document.querySelector(".maze-field");
    // let x = 0;
    // let y = 0;
    // for (let i = 0; i < maze.length; i++) {
        // let divEl = document.createElement("div");
        // divEl.style.width = '25px';
        // divEl.style.height = '25px';
        // x += 0.5;
        // y += 1;
        // console.log(y);
        // switch (matrix[0][x]) {
            // case "1":
                // divEl.setAttribute("class", "wall");
                // divEl.style.backgroundColor = 'black';
                // divElQ.append(divEl);
                // break;
            // case "W":
                // divEl.setAttribute("id", "win");
                // divEl.style.backgroundColor = 'green';
                // divElQ.append(divEl);
                // break;
            // case "P":
                // divEl.setAttribute('id', 'spawnplayer');
                // divElQ.append(divEl);
                // break;
            // default:
                // console.error('0');
                // break;
        // }
    // }
// }