<?php
    // echo $_SESSION["setor"] . " " . $_SESSION["setor"] != 1;

    if($_SESSION["setor"] != 1){
        header("location:../index.html");
    }
?>