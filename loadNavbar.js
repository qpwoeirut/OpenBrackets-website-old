function loadNavbar(pageName) {
    console.log(pageName + "-nav");
    $("nav#navbar").load("navbar.html", function() {
        document.getElementById(pageName + "-nav").classList.add("active");
    });
}