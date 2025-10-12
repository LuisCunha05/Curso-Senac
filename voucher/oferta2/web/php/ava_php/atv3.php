<?php

    for ($i=1; $i <= 100; $i++) { 
        if(!($i % 3) && !($i % 5)){
            echo "$i: AB";
        }else if(!($i % 3)){
            echo "$i: A";
        }else if(!($i % 5)){
            echo "$i: B";
        }else{
            echo "$i: $i";
        }
        echo "<br>";
    }
?>