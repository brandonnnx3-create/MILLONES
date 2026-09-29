# 02 — Sistema de puntuación

## Criterios y pesos

Todos los criterios se puntúan de 0 a 10, donde **10 siempre es "mejor para vos"**. En los criterios de costo o esfuerzo
eso significa lo inverso: en *capital*, 10 = casi no requiere capital; en *tiempo*, 10 = casi no depende de tus horas.

| Criterio | Qué mide | Peso |
|---|---|---|
| rentabilidad | Techo de ingresos realista para una persona (no el teórico) | **2** |
| automatizacion | Parte del trabajo diario que puede hacer la IA o un sistema | **2** |
| escalabilidad | Cuánto crece el ingreso sin que crezcan tus horas | **2** |
| tiempo | Baja dependencia de tus horas una vez en marcha | **2** |
| primeros_clientes | Facilidad para conseguir los primeros 10–20 clientes | 1,5 |
| recurrencia | Ingresos recurrentes (suscripción o uso continuo) | 1,5 |
| demanda | Evidencia de que hoy se paga por esto | 1 |
| margen | Margen bruto después de comisiones de plataforma, IA e infraestructura | 1 |
| capital | Poco capital inicial necesario | 1 |
| dificultad | Facilidad de ejecución para una persona que aprende | 1 |

Los cuatro criterios que pediste priorizar (rentabilidad, automatización, escalabilidad y baja dependencia de tu tiempo) tienen
peso doble. *Primeros clientes* tiene 1,5 porque pediste penalizar lo que se automatiza bien pero es muy difícil de vender.

## Puntajes y justificación

| Modelo | Rent. | Dem. | Marg. | Autom. | Escal. | Cap. | Dific. | Tiempo | 1.os cl. | Recur. | Justificación breve |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Micro-SaaS back-office en Shopify App Store | 8 | 8 | 9 | 7 | 8 | 9 | 5 | 6 | 5 | 9 | Bolsa de más de USD 1.000M/año pagada a desarrolladores. Sin comisión hasta USD 1M. La tienda trae la búsqueda con intención. Arrancar sin reseñas es duro (el 55 % de las apps no tiene ninguna). |
| Micro-SaaS independiente (web propia) | 8 | 6 | 8 | 7 | 8 | 8 | 5 | 5 | 2 | 9 | Mismo potencial pero sin canal propio. SEO en retroceso, anuncios que requieren capital. El *merchant of record* se lleva alrededor del 5 %. |
| App para Tiendanube (LatAm) | 4 | 6 | 8 | 6 | 4 | 9 | 6 | 5 | 6 | 8 | Menos competencia por tienda, pero precios bajos en ARS/BRL y un mercado de unas 190.000 tiendas. |
| Actors en Apify Store | 4 | 7 | 7 | 8 | 6 | 10 | 6 | 6 | 6 | 6 | Muy automatizable. Promedio de ~USD 470 por desarrollador. Mantenimiento cuando cambian los sitios. Ingresos por uso, volátiles. |
| Extensión de Chrome freemium | 4 | 6 | 8 | 8 | 6 | 10 | 7 | 7 | 4 | 6 | Conversión del 0,5–2 %, precios bajos, cobro por Stripe (problema en Argentina). |
| Agencia de automatización con IA | 7 | 8 | 6 | 3 | 3 | 9 | 6 | 2 | 6 | 5 | Factura rápido, pero cada cliente consume horas tuyas. Viola la restricción principal. |
| SaaS de agentes de WhatsApp (pymes LatAm) | 5 | 8 | 5 | 4 | 5 | 8 | 5 | 3 | 5 | 6 | Demanda real con competidores financiados. Puesta en marcha que requiere mucho acompañamiento. Cobro en ARS. |
| Generación de leads pay-per-lead | 6 | 8 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | Requiere anuncios o SEO, gestionar disputas y manejar compradores. |
| Productos digitales (plantillas, Etsy, Gumroad) | 3 | 5 | 9 | 7 | 5 | 10 | 9 | 7 | 3 | 1 | Saturado de contenido generado con IA, sin recurrencia, precio que tiende a cero. |
| Contenido / afiliación / SEO programático | 3 | 4 | 8 | 7 | 6 | 8 | 6 | 6 | 2 | 3 | Clics a la mitad con los resúmenes de IA de Google. Caídas de tráfico del 50–95 %. |
| Canal de contenido *faceless* | 4 | 6 | 8 | 6 | 6 | 8 | 6 | 5 | 2 | 3 | Depende del algoritmo. **Juicio, no investigado a fondo.** |
| Cursos e infoproductos | 5 | 5 | 9 | 6 | 7 | 9 | 6 | 4 | 2 | 2 | Requiere audiencia y autoridad previas. **Juicio.** |
| E-commerce / dropshipping con IA | 5 | 7 | 3 | 4 | 6 | 3 | 5 | 4 | 5 | 2 | Capital para anuncios, márgenes finos, logística. **Juicio.** |
| Servicio productizado en Fiverr/Upwork | 4 | 7 | 6 | 4 | 3 | 10 | 8 | 2 | 7 | 2 | Fácil de empezar, pero son horas humanas por pedido y hay presión de precio. **Juicio.** |

