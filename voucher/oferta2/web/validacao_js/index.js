function nameValidate(){
    const input_field = document.getElementById('inputEmail')
    console.log(document.getElementsByClassName('span_required')[0].innerText)
    if(!input_field.value.includes('@')){
        console.log('Email precisa ter @')
        setInputMessage('Email precisa ter @', 'orange')

    }else if(input_field.value.split('@')[0].length < 3){
        console.log('O email precisa ter 3 caracteres!!!')
        setInputMessage('O email precisa ter 3 caracteres!!!', 'red')

        }else if(!input_field.value.split('@')[1].includes('.') || input_field.value.split('.')[1].length < 2){
            setInputMessage('Email com domínio inválido', 'purple')
            console.log('Email com domínio inválido')

            }else{
                console.log('Validado com sucesso!')
                setInputMessage('Validado com sucesso!', 'blue')
                const id_timeout = setTimeout(callback => {
                    document.getElementsByClassName('span_required')[0].style.display = 'none'
                    window.clearTimeout(id_timeout)
                }, 2000)
            }
}
/**
 * Altera menssagem do span e cor
 * @param {string} text 
 * @param {string} color 
 */
function setInputMessage(text, color){
    document.getElementsByClassName('span_required')[0].innerText = text
    document.getElementsByClassName('span_required')[0].style.display = 'block'
    document.getElementsByClassName('span_required')[0].style.color = color
}