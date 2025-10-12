
<?php
    // echo $_SESSION["name"] . "<br>" . !$_SESSION["name"];
    if(!$_SESSION["name"]){
        header("location:../index.html");
    }
?>