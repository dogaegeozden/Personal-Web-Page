// Creating variables by selecting elements from the DOM.
const hamburgerBtn = document.querySelector(".Icon"),
    navBar = document.querySelector("#MyTopNav"),
    dropDownBtn = document.querySelector(".DropBtn"),
    dropDownCont = document.querySelector(".DropDownContent"),
    dropDownBtn2 = document.querySelector(".DropBtn2"),
    dropDownCont2 = document.querySelector(".DropDownContent2");

// Event listener for the hamburger button.
hamburgerBtn.addEventListener("click", toggleNavBar);

// Event listener for the dropdown button.
dropDownBtn.addEventListener("click", function(){
    toggleDropDownMenu(id=1)
});

dropDownBtn2.addEventListener("click", function(){
    toggleDropDownMenu(id=2)
});

function toggleNavBar() {

    // Close dropdowns if they are open
    closeDropDown(1);
    closeDropDown(2);

    // Toggle responsive class for navigation bar
    navBar.className = navBar.className === "TopNav" ? "TopNav Responsive" : "TopNav";
    
};

function toggleDropDownMenu(id) {

    if (id==1) {

        // Toggle the dropdown menu
        if (dropDownCont.className === "DropDownContent") {
        
            openDropDown(id);
        
        } else {
        
            closeDropDown(id);
        
        }

    } else {
        
        
        // Toggle the dropdown menu
        if (dropDownCont2.className === "DropDownContent2") {
            
            openDropDown(id);
        
        } else {
        
            closeDropDown(id);
        
        }
    }
};

function openDropDown(id) {

    if (id==1) {
        // Open the dropdown menu
        dropDownCont.style.display = "block";
        
        dropDownCont.setAttribute("class", "DropDownContent Close");
        
        changeIconClass(id, "fa-caret-up", "fa-caret-down");

    } else {

        // Open the dropdown menu
        dropDownCont2.style.display = "block";

        dropDownCont2.setAttribute("class", "DropDownContent2 Close");
        
        changeIconClass(id, "fa-caret-up", "fa-caret-down");
    }

};

function closeDropDown(id) {
    
    if (id==1) {

        // Close the dropdown menu
        dropDownCont.style.display = "none";
        
        dropDownCont.setAttribute("class", "DropDownContent");
        
        changeIconClass(id, "fa-caret-down", "fa-caret-up");
    
    } else {

        // Close the dropdown menu
        dropDownCont2.style.display = "none";

        dropDownCont2.setAttribute("class", "DropDownContent2");
        
        changeIconClass(id, "fa-caret-down", "fa-caret-up");

    }

};

function changeIconClass(id, oldClass, newClass) {

    if (id==1) {

        // Change the class of the dropdown button icon
        const dropDownBtnIco = document.querySelector(`#CaretBtn1`);
        
        if (dropDownBtnIco) {
        
            dropDownBtnIco.setAttribute("class", `fa-solid ${newClass}`);
        
        }

    } else {

        // Change the class of the dropdown button icon
        const dropDownBtnIco2 = document.querySelector(`#CaretBtn2`);

        if (dropDownBtnIco2) {
        
            dropDownBtnIco2.setAttribute("class", `fa-solid ${newClass}`);
        
        }

    }

};