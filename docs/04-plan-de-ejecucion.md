# 04 — Plan de ejecución

> **Regla de oro:** cada etapa termina en una **compuerta**, es decir, un umbral numérico que decide si seguís, si cambiás de
> nicho o si abandonás. Lo decide el número, no el ánimo del día.
> "Vos" = tareas humanas. "IA" = tareas que delegás (Claude Code, Claude con búsqueda o navegador, API).
> Horas estimadas: 6–8 por día en validación y MVP.

---

## Semana 1–2: Validación (días 1–10)

### Día 1 — Base operativa y verificación de cobro

- **Vos**
  - Crear la cuenta de **Shopify Partners** y una *development store*.
  - En el panel de Partners, ir a *Payouts* y **anotar qué métodos aparecen para Argentina** (PayPal, banco, transferencia en USD).
    Guardar captura.
  - Abrir o verificar una cuenta de PayPal a tu nombre.
  - Instalar Node LTS, Git, Shopify CLI y Claude Code.
  - Crear un repositorio privado para la app.
- **IA**
  - Armar una ficha comparativa de LevelOps y AutoApprove: funciones, precios, textos del listado, reseñas y lo que prometen.
  - Redactar 3 versiones del mensaje de outreach y un guion de entrevista de 10 preguntas
    (volumen de órdenes, formatos, quién las carga, cuánto tarda, errores, qué usan hoy, cuánto pagarían).
- **Compuerta del día:** si **no hay ninguna** vía de cobro para Argentina, se resuelve antes de seguir (PayPal casi seguro
  existe; si no, el plan cambia a otro marketplace). Es poco probable, pero es la única condición que invalida el modelo entero.

### Día 2 — Lista de prospectos

- **IA**
  - Encontrar **300 marcas o mayoristas en Shopify** con señales B2B: página *Wholesale*, "Become a stockist", presencia en Faire,
    listados de expositores de ferias mayoristas de EE.UU.
  - Para cada uno, verificar que usa Shopify y buscar el contacto de operaciones o del dueño.
  - Entregar un CSV con: tienda, vertical, señal B2B y contacto.
- **Vos:** revisar a mano 30 filas al azar. Si más del 20 % tiene errores, corregir las instrucciones y rehacer.
- **Vos:** comprar un dominio aparte para outreach (no el de la app) y crear la casilla. Activar el calentamiento del dominio (*warm-up*).

### Día 3 — Mensajes y comunidades

- **Vos**
  - Aprobar el mensaje final. Una pregunta, sin link, sin venta: *"¿Cuántas órdenes de compra por PDF o email cargás por semana en
    Shopify? Estoy armando algo que las carga solo y busco 5 mayoristas para cargárselas gratis durante 2 semanas."*
  - Agregar el pie legal: tu nombre, una dirección física y la opción de darse de baja (CAN-SPAM).
- **IA**
  - Buscar 20 hilos recientes sobre B2B y órdenes de compra en Shopify Community y r/shopify.
  - Redactar respuestas útiles que **no** mencionen la app. **Vos** publicás 5.
- **Vos:** enviar 20 mensajes por LinkedIn a responsables de operaciones o wholesale de la lista.

### Día 4 — Arranca el outreach y el set de prueba

- **Vos:** enviar los primeros 30 emails, uno por uno y en texto plano.
- **IA**
  - Generar un **set de 30 órdenes de compra sintéticas** con sus datos correctos: PDF de ERP, tablas en Excel, texto en el
    cuerpo del email, fotos escaneadas y alguna orden en español.
  - Crear un catálogo de prueba en la *development store* con SKUs y variantes parecidos a los de un mayorista real.

### Día 5 — Prototipo de extracción (un script, todavía no la app)

- **IA:** escribir un script que toma un PDF o imagen, llama a la API de Claude con salida estructurada y devuelve el JSON de la
  orden. Otro script lo cruza con el catálogo de prueba y mide la **precisión por línea** contra los datos correctos.
- **Vos:** correrlo y revisar los errores uno por uno. **Objetivo:** 90 % o más de precisión por línea en el set sintético.
  Si da menos, la IA itera los prompts y el cruce.
- **Vos:** enviar 30 emails más y responder a los que contestaron.

