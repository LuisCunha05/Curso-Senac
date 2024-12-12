<?php
    $input_nome = $_POST["input_nome"];
    $input_rg = $_POST["input_rg"];
    $input_cpf = $_POST["input_cpf"];
    $input_endereco = $_POST["input_endereco"];
    $input_idade = $_POST["input_idade"];
    $input_sexo = $_POST["input_sexo"];
    $input_data = $_POST["input_data"];
    $input_cor = $_POST["input_cor"];
    $input_estacao = $_POST["input_estacao"];//Array
    $input_pet = $_POST["input_pet"];
    $input_achocolatado = $_POST["input_achocolatado"];
    $input_bolacha = $_POST["input_bolacha"];
    $input_idioma = $_POST["input_idioma"];
    $input_dia = $_POST["input_dia"];
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="dados.css">
    <title>Dados</title>
</head>
    <body>
        <h2>Dados do Usuário</h2>
        <table>
            <tr>
                <th>Nome</th>
                <th>RG</th>
                <th>CPF</th>
                <th>Endereço</th>
                <th>Idade</th>
                <th>Sexo</th>
                <th>Data</th>
                <th>Cor</th>
                <th>Estação do Ano</th>
                <th>Pet</th>
                <th>Achocolatado</th>
                <th>Bolacha</th>
                <th>Idioma</th>
                <th>Dia</th>
            </tr>
            <tr>
                <td><?php echo $input_nome?></td>
                <td><?php echo $input_rg?></td>
                <td><?php echo $input_cpf?></td>
                <td><?php echo $input_endereco?></td>
                <td><?php echo $input_idade?></td>
                <td><?php echo $input_sexo?></td>
                <td><?php echo $input_data?></td>
                <td><?php echo $input_cor?></td>
                <td>
                    <?php
                        foreach($input_estacao as $value){
                            echo "$value<br>";
                        }
                    ?>
                </td>
                <td><?php echo $input_pet?></td>
                <td><?php echo $input_achocolatado?></td>
                <td><?php echo $input_bolacha?></td>
                <td><?php echo $input_idioma?></td>
                <td><?php echo $input_dia?></td>
            </tr>
        </table>
    </body>
</html>