const chevronRef = document.querySelectorAll("#chevron")
const needsValidationFormRef = document.querySelectorAll('needs-validation');

chevronRef.addEventListener("click", e => {
  chevronRef.classList.remove('fa-chevron-down');
  chevronRef.classList.add('fa-chevron-up');
});