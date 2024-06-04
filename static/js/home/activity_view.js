// A global variable to track whether the script should run
let shouldRunScript = false;

// Check if all necessary elements are available before running the script
function checkElements() {
    let sAIB = document.querySelectorAll(".SAIB");
    let sATB = document.querySelectorAll(".SATB");

    // Check if the necessary elements are present
    if (sAIB.length > 0 && sATB.length > 0) {
        shouldRunScript = true;
        runScript();
    }
}

// Run the script only when shouldRunScript is true
function runScript() {
    if (shouldRunScript) {
        // Creating an array from the elements that have SAIB class.
        let sAIB = document.querySelectorAll(".SAIB"),
        // Creating an array from the elements that have SATB class.
            sATB = document.querySelectorAll(".SATB");

        function classifyElements() {
            // A function that sets the class attribute of specific elements.

            // Looping through each element in sAIB array
            for (let i = 0; i < sAIB.length; i++) {
                // Creating a boolean variable called oddOrEvenIdent, which returns true if the division of an integer is giving another integer
                let oddOrEvenIdent = Number.isInteger(i / 2);

                // If a number's division by 2 gives an integer, that means that number is an even number.
                // Checking if the oddOrEvenIdent variable is equal to false, which is equal to an odd number
                if (oddOrEvenIdent == false) {
                    // Setting the element's class to SAIB RightSAIB
                    sAIB[i].setAttribute("class", "SAIB RightSAIB");
                    // Setting the element's class to SATB RightSATB
                    sATB[i].setAttribute("class", "SATB RightSATB");
                // Checking if the oddOrEvenIdent variable is equal to true, which is equal to an odd number
                } else {
                    // Setting the element's class to SAIB LeftSAIB
                    sAIB[i].setAttribute("class", "SAIB LeftSAIB");
                    // Setting the element's class to SATB LeftSATB
                    sATB[i].setAttribute("class", "SATB LeftSATB");
                }
            }
        }

        // Calling the classifyElements function.
        classifyElements();
    }
}

// Listen for the DOMContentLoaded event
document.addEventListener("DOMContentLoaded", function () {
    // Check if all necessary elements are available
    checkElements();
});
