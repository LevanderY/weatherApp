window.onload = function() {

    let d = new Date;
    let year = d.getFullYear();
    document.getElementById("year").innerHTML = year;

    VANTA.CLOUDS({
        el: "#main",
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 200.00,
        minWidth: 200.00,
        cloudColor: 0x437ed4,
        speed: 1.90
    });
}