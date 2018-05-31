const net = require('./network.js');

function async(func) {
    async function afunc(...args) {
        let response = await func(...args);
        return await response.json();
    }
    return afunc;
}

export { async}