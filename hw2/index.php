<!DOCTYPE html>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
  if (!empty($_POST["name"])){
    setcookie("input", $_POST["name"], time()+ 60*3, "/");
    header("Refresh:0");
  }
}
?>

<html>
  <head>
    <meta charset="utf-8">
    <title>index page</title>
  </head>

  <body>
  <form name="Cookie Submit" action="" method="POST">
    Cookie Submit: <input type="text" name="name">
    <input type="submit" value="Submit">
  </form>

  <form action="page2.php" method="GET">
    <form method="GET" action='page2.php'>
    <button type=submit>Cookie</button>
  </form>
  </body>

</html>
