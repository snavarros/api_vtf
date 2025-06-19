# Proyecto VTF_TEAM

Este proyecto tiene como finalidad que el equipo VTF tanto Regional como Dirnac puedan acceder y realizar tareas automatizadas en pro de mejorar procesos y responder a distintas necesidades.

El sistema se basa en roles, tal que las regiones solo puedan ver informacion relacionada a su REGION. Desde DIRNAC podran ver informacion global de todo el pais y los usuarios que sean Administradores puedan tener mayores privilegios, tales como; administrar usuarios.

Los usuarios deben autenticarse para poder ingresar a este sistema.

## 🚀 Fase 1: Diseño del Proyecto

Estructura Base con Clean Architecture
Clean Architecture se basa en separar responsabilidades en capas bien definidas. 

### 🧠 Clean Architecture: Filosofía General
La Clean Architecture busca aislar las reglas del negocio del resto del sistema (frameworks, bases de datos, entradas/salidas). Así logramos:

* Escalabilidad.
* Bajo acoplamiento.
* Testeabilidad.
* Flexibilidad tecnológica (cambiar DB o framework sin afectar la lógica de negocio).

#### Clean Arquitecture + Screaming

Por " quien eres y tipo"

https://youtu.be/y3MWfPDmVqo?si=kBDOjrv8sA9P5eYn

✅ USUARIO FUNCIONALIDADES
1. Crear usuario
2. Resetear contraseña con código enviado por correo
3. Actualizar usuario
4. Desactivar usuario (activo/inactivo)


### TODO List

- [ ] Autenticacion y Autorizacion de usuarios
- [ ] FRONTEND REACT login usuarios.
- [ ] Envio de Proyeccion Presupuestaria.
- [ ] Crear Dockers and Postgres
- [ ] Crear Orquestador


### Caracteristicas FUTURAS (Requiere autorizacion de TI)
- [ ] Autenticarse con la cuenta de correo JUNJI.
- [ ] Almacenar informacion en SHAREPOINT.
- [ ] Cambiar contrasenia a traves del correo institucional.
- [ ] Notificaciones a traves de Microsoft Teams.





### Component Test

docker-compose -f docker-compose-dev.yml exec web pytest --verbose tests/

### Docker commands

docker-compose -f docker-compose-dev.yml up -d --build

#### Develop to docker
Si estas desarrollando algo e instalaste librerias

[ ]  Freeze requirements

No esta refrescando los tests, porque estan fuera de app y docker lee desde app los cambios