### Día 6 — Conversaciones

- **Vos:** hacer las entrevistas con quienes respondieron (videollamada o email) y ofrecer la **prueba manual gratis de 2 semanas**.
  Pedir permiso explícito para procesar sus órdenes.
- **IA:** resumir cada entrevista en una ficha estándar (volumen, formatos, dolor del 1 al 5, precio mencionado, objeciones).
- **Vos:** enviar 30 emails más.

### Día 7 — Primera revisión semanal

- **IA:** tablero de la semana (enviados, % de respuesta, entrevistas, volumen declarado, interesados).
- **Vos:** decidir ajustes al mensaje o al segmento. Por ejemplo, si responden más los de alimentos que los de indumentaria,
  concentrarse ahí.

### Días 8–10 — Servicio manual (*concierge*)

- **Vos + IA:** con 1 a 3 mayoristas:
  1. Te reenvían las órdenes a una casilla.
  2. El script las procesa.
  3. **Vos revisás cada línea.**
  4. Les devolvés un CSV listo para importar, o creás los draft orders con acceso de colaborador si lo aceptan.
- **Registrar cada error:** qué campo falló y por qué. Es la semilla de la batería de evaluación real.
- **Vos:** seguir con el outreach a 30 emails por día (unos 250 en total al día 10).

### ✅ Compuerta de validación — Día 10

| Métrica | Umbral para seguir |
|---|---|
| Contactados | 150 o más |
| Respuestas | 5 % o más (8 o más) |
| Mayoristas que confirman 10+ órdenes/mes por PDF o email | 5 o más |
| Aceptan la prueba manual y mandan órdenes reales | 2 o más |
| Precisión por línea en órdenes reales (con tu revisión) | 90 % o más |

- **Si pasa:** seguís al MVP.
- **Si falla por demanda o acceso a clientes:** repetís los días 2 a 10 con el nicho B (facturación CFDI en México) o con el mejor
  nicho que salga de relevar el App Store (ver el anexo). **No se rediscute el modelo.**
- **Si falla solo por precisión:** acotás el alcance (solo Excel/CSV y PDF digitales, sin fotos) y volvés a medir.

---

## Semanas 3–6: MVP (días 11–40)

### Días 11–12 — Esqueleto de la app

- **IA (Claude Code):**
  - Crear la app con la plantilla oficial de Shopify CLI.
  - Autenticación, permisos mínimos (`read_products`, `write_draft_orders`, `read_customers`/empresas B2B, solo lo necesario).
  - Webhooks obligatorios de GDPR.
  - Base Postgres con Prisma.
  - Deploy en un hosting con plan gratis o barato.
- **Vos:** revisar permisos y seguridad; entender cada archivo (pedile a la IA que te lo explique); hacer el primer deploy.

### Días 13–15 — Entrada de documentos

- **IA:**
  - Casilla única por tienda (`<tienda>@tu-dominio`) conectada al servicio de email entrante.
  - Carga de PDF, Excel, CSV e imágenes desde el panel.
  - Cola de trabajos, reintentos, guardado cifrado y borrado automático a los 60 días.
- **Vos:** probar con el set sintético y con las órdenes reales anonimizadas del servicio manual.

### Días 16–18 — Extracción, cruce y pantalla de revisión

- **IA:**
  - Pasar el script del día 5 a la app.
  - Cruce por SKU exacto → código de barras → coincidencia aproximada por nombre y variante, y la IA elige entre los 5 mejores candidatos.
  - Identificación de la empresa o cliente.
  - Pantalla de revisión con Polaris: documento a la izquierda, líneas a la derecha, marcas de baja confianza, edición en línea,
    botón "Crear draft order".
- **Vos:** probar como si fueras el comerciante. Registrar cada fricción.

### Días 19–20 — Memoria y cobro

- **IA:**
  - Tabla de equivalencias por comprador que se completa con cada corrección.
  - Planes con Shopify Billing (Starter, Growth, Scale, prueba de 14 días) y cargos de excedente por uso.
  - Límites por plan.
  - Aviso por email cuando hay un draft listo.
- **Vos:** probar la facturación en modo test en la *development store*.

### Días 21–22 — Calidad y cumplimiento

