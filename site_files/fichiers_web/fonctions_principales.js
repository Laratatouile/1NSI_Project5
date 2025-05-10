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

// ouvrir et fermer la partie 3
function rap_ouv_III() {
    if (document.getElementById("somm3_1").style.display == "none") {
        document.getElementById("somm3_1").style.display = "block";
        document.getElementById("ouv_img_3").style.transform = 'rotate(0deg)';
    } else {
        document.getElementById("somm3_1").style.display = "none";
        document.getElementById("ouv_img_3").style.transform = 'rotate(-90deg)';
    }
}

// ouvrir et fermer la partie 4
function rap_ouv_IV() {
    if (document.getElementById("somm4_1").style.display == "none") {
        document.getElementById("somm4_1").style.display = "block";
        document.getElementById("ouv_img_4").style.transform = 'rotate(0deg)';
    } else {
        document.getElementById("somm4_1").style.display = "none";
        document.getElementById("ouv_img_4").style.transform = 'rotate(-90deg)';
    }
}

// ouvrir et fermer la partie 5
function rap_ouv_V() {
    if (document.getElementById("somm5_1").style.display == "none") {
        document.getElementById("somm5_1").style.display = "block";
        document.getElementById("ouv_img_5").style.transform = 'rotate(0deg)';
    } else {
        document.getElementById("somm5_1").style.display = "none";
        document.getElementById("ouv_img_5").style.transform = 'rotate(-90deg)';
    }
}

// ouvrir et fermer la partie 6
function rap_ouv_VI() {
    if (document.getElementById("somm6_1").style.display == "none") {
        document.getElementById("somm6_1").style.display = "block";
        document.getElementById("ouv_img_6").style.transform = 'rotate(0deg)';
    } else {
        document.getElementById("somm6_1").style.display = "none";
        document.getElementById("ouv_img_6").style.transform = 'rotate(-90deg)';
    }
}

// ouvrir et fermer la partie 7
function rap_ouv_VII() {
    if (document.getElementById("somm7_1").style.display == "none") {
        document.getElementById("somm7_1").style.display = "block";
        document.getElementById("ouv_img_7").style.transform = 'rotate(0deg)';
    } else {
        document.getElementById("somm7_1").style.display = "none";
        document.getElementById("ouv_img_7").style.transform = 'rotate(-90deg)';
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