document.addEventListener("DOMContentLoaded", function () {
  const messageBox = document.getElementById('messages-notes-main');
  if (messageBox) {
    setTimeout(() => {
      messageBox.style.display = 'none';
    }, 4000);
  }
});