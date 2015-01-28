var dataArray  = [];

//Method to make Ajax call and push data into array
function times(){
var timesAPI = "http://timesofindia.indiatimes.com/feeds/newsfeed/-2128936835.cms?feedtype=json";
$.getJSON( timesAPI, {})
  .done(function( data ) 
  {$.each(data['NewsItem'], function(key, value) {
       if (value.Story.div.div['#text']) dataArray.push({url: value.WebURL, text: value.Story.div.div['#text'].join('')});  //push third level nested value
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