function main(){
    let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    /**
     * Returns the double of the given number
     * @param {number} num 
     * @returns {number | null}
     */
    const double = num => {
        if( typeof num == 'number'){
            return num * 2
        }
        return null
    }
    
    const doubled = nums.map(number => double(number)).reverse()
    
    doubled.forEach(number => console.log(`Original: ${number}, New: ${number + ' Limões!'}`))
    
    console.log(doubled)
}
//Call the main Function, this ensures that wont be variables left in the global scope
main()