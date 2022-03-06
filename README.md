# API - Sign Documents
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descripción Y Contexto
Esta API esta construido en el lenguaje Python usando las tecnologias de Django REST Framework

## Requirements
- Python 3.9.10
- Django 4.0.2
- Django REST Framework 3.13.1
- Tensorflow 2.8.0

### Nota
Descarga el [modelo](https://drive.google.com/file/d/1-2abDVQcrRF9CUYRqTMIVXn5f_DGUizW/view?usp=sharing).

## Instalación
Primero, clone el repositorio en su máquina local:
```bash
git clone https://github.com/Sachica/validate_signature.git
```

Después de clonar el repositorio, desea crear un entorno virtual, por lo que tiene una instalación de python limpia.
Puedes hacer esto ejecutando el comando:
```
python -m venv venv
```

Después de esto, es necesario activar el entorno virtual, puede obtener más información al respecto [Aqui](https://docs.python.org/3/tutorial/venv.html)
```
venv\Scripts\activate
```

Luego instalar todas las dependencias requeridas ejecutando el comando:
```
pip install -r requirements.txt
```

### Ejecutar el Proyecto localmente
Finalmente, ejecute el servidor de desarrollo:
```bash
python manage.py runserver
```

El proyecto estará disponible en **127.0.0.1:8000/api/v1/users/**

## Explore Rest APIs
La aplicación define las siguientes API CRUD.

baseURL = http://52.240.59.172:8000

### Files Services

| Method | URL | Decription | Body | 
| ------ | --- | ---------- | --------------------------- |
| GET   | /api/v1/files/ | List files | |
| POST   | /api/v1/files/ | Upload file | [JSON](#upload-file) |
| DELETE   | /api/v1/files/{id_file}/ | Delete files | |

### Auth Services

| Method | URL | Decription | Body | 
| ------ | --- | ---------- | --------------------------- |
| POST   | /api/v1/users/ | Sign up | [JSON](#sign-up) |
| POST   | /api/v1/auth/user/ | Sign in | [JSON](#sign-in) |

### Users Services

| Method | URL | Description | Body |
| ------ | --- | ----------- | ------------------------- |
| GET   | /api/v1/users/ | List users | |
| POST   | /api/v1/users/ | Create user | [JSON](#user-create) |
| PUT    | /api/users/{id_user}/ | Update user| [JSON](#user-update) |
| DELETE | /api/users/{id_user}/ | Delete user | |

### Signature Request Services

| Method | URL | Description | Body |
| ------ | --- | ----------- | ------------------------- |
| GET   | /api/v1/signature_requests/ | Signature request list | |
| GET   | /api/v1/signature_requests_by_user/{id_user}/ | List of signature request made by user | |
| POST   | /api/v1/signature_requests/ | Create Signature Request | [JSON](#signature-request-create) |
| PUT    | /api/v1/signature_requests/{id_signature_request}/ | Update signature request | [JSON](#signature-request-update) |
| DELETE | /api/v1/signature_requests/{id_signature_request}/ | Delete signature request | |


### Signature Request User Services

| Method | URL | Description | Body |
| ------ | --- | ----------- | ------------------------- |
| GET   | /api/v1/signature_request_users_by_request/{id_signature_request}/ | List signature request users by signature request | |
| GET   | /api/v1/signature_request_users_by_user/{id_user}/ | List of requests received by user | |
| POST   | /api/v1/signature_request_users/ | Create signature request by user | [JSON](#signature-request-user-create) |
| PUT    | /api/v1/signature_request_users/{id_user_to_signed}/ | Update user| [JSON](#signature-request-user-update) |
| DELETE | /api/v1/signature_request_users/{id_signature_request}/ | Delete Signature request | |

### Generate Signed File Services

| Method | URL | Description | Body |
| ------ | --- | ----------- | ------------------------- |
| GET   | /api/v1/generate_pdf/{id_signature_request}/ | List users | |

## JSON Request Bodys

##### <a id="sign-up">Sign Up -> /api/v1/users/</a>
```json
{
    "full_name": "Test",
    "username": "test",
    "email": "test@ufps.edu.co",
    "password": "test"
}
```

## Autor(es)

**David Fernando Rojas Sáchica - Desarrollador**

-   <https://github.com/Sachica>
 
**Manuel Alejandro Coronel Andrade - Desarrollador**

-   <https://github.com/ManuelCoronelAndrade>
   
**Stiward Jherikof Carrillo Ramírez - Desarrollador**

-   <https://github.com/stiwardjherikofcr>

## Institución Académica

**[Programa de Ingeniería de Sistemas]** de la **[Universidad Francisco de Paula Santander]**

[Programa de Ingeniería de Sistemas]: https://ingsistemas.cloud.ufps.edu.co/
[Universidad Francisco de Paula Santander]: https://ww2.ufps.edu.co/

## Licencia
El código fuente se publica bajo la [MIT License](https://github.com/Arquitectura-de-Software-UFPS-2022-I/sign-documents-api/blob/master/LICENSE).