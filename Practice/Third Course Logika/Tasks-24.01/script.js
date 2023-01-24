const customElement = document.createElement(tag = 'input', properties = [['innerHTML', 'Lorem Ipsum'], ['type', 'text'], ["placeholder", "nenavishu eto zadanie"]], styles = [['color', 'red'], ['fontSize', '24px']], parentEl = document.querySelector(".Rock"));
const path = parentEl;
console.log("Defined or not?", `${properties[1][1]}`, `${styles[0][1]}`, `${properties[2][0]}`, properties[2]);
for (let propertie of properties) {
    customElement.setAttribute(`${propertie[0][0]}`, `${propertie[0][1]}`);
    customElement.setAttribute(`${propertie[1][0]}`, `${propertie[1][1]}`);
    customElement.setAttribute(`${properties[2][0]}`, `${properties[2][1]}`);
}
for (let design of styles) {
    customElement.style.color = "red"; //`${design[0][1]}`
    customElement.style.fontSize = "24px"; // `${design[1][1]}`
}
path.append(customElement)