// Initialize Firebase
var config = {
    apiKey: "AIzaSyBbjWaJsINCmpUKSDacUi8NVgO-i9Wx5hA",
    authDomain: "messaging-rishavb123.firebaseapp.com",
    databaseURL: "https://messaging-rishavb123.firebaseio.com",
    projectId: "messaging-rishavb123",
    storageBucket: "",
    messagingSenderId: "354766583193"
};
firebase.initializeApp(config);

function updateScroll(){
    var element = document.getElementById("messages");
    element.scrollTop = element.scrollHeight;
}

var textForEventListener = document.getElementById('textfield');
console.log(textForEventListener)



var object = {
    
}

var size = 0;
var dbRef = firebase.database().ref()
var full = dbRef.child("Messages")
full.on('value', function(snap){
    var messages = document.getElementById('messages');
    var msgs = "";
    var title = document.getElementById('title');
    size = snap.val().length;
    
    object = {

    }
    for (value in snap.val()) {
        object[value] = snap.val()[value];
        msgs+="<p>"+snap.val()[value]+"</p>";
        title.innerHTML = snap.val()[value];
    }

    messages.innerHTML = msgs;
    
    updateScroll();
    
});

function enter(e) {
    if( e.keyCode == 13 )
        send();
}


function send() {
    var title = document.getElementById('title');
    var text = document.getElementById('textfield');

    object[size] = text.value;
    title.innerHTML = text.value;
    size++;
    
    full.set(object);
    
    updateScroll();
    text.value="";
    
}
