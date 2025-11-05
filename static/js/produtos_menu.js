document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.getElementById("menu_icon");
  const nav = document.querySelector("nav");

  menuIcon.onclick = () => {
    nav.classList.toggle("open");
    menuIcon.classList.toggle("bx-x");
  };
});
