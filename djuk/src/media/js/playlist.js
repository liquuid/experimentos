var play_list = new Array();
var lista;
$(document).ready(function() {
    var current=0;
    $("#player").append('<audio src="" controls="" preload="" >Your browser does not support the audio element.</audio>');
    var a = document.getElementsByTagName('audio')[0];

    $("#playBut").click( function() { a.play(); });
    $("#pauseBut").click( function() { a.pause(); });
    $("#forwBut").click( function() { nextTrack();a.play();drawList(lista);});
    $("#rewBut").click( function()  { prevTrack();a.play();drawList(lista);});

    inter = setInterval(function (){
        $.ajax({
            type: "GET",
            url: "/get_track/",
            dataType: "json",
            success: function(retorno)
            {
                lista = eval(retorno)
                if (lista == null){
                    return;
                    }
                drawList(lista);
                if (a.src!=lista[current].fields['url']){
                    a.src=lista[current].fields['url'];
                }
                a.addEventListener('ended',function(){ $("#player").empty()  },true);
            }

         });
        da = new Date();
//        $("#clock").html(da.getSeconds());
        $("#current").html(current+' '+a.currentTime+' '+a.duration+' '+lista.length);
        if ( a.currentTime >= a.duration ){
            nextTrack();
            a.play();
        }
        if ( current + 1 >= lista.length ){
            current = 0;
            a.play();
        }
        if ( current < 0 ){
            current = lista.length - 1;
            a.play();
        }


        setTimeout(function() {
            if ( isNaN(a.duration) && a.src!=""){
                nextTrack();
                a.play();
            }
        },1000
        );
    },1000 
    );

    function drawList(list){
        for ( i in list){
            if ( i == current ){ 
                play_list[i]='<b>'+list[i].fields['url']+'</b><br>';
            }
            else{
                play_list[i]=list[i].fields['url']+'<br>';
            }
     }

        $("#lista").html(play_list.join(''));
    }

    function nextTrack(){
        current++; a.src=lista[current].fields['url']; a.load();
    }
    function prevTrack(){
        current--; a.src=lista[current].fields['url']; a.load();
    }
});

