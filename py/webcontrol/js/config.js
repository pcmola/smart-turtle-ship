var SERVER_IP = "192.168.0.8";
webiopi().ready(function() {
    //Get Alarm TIme
    getAlarmTime();
    
    //Set Alarm Time
    setAlarmTime();  
}); 


function getAlarmTime() {
    url= "http://" + SERVER_IP + ":8000/macros/getAlarmTime/"; // url to the pi -> http is required 
     
     jQuery.ajax({                          
            url: url,                        
            type: 'POST',
            success: function(data){  
            $('#hourValue').val(data.slice(0,2));
            $('#minValue').val(data.slice(3,5));   
            //alert(data)
            },
            error :function() {                    
            alert('Sorry, something went wrong :-(')},
     })    
}

function setAlarmTime() {
    $("#submit").click(function() { 
        hourValue = $('#hourValue').val();   // set the hour value
        minValue  = $('#minValue').val();    // set the minute value
        url= "http://" + SERVER_IP + ":8000/macros/setAlarmTime/" + hourValue + ":" + minValue; // url to the pi -> http is required 
         
         jQuery.ajax({                          
                url: url,                        
                type: 'POST',
                success: function(data){        
                alert('Alarm was set')
                },
                error :function() {                    
                alert('Sorry, something went wrong :-(')},
         })
    })
}
