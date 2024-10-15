function start(){
    for (let x = 10; x > 1; x -= 2)
        console.log("hello");
    let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];

    for(let number of numbers){
        //console.log(number)
        if(number & 1) continue

        console.log(number)
    }
}
start()