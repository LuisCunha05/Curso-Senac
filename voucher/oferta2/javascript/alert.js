function main(){
    let width = window.prompt("Type the width of the box?", '10');
    let height = window.prompt("Type the height of the box?", '10');
    let length = window.prompt("Type the length of the box?", '10');
    const volume = +width * height * length
    console.log(volume) 
}

main()