let itemQuantity = 0;
const setItemQuantity = (quantity) => {
  itemQuantity = quantity;
  const span = document.querySelector('#basket-counter');
  const spanContent = span.childNodes[0];
  spanContent.textContent = itemQuantity;

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
  setItemQuantity(itemQuantity + 1);

}

window.onload = () => {
    
}
