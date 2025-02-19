<?php

    if(isset($_POST["a2_num1"]) && $_POST["a2_num1"] != ''){
        $idade =  $_POST["a2_num1"];
    }else{
        echo "Digite sua idade para visualizar os resultados!<br>";
        echo "<a href='./index.html'>Voltar</a>";
        exit();
    }
?>
<a href="./index.html">Voltar</a>

<?php
    if($idade < 18){
        echo "<p>Você é menor de idade <br>Sua Idade: $idade</p>";
    }else if($idade < 60){
        echo "<p>Você é maior de idade <br>Sua Idade: $idade</p>";
    }else{
        echo "<p>Você é Idoso <br>Sua Idade: $idade</p>";
    }
?>