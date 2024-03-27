
const chat = document.querySelector(".chat");
const inputText = document.getElementById("inputText");
const btn = document.querySelector(".plane");


const santaPhrases = [
    "No gifts for you this year.",
    "You've been a naughty kid.",
    "Wait until next year for your presents",
    "I don't feel like arguing",
    "Give me some fucking milk and biscuits",
    "Where's my damn reindeer?"
]

btn.addEventListener("click", () => {
    let random = Math.floor(Math.random() * santaPhrases.length);
    let santaSays = santaPhrases[random];

    let pU = document.createElement("p");
    pU.innerHTML = inputText.value;
    pU.classList.add("userMessage");
    chat.appendChild(pU);
    inputText.value = "";
    chat.scrollTop = chat.scrollHeight;

    let typing = document.createElement("p");
    typing.innerHTML = "Santa is typing...";
    typing.style.fontSize = "1.3rem";
    chat.appendChild(typing);
    setTimeout(() => {
        let pS = document.createElement("p");
        pS.innerHTML = santaSays;
        pS.classList.add("santaMessage");
        chat.appendChild(pS);
        chat.scrollTop = chat.scrollHeight;
        chat.removeChild(typing);
    }, 2000);

})



inputText.addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
        let random = Math.floor(Math.random() * santaPhrases.length);
        let santaSays = santaPhrases[random];

        let pU = document.createElement("p");
        pU.innerHTML = inputText.value;
        pU.classList.add("userMessage");
        chat.appendChild(pU);
        inputText.value = "";
        chat.scrollTop = chat.scrollHeight;

        let typing = document.createElement("p");
        typing.innerHTML = "Santa is typing...";
        typing.style.fontSize = "1.3rem";
        chat.appendChild(typing);
        setTimeout(() => {
            let pS = document.createElement("p");
            pS.innerHTML = santaSays;
            pS.classList.add("santaMessage");
            chat.appendChild(pS);
            chat.scrollTop = chat.scrollHeight;
            chat.removeChild(typing);
        }, 2000);
    }
})

