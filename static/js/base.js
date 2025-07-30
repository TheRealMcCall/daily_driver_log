/**
 * Auto-dismisses flash messages (e.g., success/error alerts) after a delay.
 * Triggered when the DOM is fully loaded.
 */
document.addEventListener("DOMContentLoaded", function () {
  const messageBox = document.getElementById('messages-notes-main');
  if (messageBox) {
    setTimeout(() => {
      messageBox.style.display = 'none';
    }, 4000);
  }
});