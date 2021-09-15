<?php


include("dbcon.php");
if(isset($_POST["btn-submit"])){

    $name = $_POST['user_name'];
    $number = $_POST['user_number'];
    $email = $_POST['user_email'];


$postData = [

    'name'=> $name,
    'number'=> $number,
    'email'=> $email,
];

$postRef = $database->getReference('/posts')->push($postData);
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <h1 class="text-center">
        FIREBASE INSTALLATION AND CONNECTION WITH PHP
    </h1>
    <form action="index.php" method="POST">
    <div class="container">
    <div class="form-group m-3">
        <input type="text" class="form-control" name = "user_name" placeholder = "Enter Your Name">
    </div>
    <div class="form-group m-3">
        
        <input type="number" class="form-control" name = "user_number" placeholder = "Enter Your Number">
    </div>
    <div class="form-group m-3">
        <input type="email" class="form-control"  name = "user_email" placeholder = "Enter Your Email ID">

    </div>
     <div class="form-group m-3">
         <button class="btn btn-primary" name="btn-submit" type="submit">SUBMIT DATA</button>

     </div>
    </div>
    </form>

</body>
</html>