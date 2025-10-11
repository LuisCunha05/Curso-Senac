<?php
    session_start();
    include('./verificacao.php');
    include('./verificacao_admin.php');

    echo "Nome: " . $_SESSION["name"] . "<br>";
    echo "Setor: " . $_SESSION["setor"] . "<br>";
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastrar Cliente</title>
    <?php include('./link_style.php');?>
</head>
<body>
    <a href="./admin.php">Home</a>
    <a href="./logout.php">Sair</a>
    <br>
    <br>
    <form action="action_user.php" method="post">
        <p>Nome: <input type="text" name="nome" id="i_nome"></p>
        <p>Sobrenome: <input type="text" name="sobrenome" id="i_snome"></p>
        <p>Telefone: <input type="text" name="telefone" id="i_telefone"></p>
        <p>Endereço: <input type="text" name="endereco" id="i_endereco"></p>
        <p>Email: <input type="text" name="email" id="i_email"></p>
        <fieldset>
            <legend>Sexo</legend>
            <input type="radio" name="sexo" id="i_sexo1" value="Masculino" checked>Masculino
            <input type="radio" name="sexo" id="i_sexo2" value="Feminino">Feminino
        </fieldset>
        <input type="submit">Cadastrar
    </form>
</body>
</html>