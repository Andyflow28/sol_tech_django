// Funcionalidades JavaScript para el proyecto

// Cerrar automáticamente las alertas después de 5 segundos
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
});

// Validación de formularios
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            const requiredFields = form.querySelectorAll('[required]');
            let valid = true;
            
            requiredFields.forEach(function(field) {
                if (!field.value.trim()) {
                    valid = false;
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!valid) {
                event.preventDefault();
                event.stopPropagation();
                
                // Mostrar mensaje de error general
                const errorDiv = document.createElement('div');
                errorDiv.className = 'alert alert-accent mt-3';
                errorDiv.textContent = 'Por favor, complete todos los campos requeridos.';
                form.appendChild(errorDiv);
                
                // Hacer scroll al primer error
                const firstInvalid = form.querySelector('.is-invalid');
                if (firstInvalid) {
                    firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        });
    });
});

// Funcionalidad para copiar API Key
document.addEventListener('DOMContentLoaded', function() {
    const copyButtons = document.querySelectorAll('.copy-api-key');
    
    copyButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const apiKey = this.getAttribute('data-api-key');
            navigator.clipboard.writeText(apiKey).then(function() {
                // Mostrar mensaje de éxito
                const originalText = button.innerHTML;
                button.innerHTML = '<i class="bi bi-check"></i> Copiado';
                button.classList.add('btn-success');
                
                setTimeout(function() {
                    button.innerHTML = originalText;
                    button.classList.remove('btn-success');
                }, 2000);
            }).catch(function(err) {
                console.error('Error al copiar: ', err);
            });
        });
    });
});