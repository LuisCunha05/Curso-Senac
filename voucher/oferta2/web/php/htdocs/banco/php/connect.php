<?php
    $host = '10.28.2.34';
    $user = 'suporte';
    $password = 'suporte';
    $database = 'turma139';

    $db = new mysqli($host,$user,$password,$database);

    if($db->connect_errno){
        echo "erro: " . $db->connect_error;
    }else{
        echo $db->host_info . "<br><br>";
    }
?>