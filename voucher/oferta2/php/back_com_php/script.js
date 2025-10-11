
/**
 * 
 * @param {InputEvent} event 
 */
const maskPhone = (event) => {
    /**
     * @type {string}
     */
    let oldValue = event.target.value

    oldValue = oldValue
        .replace(/\D/g, '')
        .replace(/(^\d{2})(\d)/g, '($1)$2')
        .replace(/(\(\d{2}\)\d{4})(\d)/g, '$1-$2')
        .replace(/(\(\d{2}\)\d{4}-\d{4})(\d)/g, '$1')

    event.target.value = oldValue
}

/**
 * 
 * @param {InputEvent} event 
 */
const maskIdade = (event) => {
    /**
     * @type {string}
     */
    let oldValue = event.target.value

    oldValue = oldValue
        .replace(/^(1[01]?\d|120|[1-9]?[0-9])(\d)$/g, '$1')

    event.target.value = oldValue
    console.log(oldValue)
}


document.getElementById('iCelular').addEventListener('input', maskPhone)
document.getElementById('iIdade').addEventListener('input', maskIdade)