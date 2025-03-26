<?php
session_start();

if(!$_SESSION["user"] || $_SESSION["user"] != "admin"){
    echo "errrorr!";
    header("location:./index.html");
    exit();
}
// Set header to identify AJAX request
header('X-Requested-With: XMLHttpRequest');

// Validate form data
$errors = [];
$valid = true;

// Example validation
if (empty($_POST['name'])) {
    $errors['name'] = 'Name is required';
    $valid = false;
}

if (!filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
    $errors['email'] = 'Valid email is required';
    $valid = false;
}

// Return appropriate response
if ($valid) {
    // Process valid form data here (save to DB, send email, etc.)
    
    // Return success
    http_response_code(200);
    echo json_encode(['message' => 'Success']);
} else {
    // Return validation errors
    http_response_code(422);
    echo json_encode($errors);
}
?>