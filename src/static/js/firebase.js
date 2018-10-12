 var config = {
    apiKey: "AIzaSyA-Cv6idM2tNQ-ZuIO6QYmiyIPQhrV-O70",
    authDomain: "student-chapter-3740d.firebaseapp.com",
    databaseURL: "https://student-chapter-3740d.firebaseio.com",
    projectId: "student-chapter-3740d",
    storageBucket: "student-chapter-3740d.appspot.com",
    messagingSenderId: "686657493418"
  };
  firebase.initializeApp(config);

var messageRef = firebase.database().ref('newsletter');

document.getElementById('subscribe').addEventListener('submit', submitForm);


function submitForm(e) {
     e.preventDefault();

     //Get Values
     var email = getInputVal('email1');

     //Save Message
     saveMessage(email);

     //Show Alert
     document.querySelector('.alert').style.display = 'block';

     //Hide alert after 3 seconds
     setTimeout(function () {
         document.querySelector('.alert').style.display = 'none';
     }, 3000);

     //clear Form
     //document.('subscribe').reset();
 }



 function  getInputVal(id) {
     return document.getElementById(id).value;
 }

 //Save messages to firebase
function  saveMessage(email) {
     var newMessageref = messageRef.push();
     newMessageref.set({
         email: email
     })

}