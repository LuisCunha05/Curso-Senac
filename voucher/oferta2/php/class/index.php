<?php

function br(){
  echo "<br><br>";
}

class Pessoa {
  private $nome;

  public function setNome($nome) {
      $this->nome = $nome;
  }

  public function getNome() {
      return $this->nome;
  }
}

class Funcionario extends Pessoa {
  protected $cargo;

  public function setCargo($cargo) {
      $this->cargo = $cargo;
  }

  public function getCargo() {
      return $this->cargo;
  }

  // public function trabalha(){
  //   echo "$this->nome é trabalhador";
  // }

  // public function setNome(){
  //   $this->nome = 'opa';
  // }
}

$funcionario = new Funcionario();
$funcionario->setNome("Carlos");
$funcionario->setCargo("Desenvolvedor");

echo "Nome: " . $funcionario->getNome() . "<br>";
echo "Cargo: " . $funcionario->getCargo() . "<br>";

?>

