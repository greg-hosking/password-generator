function getAvailableChars(formData) {

    charGroups = {
        uppercase: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        lowercase: "abcdefghijklmnopqrstuvwxyz",
        numbers  : "0123456789",
        symbols  : "!@#$%^&*-=_+?",
        ambiguous: "{}[]()/\\|'\"`~,;:.<>"
    };
    availableChars = "";

    // Get the data from the form fields
    includeUppercase = formData.get("checkbox-1") == "on";
    includeLowercase = formData.get("checkbox-2") == "on";
    includeNumbers   = formData.get("checkbox-3") == "on";
    includeSymbols   = formData.get("checkbox-4") == "on";
    excludeAmbiguous = formData.get("checkbox-5") == "on";

    // Add the correct character groups to available chars based on form data    
    availableChars = (includeUppercase ? availableChars + charGroups.uppercase : 
                                         availableChars);
    availableChars = (includeLowercase ? availableChars + charGroups.lowercase : 
                                         availableChars);
    availableChars = (includeNumbers   ? availableChars + charGroups.numbers   :
                                         availableChars);
    availableChars = (includeSymbols   ? availableChars + charGroups.symbols   :
                                         availableChars);
    availableChars = (excludeAmbiguous ? availableChars :
                                         availableChars + charGroups.ambiguous);

    return availableChars;
}

function generatePassword() {
    
    // Get the password form element and the password length
    formElement = document.getElementById("password-form");
    formData    = new FormData(formElement);
    passwordLength = formData.get("password-length-select");

    // Get the characters that the password should be made up of
    availableChars = getAvailableChars(formData);

    // Generate the password
    password = "";
    for (i = 0; i < passwordLength; i++) {
        password += availableChars[Math.floor((Math.random() * 
                                               availableChars.length))];
    }

    // Fill the password textbox with the newly-generated password
    document.getElementById("password-textbox").value = password;
}
