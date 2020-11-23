document.addEventListener("DOMContentLoaded", function () {
    currencyConverter("#example-1");

    currencyConverter("#example-2", {
        fromCurrency: "USD",
        currencyData: {
            USD: 1,
            BTC: 0.000054,
            NGN: 500,
        },
        toCurrency: "NGN"
    });

    currencyConverter("#example-3", {
        withText: false
    });

    const elm = document.getElementById( 'example-4' );
    const cc = currencyConverter(elm, {
        baseAmount: 10,
        fromCurrency: "INR",
        toCurrency: "JPY",
        precision: 2,
        locale: {
            From: "Von",
            To: "Zu",
            INR: "Indian Rupee",
            JPY: "Japanese Yen"
        }
    });


    // Bind the events
    elm.addEventListener( 'onReady', function ( event ) {
        // Set amount
        cc.setAmount( 500 );
    } );

    elm.addEventListener( 'onChange', function ( event ) {
        console.log( event.data );
    } );
});
