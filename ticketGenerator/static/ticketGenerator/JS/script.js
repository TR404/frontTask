

//Copy text using Click Button Today's offer 3 buttons.

	document.getElementById("cp_btn").addEventListener("click", copy_password);

function copy_password() {
    var copyText = document.getElementById("pwd_spn");
    var textArea = document.createElement("textarea");
    textArea.value = copyText.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("Copy");
    textArea.remove();
    
    
}

	document.getElementById("cp_btn1").addEventListener("click", copy_password);

function copy_password() {
    var copyText = document.getElementById("pwd_spn1");
    var textArea = document.createElement("textarea");
    textArea.value = copyText.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("Copy");
    textArea.remove();
}

	document.getElementById("cp_btn2").addEventListener("click", copy_password);

function copy_password() {
    var copyText = document.getElementById("pwd_spn2");
    var textArea = document.createElement("textarea");
    textArea.value = copyText.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("Copy");
    textArea.remove();
}
