// 네이버에서 특정한 도메인 메일만 체크하기
const mailElements = document.querySelectorAll('.mail');

mailElements.forEach((mailElement) => {
  const senderButton = mailElement.querySelector('.button_sender');
  if (senderButton) {
    const senderEmail = senderButton.getAttribute('title');
    if (senderEmail.includes('spotv.net')) {
      const checkBox = mailElement.querySelector('.button_checkbox_wrap input[type="checkbox"]');
      checkBox.checked = true;
    }
  }
});
