const chevronRef = document.querySelectorAll("#chevron")
    
chevronRef.addEventListener("click", e => {
chevronRef.classList.remove('fa-chevron-down');
chevronRef.classList.add('fa-chevron-up');
});


// Bootstrap form validation code from documentation
(function() {
    'use strict';
    window.addEventListener('load', function() {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation');
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();