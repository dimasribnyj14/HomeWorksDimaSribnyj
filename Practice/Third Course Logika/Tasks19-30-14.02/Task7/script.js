let matrix = [
    ['P', '1', "0", '0', "1", '0', "1", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
]

function onMove(event) {
    const coordsPlayer = document.getElementById('player');
    if (event.code == "KeyW") {
        if (coordsPlayer.style.top != '0px') {
            coordsPlayer.style.top = (parseInt(coordsPlayer.style.top || getComputedStyle(coordsPlayer)['left'], 10) - 25) + 'px';
        }
    } else if (event.code == 'KeyD') {
        if (coordsPlayer.style.left != '475px') {
            coordsPlayer.style.left = (parseInt(coordsPlayer.style.left || getComputedStyle(coordsPlayer)['left'], 10) + 25) + 'px';
        }
    } else if (event.code == 'KeyA') {
        if (coordsPlayer.style.left != '0px') {
            coordsPlayer.style.left = (parseInt(coordsPlayer.style.left || getComputedStyle(coordsPlayer)['left'], 10) - 25) + 'px';
        }
    } else if (event.code == 'KeyS') {
        if (coordsPlayer.style.top != '475px') {
            coordsPlayer.style.top = (parseInt(coordsPlayer.style.top || getComputedStyle(coordsPlayer)['left'], 10) + 25) + 'px';
        }
    }
}
function draw() {
    let divElQ = document.querySelector('.maze-field');
    for (let i = 0; i < matrix.length; i++) {
        let divEl = document.createElement("div");
        divEl.style.width = '25px';
        divEl.style.height = '25px';
        divEl.style.backgroundColor = 'black';
        divElQ.append(divEl);
    }
}
// draw()
const drawMaze = (maze) => {
    let divElQ = document.querySelector(".maze-field");
    if (maze) {
        for (let i = 0; i < maze.length; i++) {
            let divEl = document.createElement("div");
            divEl.style.width = '25px';
            divEl.style.height = '25px';
            switch (maze.items[0][1]) {
                case 1:
                    divEl.setAttribute("class", "wall");
                    console.log('good');
                    divEl.style.backgroundColor = 'black';

                    break;
                case "W":
                    divEl.setAttribute("id", "win");
                    divEl.style.backgroundColor = 'green';
                    console.warn('great');
                    break;
                case "P":
                    divEl.setAttribute('id', 'spawnplayer');
                    divEl.style.opacity = 0;
                    console.warn('CHUDOVO!');
                default:
                    console.error('error');
            }
        }
    }
}

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

drawMaze(matrix);
document.addEventListener('keydown', onMove);