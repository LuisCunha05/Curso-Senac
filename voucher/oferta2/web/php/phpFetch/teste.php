<?php
    session_start();
    if(!isset($_SESSION["user"]) || ($_SESSION["user"] != "admin")){
        header("location:./index.html");
        exit();
    }
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./style.css">
    <title>Form Request</title>
</head>
<body>
    <form class="form-js" method="POST" action="./form.php">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">
        </div>
        <div>
            <label for="email">Email:</label>
            <input id="email" name="email">
        </div>
        <button type="submit">Submit</button>
    </form>
    <button id="loggout">Voltar</button>
    <script src="./script.js"></script>
</body>
</html>