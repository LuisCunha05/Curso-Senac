<?php
// Captura todos os dados enviados pelo formulário
$dadosFormulario = $_POST;

// Exibe os dados no console usando JavaScript
echo "<script>console.log(" . json_encode($dadosFormulario) . ");</script>";

// Outra opção é exibir os dados em um formato legível na página
echo "<pre>";
print_r($dadosFormulario);
echo "</pre>";
?>
