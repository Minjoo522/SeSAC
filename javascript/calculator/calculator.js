const expression = document.querySelector('.form-control');
function input_expression(char) {
  const operators = document.querySelectorAll('.operator');
  expression.value += char;
  if (
    expression.value.endsWith('+') ||
    expression.value.endsWith('-') ||
    expression.value.endsWith('*') ||
    expression.value.endsWith('/')
  ) {
    operators.forEach((operator) => operator.setAttribute('disabled', ''));
  } else {
    operators.forEach((operator) => operator.removeAttribute('disabled', ''));
  }
}

function get_result() {
  if (expression.value.endsWith('/0')) {
    expression.value = '';
    expression.setAttribute('placeholder', '오류');
  } else {
    let result = eval(expression.value);
    expression.value = result;
  }
}

function clear_event() {
  expression.value = '0';
}
