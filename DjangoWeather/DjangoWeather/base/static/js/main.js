$('#lancer').click(function() {
    $.ajax({
        url:'/wheels',
        type:'GET',
        success: function(data){
            if(game) {
                if (countLancer === 0) {
                    game = false;
                } else {
                    countLancer--;
                    spinAnimation()
                    $("#roulette").text(data.roulette1.nom);
                    $("#roulette2").text(data.roulette2.nom);
                    $("#roulette3").text(data.roulette3.nom);
                    let resultat = AnalyzeLancers(data.roulette1, data.roulette2, data.roulette3)
                    console.log(resultat)
                    let liste = [data.roulette1.nom, data.roulette2.nom, data.roulette3.nom];
                    let compteur = 0;
                    for (let i = 0; i < liste.length; i++) {
                        if (liste[i] === betweather) {
                            compteur++;
                        }
                    }
                    let multiplicateur = resultat.multiplicateur;
                    if (compteur === 1 && multiplicateur === 1) {
                        multiplicateur -= 0.5;
                    } else if (compteur === 1 && multiplicateur > 1) {
                        multiplicateur += 0.5;
                    } else if (compteur === 2) {
                        multiplicateur += 1.5;
                    } else if (compteur === 3) {
                        multiplicateur += compteur
                    }

                    let ajout = mise
                    let gainBrut = 0

                    if (gain === 0 && multiplicateur != 1) {
                        ajout = mise * multiplicateur
                        gain += parseInt(ajout)
                        gainBrut = ajout
                    } else if (0 < multiplicateur && multiplicateur < 1) {
                        gain += parseInt(mise * multiplicateur);
                        gainBrut = mise * multiplicateur
                    } else if (multiplicateur === 0){
                        gain = 0
                        gainBrut = 0
                    } else {
                        gain += parseInt(mise * multiplicateur)
                        gainBrut = mise * multiplicateur
                    }

                    countLancer += resultat.lancers_bonus
                    $("#countlancer").text(countLancer);
                    $("#gain").text(gain + " €");

                    gainPreview(gainBrut, resultat.lancers_bonus)
                    onChangeCountLancer(countLancer)
                }
            }
        }
    })
})

$('#rejouer').click(function (){
    window.location.href = '/play'
})


function gainPreview(gainNumber, lancerNumber){
    let gainPreview = document.querySelector('#gainPreview')
    gainPreview.innerHTML = '+ ' + gainNumber + ' €'
    gainPreview.classList.add('active')

    let lancerPreview = document.querySelector('#lancerPreview')
    lancerPreview.innerHTML = '+ ' + lancerNumber
    lancerPreview.classList.add('active')

    setTimeout(() => {
        gainPreview.classList.remove('active')
        lancerPreview.classList.remove('active')
    }, 3000)
}

function onChangeCountLancer(newValue){
    if (newValue === 0){
        $('#rejouer').show()
        $('#lancer').hide()
        $('#recup').show()
    }
}

 function spinAnimation(){
        var imagesContainer = document.querySelectorAll('.images-container');
        imagesContainer[0].classList.add('spin')
        setTimeout(() => {
            imagesContainer[1].classList.add('spin')
        },600)
        setTimeout(() => {
            imagesContainer[2].classList.add('spin')
        },1200)
        setTimeout(() => {
            imagesContainer[0].classList.remove('spin')
            imagesContainer[0].querySelector('img').src = getSrcImage(document.querySelector('#roulette').innerHTML)
        },2200)
        setTimeout(() => {
            imagesContainer[1].classList.remove('spin')
            imagesContainer[1].querySelector('img').src = getSrcImage(document.querySelector('#roulette2').innerHTML)
        },2800)
        setTimeout(() => {
            imagesContainer[2].classList.remove('spin')
            imagesContainer[2].querySelector('img').src = getSrcImage(document.querySelector('#roulette3').innerHTML)
        },3400)
    }


    function getSrcImage(weatherName){
        if (weatherName === "Soleil"){
            return "/static/images/sun.png"
        }else if (weatherName === "Nuages"){
            return "/static/images/cloud.png"
        }else if (weatherName === "Pluie"){
            return "/static/images/rain.webp"
        }else if (weatherName === "Orage"){
            return "/static/images/stormwebp.webp"
        }else if(weatherName === "Vent"){
            return "/static/images/tornado.webp"
        } else if(weatherName === "Chance"){
             return "/static/images/chance.png"
        }
    }

function AnalyzeLancers(roulette1, roulette2, roulette3){
    let resultat = {}
    if(roulette1.nom === roulette2.nom && roulette1.nom === roulette3.nom){
        resultat = {
            'multiplicateur': roulette1.multiplicateur3,
            'lancers_bonus': roulette1.lancers3
        }
    } else if(roulette1.nom === roulette2.nom || roulette1.nom === roulette3.nom || roulette2.nom === roulette3.nom){
        if(roulette1.nom === roulette2.nom){
            resultat = {
                'multiplicateur': roulette1.multiplicateur2 * roulette3.multiplicateur,
                'lancers_bonus': roulette1.lancers2 + roulette3.lancers
            }
        }
        if(roulette2.nom === roulette3.nom){
            resultat = {
                'multiplicateur': roulette2.multiplicateur2 * roulette1.multiplicateur,
                'lancers_bonus': roulette2.lancers2 + roulette1.lancers
            }
        }
        if(roulette1.nom === roulette3.nom){
            resultat = {
                'multiplicateur': roulette1.multiplicateur2 * roulette2.multiplicateur,
                'lancers_bonus': roulette1.lancers2 + roulette2.lancers
            }
        }
    } else {
        resultat = {
                'multiplicateur': roulette1.multiplicateur * roulette2.multiplicateur * roulette3.multiplicateur,
                'lancers_bonus': roulette1.lancers + roulette2.lancers + roulette3.lancers
            }
    }
    return resultat
}

$("#recup").click(function(){
    $.ajax({
        url: '/gain/',
        type: 'GET',
        data: {'gain': gain},
        success: function(response) {
            $("#money").text(response.usermoney + " €")
        }
    });
})

