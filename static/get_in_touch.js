
document.addEventListener('DOMContentLoaded', function () {
    const inputFields = document.querySelectorAll('.input-text');

    inputFields.forEach((input) => {
      // Check if the input field is not empty when the page loads
      if (input.value) {
        input.classList.add('not-empty');
      }

      input.addEventListener('input', function () {
        if (input.value) {
          input.classList.add('not-empty');
        } else {
          input.classList.remove('not-empty');
        }
      });
    });
  });

