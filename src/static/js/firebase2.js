 var config = {
    apiKey: "AIzaSyA-Cv6idM2tNQ-ZuIO6QYmiyIPQhrV-O70",
    authDomain: "student-chapter-3740d.firebaseapp.com",
    databaseURL: "https://student-chapter-3740d.firebaseio.com",
    projectId: "student-chapter-3740d",
    storageBucket: "student-chapter-3740d.appspot.com",
    messagingSenderId: "686657493418"
  };
  firebase.initializeApp(config);

  var contactRef =firebase.database().ref('contact1');

  document.getElementById('contact1').addEventListener('submit', contactForm);

  function contactForm(e) {
     e.preventDefault();

     var name = getInputVal('name');
     var email = getInputVal('email2');
     var phone = getInputVal('phone');
     var message = getInputVal('message')


     //Save Contact us
     saveContact(name,email,phone,message)

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

 function  saveContact(name,email2,phone,message) {
     var contactRef = contactRef.push();
     newcontactRef.set({
     	 name : name,
     	 email : email2,
     	 phone : phone,
     	 message : message
     })

}