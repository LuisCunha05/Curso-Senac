<?php
    session_start();
    include("./verificacao.php");
    include("./verificacao_admin.php");

?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin</title>
    <?php include('./link_style.php');?>
</head>
<body>
    <a href="./user.php" >Cadastrar Cliente</a>
    <br>
    <a href="./relatorio.php">Relatório Produto</a>
    <br>
    <a href="./logout.php" >Sair</a>
</body>
</html>
