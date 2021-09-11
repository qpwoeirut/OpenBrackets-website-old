function setActiveNav(pageName) {
    console.log(pageName + "-nav");
    document.getElementById(pageName + "-nav").classList.add("active");
    const dropdownButton = document.querySelector("#" + pageName + "-nav button.dropdown-toggle");
    if (dropdownButton) {
        dropdownButton.classList.add("active");
    }
}