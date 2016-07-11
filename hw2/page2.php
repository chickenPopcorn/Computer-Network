<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>page2</title>
  </head>
  <body>
    <h2>Get Cookie</h2>

    <?php
    if (!isset($_COOKIE["input"])){
      echo "Cookie value empty";
    }
    else{
      echo "Cookie value is " . $_COOKIE["input"];
    }
    ?>

    <form action="index.php" method="GET">
      <button type=submit>Back</button>
    </form>
  </body>
</html>

<html>
<head>
<title>page 2</title>
</head>
<body>

</body>
