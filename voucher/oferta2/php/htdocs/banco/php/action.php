<?php
    session_start();
    include("./connect.php");
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cliente</title>
    <link rel="stylesheet" href="./../action.css">
    <?php include('./link_style.php');?>
</head>
<body>

</body>
</html>
<?php
    $nome = mysqli_real_escape_string($db, $_POST["nome"]);

    $senha = mysqli_real_escape_string($db, $_POST["senha"]);


    echo "Nome: $nome; Senha: $senha<br>";
    if (empty($nome) || empty($senha)) {

        echo "<script>
                alert('Por favor, preencha todos os campos.');
                setTimeout(function(){
                    window.location.href = 'index.html';
                }, 2000); // Espera 2 segundos antes de redirecionar
            </script>";
        exit(); 
    }

    $query = "select * from usuario where nome = '{$nome}' and senha = '{$senha}' ";

    $result= mysqli_query($db, $query);
    $retorno = mysqli_fetch_array($result);


    $row = mysqli_num_rows($result);

    if(!$row){
        echo "<script>
                alert('Usuário ou Senha inválida!');
                window.location.href = 'index.html';

                //setTimeout(function(){
                //    window.location.href = 'index.html';
                //}, 2000); // Espera 2 segundos antes de redirecionar
            </script>";
        exit(); 
    }

    echo    "<div id='shadowBox'>
                <h3 class='rainbow rainbow_text_animated'>Bem Vindo! $nome/h3>
            </div>";
    
    $_SESSION["name"] = $nome;
    $_SESSION["setor"] = $retorno['setor'];
    switch ($_SESSION["setor"]) {
        case 1:
            echo    "<script>
                        setTimeout(function(){
                            window.location.href = 'admin.php';
                        }, 2000);
                    </script>";
            break;
        
        case 0:
            echo    "<script>
                        setTimeout(function(){
                            window.location.href = 'common.html';
                        }, 1000);
                    </script>";
            break;
        
        default:
            "<script>
                alert('Setor não encontrado!');
                window.location.href = 'index.html';
            </script>";
            break;
    }
    exit(); 

?>