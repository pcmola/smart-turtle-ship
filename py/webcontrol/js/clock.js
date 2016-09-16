var GPIO_ARRAY = [22, 23, 24, 25];
webiopi().ready(function() {
    /*
    GPIO PIN 세 개(22~24) ON/OFF에 따라 표시할 지역 결정
    000 : 서울
    001 : 뉴욕
    010 : 베이징
    011 : 런던
    100 : 파리
    101 : 시드니
    */
    webiopi().setFunction(GPIO_ARRAY[0],"out"); //city1
    webiopi().setFunction(GPIO_ARRAY[1],"out"); //city2
    webiopi().setFunction(GPIO_ARRAY[2],"out"); //city3
    webiopi().setFunction(GPIO_ARRAY[3],"out"); //on_off
    
    var content, button;
    content = $("#content");
    
    button = webiopi().createMacroButton("jong", "", "jong_strike");
    content.append(button);

    button = webiopi().createMacroButton("book", "", "book_strike");
    content.append(button);

    button = webiopi().createMacroButton("jing", "", "jing_strike");
    content.append(button);

});

$(document).ready(function() {
    //시차 설정(서울 기준)
    var OFFSET_NEWYORK = -13;
    var OFFSET_BEIJING =  -1;
    var OFFSET_LONDON  =  -8; //런던은 3월 마지막 일요일~10월 마지막 일요일 써머타임
    var OFFSET_PARIS   =  -7;
    var OFFSET_SYDNEY  =   1;    

    activateCity("seoul");
 
    $("#seoul_bg").click(function(){
        unactivateCityAll();
        activateCity("seoul");
        webiopiControl(0, 0, 0);
    });
    
    $("#newyork_bg").click(function(){
        unactivateCityAll();
        activateCity("newyork");
        webiopiControl(0, 0, 1);
    });
    
    $("#beijing_bg").click(function(){
        unactivateCityAll();
        activateCity("beijing");
        webiopiControl(0, 1, 0);
    });

    $("#london_bg").click(function(){
        unactivateCityAll();
        activateCity("london");
        webiopiControl(0, 1, 1);
    });

    $("#paris_bg").click(function(){
        unactivateCityAll();
        activateCity("paris");
        webiopiControl(1, 0, 0);
    });
    
    $("#sydney_bg").click(function(){
        unactivateCityAll();
        activateCity("sydney");
        webiopiControl(1, 0, 1);
    });        
        
    //도시 명 세팅
    $("#seoul_city").html("Seoul&nbsp");
    $("#newyork_city").html("New York&nbsp");
    $("#beijing_city").html("Beijing&nbsp");
    $("#london_city").html("London&nbsp");
    $("#paris_city").html("Paris&nbsp");
    $("#sydney_city").html("Sydney&nbsp");

    //도시별, 시간의 10의 자리 세팅(1~12시 표시 기준)
    setInterval( function() {
        var hours = new Date().getHours();
        $("#seoul_hours1").html(calcHours1(hours));
        
        var newyork_hours = resetHours(hours, OFFSET_NEWYORK);
        $("#newyork_hours1").html(calcHours1(newyork_hours));
        
        var beijing_hours = resetHours(hours, OFFSET_BEIJING);
        $("#beijing_hours1").html(calcHours1(beijing_hours));
        
        var london_hours = resetHours(hours, OFFSET_LONDON);
        $("#london_hours1").html(calcHours1(london_hours));
        
        var paris_hours = resetHours(hours, OFFSET_PARIS);
        $("#paris_hours1").html(calcHours1(paris_hours));
        
        var sydney_hours = resetHours(hours, OFFSET_SYDNEY);
        $("#sydney_hours1").html(calcHours1(sydney_hours));
        
    }, 1000);


    //도시별 시간의 1의 자리 세팅(1~12시 표시 기준)
    setInterval( function() {
        var hours = new Date().getHours();
        $("#seoul_hours2").html(calcHour2(hours));
            
        var newyork_hours = resetHours(hours, OFFSET_NEWYORK);
        $("#newyork_hours2").html(calcHour2(newyork_hours));
        
        var beijing_hours = resetHours(hours, OFFSET_BEIJING);
        $("#beijing_hours2").html(calcHour2(beijing_hours));
        
        var london_hours = resetHours(hours, OFFSET_LONDON);
        $("#london_hours2").html(calcHour2(london_hours));
        
        var paris_hours = resetHours(hours, OFFSET_PARIS);
        $("#paris_hours2").html(calcHour2(paris_hours));
                
        var sydney_hours = resetHours(hours, OFFSET_SYDNEY);
        $("#sydney_hours2").html(calcHour2(sydney_hours));
    }, 1000);
        
    //도시별 분의 10의 자리 세팅
    setInterval( function() {
        var minutes = new Date().getMinutes();
        $("#seoul_min1").html(Math.floor(minutes/10, 1));
        $("#newyork_min1").html(Math.floor(minutes/10, 1));
        $("#beijing_min1").html(Math.floor(minutes/10, 1));
        $("#london_min1").html(Math.floor(minutes/10, 1));
        $("#paris_min1").html(Math.floor(minutes/10, 1));
        $("#sydney_min1").html(Math.floor(minutes/10, 1));
    },1000);
        
    //도시별 분의 1의 자리 세팅
    setInterval( function() {
        var minutes = new Date().getMinutes();
        $("#seoul_min2").html(minutes-(Math.floor(minutes/10)*10));
        $("#newyork_min2").html(minutes-(Math.floor(minutes/10)*10));
        $("#beijing_min2").html(minutes-(Math.floor(minutes/10)*10));
        $("#london_min2").html(minutes-(Math.floor(minutes/10)*10));
        $("#paris_min2").html(minutes-(Math.floor(minutes/10)*10));
        $("#sydney_min2").html(minutes-(Math.floor(minutes/10)*10)); 
        
    },1000);                

}); 


