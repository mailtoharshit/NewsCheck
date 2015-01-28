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