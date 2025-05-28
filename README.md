# 🧠 PokeRecom – Recomendador Pokémon por Tipo

Bienvenido a **PokeRecom**, un sistema web interactivo que te recomienda Pokémon aleatorios basados en su tipo (fuego, agua, planta, etc.) usando la **PokéAPI**. Inspirado en la estética de la consola clásica de **Game Boy Advance**, este proyecto busca combinar nostalgia con funcionalidad educativa, integrando conceptos de programación web y consumo de APIs REST.

## 🎮 Características principales

- Interfaz estilo **Game Boy Advance**
- Selección de tipos de Pokémon
- Generación de Pokémon aleatorios con:
  - Nombre
  - ID
  - Sprite
  - Primeros 4 ataques
- Arquitectura basada en Flask + HTML/CSS + Jinja2

---

## 📁 Estructura del proyecto
## Ejecución

poke-recom/
│
├── app.py # Lógica principal del backend (Flask)
├── pokemon.py # Clase Pokemon y funciones auxiliares
│
├── templates/
│ └── index.html # Interfaz HTML con Jinja2
│
├── static/
  ├── style.css # Estilos personalizados
  ├── logo.png # Logo de Pokémon
  └── gba-logo.png # Logo de Game Boy Advance

## ⚙️ Requisitos
- Versión Python 3.8+

1. Instala Flask:
```bash
pip install flask
```

## 🛠️ Instalación
1. **Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/poke-recom.git
```

2. Abrir folder en Visual Studio Code y ejecutar el siguiente comando dentro de la misma carpeta
```bash
python app.py
```

3. Abre en tu navegador:
```
http://127.0.0.1:5000
```
