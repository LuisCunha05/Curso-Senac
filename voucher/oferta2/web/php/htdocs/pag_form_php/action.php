<?php
    /**
     * Pula linha e adiciona uma tag hr. Separador
     */
    function br(){
        echo "<br><hr>";
    }

    $input_nome = $_POST['input_nome'];
    $input_idade = $_POST['input_idade'];
    $input_sistema = $_POST['sistema'];

    echo "Nome digitado: " . $_POST['input_nome'];
    br();
    echo "Idade digitada: " . $_POST['input_idade'];
    br();
    echo "Sistema escolhido: " . $_POST['sistema'];
    br();
    echo "Melhores professores:<br>";
    foreach ($_POST['prof'] as $name){
        echo "&emsp;$name<br>";
    }

    
?>