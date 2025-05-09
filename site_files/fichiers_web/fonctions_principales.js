// l'arriere plan
function bg_color(){
    var color1 = "rgb(75, 75, 75)";
    var color2 = "rgb(221, 221, 221)";
    if (document.body.style.background == color1){
        document.body.style.backgroundColor = color2;
    }else{
        document.body.style.background = color1;
    }
}

// ouvrir et fermer la partie 1
function rap_ouv_I() {
    if (document.getElementById("somm1_1").style.display == "none") {
        document.getElementById("somm1_1").style.display = "block";
        document.getElementById("ouv_img_1").style.transform = 'rotate(0deg)';
    } else {
        document.getElementById("somm1_1").style.display = "none";
        document.getElementById("ouv_img_1").style.transform = 'rotate(-90deg)';
    }
}

// ouvrir et fermer la partie 2
function rap_ouv_II() {
    if (document.getElementById("somm2_1").style.display == "none") {
        document.getElementById("somm2_1").style.display = "block";
        document.getElementById("ouv_img_2").style.transform = 'rotate(0deg)';
    } else {
        document.getElementById("somm2_1").style.display = "none";
        document.getElementById("ouv_img_2").style.transform = 'rotate(-90deg)';
    }
}


// asombrir a la navigation rapide
const box = document.getElementById("panneau_droite");

box.addEventListener("mouseenter", () => {
    var color1 = "rgb(75, 75, 75)";
    var color2 = "rgb(221, 221, 221)";
    var color3 = "rgb(0, 0, 1)";
    var color4 = "rgb(0, 0, 0)";
    if (document.body.style.background == color1){
        document.body.style.background = color3;
    }else{
        document.body.style.background = color4;
    }
    document.getElementById("la_page").style.opacity = "0.1";
});

box.addEventListener("mouseleave", () => {
    var color1 = "rgb(75, 75, 75)";
    var color2 = "rgb(221, 221, 221)";
    var color3 = "rgb(0, 0, 1)";
    var color4 = "rgb(0, 0, 0)";
    if (document.body.style.background == color3){
        document.body.style.background = color1;
    }else{
        document.body.style.background = color2;
    }
    document.getElementById("la_page").style.opacity = "1";
});