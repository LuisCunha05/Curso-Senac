<?php
    session_start();
    include("./verificacao.php");
    include("./verificacao_admin.php");
    include('./connect.php');

    echo "<a href='./admin.php'>Home</a>";
    echo "<a href='./logout.php'>Sair</a><br>";


    $query = "select * from produto;";

    $result = mysqli_query($db,  $query);
?>

<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relatório</title>
        <style>
            table, thead, th, td, tbody{
                border: 1px solid #000;
            }
        </style>
        <?php include('./link_style.php');?>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Descrição</th>
                    <th>Preço</th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($retorno = mysqli_fetch_array($result)){?>
                    <tr>
                        <td><?php echo $retorno["id_produto"]; ?></td>
                        <td><?php echo $retorno["nome"]; ?></td>
                        <td><?php echo $retorno["descricao"]; ?></td>
                        <td><?php echo $retorno["preco"]; ?></td>
                    </tr>
                <?php }?>
            </tbody>
        </table>
    </body>
</html>