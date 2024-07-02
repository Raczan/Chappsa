function validateForm() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var errorMsg = document.getElementById('error-msg');

    if (name.trim() === '' || email.trim() === '') {
      errorMsg.innerText = 'Por favor, complete todos los campos.';
      return false;
    } else {
      errorMsg.innerText = '';
      return true;
    }
  }