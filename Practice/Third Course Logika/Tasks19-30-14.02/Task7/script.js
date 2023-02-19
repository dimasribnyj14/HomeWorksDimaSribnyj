// Variables
let point = 0;
const coordinate = {
    'left': 1,
    'top': 1
}
const coordsPlayer = document.getElementById('player');
coordinate["left"] = coordsPlayer.style.left / 25;
coordinate["top"] = coordsPlayer.style.top / 25;
// Map
let list = [
    "P0000000000000000001".split(""),
    "01000011000000001001".split(""),
    "01000001000000100000".split(""),
    "01000001010000100001".split(""),
    "01001001010010100000".split(""),
    "01001001010000100000".split(""),
    "01001001010000100000".split(""),
    "01001001010000100000".split(""),
    "01001001010000100000".split(""),
    "01001000000000000000".split(""),
    "01000011111111111100".split(""),
    "01000000000000000000".split(""),
    "01010011111100010010".split(""),
    "01010011111100010010".split(""),
    "01010011111100010010".split(""),
    "01010011111100010010".split(""),
    "01010011111100010010".split(""),
    "01010011111100010010".split(""),
    "01010011111100010010".split(""),
    "0100011111111001001W".split("")
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
    let pMusic = document.createElement('p');
    let music = document.createElement('audio');
    let source = document.createElement('source');
    let audio = document.querySelector('.music');
    pMusic.classList.add('winner');
    music.setAttribute('controls', 'true');
    music.setAttribute('autoplay', 'true');
    source.setAttribute('src', 'winner.mp3');
    source.setAttribute('type', "audio/ogg");
    let warper = document.querySelector('.wrapper');
    let wonEl = document.createElement('strong');
    audio.remove()
    music.append(source);
    // pMusic.append(pMusic);
    // warper.append(pMusic);
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
        if (coordsPlayer.style.top != '0px' && list[coordinate["top"] - 1][coordinate["left"]] != 1) {
            coordsPlayer.style.top = (parseInt(coordsPlayer.style.top || getComputedStyle(coordsPlayer)['left'], 10) - 25) + 'px';
            coordinate['top'] -= 1;
            console.log(coordinate["left"]);
            console.warn(coordinate['top']);
        }
    } else if (event.code == 'KeyD') {
        if (coordsPlayer.style.left != '475px' && list[coordinate["top"]][coordinate["left"] + 1] != 1) {
            coordsPlayer.style.left = (parseInt(coordsPlayer.style.left || getComputedStyle(coordsPlayer)['left'], 10) + 25) + 'px';
            console.log(coordinate["left"]);
            coordinate['left'] += 1;
            console.warn(coordinate['top']);
            if (coordsPlayer.style.left == '475px' && coordsPlayer.style.top == '475px') {
                Win();
            }
        }
    } else if (event.code == 'KeyA') {
        if (coordsPlayer.style.left != '0px' && list[coordinate["top"]][coordinate["left"] - 1] != 1) {
            coordsPlayer.style.left = (parseInt(coordsPlayer.style.left || getComputedStyle(coordsPlayer)['left'], 10) - 25) + 'px';
            console.log(coordinate["left"]);
            console.warn(coordinate['top']);
            coordinate['left'] -= 1;
        }
    } else if (event.code == 'KeyS') {
        if (coordsPlayer.style.top != '475px' && list[coordinate["top"] + 1][coordinate["left"]] != 1) {
            coordsPlayer.style.top = (parseInt(coordsPlayer.style.top || getComputedStyle(coordsPlayer)['left'], 10) + 25) + 'px';
            console.log(coordinate["left"]);
            console.warn(coordinate['top']);
            coordinate['top'] += 1;
            if (coordsPlayer.style.left == '475px' && coordsPlayer.style.top == '475px') {
                Win();
            }
        }
    }
}
function matrixDraw() {
    const divElQ = document.querySelector(".maze-field");
    for (x in list) {
        for (y in list[x]) {
            switch (list[x][y]) {
                case '1':
                    var elemDiv = document.createElement("div");
                    elemDiv.classList.add('maze-block');
                    elemDiv.style.width = '25px';
                    elemDiv.style.position = 'absolute';
                    elemDiv.style.height = '25px';
                    elemDiv.style.backgroundColor = 'white';
                    elemDiv.style.top = String(x * 25) + "px";
                    elemDiv.style.left = String(y * 25) + "px";
                    divElQ.append(elemDiv);
                    break;
                case 'W':
                    var winDiv = document.createElement("div");
                    winDiv.classList.add('win-block');
                    winDiv.style.width = '25px';
                    winDiv.style.position = 'absolute';
                    winDiv.style.height = '25px';
                    winDiv.style.top = '475px';
                    winDiv.style.backgroundColor = 'green';
                    winDiv.style.left = '475px';
                    divElQ.append(winDiv);
                    break;
                default:
                    break;
            }

        }
    }
}
matrixDraw()
document.addEventListener('keydown', onMove);
// drawMatrix()
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
//
// Call Modules
// draw();
// Events
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
// function drawMatrix() {
//     const divElQ = document.querySelector(".maze-field");
//     const coordsPlayer = document.getElementById('player');
//     let x = -25
//     let y = -25
//     let count = -1
//     for (let i = 0; i < matrix.length; i++) {
//         count += 1
//         console.error(count)
//         // if (y <= 475) {
//         y += 25
//         // } else {
//         //     y = 0
//         // }
//         console.log(y + "Y")
//         const wallEl = document.createElement('div');
//         wallEl.style.width = '25px';
//         wallEl.style.height = '25px';
//         wallEl.style.position = 'absolute';
//         wallEl.className = 'wall';
//         wallEl.style.backgroundColor = 'black';
//         wallEl.style.top = y + 'px';
//         const winEl = document.createElement('div');
//         winEl.style.width = '25px';
//         winEl.style.height = '25px';
//         winEl.style.position = 'absolute';
//         winEl.className = 'win';
//         winEl.style.backgroundColor = 'green';
//         winEl.style.left = '475px';
//         winEl.style.top = '475px';
//         const playerEl = document.createElement('div');
//         playerEl.style.width = '25px';
//         playerEl.style.height = '25px';
//         playerEl.style.position = 'absolute';
//         playerEl.className = 'player';
//         playerEl.style.left = coordsPlayer.style.left;
//         playerEl.style.top = coordsPlayer.style.top;
//         for (let o = 0; o < matrix[i].length; o++) {
//             if (x <= 475) {
//                 x += 2.5
//                 console.log(x + 'X')
//             } else {
//                 x = 0
//             }
//             wallEl.style.left = x + 'px';
//             matrix.forEach(function callback(currentValue, index, array) {
//                 console.log(currentValue[count])
//                 switch (currentValue[count]) {
//                     case '1':
//                         divElQ.append(wallEl)
//                         break;
//                     case 'W':
//                         divElQ.append(winEl)
//                         break;
//                     case "P":
//                         divElQ.append(playerEl)
//                         break;
//                     case 'undefined':
//                         break;
//                     default:
//                         // console.error(currentValue[y]);
//                         break;
//                 }
//             });
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
// let matrix = [
//     ['P', '0', "0", '1', "1", '1', "1", '1', "1", '1'],
//     ['0', '1', "0", '0', "0", '1', "0", '0', "0", '1'],
//     ['0', '1', "0", '1', "0", '1', "1", '1', "1", '1'],
//     ['0', '1', "0", '1', "0", '0', "0", '0', "1", '1'],
//     ['0', '1', "1", '1', "1", '1', "1", '0', "1", '1'],
//     ['0', '1', "0", '0', "0", '0', "1", '0', "1", '1'],
//     ['0', '1', "0", '0', "0", '0', "1", '0', "1", '1'],
//     ['0', '1', "0", '0', "0", '0', "1", '0', "1", '1'],
//     ['0', '1', "0", '0', "0", '0', "0", '0', "1", '1'],
//     ['0', '0', "0", '1', "1", '0', "1", '1', "1", '1'],
//     ['0', '1', "0", '0', "0", '0', "0", '0', "0", '0'],
//     ['0', '1', "0", '1', "1", '1', "1", '1', "1", '0'],
//     ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
//     ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
//     ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
//     ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
//     ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
//     ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
//     ['0', '1', "0", '1', "1", '1', "0", '1', "1", '0'],
//     ['0', '0', "0", '0', "0", '0', "0", '0', "1", 'W'],
// ]
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