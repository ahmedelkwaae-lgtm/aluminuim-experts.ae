document.addEventListener('DOMContentLoaded', function(){
  // Toggle mobile menu
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      nav.classList.toggle('open');
    });
  }

  // Contact form validation (client-side)
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function(e){
      const usesFormspree = form.getAttribute('action')?.includes('formspree.io');
      if (!usesFormspree) e.preventDefault();

      const name = form.querySelector('#name');
      const email = form.querySelector('#email');
      const message = form.querySelector('#message');
      const status = document.getElementById('formStatus');

      let valid = true;

      // Name
      if (!name.value.trim()) { showError(name, true); valid = false; }
      else { showError(name, false); }

      // Email
      const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim());
      if (!emailOk) { showError(email, true); valid = false; }
      else { showError(email, false); }

      // Message
      if (!message.value.trim()) { showError(message, true); valid = false; }
      else { showError(message, false); }

      if (!valid) {
        if (status) {
          status.textContent = 'يرجى إكمال الحقول المطلوبة بشكل صحيح.';
          status.style.color = '#b00020';
        }
        return;
      }

      if (!usesFormspree) {
        if (status) {
          status.textContent = 'تم إرسال رسالتك بنجاح (محاكاة). عدّل الكود للربط الفعلي.';
          status.style.color = '#0a8f3a';
        }
        form.reset();
      }
    });

    function showError(input, show){
      const msg = input.parentElement.querySelector('.error-msg');
      if (!msg) return;
      msg.style.display = show ? 'block' : 'none';
      input.style.borderColor = show ? '#b00020' : '#ddd';
    }
  }
});
