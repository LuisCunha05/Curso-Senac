
/**
 * 
 * @param {HTMLInputElement} element 
 */
const numberMask = (element) => {

    let value = element.value;

    value = value.replace(/[^0-9.]/g, '');

    const decimalCount = (value.match(/\./g) || []).length;
    if (decimalCount > 1) {
        value = value.slice(0, -1);
    }

    element.value = value;
    
}