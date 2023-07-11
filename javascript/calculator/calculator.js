const expression = document.querySelector('.form-control');

function input_expression(char) {
  const operators = document.querySelectorAll('.operator');
  expression.value += char;
  // 연산자 뒤 연산자 입력 불가하게
  if (
    expression.value.endsWith('+') ||
    expression.value.endsWith('-') ||
    expression.value.endsWith('*') ||
    expression.value.endsWith('/')
  ) {
    operators.forEach((operator) => operator.setAttribute('disabled', ''));
  } else if (expression.value == '0' || null) {
    char == '0' ? (expression.value = '') : (expression.value = char);
  } else {
    operators.forEach((operator) => operator.removeAttribute('disabled', ''));
  }
}

function get_result() {
  if (expression.value.endsWith('/0')) {
    expression.value = '';
    expression.setAttribute('placeholder', '오류');
  } else if (expression.value != '') {
    let result = eval(expression.value, 10);
    expression.value = result;
  } else {
    expression.value = '';
  }
}

function clear_event() {
  expression.value = '';
}
