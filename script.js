function showAlert() {
  alert("Button clicked! This is a UI test alert.");
}

// Shopping cart logic for products.html
const cart = [];

function addToCart(product) {
  cart.push(product);
  document.getElementById("cart").innerHTML =
    "<strong>Cart:</strong> " + cart.join(", ");
}

// Contact form logic for contact.html
window.onload = function() {
  var contactForm = document.getElementById("contactForm");
  if (contactForm) {
    contactForm.onsubmit = function(e) {
      e.preventDefault();
      const name = contactForm.name.value;
      const email = contactForm.email.value;
      const message = contactForm.message.value;
      document.getElementById("formResult").innerHTML =
        `<p>Thank you, <strong>${name}</strong>! We received your message:</p>
         <blockquote>${message}</blockquote>
         <p>We will respond to <strong>${email}</strong> soon.</p>`;
      contactForm.reset();
    };
  }
};