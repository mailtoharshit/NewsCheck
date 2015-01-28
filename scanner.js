/*
* Copyright (c) 2015.
* Author- Harshit Pandey
* Feed Reader Script - Class for Reading URL feed through crawler script
*Endpoint URL - http://timesofindia.indiatimes.com/feeds/newsfeed/-2128936835.cms?feedtype=sjson
*/

function injscript() {
    var script = document.createElement("script");
    script.src = "//code.jquery.com/jquery-2.1.3.min.js";
    script.onload = script.onreadystatechange = function(){ /* your callback here */ };
    document.body.appendChild( script );
}

//Hold temp data for third iteration
var dataArray  = [];

//Method to make Ajax call and push data into array
function times(){
var timesAPI = "http://timesofindia.indiatimes.com/feeds/newsfeed/-2128936835.cms?feedtype=json";
$.getJSON( timesAPI, {})
  .done(function( data ) 
  {$.each(data, function(key, value) {
       $.each(value, function(key, value){
       dataArray.push(value);  //push third level nested value
  });
})});}

//Jscript doesnt hold and wait for context to finish, hence in chrome console run this command individually to test
//populate array 
times();
//print array
dataArray;

//clean up array - last part under contrustion, once this work, I can parse through url and dump on a page.
for (i = 0; i < 4; i++) {dataArray.shift();}
var stories = [];
function scan(data){ 
  $.each(data, function(idx, obj){ 
      $.each(obj, function(key, value){ 
          if(key.toString().toLowerCase() ==="story")
          console.log(key + ": " + value);
      });
  }); }