//시간 10의 자리 표시
function calcHours1(hours) {
    if(hours == 10 || hours == 11 || hours == 12 || hours == 22 || hours == 23 || hours == 0){
        return "1"
    } else {
        return "&nbsp;"
    }
}


//시간 1의 자리 표시
function calcHour2(hours) {
    if(hours == 0){
        return "2"
    }
    if(hours >= 1 && hours <= 9){
        return hours
    } 
    if(hours >= 10 && hours <= 12){
        return hours-10
    }
    if(hours >= 13 && hours <= 21){
        return hours-12
    }
    if(hours >= 22 && hours <= 23){
        return hours-22
    }
}

//시차(서울 기준)에 따른 시간 재설정
function resetHours(hours, offset) {
    if ((hours+offset) >= 24) {
        return hours+offset-24;
    }
    if ((hours+offset) >= 0 && (hours+offset)<= 23) {
        return hours+offset;
    }
    if ((hours+offset) < 0) {
        return hours+offset+24;
    }
}

function activateCity(city) {
    $("#"+city+"_city").css({"color": "#202020"});
    $("#"+city+"_bg").css({"background": "#BBBBBB"});
    $("#"+city+"_hours1").css({"color": "#008F2E"});
    $("#"+city+"_hours2").css({"color": "#2060B4"});
    $("#"+city+"_min1").css({"color": "#C10000"});
    $("#"+city+"_min2").css({"color": "#FFD90A"});
}

function unactivateCity(city) {
    $("#"+city+"_city").css({"color": "#bbbbbb"});
    $("#"+city+"_bg").css({"background": "#202020"});
    $("#"+city+"_hours1").css({"color": "#bbbbbb"});
    $("#"+city+"_hours2").css({"color": "#bbbbbb"});
    $("#"+city+"_min1").css({"color": "#bbbbbb"});
    $("#"+city+"_min2").css({"color": "#bbbbbb"});
}

function unactivateCityAll() {
    unactivateCity("seoul");
    unactivateCity("newyork");
    unactivateCity("beijing");
    unactivateCity("london");
    unactivateCity("paris");
    unactivateCity("sydney");
}

function webiopiControl(var1, var2, var3) {
    webiopi().digitalWrite(GPIO_ARRAY[0], var1);
    webiopi().digitalWrite(GPIO_ARRAY[1], var2);
    webiopi().digitalWrite(GPIO_ARRAY[2], var3); 
}
