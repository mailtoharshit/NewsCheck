//Endpoint URL - http://timesofindia.indiatimes.com/feeds/newsfeed/-2128936835.cms?feedtype=sjson


var dataArray  = [];

//Method to make Ajax call and push data into array
function times(){
var timesAPI = "http://timesofindia.indiatimes.com/feeds/newsfeed/-2128936835.cms?feedtype=json";
$.getJSON( timesAPI, {})
  .done(function( data ) 
  {$.each(data, function(key, value) {
       $.each(value, function(key, value){
       dataArray.push(value);
  });

})});}

//populate array 
times();
//print array
dataArray;

//clean up array
for (i = 0; i < 4; i++) {dataArray.shift();}

var stories = [];
function scan(data){ 
  $.each(data, function(idx, obj){ 
      $.each(obj, function(key, value){ 
          if(key.toString().toLowerCase() ==="story")
          console.log(key + ": " + value);
      });
  }); }


