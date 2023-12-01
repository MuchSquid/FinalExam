# FinalExam

## Respuestas ejercicio 3:

### Modificar la Lógica de Negocio: 

 - Agrega un método en la clase Cuenta para verificar el total transferido en el día y compáralo con el límite de 200 soles antes de permitir una nueva transferencia.

### Actualizar Pruebas Unitarias: 

 - Incluye nuevos casos de prueba para verificar que la restricción funciona correctamente: una prueba para transferencias dentro del límite, otra para cuando se intenta exceder el límite, una tercera para múltiples transferencias en un día y una última prueba para confirmar que el límite se resetea al día siguiente.

### Gestionar Riesgos: 
 - Realiza pruebas de regresión para asegurarte de que los cambios no afecten las funcionalidades existentes, y considera un despliegue gradual con monitoreo cuidadoso para detectar y corregir rápidamente cualquier problema.
