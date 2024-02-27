const Counter = (function () {
    let privateVal = 0;

    function change(val) {
        privateVal += val
    }

    return {
        add: function () {
            change(1)
        },
        minus: function () {
            change(-1)
        },
        value: function () {
            return privateVal
        }
    }
})()



console.log(Counter.value())

counter1.add()
counter1.add()
counter2.add()

console.log(counter1.value())
console.log(counter2.value())