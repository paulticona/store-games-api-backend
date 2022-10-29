Store Games[Tutorial Flask Clic Aqui](TUTORIAL.md)

```





			Store Games

StoreGames: Es una tienda de videojuegos
con un mercado de todo tipo de artículos coleccionables
de los personajes y mundo de cada juego que se vende. 

Modulos
- Usuarios (con permisos) (✓)
- Roles (✓)
- Juegos (Nivel 1º Categoria) (✓)
- Articulos de los juegos (Nivel 1º Categoria) (✓)
- Categorias (✓)
- Billetera (✓)
- Metodos de pago (✓)
- Pedidos (Pendiente, Pagado) (✓)
- Carrito de compras (✓)


		Empezemos

Proyecto Realizado con:
Python 
Flask

Dependencias:
	python: python -m venv venv
		source venv/Scripts/activate -> Windows
		source venv/bin/activate -> Linux / MacOS

	flask: 	pip install -r requirements.txt
		pip freeze > requirements.txt


Variables de Entorno:
	FLASK_ENV='development'
	FLASK_APP='main.py'
	FLASK_RUN_HOST=127.0.0.1
	FLASK_RUN_PORT=5000


	DATABASE_URL='postgresql://postgres:mysql@localhost:5432/Storegames'

	JWT_SECRET='tecsup'

	MAIL_SERVER='smtp.gmail.com'
	MAIL_PORT=587
	MAIL_USE_TLS=true
	MAIL_USERNAME='usuario@gmail.com'
	MAIL_PASSWORD='password_aplicacion'

	AWS_ACCESS_KEY_ID=''
	AWS_SECRET_ACCESS_KEY=''
	AWS_REGION=''



```

### * Planteamos los modelos y sus relaciones en Grafico UML y lo implementamos

![1667016004882](image/README/1667016004882.png)

### * Realizamos las migraciones de los modelos a un BD previamente configurada

![1667016138786](image/README/1667016138786.png)

```
flask db init -> Iniciamos
flask db migrate -m "Comentario" -> Crear una migración
flask db upgrade -> Subimos los cambios a la base de datos

```

### Realizamos UN CRUD para cada modelo con su logica de validacion

![1667017022952](image/README/1667017022952.png)

### Realizamos pruebas

![1667017200596](image/README/1667017200596.png)

![1667017247560](image/README/1667017247560.png)
