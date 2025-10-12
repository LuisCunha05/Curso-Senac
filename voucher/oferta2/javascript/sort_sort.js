function start(){
    let numbers = [50, 10, 40, 30, 30, 20];

    /* function compareNumbers(a, b) {
        let retVal = 0;
        if (a < b) {
        retVal = -1;
        } else if(a > b) {
        retVal = 1;
        }
        return retVal;
    } */

let sorted = numbers.sort((a, b) => a == b || a > b ? 1 : -1 );
console.log(sorted); // [10, 20, 30, 40, 50]
}
start()