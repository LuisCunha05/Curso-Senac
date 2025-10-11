window.onload = function (){

    FahToCel()
    calcularVenda()
    realParaDolar()
}

/**
 * Faz um prompt e retorna um número se o input for válido ou null caso contrário
 * @param {String} prompt
 * @returns {Number|null}
 */
function getNumber(prompt){
    let num = window.prompt(prompt)
    if(isFinite(num) && !isNaN(num))
        return Number(num)
    return null
}

/**
 * Calcula a temperatura de Fahrenheit para Celsius
 */
function FahToCel(){
    let fah;
    while(!fah)
        fah = getNumber('Digite uma temperatura em Fahenrit:')

    alert(`${fah.toFixed(2)} Fahrenheit para Celsius: ${((fah - 32) * (5/9)).toFixed(0)}`)
}

function calcularVenda(){
    let pNome, pQuantidade, pPreco, pDesconto;

    while(!pNome)
        pNome = window.prompt('Digite o nome do produto:')
    while(!pQuantidade)
        pQuantidade = getNumber('Digite a quantidade comprada do produto:')
    while(!pPreco)
        pPreco = getNumber('Digite o preço unitário do produto:')
    while(!pDesconto)
        pDesconto = getNumber('Digite o desconto aplicado a venda, exemplo: 10 para 10%:')
    

    alert(`Compra: 
            Produto: ${pNome}
            Quantidade: ${pQuantidade}
            Preço: ${pPreco}
            Valor a pagar: ${(pPreco*pQuantidade*(1 - (pDesconto/100))).toFixed(2)}`)
}

function realParaDolar(){
    let real, cotacao;

    while(!real)
        real = getNumber('Digite o valor em Real:')
    while(!cotacao)
        cotacao = getNumber('Digite a cotação do dolar:')

    alert(`R$ ${real.toFixed(2)} em dolar: ${(real/cotacao).toFixed(2)}$`)
}