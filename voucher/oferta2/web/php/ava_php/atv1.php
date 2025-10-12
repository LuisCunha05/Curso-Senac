
<?php


if(isset($_POST["a1_num1"]) && isset($_POST["a1_num2"]) && $_POST["a1_num2"] != '' && $_POST["a1_num1"] != ''){
    $a1_n1 =  $_POST["a1_num1"];
    $a1_n2 =  $_POST["a1_num2"];
    $sum = $a1_n1 + $a1_n2;
    $sub = $a1_n1 - $a1_n2;
    $mul = $a1_n1 * $a1_n2;
    $div = $a1_n1 / $a1_n2;
}else{
    echo "Digite 2 números para visualizar os resultados!<br>";
    echo "<a href='./index.html'>Voltar</a>";
    exit();
}


?>
<a href="./index.html">Voltar</a>
<p>Soma: <?=$sum;?> Tipo: <?= gettype($sum)?></p>
<p>Subtração: <?= $sub?> Tipo: <?= gettype($sub)?></p>
<p>Multiplicação: <?= $mul?> Tipo: <?= gettype($mul)?></p>
<p>Divisão: <?= $div?> Tipo: <?= gettype($div)?></p>