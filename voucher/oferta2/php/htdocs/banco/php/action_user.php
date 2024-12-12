<?php
    session_start();
    include('./verificacao.php');
    include('./verificacao_admin.php');
    include('./connect.php');

    $nome = mysqli_real_escape_string($db, $_POST["nome"]);
    $s_nome = mysqli_real_escape_string($db, $_POST["sobrenome"]);
    $telefone = mysqli_real_escape_string($db, $_POST["telefone"]);
    $endereco = mysqli_real_escape_string($db, $_POST["endereco"]);
    $email = mysqli_real_escape_string($db, $_POST["email"]);
    $sexo = mysqli_real_escape_string($db, $_POST["sexo"]);

    $query_insert = "insert into cliente(nome,sobrenome,telefone,endereco,email,sexo) values ('$nome', '$s_nome', '$telefone', '$endereco', '$email', '$sexo');";

    try{
        $result = mysqli_query($db, $query_insert);
    }

    catch(mysqli_sql_exception $e){
        echo $e;
        echo "<script>
                alert('Erro ao efetuar cadastro!');
                window.location.href = 'admin.php';
            </script>";
    }

    // echo $result;
    if(!$result){
        echo "<script>
                alert('Erro ao efetuar cadastro!');
                window.location.href = 'admin.php';
            </script>";
    }

    echo    "<p>
                Cliente: $nome, $s_nome, $telefone, $endereco, $email, $sexo <br>
                Adicionado com sucesso!
            </p>";

?>