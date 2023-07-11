const expression = document.querySelector('.form-control');

function inputExpression(char) {
  if (expression.value === '오류') {
    expression.value = char;
  } else {
    expression.value += char;
  }
  checkFirstChar(char);
  checkLastChar();
}

function checkFirstChar(char) {
  if (expression.value === '0' || expression.value === null) {
    expression.value = char === '0' ? '' : char;
  }
}

function checkLastChar() {
  const operators = document.querySelectorAll('.operator');
  const lastChar = expression.value.slice(-1);
  const isOperator = ['+', '-', '*', '/'].includes(lastChar);

  operators.forEach((operator) => {
    if (isOperator) {
      operator.setAttribute('disabled', '');
    } else {
      operator.removeAttribute('disabled');
    }
  });
}

function getResult() {
  if (expression.value.endsWith('/0')) {
    expression.value = '오류';
  } else if (expression.value) {
    const result = eval(expression.value);
    expression.value = result;
  }
}

function clickClear() {
  expression.value = '';
}
