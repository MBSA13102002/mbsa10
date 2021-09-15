<?php

require __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;


$factory = (new Factory())
    ->withServiceAccount('php-mbsa-firebase-adminsdk-63hg6-b8a626ef89.json')
    ->withDatabaseUri('https://php-mbsa-default-rtdb.firebaseio.com/');

    $database = $factory->createDatabase();



?>