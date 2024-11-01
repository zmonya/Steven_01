/*     // Function to set the active link based on scroll position
    window.addEventListener("scroll", () => {
        const sections = document.querySelectorAll("section");
        const navLinks = document.querySelectorAll(".navbar a");

        let currentSection = "";

        // Find the current section based on scroll position
        sections.forEach(section => {
        const sectionTop = section.offsetTop - 80; // Offset to align with navbar height
        if (window.scrollY >= sectionTop) {
            currentSection = section.getAttribute("id");
        }
        });

        // Add 'active' class to the navbar link of the current section
        navLinks.forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href").includes(currentSection)) {
            link.classList.add("active");
        }
        });
    });
 */
    function toggleMode() {
        document.body.classList.toggle("light-mode");
    }


    let menuIcon = document.querySelector('#menu-icon');
    let navbar = document.querySelector('.navber');

    let section = document.querySelectorAll('section');
    let navLinks = document.querySelectorAll('header nav a');

    window.onscroll = ()=>{
        section.forEach(sec =>{
            let top = window.scrollY;
            let Offset =sec.offsetTop - 150;
            let height = sec.offsetHeight;
            let id =sec.getAttribute('id');

            if(top >= Offset && top < Offset + height){
                navLinks.forEach(links =>{
                    links.classList.remove('active');
                    document.querySelector('header nav a [href*=' + id +' ]' ).classList.add
                    ('active');
                })
            }
        })
    }

    menuIcon.onclick = () =>{
        menuIcon.classList.toggle('bx-x');
        navbar.classList.toggle('active');
    }