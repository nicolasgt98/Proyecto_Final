Nombre Proyecto: ReminderMate - Aplicación Web para gestión de recordatorios

Autor: Nicolás Garcés Toro

Correo: nicolasgt98@hotmail.com

Justificación: ReminderMate es una aplicación web diseñada para la gestión simple de recordatorios y fechas importantes

Modelos: Se crearon 3 modelos: tareas, eventos y pagos. Todos los modelos cuentan con los siguientes campos en común.

(Nota: Los campos con * son obligatorios)

a. Nombre*: Permite al usuario ingresar el nombre de la tarea/pago/evento para una fácil identificación
b. Etiqueta*: Permite al usuario indicar una etiqueta para agrupar tareas/pagos/eventos
c. Recordatorio*: Permite al usuario ingresar una fecha que ayudará a gestionar tareas/pagos/eventos priorizando las fechas más próximas.
	La idea de este campo es que el usuario ingrese una fecha anterior a la fecha límite del pago/finalización de la tarea o fecha del evento para que en próximas actualizaciones de la aplicación, cada día salgan en la pantalla principal, los recordatorios según esta fecha.
d. Descripción: Permite al usuario indicar datos adicionales
		

Explicación de cada modelo

1. Tareas: En este modelo se pretende que el usuario pueda ingresar una tarea con un plazo máximo, es decir, que se puede terminar antes de esta fecha
	Fecha Límite*: Fecha máxima para completar la tarea

2. Eventos: En este modelo se pretende que el usuario pueda ingresar un evento llevado a cabo un día en específico
	Lugar*: Lugar del evento
	Fecha del Evento*: Fecha específica en la que se lleva a cabo el evento

3. Pagos:En este modelo se pretende que el usuario pueda ingresar un pago programado que se debe realizar con un plazo máximo
	Fecha Límite de Pago*: Fecha máxima para hacer el pago
	Valor*: Valor que se debe pagar
	Proveedor*: Proveedor al que se debe pagar

Comentarios adicionales

1. La sección del contenido con el título "Recordatorio"s en la página "home" se actualizará para una próxima versión. Acá se pretende añadir una tabla en la que cada día aparecerán únicamente las tareas/pagos/eventos cuya fecha recordatorio es igual o mayor a la fecha actual. Esto con el objetivo de usar esta vista para priorizar y no saturarnos con tantas tareas/pagos/eventos.

2. Las vistas "Sobre Mi" y "Contacto" estarán disponibles para una próxima versión

3. Pendiente corregir el archivo "styles.css" pues no logré hacer que el css se leyera desde ahí, por lo que tuve que recurrir a agruparlo en el header del mismo archivo "home.html" (Si me pueden guiar en esta parte se los agradezco)

4. Pendiente corregir la altura de los títulos de los modelos, pues están pegados a toda la margen superior, a diferencia del título en la página principal que si está separado (Si me pueden guiar acá también se los agradezco pues no supe como corregir esto)

5. Las demás funcionalidades como crear, actualizar, eliminar y otras adicionales se incluirán en la próxima versión


Usuarios:

Usuario: coderhouse
Contraseña: coder12345


Usuario: prueba2
Contraseña: nicolas123

