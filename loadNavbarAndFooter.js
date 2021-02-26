function loadNavbarAndFooter(pageName) {
    console.log(pageName + "-nav");
    $("nav#navbar").load("/OpenBracketsWebsite/navbar.html", function() {
        document.getElementById(pageName + "-nav").classList.add("active");
        const dropdownButton = document.querySelector("#" + pageName + "-nav button.dropdown-toggle");
        if (dropdownButton) {
            dropdownButton.classList.add("active");
        }
    });
    $("footer#footer").load("/OpenBracketsWebsite/footer.html");
}