- **IA:**
  - **Batería de evaluación** que corre en GitHub Actions ante cada cambio de prompt o de modelo y falla si la precisión baja.
  - Integración con Sentry y logs.
  - Borradores de términos, política de privacidad y documentación de ayuda.
- **Vos:** revisar los textos legales (si podés, que un abogado mire los términos) y definir la cláusula de responsabilidad:
  el comerciante siempre aprueba antes de que se cree el pedido.

### Días 23–26 — Beta cerrada con los clientes del servicio manual

- **Vos:** instalar la app en las tiendas de 2–3 clientes del servicio manual (con su permiso) y acompañar las primeras 10 órdenes
  de cada uno.
- **IA:** corregir los errores que aparezcan, ampliar la batería de evaluación con las órdenes reales anonimizadas y preparar la
  cuenta de horas ahorradas.
- **Vos:** cobrar la segunda quincena del servicio manual, o acordar el precio de fundador en la app.

### Días 27–28 — Listado y envío a revisión

- **IA:**
  - Textos del listado con 3 variantes de título y subtítulo orientados a búsquedas.
  - Capturas de pantalla.
  - Guion del video demo de 60–90 segundos.
  - Preguntas frecuentes.
- **Vos:**
  - Grabar el video.
  - Pagar los USD 19.
  - Correr la **herramienta de auto-revisión con IA de Shopify**.
  - **Enviar a revisión.**

### Días 29–40 — Mientras dura la revisión (ver el supuesto de 1–4 semanas)

- **Vos:** seguir con el outreach (unos 30 por día) y armar una **lista de espera** de mayoristas que quieren la app al lanzar.
  Responder rápido lo que pida el equipo de revisión.
- **IA:**
  - 5 guías o páginas de ayuda y 2 comparativas honestas ("cómo cargar órdenes de compra en Shopify B2B", "LevelOps vs. X").
  - Base de conocimiento para el agente de soporte.
  - Secuencias de email automáticas: bienvenida, "procesá tu primera orden", "aprobaste 10 órdenes: dejanos tu opinión".
- **Vos:** configurar el agente de soporte con IA y probarlo con 20 preguntas reales de la beta.

### ✅ Compuerta del MVP

| Métrica | Umbral para lanzar |
|---|---|
| Precisión por línea en la batería de evaluación con órdenes reales | 95 % o más |
| Beta: órdenes procesadas de punta a punta sin tu intervención | 20 o más |
| Beta: al menos 1 cliente dispuesto a pagar la app | Sí |
| App aprobada en el App Store | Sí |

---

## Día del lanzamiento y primeras semanas (días 41–90)

- **Día de lanzamiento**
  - **Vos:** avisar a la lista de espera y a los clientes de la beta.
  - **IA:** mandar la secuencia de alta.
  - **Vos:** pedir reseñas **solo** a quien ya ahorró tiempo real. Nada de incentivos ni reseñas falsas: Shopify las detecta y puede dar de baja la app.
- **Semanas 7–12**
  - **Vos:** 30 emails por día de outreach aprobados en lote; atender a los primeros 20 clientes con atención personalizada
    (es tu fuente de mejoras); 1 entrevista de cancelación por cada cliente que se va.
  - **IA:** analizar las desinstalaciones, proponer una mejora de activación por semana, probar variantes del listado cada
    30–60 días y mandar el reporte semanal.
- **Semanales:** revisión de métricas (plantilla en `03-negocio-elegido.md`, sección 27) y una decisión por semana.

---

## Las 5 fases, con qué hacés vos y qué hace la IA

### FASE 1 — Validación (días 1–10)

| Vos | IA |
|---|---|
| Cuenta de Partners y verificación de cobro | Ficha de competidores y análisis de reseñas |
| Aprobar mensajes y listas; mandar el outreach | Encontrar, verificar y enriquecer 300 prospectos |
| Entrevistas y servicio manual (revisión humana de cada orden) | Guion de entrevista, resúmenes, set de prueba sintético |
| Decidir en la compuerta del día 10 | Script de extracción y medición de precisión; tablero semanal |

**Salida:** nicho confirmado (o cambiado), 2 clientes o más con órdenes reales, primer cobro por el servicio manual.

### FASE 2 — MVP (días 11–40)

