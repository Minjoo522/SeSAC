const expression = document.querySelector('.form-control');

function inputValue(value) {
  if (expression.value === '오류') {
    expression.value = value;
  } else {
    expression.value += value;
  }
  checkFirstValue(value);
  checkLastValue();
}

function checkFirstValue(value) {
  if (expression.value === '0' || expression.value === null) {
    expression.value = value === '0' ? '' : value;
  }
}

function checkLastValue() {
  const operators = document.querySelectorAll('.operator');
  const lastValue = expression.value.slice(-1);
  const isOperator = ['+', '-', '*', '/'].includes(lastValue);

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
