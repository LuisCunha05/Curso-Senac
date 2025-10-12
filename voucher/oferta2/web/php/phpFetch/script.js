document.addEventListener('DOMContentLoaded', function() {
    // Select all forms with class 'ajax-form' (you can change this selector)
    const forms = document.querySelectorAll('form.form-js');
    const loggout = document.getElementById('loggout')

    if(loggout){
        loggout.addEventListener('click', () => {
            fetch('./loggout.php', {
                method: 'post',
                credentials:"same-origin",
                headers: {
                    'X-Requested-With': 'XMLHttpRequest' // Optional header to identify AJAX requests
                }
            })
            .then(response => window.location.href = "./index.html")
            .catch(err => console.log({err}))
        })
    }
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent default form submission
            
            // Get form data
            const formData = new FormData(form);
            
            // Optional: Add loading state
            form.classList.add('loading');
            
            // Fetch to PHP endpoint
            fetch(form.action, {
                method: form.method,
                body: formData,
                credentials:"same-origin",
                headers: {
                    'X-Requested-With': 'XMLHttpRequest' // Optional header to identify AJAX requests
                }
            })
            .then(response => {
                // Remove loading state
                form.classList.remove('loading');
                
                if (response.status === 200) {
                    // Form is valid - success case
                    form.classList.add('success');
                    form.classList.remove('error');
                    
                    // Optional: Reset form after success
                    form.reset();
                    
                    if(window.location.href.includes('index')){
                        console.log('mudara')
                        const id = setTimeout(() => {
                            clearTimeout(id)
                            console.log('mudadando')
                            window.location.href = "./teste.php"
                        }, 3000)
                    }
                    // Optional: Show success message
                    // alert('Form submitted successfully!');

                    
                    
                    // You can redirect here if needed
                    // window.location.href = '/success-page';
                    
                } else if (response.status === 422) {
                    // Form is invalid - validation errors
                    form.classList.add('error');
                    form.classList.remove('success');
                    
                    // Parse JSON response to get error messages
                    return response.json().then(errors => {
                        // Handle validation errors (example clears previous errors)
                        clearErrors(form);
                        displayErrors(form, errors);
                    });
                } else {
                    // Handle other status codes
                    throw new Error('Server response was not OK');
                }
            })
            .catch(error => {
                form.classList.remove('loading');
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
        });
    });
    
    // Helper function to clear previous errors
    function clearErrors(form) {
        // Remove existing error messages
        const errorMessages = form.querySelectorAll('.error-message');
        errorMessages.forEach(el => el.remove());
        
        // Remove error classes from inputs
        const errorInputs = form.querySelectorAll('.error');
        errorInputs.forEach(el => el.classList.remove('error'));
    }
    
    // Helper function to display new errors
    function displayErrors(form, errors) {
        for (const field in errors) {
            if (errors.hasOwnProperty(field)) {
                // Find the input element
                const input = form.querySelector(`[name="${field}"]`);
                if (input) {
                    // Add error class to input
                    input.classList.add('error');
                    
                    // Create error message element
                    const errorElement = document.createElement('div');
                    errorElement.className = 'error-message';
                    errorElement.textContent = errors[field];
                    errorElement.style.color = 'red';
                    
                    // Insert after input (adjust based on your HTML structure)
                    input.parentNode.insertBefore(errorElement, input.nextSibling);
                }
            }
        }
    }
});