| Vos | IA |
|---|---|
| Revisar arquitectura, permisos y seguridad; salir a producción | Escribir el 70–90 % del código y los tests |
| Probar como comerciante; priorizar | Batería de evaluación en GitHub Actions; arreglos |
| Textos legales finales; enviar a revisión; video | Borradores legales, listado, documentación |
| Beta con clientes reales | Ampliar la batería con órdenes reales |

**Salida:** app aprobada, 95 % o más de precisión, 1 cliente pago o más dentro de la app.

### FASE 3 — Primeros ingresos (días 41–120)

| Vos | IA |
|---|---|
| Atender a los primeros 20 clientes; entrevistas de cancelación | Secuencias de alta y activación; alertas de uso en baja |
| Aprobar lotes de outreach; publicar en comunidades | Prospección continua, seguimientos, respuestas en foros (borradores) |
| Pedir reseñas en el momento justo | Detectar el "momento de valor" (X horas ahorradas) para pedir la reseña |
| Decidir precios y funciones | Reporte semanal con recomendaciones |

**Objetivo:** USD 1.000 MRR (unos 14–15 clientes), 10 reseñas o más, churn del 5 % o menos.
**Compuerta:** menos de USD 300 MRR a los 120 días → cambiar de nicho reutilizando el motor.

### FASE 4 — Automatización (meses 4–9)

| Vos | IA |
|---|---|
| Definir reglas de escalamiento de soporte | Agente de soporte con 70–80 % de resolución |
| Aprobar arreglos propuestos | Errores → *issue* → propuesta de arreglo con tests |
| Revisar la batería de evaluación una vez por semana | Aprobación automática opcional para compradores de confianza |
| Postularte a *Built for Shopify* | Monitoreo de rendimiento (tiempo de respuesta) y checklist de requisitos |
| Programa de socios | Materiales para socios y seguimiento de referidos |

**Objetivo:** bajar tu dedicación a **15–20 h/semana** con MRR creciente; USD 2.000–3.000 MRR.

### FASE 5 — Escalamiento (meses 9–24)

| Vos | IA |
|---|---|
| Subir precios a los clientes nuevos (con 30+ reseñas) | Análisis de sensibilidad al precio por grupo de clientes |
| Decidir la segunda palanca: plan Scale e integraciones con ERP, segundo producto sobre el motor, o nueva plataforma | Especificación y el 80 % del código de la palanca elegida |
| Anuncios en el App Store con presupuesto chico y medido | Optimización de palabras clave y del listado |
| Contador: ¿seguís en monotributo o pasás a Responsable Inscripto o sociedad? | Proyección de facturación y alertas de tope de categoría |

**Objetivo:** USD 5.000 MRR (unos 65–70 clientes) a los 18 meses, con 5–10 h/semana tuyas.
USD 10.000 MRR solo si se cumplen **todas** las condiciones de la sección 23 de `03-negocio-elegido.md`.

---

## Anexo — Procedimiento de relevamiento de nichos (si falla el nicho A, o para buscar un segundo producto)

Correlo desde tu PC con Claude y navegador. Desde el entorno de este análisis el App Store estaba bloqueado.

1. **IA:** para cada categoría de back-office del App Store (operaciones, inventario, pedidos, B2B, finanzas, catálogo), listar las
   30 apps principales con: reseñas totales, rating, reseñas de los últimos 90 días, precio más bajo pago, fecha de la última
   actualización y si tienen el sello *Built for Shopify*.
2. **Filtros duros:**
   - sin inyección en el tema de la tienda;
   - trabajo recurrente (no se usa una sola vez);
   - al menos 3 apps pagas con más de 100 reseñas sumadas (demanda probada);
   - el líder tiene rating ≤ 4,5, o más del 20 % de reseñas negativas en los últimos 12 meses, o no se actualiza hace más de 12 meses;
   - no aparece en las últimas Shopify Editions como función nativa.
3. **IA:** minar las reseñas de 1–3★ de los 5 líderes de cada nicho que pasa los filtros. Agrupar quejas: precio, soporte, errores, faltantes.
4. **Puntuar** los nichos que sobreviven con `scoring/nichos.csv` y elegir el primero.
5. **Validar** con los mismos días 2–10 de este plan.
