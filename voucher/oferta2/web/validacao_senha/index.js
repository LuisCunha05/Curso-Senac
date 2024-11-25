function validateSenha1(){
    const input_senha1 = document.getElementById('senha_1')
    if(input_senha1.value.length < 6)
        setInputMessage('A senha precisa ter no mínimo 6 caracteres', 'green', 0)
    else if(!input_senha1.value.includes('$'))
        setInputMessage("A senha deve conter pelo menos um '$'", 'orange', 0)
    else
        setInputMessage('Senha válida!', 'blue', 0, true)
}      

function validateSenha2(){
    const input_senha2 = document.getElementById('senha_2')
    if(input_senha2.value.length < 6)
        setInputMessage('A senha precisa ter no mínimo 6 caracteres', 'green', 1)
    else if(!input_senha2.value.includes('$'))
        setInputMessage("A senha deve conter pelo menos um '$'", 'orange', 1)
    else if(input_senha2.value != document.getElementById('senha_1').value)
        setInputMessage('As senhas precisam ser iguais!', 'red', 1)
    else    
        setInputMessage('Senha correta!', 'blue', 1, true)
}

/**
 * Altera menssagem do span e cor
 * @param {string} text Menssagem a ser exibida
 * @param {string} color Cor da menssagem
 * @param {number} index Index da Classe a ser utilizada
 * @param {boolean} temporary Se a mensagem será removido após 2 segundos
 */
function setInputMessage(text, color = 'black', index = 0, temporary = false){
    document.getElementsByClassName('span_required')[index].textContent = text
    document.getElementsByClassName('span_required')[index].style.display = 'block'
    document.getElementsByClassName('span_required')[index].style.color = color

    if(temporary){
        const id_timeout = setTimeout(callback => {
            document.getElementsByClassName('span_required')[index].style.display = 'none'
            window.clearTimeout(id_timeout)
        }, 2000)
    }
}