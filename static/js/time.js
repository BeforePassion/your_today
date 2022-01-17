function getTime() {
    const date = new Date();

    let hour = date.getHours();
    let min = date.getMinutes();

    if (hour > 12) {
        hour -= 12;
    }

    hour = hour < 10 ? '0' + hour : hour;
    min = min < 10 ? '0' + min : min;

    let result = hour + ':' + min;

    document.getElementById('time').innerHTML = result;
}

function init() {
    getTime();
    setInterval(getTime, 1000);
}

init();