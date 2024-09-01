# OSINT Analyzer

## Descripción

**OSINT Analyzer** es una aplicación diseñada para automatizar el análisis de datos provenientes de fuentes abiertas (OSINT) en el ámbito de la ciberseguridad. Utilizando modelos avanzados de procesamiento de lenguaje natural (NLP) e inteligencia artificial, la aplicación permite a los analistas procesar y extraer inteligencia de textos y audios de manera rápida y precisa.

## Características

- **Análisis de Textos:**
  - Resúmenes automáticos generados con el modelo BART (`facebook/bart-large-cnn`).
  - Análisis de sentimiento utilizando el modelo BERT (`nlptown/bert-base-multilingual-uncased-sentiment`).
  
- **Transcripción de Audio:**
  - Conversión automática de audios a texto mediante el modelo Whisper de OpenAI.

- **Interfaz de Usuario Intuitiva:**
  - Visualización clara de resúmenes, análisis de sentimientos y otros resultados del análisis.

- **Optimización y Escalabilidad:**
  - Capacidad para aprovechar tanto CPU como GPU, asegurando un rendimiento óptimo en diferentes entornos.

## Requisitos

- **Anaconda/Miniconda**
- **Python 3.8+**
- **Bibliotecas Principales:**
  - Flask
  - Transformers (Hugging Face)
  - OpenAI Whisper
  - spaCy (opcional para futuras implementaciones de NER)

Puedes encontrar todas las dependencias necesarias en el archivo `requirements.txt`.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Jpsuarez54/OSINT_ANALYZER
   cd OSINT_Analyzer
2. **Crear un entorno con Anaconda:**
   ```bash
   conda create --name osint_analyzer python=3.8
   conda activate osint_analyzer
3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   
## Uso

**Iniciar la aplicación :**
  ```bash
   python app.py
  ```
## Acceder a la interfaz:
Una vez iniciada la aplicación, puedes acceder a la interfaz de usuario en tu navegador en http://localhost:5000

## Cargar datos:
Sube archivos de texto o audio a través de la interfaz y selecciona el tipo de análisis que deseas realizar.

##Ver resultados:
Los resultados del análisis se mostrarán en la interfaz, incluyendo resúmenes, análisis de sentimientos y transcripciones de audio.

## Contribución
**¡Contribuciones son bienvenidas! Si deseas colaborar, por favor sigue estos pasos:**

- Haz un fork del repositorio.
- Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
- Realiza tus cambios y haz un commit (git commit -m 'Añadir nueva funcionalidad').
- Sube los cambios a tu repositorio (git push origin feature/nueva-funcionalidad).
- Abre un pull request.
- Futuras Implementaciones
- Análisis de Entidades y Relaciones:

## Integración futura de modelos de NER para la identificación automática de entidades relevantes en textos:
**Análisis de Video:**
Planificación de la inclusión de capacidades de análisis de video en futuras versiones.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto
Para preguntas o sugerencias, puedes contactarme a través de [tu email] o abrir un issue en este repositorio.
