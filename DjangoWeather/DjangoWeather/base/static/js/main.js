

$('#lancer').click(function() {
    $.ajax({
        url:'/wheels',
        type:'GET',
        success: function(data){
            if(game) {
                $("#roulette").text(data.roulette1.nom);
                $("#roulette2").text(data.roulette2.nom);
                $("#roulette3").text(data.roulette3.nom);
            }

        }
    })
})