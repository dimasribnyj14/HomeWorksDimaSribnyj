const input = document.createElement(tag = "input", properties = [["innerHTML", "Lorem ipsum"], ["type", "text"], ["placeholder", "dolor sit amet"]], styles = [["fontSize", "18px"], ["color", "red"]]);
for (let propertie of properties) {
    propertie.style = [['fontSize', '72px'], ['backgroundColor', 'yellow']];
    console.log("rock")
}
console.log("checking append")
const rock = document.querySelector('.Rock');
rock.append(input);