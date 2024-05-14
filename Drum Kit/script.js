
function playSound(instrument){
    if (instrument == "tom"){
        var audio = new Audio("Sounds/tom.wav");
    }else if (instrument == "bass"){
        var audio = new Audio("Sounds/bass.wav");
    }else if (instrument == "crash"){
        var audio = new Audio("Sounds/crash.wav");
    }else if (instrument == "clap"){
        var audio = new Audio("Sounds/clap.wav");
    }
    
    audio.play();
}