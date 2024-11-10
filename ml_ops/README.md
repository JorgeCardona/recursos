
| **Característica**                | **Git**                                              | **DVC (Data Version Control)**                           |
|-----------------------------------|------------------------------------------------------|---------------------------------------------------------|
| **Función principal**             | Versionado de código y archivos pequeños             | Versionado de archivos grandes (datasets, modelos)      |
| **Almacenamiento**                | Repositorio Git (GitHub, GitLab, etc.)               | Almacenamiento remoto (Google Drive, S3, Azure, etc.)   |
| **Tipo de archivos manejados**    | Código fuente, archivos de configuración             | Datasets grandes, modelos entrenados, imágenes pesadas  |
| **Formato de versionado**         | Historial de commits                                 | Archivos `.dvc` que contienen metadata de versionado    |
| **Sincronización**                | `git push` y `git pull` sincronizan con el repositorio de Git  | `dvc push` y `dvc pull` sincronizan con el almacenamiento remoto |
| **Control del historial**         | Historial de cambios y diffs para código             | Historial y versiones para archivos grandes sin sobrecargar Git |
| **Archivo de metadata**           | `.git` para almacenar el historial de commits        | Archivos `.dvc` para rastrear versiones de los archivos grandes |
| **Gestión de espacio**            | Crece rápido con archivos grandes                    | Almacena solo referencias en Git, datos grandes van al remoto |
| **Colaboración**                  | Código compartido en GitHub para todos los colaboradores | Archivos grandes descargables bajo demanda con `dvc pull` |
| **Compatibilidad**                | Ideal para texto y archivos pequeños, poco eficiente con grandes | Optimizado para archivos grandes y pesados (datasets, modelos) |

**Resumen**: Git se encarga del código y archivos pequeños almacenándolos en un repositorio (como GitHub), mientras que DVC gestiona archivos grandes versionándolos en un almacenamiento remoto adecuado. Trabajan juntos para ofrecer un flujo de trabajo eficiente en proyectos de machine learning o ciencia de datos, donde es necesario versionar tanto el código como los datasets y modelos grandes.

# Iniciar el Repositorio Git/DVC
```
git init
dvc init
```

# Estructura de archivos del repositorio Git/DVC
```
repo/
├── 📂 .dvc/                     # Metadatos de DVC que gestionan los archivos y el flujo de trabajo
│    ├── ⚙️ config                # Configuración del almacenamiento remoto y otras opciones de DVC
│    ├── 🚫 .gitignore            # Ignora archivos y directorios gestionados por DVC (caché, metadatos, etc.)
│    ├── ⚠️ dvc.ignore            # Archivos de configuración para ignorar archivos no rastreados por DVC
│    ├── 🗂️ cache/                # Caché local de DVC (almacena versiones de archivos gestionados por DVC)
│    │   ├── 🔑 <hash_file1>      # Hash de un archivo gestionado por DVC
│    │   ├── 🔑 <hash_file2>      # Otro hash de archivo
│    │   └── ...                  # Más archivos de caché con hashes
│    ├── 📄 dvc.lock              # Archivo de bloqueo que guarda los estados de las etapas y dependencias de los pipelines
│    ├── 📄 dvc.yaml              # Define el flujo de trabajo de DVC y las etapas del pipeline
├── 📊 datasets/                 # Carpeta de datasets utilizados en el proyecto
│   ├── 🗂️ dataset.csv.dvc       # Metadatos de DVC para rastrear `dataset.csv` en el almacenamiento remoto
├── 🤖 models/                   # Carpeta de modelos entrenados
│   ├── 🗂️ model.pkl.dvc         # Metadatos de DVC para rastrear `model.pkl` en el almacenamiento remoto
├── 💻 src/                      # Código fuente para entrenar, evaluar y desplegar el modelo
│   ├── 🏋️‍♂️ train.py             # Script para el entrenamiento del modelo
│   ├── 📊 evaluate.py           # Script para evaluar el modelo
│   └── 🚀 deploy.py             # Script para desplegar el modelo
└── 🚫 .gitignore                # Ignora archivos temporales, dependencias y otros archivos no deseados en Git (ej. __pycache__, .env)
```

# Estructura de archivos para el almacenamiento en Google Drive o Almacenamientos Externos
```
📂 Google Drive/
├── 📁 dvc_storage/
│   ├── 🗑️ cache/
│   │   ├── 🔑 34f3e9b6dfef63bcd3eecf4fb90f8bc1  # Hash de la versión 1 de model.pkl
│   │   ├── 🔑 12345abcdeabc890abcdfe3bf87b45cd  # Hash de la versión 1 de dataset.csv
│   │   ├── 🔑 28b6c73e32997e8e0b125fbfbbd8c6c0  # Hash de la versión 2 de model.pkl
│   │   └── 🔑 67a5fba5c63fa8ac0ab234bdfcaa71e0  # Hash de la versión 2 de dataset.csv
│   ├── 🧑‍💻 models/
│   │   ├── 📦 model.pkl        # Última versión del modelo (basado en hash)
│   │   └── 🗂️ model.pkl.dvc    # Metadatos de DVC que referencian el modelo
│   └── 🗃️ datasets/
│       ├── 📊 dataset.csv      # Última versión del dataset (basado en hash)
│       └── 🗂️ dataset.csv.dvc  # Metadatos de DVC que referencian el dataset
└── 🗂️ .dvc/                   # Metadatos de DVC
```

