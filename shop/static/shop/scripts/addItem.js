let itemNumber = 0;
const setItemNumber = (number) => {
  itemNumber = number;
  const span = document.querySelector('#basket-counter');
  const spanContent = span.childNodes[0];
  spanContent.textContent = itemNumber;

  // const spanContent = document.createTextNode('test');
  // span.appendChild(spanContent);
  // console.log(spanContent);
  // spanContent.textContent = 'a';
}

const addItem = async (button, url) => {
  const oldClassName = button.className;
  const oldDisabled = button.disabled;
  button.className += ' is-loading ';
  button.disabled = true;
  let response = fetch(url);
  const wait = await new Promise(res => setTimeout(res, 1000));
  response = await response;
  button.className = oldClassName;
  button.disabled = oldDisabled;
  setItemNumber(itemNumber + 1);

}

window.onload = () => {
    
}
