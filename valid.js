function validate(e){
    e.preventDefault();
    var myemail=document.getElementById("email").innerHTML;
    var mypassword=document.getElementById("password").innerHTML;
    var myage=document.getElementById("age").innerHTML;
    var msgbox=document.getElementById("message").innerHTML;
    let message= ""
  if (email==""){
    message="Please enter email";
    msgbox.style.color="red";

  }
  else if(pass==""){
    message="Please enter password";
    msgbox.style.color="red";
  }
  else if(age==""){
    message="Please enter age";
    msgbox.style.color="red";
  }
  else{
    message ="login successful!";
    msgbox.style.color="green";
  }
  msgbox.innerHTML="message";
}
