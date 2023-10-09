
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
}
