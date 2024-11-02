

  function toggleMode() {
    document.body.classList.toggle("light-mode");
}

  // JavaScript for toggle functionality
const menuIcon = document.getElementById("menu-icon");
const navbar = document.querySelector(".navbar");

menuIcon.addEventListener("click", () => {
    navbar.classList.toggle("active"); // Toggles 'active' class on the navbar
});


let section = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = ()=>{
    section.forEach(sec =>{
        let top = window.scrollY;
        let Offset = sec.offsetTop - 250;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= Offset && top < Offset + height){
            navLinks.forEach(links =>{
                links.classList.remove('active');
                document.querySelector('.navbar a[href*="' + id + '"]').classList.add('active');
            })
        }
    })
}


// Function to open the popup with the specific image
function openPopup(imageSrc) {
  document.getElementById("popup-img").src = imageSrc;
  document.getElementById("popup").style.display = "flex";
}

// Function to close the popup
function closePopup() {
  document.getElementById("popup").style.display = "none";
}










