# 🚀 Multipagos QR – Auth Service (CQRS con Django)

## 📌 Descripción

Este proyecto implementa el módulo de autenticación (**Auth Service**) del sistema **Multipagos QR**, utilizando el patrón arquitectónico **CQRS (Command Query Responsibility Segregation)**.

El objetivo es separar claramente:

* **Command (Write)** → operaciones de escritura (registro de usuarios)
* **Query (Read)** → operaciones de lectura optimizadas

Además, se implementa:

* Arquitectura basada en eventos
* Multi base de datos (write_db / read_db)
* API REST con Django REST Framework

---

## 🧠 Arquitectura

```text
Cliente (Frontend / Postman)
        ↓
   API REST (Django)
        ↓
-----------------------------
| COMMAND (write_db)        |
| - Registro de usuario     |
| - Lógica de negocio       |
-----------------------------
        ↓
        EVENTO (user_created)
        ↓
-----------------------------
| QUERY (read_db)           |
| - Lectura optimizada      |
| - UserReadModel           |
-----------------------------
        ↓
   Respuesta al cliente
```

---

## 🧩 Tecnologías usadas

* Python 3.13
* Django 6
* Django REST Framework
* SQLite (2 bases de datos)
* Arquitectura CQRS

---

## 📁 Estructura del proyecto

```text
config/
│── config/              # Configuración principal Django
│── core/                # Modelos principales (User, Company)
│── command/             # Lado WRITE (CQRS)
│   ├── handlers/
│   ├── services/
│   └── api/
│── query/               # Lado READ (CQRS)
│   ├── models/
│   └── api/
│── events/              # Eventos del sistema
│── manage.py
```

---

## ⚙️ Configuración del proyecto

### 1. Clonar repositorio

```bash
git clone <repo-url>
cd AuthCqrs/config
```

---

### 2. Crear entorno virtual

```bash
python -m venv my_env
my_env\Scripts\activate   # Windows
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Aplicar migraciones

#### Base de datos WRITE:

```bash
python manage.py migrate
```

#### Base de datos READ:

```bash
python manage.py migrate query --database=read_db
```

---

### 5. Ejecutar servidor

```bash
python manage.py runserver
```

---

## 🔌 Endpoints disponibles

### 🔹 Command (WRITE)

#### ➤ Registrar usuario

```http
POST /api/command/register/
```

**Body:**

```json
{
  "username": "usuario1",
  "email": "user@test.com",
  "password": "123456"
}
```

---

### 🔹 Query (READ)

#### ➤ Listar usuarios

```http
GET /api/query/users/
```

---

## 🔄 Flujo CQRS

1. Se registra un usuario (Command)
2. Se guarda en `write_db`
3. Se dispara un evento (`user_created_event`)
4. El evento replica los datos en `read_db`
5. El cliente consulta desde `read_db` (Query)

---

## 🧪 Pruebas

Puedes usar:

* Navegador (Django REST UI)
* Postman
* Thunder Client (VSCode)

---

## ⚠️ Notas importantes

* El endpoint `/api/command/register/` solo acepta **POST**
* Las consultas se realizan únicamente desde `read_db`
* El sistema usa eventos para sincronizar datos

---

## 🚀 Próximas mejoras

* 🔐 Autenticación con JWT
* 🏢 Multi-tenant (company_id)
* 📊 Roles (admin, provider, user)
* 📦 Integración con microservicios
* 📨 Uso de broker (Kafka / RabbitMQ)

---

## 👨‍💻 Autor

Proyecto desarrollado como parte de la materia **Web III**
Enfoque en arquitectura moderna y buenas prácticas backend.

---

## 🧠 Conceptos aplicados

* CQRS
* Event-driven architecture
* Separación de responsabilidades
* Multi-database en Django
* APIs REST

---