## Resultado (salida de `python3 scoring/score.py scoring/modelos.csv`)

### Ranking con pesos base

| # | Opción | Puntaje ponderado (0-10) |
|---|---|---|
| 1 | Micro-SaaS back-office en Shopify App Store | 7.33 |
| 2 | Micro-SaaS independiente (web propia) | 6.63 |
| 3 | Actors en Apify Store (datos/scraping) | 6.40 |
| 4 | Extension de Chrome freemium | 6.40 |
| 5 | App para Tiendanube (LatAm) | 5.87 |
| 6 | Productos digitales (plantillas/Etsy/Gumroad) | 5.53 |
| 7 | Cursos e infoproductos | 5.27 |
| 8 | Contenido/afiliacion/SEO programatico | 5.17 |
| 9 | Canal de contenido faceless (YouTube/TikTok) | 5.17 |
| 10 | SaaS de agentes de WhatsApp para pymes LatAm | 5.10 |
| 11 | Generacion de leads pay-per-lead | 5.10 |
| 12 | Agencia de automatizacion con IA | 5.03 |
| 13 | Servicio productizado en Fiverr/Upwork | 4.70 |
| 14 | E-commerce/dropshipping con IA | 4.43 |

### Sensibilidad a los pesos

| Escenario | 1.º | 2.º | 3.º |
|---|---|---|---|
| Pesos iguales | Shopify App Store (7.40) | Micro-SaaS independiente (6.60) | Apify (6.60) |
| Prudente (castiga capital, dificultad y captación difícil) | Shopify App Store (7.16) | Apify (6.63) | Extensión de Chrome (6.53) |
| Solo automatización + baja dependencia de tiempo | Shopify App Store (7.14) | Extensión de Chrome (6.86) | Apify (6.71) |
| Solo dinero (rentabilidad + escalabilidad + recurrencia) | Shopify App Store (7.75) | Micro-SaaS independiente (7.25) | Apify (6.12) |

### Robustez

Si a cada puntaje se le suma ruido aleatorio de ±1 punto, en 10.000 simulaciones el micro-SaaS en Shopify queda primero en el
**99,7 %** de los casos y el micro-SaaS independiente en el 0,3 %.

## Cómo leer esto sin engañarse

- **La robustez mide si el resultado aguanta errores aleatorios en mis puntajes, no errores sistemáticos.** Si yo tuviera un
  sesgo a favor del software (lo tengo: es lo que mejor sé evaluar), el ruido de ±1 no lo corrige. El control real es la validación
  de los días 1 a 10, que se apoya en comportamiento de clientes y no en mis puntajes.
- **"Micro-SaaS independiente" queda segundo con el mismo potencial económico.** Lo que lo baja es *primeros_clientes*.
  Por eso la estrategia es *marketplace primero, canal propio después*.
- **La agencia de IA factura más rápido que cualquier opción de esta lista.** Si tu prioridad real fuera "plata este mes", ganaría.
  No gana porque pediste explícitamente minimizar tu tiempo. Es una decisión de preferencia, no un hecho.

## Nichos dentro del modelo ganador (`scoring/nichos.csv`)

| Criterio | Peso |
|---|---|
| demanda_probada | 2 |
| debilidad_competencia | 2 |
| recurrencia_trabajo | 1,5 |
| bajo_soporte | 1,5 |
| riesgo_plataforma (10 = Shopify difícilmente lo construya) | 1,5 |
| arpu | 1,5 |
| ventaja_ia | 1 |
| velocidad_mvp | 1 |
| riesgo_legal (10 = bajo) | 1 |
| alcance_clientes | 1 |

| # | Nicho | Puntaje |
|---|---|---|
| 1 | A. Carga automática de órdenes de compra B2B (PDF/email/Excel → draft orders) | 7.00 |
| 2 | B. Facturación electrónica regional (México CFDI / España Verifactu) | 5.96 |
| 3 | D. Importación de archivos de proveedores con IA | 5.68 |
| 4 | C. Catálogo listo para agentes de IA (GEO/atributos) | 5.32 |

**A** queda primero en todos los escenarios de pesos y en el 100 % de las simulaciones con ruido.
Sus puntos débiles son *demanda_probada* (6) y *alcance_clientes* (5): no sabemos cuántos comerciantes reciben órdenes en PDF
ni qué tan fácil es encontrarlos. **Son justo las dos cosas que valida la Fase 1.**

**B** (facturación regional) es el plan B si A falla, con una advertencia importante. En España, quien produce el software de
facturación responde por su cumplimiento de Verifactu, con multas altas. La fecha obligatoria es el 01/01/2027 para sociedades
y el 01/07/2027 para autónomos ([Holded](https://www.holded.com/es/blog/shopify-verifactu), [TeamSystem](https://teamsystem.es/magazine/verifactu-se-retrasa-2027/)).
En México, el sello fiscal lo pone un proveedor certificado (PAC), lo que reduce el riesgo legal.
Si se activa el plan B, conviene empezar por México.
