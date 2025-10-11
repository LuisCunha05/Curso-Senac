<?php
    session_start();

    header('X-Requested-With: XMLHttpRequest');

    // Validate form data
    $errors = [];
    $valid = true;

    // Example validation
    if (empty($_POST['name'])) {
        $errors['name'] = 'Name is required';
        $valid = false;
    }
    if ($_POST['name'] != "admin") {
        $errors['name'] = 'Usuário Incorreto';
        $valid = false;
    }
    
    // Return appropriate response
    if ($valid) {
        // Process valid form data here (save to DB, send email, etc.)
        $_SESSION["user"] = "admin";
        // Return success
        http_response_code(200);
        echo json_encode(['message' => 'Success']);
    } else {
        // Return validation errors
        http_response_code(422);
        echo json_encode($errors);
    }
?>