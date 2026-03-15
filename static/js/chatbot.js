// SEND MESSAGE FUNCTION
function sendMessage(){

let input = document.getElementById("userInput");
let message = input.value.trim();

if(message === "") return;

let chatbox = document.getElementById("chatbox");

// USER MESSAGE
chatbox.innerHTML += `
<div class="message user-message">
<div class="bubble">${message}</div>
<img src="/static/images/user.png">
</div>
`;

input.value = "";

// BOT TYPING INDICATOR
let typingId = "typing-" + Date.now();

chatbox.innerHTML += `
<div class="message bot-message" id="${typingId}">
<img src="/static/images/bot.jpg">
<div class="bubble typing">
<span></span>
<span></span>
<span></span>
</div>
</div>
`;

chatbox.scrollTop = chatbox.scrollHeight;

// SEND MESSAGE TO SERVER
fetch("/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:message})
})
.then(response => response.json())
.then(data => {

document.getElementById(typingId).remove();

chatbox.innerHTML += `
<div class="message bot-message">
<img src="/static/images/bot.jpg">
<div class="bubble">${data.reply}</div>
</div>
`;

chatbox.scrollTop = chatbox.scrollHeight;

})
.catch(error => {

document.getElementById(typingId).remove();

chatbox.innerHTML += `
<div class="message bot-message">
<img src="/static/images/bot.jpg">
<div class="bubble">⚠️ Sorry, something went wrong.</div>
</div>
`;

});

}


// ENTER KEY SEND
document.addEventListener("DOMContentLoaded", function(){

let input = document.getElementById("userInput");

input.addEventListener("keypress", function(event){

if(event.key === "Enter"){
event.preventDefault();
sendMessage();
}

});

});


// AUTO WELCOME MESSAGE
window.onload = function(){

let chatbox = document.getElementById("chatbox");

chatbox.innerHTML += `
<div class="message bot-message">
<img src="/static/images/bot.jpg">
<div class="bubble">
Hello 👋<br><br>
I am the <b>Smart College AI Assistant</b>.<br><br>
You can ask me about:<br>
• Admissions<br>
• Courses<br>
• Departments<br>
• Academics<br>
• Contact details
</div>
</div>
`;

};