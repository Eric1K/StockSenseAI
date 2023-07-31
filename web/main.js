function predictGraph() {
    //graph("SPY", "2021-6-01", "2023-5-30", 100, "1d", True)
    var ticker = document.getElementById("ticker").value;
    var start = document.getElementById("start").value;
    var end = document.getElementById("end").value;
    var period = parseInt(document.getElementById("period").value);
    //maybe add custom time frames
    console.log(ticker);
    console.log(start);
    console.log(end);
    console.log(period);

    //eel.dummy("this is eel")(function(ret){console.log(ret)})
    //eel.graph(paramters)(runthis function after)

    eel.graph(ticker,start,end,period,"1d", "False");
}