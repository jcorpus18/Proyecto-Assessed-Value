

## Alcance del Proyecto

El objetivo principal de este proyecto consiste en analizar la relación entre los valores evaluados de propiedades inmobiliarias (*Assessed Value*) y sus precios reales de venta (*Sale Amount*) en distintas localidades. Para lograr esto, se utilizarán datos históricos recopilados en diferentes años, permitiendo obtener insights relevantes para decisiones en inversiones inmobiliarias, valoraciones fiscales, y estudios de mercado.

## Identificación y Recopilación de Datos

Para llevar a cabo este análisis, se han recopilado los siguientes datos:

- **Serial Number:** Identificador único para cada registro.
- **List Year:** Año de listado del inmueble.
- **Date Recorded:** Fecha en la cual se registró la venta.
- **Town:** Localidad del inmueble.
- **Address:** Dirección del inmueble.
- **Assessed Value:** Valor fiscal evaluado por autoridades locales.
- **Sale Amount:** Precio real de venta del inmueble.
- **Sales Ratio:** Proporción entre Assessed Value y Sale Amount.
- **Property Type:** Clasificación del tipo de propiedad (Residencial, Comercial, etc.).
- **Residential Type:** Tipo específico del sector residencial (ej. Single Family).
- **Non Use Code, Assessor Remarks, OPM remarks:** Información adicional de particularidades.
- **Location:** Coordenadas geográficas para análisis espacial.

## Caso de Uso Final

Estos datos se prepararán principalmente para:

1. **Tabla de Análisis:**
   - Realizar análisis descriptivos y correlacionales sobre valores fiscales y precios reales.

2. **Aplicación de Fondo:**
   - Desarrollar modelos predictivos para estimar valores reales basados en evaluaciones fiscales y localización.

3. **Base de Datos de Fuentes de Verdad:**
   - Establecer fuente confiable para consultas históricas y análisis futuros.

## Exploración y Evaluación de los Datos (EDA)

### Exploración inicial y evaluación de calidad

Se realizó un análisis exploratorio usando Python y Pandas, incluyendo:

- Detección de valores faltantes.
- Evaluación de duplicados (Serial Number).
- Revisión de formatos para fechas, valores numéricos y coordenadas.
- Estadística descriptiva para detectar outliers.

### Resultados del análisis inicial

- Valores faltantes identificados en columnas críticas fueron evaluados individualmente.
- Registros duplicados detectados y eliminados.
- Formatos de fechas y numéricos estandarizados; corrección manual requerida en coordenadas geográficas.
- Valores extremos identificados y tratados estadísticamente (imputación, transformación logarítmica).

### Documentación de pasos de limpieza

1. **Valores faltantes:** Imputación de medianas (Assessed Value), eliminación de faltantes críticos (Location).
2. **Duplicados:** Remoción basada en Serial Number.
3. **Corrección de formatos:** Estandarización fechas (YYYY-MM-DD), validación coordenadas geográficas.
4. **Tratamiento de outliers:** Transformación logarítmica, evaluación manual según contexto.

### Herramientas visuales utilizadas

- Gráficos de caja (boxplots) y dispersión para detección de outliers.

## Definición del Modelo de Datos

### Modelo de datos conceptual

Modelo predictivo basado en regresión lineal simple utilizando *Assessed Value* para predecir *Sale Amount*, fundamentado en la fuerte correlación identificada.

### Arquitectura y recursos utilizados

La arquitectura del modelo incluye:

- **Python:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn.
- **Jupyter Notebook:** Desarrollo interactivo y visualización.

### Motivos para elección de herramientas

Se eligieron estas herramientas por su flexibilidad, integración fluida, amplia comunidad y eficacia para análisis exploratorios y modelos predictivos rápidos.

### Frecuencia de actualización

Actualización trimestral para mantener una base que capture tendencias significativas sin costos excesivos.

## Ejecución del proceso ETL

Creación y ejecución de pipelines ETL con controles rigurosos de calidad (pruebas unitarias, validaciones, conteos).

### Arquitectura ETL

La arquitectura ETL implementada sigue este flujo:

1. **Extracción:** CSV utilizando Pandas.
2. **Transformación:** Limpieza y transformación con Pandas y NumPy.
3. **Carga:** Almacenamiento en base relacional SQL (SQLite o PostgreSQL).

### Arquitectura fuente AWS

```plaintext
Datos Fuente (S3)
        ↓
Procesamiento (Lambda o EC2)
        ↓
  ┌─────┴─────┐
Logs       Resultados
(CloudWatch)   (S3)
```
