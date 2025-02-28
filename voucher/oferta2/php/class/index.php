<!DOCTYPE html>
<html>
<body>

<?php
class Goodbye {
  const LEAVING_MESSAGE = "Thank you for visiting W3Schools.com!";
  public $name;

  function __construct($name){
  	$this->name = $name;
  }
  public function byebye() {
    echo self::LEAVING_MESSAGE;
    echo $this->name;
  }
}

$goodbye = new Goodbye("opa!");
$goodbye->byebye();
?>

</body>
</html>
