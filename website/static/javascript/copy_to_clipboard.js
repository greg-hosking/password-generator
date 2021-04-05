function copyToClipboard() {
    // Get the text field
    let passwordTextbox = document.getElementById("password-textbox");

    // Select the text field
    passwordTextbox.select();
    passwordTextbox.setSelectionRange(0, 99999); // For mobile devices

    // Copy the text inside the text field
    document.execCommand("copy");

    // Alert the copied text
    alert("Copied the text: " + passwordTextbox.value);
}
