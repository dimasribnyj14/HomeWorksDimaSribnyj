const matrix = [
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "P", '0', "0", '0', "0", '0', "0", '0'],
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
    ['0', '0', "0", '0', "0", '0', "0", '0', "W", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
    ['0', '0', "0", '0', "0", '0', "0", '0', "0", '0'],
]
console.log(matrix[0][3]);
function onMove(event) {
    const coordsPlayer = document.getElementById('player');
    if (event.code == "KeyW") {
        if (coordsPlayer.style.top != '0px') {
            console.log(coordsPlayer.style.top);
            coordsPlayer.style.top = (parseInt(coordsPlayer.style.top || getComputedStyle(coordsPlayer)['left'], 10) - 25) + 'px';
        }
    } else if (event.code == 'KeyD') {
        if (coordsPlayer.style.left != '475px') {
            console.log(coordsPlayer.style.left);
            coordsPlayer.style.left = (parseInt(coordsPlayer.style.left || getComputedStyle(coordsPlayer)['left'], 10) + 25) + 'px';
        }
    } else if (event.code == 'KeyA') {
        if (coordsPlayer.style.left != '0px') {
            console.log(coordsPlayer.style.left);
            coordsPlayer.style.left = (parseInt(coordsPlayer.style.left || getComputedStyle(coordsPlayer)['left'], 10) - 25) + 'px';
        }
    } else if (event.code == 'KeyS') {
        if (coordsPlayer.style.top != '475px') {
            console.log(coordsPlayer.style.top);
            coordsPlayer.style.top = (parseInt(coordsPlayer.style.top || getComputedStyle(coordsPlayer)['left'], 10) + 25) + 'px';
        }
    }
}
const drawMaze = (maze) => {
    let divElQ = document.querySelector(".maze-field");
    if (matrix) {
        for (let i = 0; i < matrix.length; i++) {
            let divEl = document.createElement("div");
            divEl.style.width = '25px';
            divEl.style.height = '25px';
            divEl.style.backgroundColor = 'black';
            let mazeW = matrix.values()
            divElQ.append(divEl);
            //             if (maze[0])
            //                 case "1":
            // divEl.setAttribute("class", "wall");
            // break;
            //                 case "0":
            // divEl.setAttribute("class", "freespace");
            // break;
            //                 case "W":
            // divEl.setAttribute("id", "win");
            // break;
            //         }
        }
    }
}
drawMaze(matrix);
document.addEventListener('keydown', onMove);