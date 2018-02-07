
RESPONSE_ID = "response";
OUTPUT_ID = "output";

function respond() {
    response = document.getElementById(RESPONSE_ID);
    output = document.getElementById(OUTPUT_ID);

    userOk = (response.value == "ok");
    userGood = (response.value == "good");
    userBad = (response.value == "bad");
    userNotOk = (response.value == "not ok");

    if (userOk || userGood) {
        output.innerHTML = "That's good.";
    } else if (userBad || userNotOk) {
        output.innerHTML = "That's not good.";
    } else {
        output.innerHTML = "I don't understand";
    }
}
