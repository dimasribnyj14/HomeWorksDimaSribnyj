const customElement = document.createElement(tag = 'input', properties = [['innerHTML', 'Lorem Ipsum'], ['type', 'text'], ["placeholder", "input"]], styles = [['color', 'red'], ['fontSize', '24px']], parentEl = document.querySelector(".form"));
const path = parentEl;

for (let propertie of properties) {
    customElement.setAttribute(`${propertie[0][0]}`, `${propertie[0][1]}`);
    customElement.setAttribute(`${propertie[1][0]}`, `${propertie[1][1]}`);
    customElement.setAttribute(`${properties[2][0]}`, `${properties[2][1]}`);
}
for (let design of styles) {
    customElement.setAttribute(`${design[0][0]}`, `${design[0][1]}`);
    customElement.setAttribute(`${styles[1][0]}`, `${design[1][1]}`); // Не работает если написать design
}
path.append(customElement)