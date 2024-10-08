function start(){
    let num = 1
    let interval_id = setInterval(() => console.log(num++), 1000)

    setTimeout(() => clearInterval(interval_id), 10000)
}
start()