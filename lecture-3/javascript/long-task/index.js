function yieldToMain() {
    return new Promise(resolve => {
        setTimeout(resolve, 0);
    });
}

const batchCount = 1000;
const batchSize = 1000000;

const buildChank = (offset) => {
    return new Array(batchSize).fill().map((item, index) => offset + index)
}

const performArray = (array) => {
    let i = 0;

    while (i < batchCount) {
        array.push(buildChank(batchSize * i));
        i++;
    }
}


const performArrayAsync = async (array) => {
    let i = 0;

    while (i < batchCount) {
        array.add(buildChank(Number(Number(batchSize) * i)));
        i++;
        await yieldToMain();
    }
}

async function runAsync() {
    const array = new Set();

    console.time('perform async')

    await performArrayAsync(array)

    console.log(array.size)

    console.timeEnd('perform async')
};

function runChunk() {
    const array = [];
    console.time('perform chunk')

    performArray(array)

    console.log(array.reduce((total, current) => total + current.length, 0))

    console.timeEnd('perform chunk')
}

function runDefault() {
    console.time('perform default')
    const array = new Array(batchCount * batchSize).fill().map((item, index) => index);

    console.log(array.length)

    console.timeEnd('perform default')
}

(async function () {

    setInterval(() => {
        const newEl = document.createElement('div')
        document.getElementById('indicator').appendChild(newEl)
    }, 100)

        
    setTimeout(() => {
        runAsync()
    }, 2000)
    //runDefault();
    //runChunk();
    //await runAsync();
})()