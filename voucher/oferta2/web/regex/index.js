// document.write(/[\bx]/.test('123x'))
const data = /^(0[1-9]|[1-2]\d|3[0-1])\/(0[1-9]|1[0-2])\/([1-9]{1}|1\d{0,3}|20(1\d|2[0-4]))$/;
const reg_email = /^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$/
///document.write(data.test('01/01/3333'))

function validateEmail(){
    const inputs = document.getElementsByClassName('required');

    for(let i = 0;i <inputs.length; i++){
        console.log(inputs[i].value)
        console.log(reg_email.test(inputs[i].value))
        if(!reg_email.test(inputs[i].value))
            setInputMessage('O email deve ter o padrão nome@empresa.com', 'red', i)
        else
            setInputMessage('O email validado', 'blue', i, true)
    }

}

/**
 * Altera menssagem do span e cor
 * @param {string} text Menssagem a ser exibida
 * @param {string} color Cor da menssagem
 * @param {number} index Index da Classe a ser utilizada
 * @param {boolean} temporary Se a mensagem será removido após 2 segundos
 */
function setInputMessage(text, color = 'black', index = 0, temporary = false){
    const element = document.getElementsByClassName('span_required')
    element[index].textContent = text
    element[index].style.display = 'block'
    element[index].style.color = color

    if(temporary){
        const id_timeout = setTimeout(callback => {
            document.getElementsByClassName('span_required')[index].style.display = 'none'
            window.clearTimeout(id_timeout)
        }, 2000)
    }
}