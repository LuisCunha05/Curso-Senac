<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="index.css">
    </head>
    <body>

    <h1>My first PHP page</h1>

    <?php
        $BUTTON_HOVER = '<a class="button" href="#" style="--color:#1e9bff;">
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            Button
                        </a>';

        $nome = "Super name!";

        $num = 3213213.14159265358979323;

        echo "Hello World!\n$nome";

    ?>
    <br>
    <br>
    <br>
    <br>

    <?php
        echo("$BUTTON_HOVER");
    ?>
    <br>
    <br>
    <br>
    <br>
    <?php
        echo number_format($num, 4, ".", ",");
    ?>
    <br>
    <form action="index.php" method="post">
        <label for="coisa11">Nome coisa:</label>
        <input type="text" name="nome_coisa" id="coisa11">
        <input type="submit" value="Opa">
    </form>
    <br>
    <br>
    <br>
    <?php
        $getted = $_POST["nome_coisa"];
        $getted = str_replace('he','HAHA', $getted);
        echo "Valor de nome coisa: $getted";

        /**
         * @param int $x Valor 1
         * @param int $y Valor 2
         * @return int $z result
         */
        function sum(int $x, int $y) {
            $z = $x + $y;
            echo($z);
            return $z;
        }
        echo 5 & (1 << 2);
    ?>

    </body>
</html>