
<?php

function calcularArea($num1, $num2){
    return $num1 * $num2;
}

if(isset($_POST["a4_num1"]) && isset($_POST["a4_num2"]) && $_POST["a4_num2"] != '' && $_POST["a4_num1"] != ''){
    $a4_n1 =  $_POST["a4_num1"];
    $a4_n2 =  $_POST["a4_num2"];
}else{
    echo "Digite 2 números para visualizar os resultados!<br>";
    echo "<a href='./index.html'>Voltar</a>";
    exit();
}


?>
<a href="./index.html">Voltar</a>
<p>Área do retangulo: <?=calcularArea($a4_n1, $a4_n2);?></p>
