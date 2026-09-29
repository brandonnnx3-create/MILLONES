# 01 — Investigación de mercado

## 0. Método y limitaciones (leer primero)

- **Cómo se hizo:** búsquedas web del 29/09/2026. Desde este entorno el proxy bloqueó la descarga directa de páginas
  (shopify.dev, apify.com, apps.shopify.com y otras), así que los datos vienen de los resúmenes de resultados de búsqueda,
  no de haber leído cada página completa. Por eso cada dato lleva un **nivel de confianza**:
  - **Alta:** fuente primaria (Shopify, Pew, ChartMogul, BCRA) o varias fuentes independientes que coinciden.
  - **Media:** agregadores o blogs de la industria que citan datos de terceros, sin verificación primaria.
  - **Baja:** una sola fuente secundaria o un número que no se puede contrastar.
- **Qué no pude hacer:** relevar el Shopify App Store completo (categorías, reseñas, precios) para detectar nichos con
  competidores débiles. Eso queda como tarea de los días 2 y 3 del plan, a correr desde tu PC.
- **Convención:** **Hecho** = dato con fuente. **Interpretación** = lo que infiero de los hechos. **Supuesto** = lo que doy por
  cierto sin evidencia directa. **Estimación** = número propio.

## 1. Hallazgo transversal: la IA abarató construir, no vender

**Hechos**

- En el Shopify App Store hay alrededor de **21.500 apps**. El ecosistema creció un 71 % entre principios de 2024 y el primer
  trimestre de 2026. En mayo de 2026 se lanzaron **2.713 apps**, y el 23,8 % mencionaba IA ([AppstorePulse](https://www.appstorepulse.com/reports/state-of-shopify-app-store-may-2026), confianza media).
- El **55,4 % de las 21.749 apps publicadas no tiene ninguna reseña** (junio de 2026, [FireBear](https://firebearstudio.com/blog/whats-wrong-with-shopify-app-store-how-to-spot-a-scam-or-low-quality-app.html), confianza media).
- ChartMogul analizó 3.500 empresas de software. Mide la **retención bruta de ingresos (GRR)**: qué parte de lo que facturás a
  tus clientes actuales seguís facturando un año después, sin contar ventas nuevas.
  La mediana en productos nativos de IA es del **40 %**, contra el **63 %** en SaaS B2B.
  En productos de IA de menos de USD 50/mes cae al **23 %**. En productos de IA de más de USD 250/mes sube al **70 %**
  ([ChartMogul](https://chartmogul.com/reports/saas-retention-the-ai-churn-wave/), confianza alta).

**Interpretación**

Si la IA le permite a cualquiera construir software, construir deja de ser una ventaja. Lo escaso pasa a ser:

1. **Distribución con intención de compra:** gente que ya busca una solución.
2. **Confianza:** reseñas, historial, soporte.
3. **Nichos con un trabajo recurrente y un retorno medible:** los productos baratos "de IA" se cancelan rápido.

Esto cambia la pregunta que planteaste. No alcanza con "qué negocio puede hacer la IA". La pregunta es
**"dónde la IA hace el trabajo y además hay un canal que trae clientes sin que yo venda uno por uno"**.

## 2. Evidencia por modelo de negocio

### 2.1 Micro-SaaS en el Shopify App Store  ← **ganador**

**Hechos**

- **Comisión:** 0 % sobre el primer USD 1.000.000 de ingresos brutos *de por vida* contados desde el 01/01/2025. Arriba de eso, 15 %.
  Registrarse para publicar cuesta un pago único de USD 19
  ([Shopify changelog](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share), [revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share), [BetaKit](https://betakit.com/shopify-app-developers-will-no-longer-be-exempt-from-sharing-their-first-1-million-usd-in-revenue-every-year/); confianza alta).
- **Tamaño del mercado:** entre 2,85 y 3,6 millones de tiendas activas según el rastreador que se use. El 87 % de los comerciantes
  instala al menos una app. El gasto promedio en apps ronda los USD 120/mes. En tiendas de USD 1–5M de facturación anual es de
  USD 1.000–3.500/mes ([MageComp](https://magecomp.com/blog/shopify-app-store-statistics/), [Eightx](https://eightx.co/blog/average-ecommerce-shopify-app-spend-by-revenue-band-2026); confianza media).
- **Pagos a desarrolladores:** Shopify pagó más de USD 1.000 millones a desarrolladores en un año ([MobiLoud](https://www.mobiloud.com/blog/shopify-statistics/), confianza media).
- **Distribución de ingresos muy desigual:**

  | Segmento de apps | Ingresos |
  |---|---|
  | Top 1 % | más de USD 1M anuales |
  | Top 10 % | más de USD 100k anuales |
  | Mediana | menos de USD 1.000 por mes |

  Fuente: [Week One Labs](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026/), confianza media.
- **Descubrimiento:** alrededor del 70 % de los descubrimientos de apps empieza en el buscador del App Store
  ([MageComp](https://magecomp.com/blog/shopify-app-store-statistics/), confianza media).
- **Qué ordena el ranking:** la **velocidad de reseñas** (cuántas reseñas nuevas por período) pesa más que el total acumulado.
  También cuentan el sello *Built for Shopify*, la relevancia de palabras clave, la velocidad de instalaciones y la frescura del listado
  ([Prys](https://prys.io/learn/shopify-app-store-ranking-factors), [MetricHQ](https://metrichq.app/blog/shopify-app-reviews-ranking-flywheel); confianza media).
- **Pérdida de clientes (churn):**
  - La app promedio pierde el 60 % de las instalaciones de prueba antes de cobrar.
  - Las apps "widget" o con poco uso real pierden un 15–20 % por mes.
  - Las herramientas críticas para la operación están por debajo del 3 % mensual.
  - Del lado de las tiendas, alrededor del 28 % cierra o abandona Shopify cada año.

  Fuentes: [Taylor Sicard](https://taylorsicard.com/blog/shopify-app-onboarding-benchmarks), [Presta](https://wearepresta.com/shopify-churn-rate-the-2026-definitive-strategic-guide-to-merchant-retention/); confianza media.
- **Riesgo de plataforma, con un caso real:** Shopify cerró su propia app de inventario *Stocky* (deja de funcionar el 31/08/2026)
  y pasó esas funciones al panel nativo ([Ordoro](https://blog.ordoro.com/2026/02/25/shopify-sunsetting-stocky-2026/), confianza alta).
  Shopify puede "absorber" categorías enteras.
- **Costo de soporte según el tipo de app:** los conflictos de las apps que se inyectan en el tema de la tienda (widgets visibles
  para el comprador) consumen muchas horas de soporte ([DEV Community](https://dev.to/jthomas2/a-taxonomy-of-shopify-app-theme-conflicts-147-issues-classified-1ng6), confianza media).
  **Interpretación:** una app de back-office, que opera solo sobre datos por API y no toca el tema, necesita mucho menos soporte humano.

**Interpretación**

Es el único canal que analicé que combina cuatro cosas: búsqueda con intención de compra, cobro recurrente resuelto por la
plataforma, clientes que son empresas con presupuesto (no consumidores) y pagos al exterior posibles desde Argentina.
El costo es que la competencia es enorme y crece rápido. Solo tiene sentido si se entra por un nicho donde la competencia es débil.

### 2.2 Micro-SaaS independiente (web propia, cobro con un *merchant of record*)

**Hechos**

- Alrededor del 70 % de los fundadores de SaaS independiente factura menos de USD 1.000 MRR y el 18 % entre USD 1.000 y 5.000
  ([SaaSRanger](https://saasranger.com/blog/micro-saas-revenue-reality-what-1000-founders-actually-earn/) citando la encuesta de MicroConf, confianza media).
- Stripe no opera con residentes argentinos. Las alternativas son *merchants of record* (empresas que venden en tu nombre y
  se ocupan de los impuestos) como Lemon Squeezy (5 % + USD 0,50 por transacción, mayo de 2026), Paddle o Polar
  ([stilllater](https://stilllater.com/dev-tools/lemonsqueezy-vs-stripe-vs-paddle/), [Affonso](https://affonso.io/blog/lemon-squeezy-alternatives-for-saas); confianza media).
- En julio de 2025 Pew midió que cuando Google muestra un resumen de IA, los usuarios hacen clic en enlaces en el 8 % de las
  visitas, contra el 15 % cuando no lo muestra. Sobre las fuentes citadas dentro del resumen, solo el 1 %
  ([Pew Research](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/), confianza alta).

**Interpretación:** tiene el mismo potencial económico que una app de Shopify, pero sin canal propio. Tendrías que conseguir
tráfico con SEO (cada vez peor por los resúmenes de IA de Google), con anuncios (necesitás capital) o con venta en frío
(necesita mucho tiempo humano). Queda segundo en el ranking. Es la evolución lógica *después* de tener tracción en un marketplace.

### 2.3 App para Tiendanube (LatAm)

**Hechos:** alrededor de 180.000–190.000 tiendas activas y más de 700 apps en su tienda
([StoreLeads](https://storeleads.app/reports/tiendanube), [Ámbito](https://www.ambito.com/negocios/tiendanube-acelera-inteligencia-artificial-y-apunta-al-millon-marcas-latinoamerica-n6198958); confianza media).
Algunas apps se cobran junto con el plan de la tienda y otras directamente al desarrollador
([Ayuda Tiendanube](https://ayuda.tiendanube.com/es_ES/aplicaciones)).

**Interpretación:** hay menos competencia por tienda (alrededor de 270 tiendas por app, contra unas 150 en Shopify, **estimación**),
pero el precio que se puede cobrar es menor y hay riesgo de cobrar en ARS/BRL. Sirve como **segundo canal** para una app que ya
funcione en Shopify, no como primer negocio.

### 2.4 Actors en Apify Store (scrapers y herramientas de datos)

**Hechos**

- Apify paga alrededor de USD 1,4M por mes entre unos 3.000 desarrolladores. Eso da un promedio de unos USD 470 por desarrollador.
- Los mejores creadores independientes superan los USD 10.000 MRR.
- El desarrollador se queda con el 80 % (menos los costos de plataforma en los modelos de pago por uso).
- Pagos mensuales por PayPal (mínimo USD 20) o transferencia (mínimo USD 100).
- La tienda tiene más de 70.000 Actors. Es válido publicar un scraper para un sitio que ya tiene otro.

Fuentes: [Apify Help](https://help.apify.com/en/articles/10057167-how-developer-payouts-work), [AgentByline](https://agentbyline.com/articles/apify-actor-passive-income-what-really-earns-in-2026-67lcfr), [Use Apify](https://use-apify.com/docs/best-apify-actors); confianza media.

**Interpretación:** es lo más automatizable (clientes técnicos que se atienden solos y casi sin soporte), pero la bolsa total de
dinero es unas 60 veces menor que la de Shopify (**estimación**: ~USD 17M/año contra más de USD 1.000M/año). Además, los ingresos
dependen del uso y son volátiles, y los scrapers se rompen cada vez que cambia el sitio que leen. Es un buen complemento, no el negocio principal.

### 2.5 Extensiones de Chrome freemium

**Hechos:** la conversión de usuarios gratis a pagos va del 0,5 % al 2,2 %. Con 1.000–5.000 usuarios activos, lo típico es
USD 100–500/mes a los 6–12 meses. Con más de 20.000 usuarios, USD 5.000/mes o más
([Chrome Goldmine](https://chromegoldmine.com/blog/chrome-extension-monetization/chrome-extension-revenue-benchmarks/), [ExtensionPay](https://extensionpay.com/articles/browser-extensions-make-money); confianza media).

**Interpretación:** se automatiza bien, pero los precios son bajos, la conversión es baja y el cobro depende de Stripe
(el mismo problema de Argentina). Hacen falta muchos usuarios para llegar a ingresos relevantes.

### 2.6 Agencia de automatización con IA

**Hechos:** los precios típicos son USD 3.000–12.000 de setup más USD 1.500–10.000 por mes, o retainers de USD 500–2.000.
La venta en frío "no fabrica la confianza" necesaria para que te dejen tocar su CRM. Los clientes se niegan a comprometerse por
más de un año porque los prompts se pueden llevar a otro proveedor
([HeyReach](https://www.heyreach.io/blog/ai-workflow-automation-agency), [SaaStr](https://www.saastr.com/the-wave-of-ai-agent-churn-to-come-prompts-are-portable/); confianza media).

**Interpretación:** es lo más rápido para facturar, pero cada cliente nuevo exige tu tiempo: venta, relevamiento e
implementación. **Viola tu restricción principal.** Penalizado.

### 2.7 SaaS de agentes de IA para WhatsApp (pymes LatAm)

**Hechos:** el mercado está lleno. Cliengo, Botmaker, Leadsales, Kommo, Whaticket, Chattigo y otros cobran entre USD 24 y 149/mes.
Una pyme mediana paga ARS 8.000–30.000/mes
([Cliengo](https://guiawabusiness.cliengo.com/mejores-agentes-ia-whatsapp), [Botias](https://botias.io/blog/mejores-chatbots-whatsapp-pymes-argentinas-2026); confianza media, fuentes interesadas).

**Interpretación:** la demanda es real, pero la configuración y la puesta en marcha requieren mucho acompañamiento humano, se
cobra en moneda local y los competidores ya tienen financiamiento. Penalizado.

### 2.8 Generación de leads por lead vendido

**Hechos:** en servicios para el hogar en EE.UU., un lead exclusivo se paga USD 100–300 y uno compartido USD 20–75.
Thumbtack cobra USD 15–70 por lead
([WebFX](https://www.webfx.com/blog/home-services/lead-generation-handbook/), [Clicksgeek](https://clicksgeek.com/pay-per-lead-services/); confianza media).

**Interpretación:** hay demanda, pero para generar los leads necesitás SEO (que se está deteriorando) o anuncios (capital).
Además tenés que manejar compradores, disputas por calidad y llamadas. Es riesgoso sin capital.

### 2.9 Productos digitales (plantillas, Etsy, Gumroad)

**Hechos:** hay saturación por contenido generado con IA. Hay vendedores con caídas del 30 % al 98 %, y Etsy reportó menos
compradores activos en el segundo trimestre de 2025
([Digital Trends](https://www.digitaltrends.com/computing/etsy-sellers-are-quitting-as-ai-slop-floods-the-handmade-marketplace/), [iTiger](https://www.itiger.com/news/2557990351); confianza media).

**Interpretación:** si la IA puede hacerlo en segundos, cualquiera puede. El precio tiende a cero y no hay recurrencia. Penalizado.

### 2.10 Sitios de contenido, afiliación y SEO programático

**Hechos**

- Pew: los clics caen del 15 % al 8 % cuando hay un resumen de IA (ver 2.2).
- Sitios independientes perdieron entre el 50 % y el 95 % de su tráfico. HouseFresh perdió el 91 %.
- Las derivaciones de Google a medios cayeron un 33 % en 2025.
- Según una fuente, la actualización de marzo de 2026 hizo perder posiciones al 71 % de los sitios de afiliación.

Fuentes: [Search Engine Land](https://searchengineland.com/review-site-google-traffic-affiliate-seo-content-440143), [TechWyse](https://www.techwyse.com/blog/general-category/googles-helpful-content-system-didnt-punish-bad-content-it-punished-honest-niches), [Ahrefs](https://ahrefs.com/blog/affiliate-marketing-is-dead/); confianza alta sobre la tendencia, media sobre cada número.

**Interpretación:** el canal se está achicando y queda a merced de actualizaciones de algoritmo. Penalizado fuerte.

### 2.11 Canal *faceless*, cursos, dropshipping y freelance en Fiverr/Upwork

No investigué estos cuatro con la misma profundidad. Los puntajes de `02-scoring.md` son **juicio**, no dato, basado en tres cosas:

- **Dependencia de algoritmos:** canales faceless.
- **Necesidad de audiencia y autoridad previas:** cursos.
- **Capital para anuncios y márgenes bajos:** dropshipping.
- **Horas humanas por pedido:** freelance.

Ninguno de esos factores se resuelve con IA. Si querés que alguno se evalúe a fondo, es una investigación aparte.

### 2.12 Marketplace de Atlassian (considerado como canal alternativo)

**Hechos:** desde 2026 cobra 0 % sobre el primer millón de ingresos *de por vida* en apps hechas con su plataforma Forge.
Después, 16–17 % ([Atlassian](https://www.atlassian.com/blog/development/updates-to-marketplace-revenue-share-2026), confianza alta).

**Interpretación:** es un canal B2B atractivo, pero exige conocer en profundidad cómo trabajan los equipos con Jira y Confluence,
y los requisitos de seguridad son de nivel empresa. Shopify tiene un comprador más simple (el dueño del negocio decide solo)
y un problema más fácil de entender. Queda como opción futura para un segundo producto.

## 3. Del modelo al nicho: qué descarté y por qué

**Primera hipótesis descartada — "catálogo listo para agentes de IA" (GEO).**

- **A favor (hechos):**
  - Shopify activó por defecto sus *Agentic Storefronts* el 11/03/2026.
  - En el primer trimestre de 2026, el tráfico que llega desde IA creció 8 veces y los pedidos 13 veces
    ([Novadata](https://novadata.io/resources/news/shopify-agentic-storefronts-chatgpt-default-2026), [Hypersku](https://www.hypersku.com/blog/shopify-ai-2026/)).
- **En contra (hechos):**
  - ChatGPT aporta alrededor del 0,06 % del tráfico de Shopify ([Launchtip](https://www.launchtip.com/blog/how-to-get-your-shopify-store-indexed-by-chatgpt-and-ai-search-engines)).
    Es un volumen chico que crece desde una base chica.
  - Ya existen como mínimo 7 apps del mismo tipo, algunas gratis: Agentic Commerce Readiness, Agentic Commerce, SKAW,
    Agentic Readiness Report, Bulk AI, Datify y ChatGPT-AI Metafield Populator
    ([App Store](https://apps.shopify.com/agentic-commerce-readiness), [SKAW](https://apps.shopify.com/skaw), [Bulk AI](https://apps.shopify.com/bulk-ai), [Datify](https://apps.shopify.com/datify)).
  - La categorización automática nativa de Shopify tiene un 85 % de aceptación ([Charle](https://www.charle.co.uk/articles/product-taxonomy/)).
- **Veredicto:** es un nicho de moda, saturado y con alto riesgo de que Shopify lo absorba. **La lección aplica a vos también:**
  la primera idea "obvia" que se te ocurre en 2026 casi siempre tiene entre 5 y 10 apps compitiendo. Por eso el plan releva
  datos antes de elegir.

**Segunda idea descartada — importación con IA de archivos de proveedores.**
Tiene demanda probada, pero ya la cubren al menos Csvio, Importier, Automated Commerce, Apport, syncX y Products Sync Master.
Incluso Matrixify publicó un tutorial para hacerlo con Claude por su cuenta
([Csvio](https://apps.shopify.com/csvio-ai-product-importer), [Matrixify](https://matrixify.app/tutorials/bulk-update-shopify-products-from-any-supplier-file-with-claude-ai-and-matrixify-mcp/)).
Además, buena parte de ese trabajo se hace una sola vez, lo que invita a desinstalar la app después de usarla.

**Nicho elegido — carga automática de órdenes de compra B2B.**

- **Hecho:** desde abril de 2026, estas funciones B2B están en **todos los planes pagos** de Shopify, no solo en Plus:
  - perfiles de empresa;
  - hasta 3 catálogos;
  - precios por volumen;
  - condiciones de pago;
  - número de orden de compra en el checkout.

  Fuentes: [Shopify changelog](https://changelog.shopify.com/posts/key-b2b-features-now-available-on-non-plus-plans), [Shopify Help](https://help.shopify.com/en/manual/b2b/getting-started/plan-features); confianza alta.
- **Hecho:** existen 2 competidores directos, LevelOps *PDF to Order* y AutoApprove.
  - LevelOps tiene 5,0★ con **18 reseñas**. Cobra USD 50/mes (15 órdenes), USD 250 (100 órdenes) y USD 750 (500 órdenes).
    Es decir, entre USD 1,50 y 3,33 por orden.
  - LevelOps afirma que cargar una orden a mano lleva 5–10 minutos. Es un dato del propio vendedor, no una medición independiente.

  Fuentes: [LevelOps](https://www.levelops.co/pdf-to-order-shopify-app), [App Store](https://apps.shopify.com/levelops-email-to-order), [AutoApprove](https://autoapprove.app/); confianza media.
- **Interpretación:** el precio publicado muestra que existe disposición a pagar por lo menos en parte del mercado.
  Las 18 reseñas indican que el mercado probablemente no es enorme, o que se vende lento.
- **Lo que NO sabemos, y el plan valida en 10 días:**
  - cuántos comerciantes de Shopify reciben órdenes en PDF o por email con frecuencia;
  - si un mayorista chico pagaría entre USD 29 y 79.

## 4. Operar desde Argentina: pagos, dólares e impuestos

**Hechos**

- **Pagos de Shopify a desarrolladores:**
  - Se emiten siempre en USD, por PayPal, cuenta bancaria o transferencia, según lo que habilite el país
    (vía Hyperwallet, con 0,5 % de comisión si hay conversión de moneda).
  - No aceptan cuentas virtuales como Payoneer.
  - No se puede convertir a pesos argentinos.

  Fuentes: [Shopify Help](https://help.shopify.com/en/partners/manage-account/manage-payouts-invoices/payout-method), [Shopify Partners](https://www.shopify.com/partners/blog/payout-methods); confianza alta.
  **Qué métodos aparecen para Argentina no se pudo confirmar desde acá.** Es la primera verificación del día 1.
- **PayPal en Argentina:**
  - Permite cobrar en USD.
  - Para retirar a un banco argentino convierte a pesos con un recargo del 3–4,5 % sobre el tipo de cambio de referencia.
  - Para retirar USD sin convertir hace falta una cuenta bancaria en EE.UU. a tu nombre, o usar intermediarios.

  Fuentes: [iProfesional](https://www.iprofesional.com/finanzas/403093-pay-pal-argentina-como-cobrar-en-dolares), [Wise](https://wise.com/ar/blog/como-retirar-dinero-de-paypal-en-argentina); confianza media.
- **Divisas:**
  - En abril de 2025 se eliminó el cepo para personas humanas.
  - Desde el 18/09/2025, quien exporta servicios puede ingresar sus dólares y **conservarlos sin pasarlos a pesos**, sin el tope
    anterior de USD 36.000 anuales.
  - En abril de 2026 hubo más flexibilizaciones (Comunicación A 8417).

  Fuentes: [La Nación](https://www.lanacion.com.ar/economia/eliminan-el-cepo-cambiario-para-personas-y-cambian-el-regimen-para-administrar-el-dolar-nid11042025/), [Infobae](https://www.infobae.com/economia/2026/04/13/cepo-cambiario-cuales-son-las-restricciones-que-se-mantienen-tras-los-cambios-del-gobierno/), [BCRA A 8417](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8417.pdf); confianza alta.
- **Monotributo, vigente desde el 01/08/2026:**

  | Categoría | Tope anual | Cuota mensual |
  |---|---|---|
  | A | ARS 12.009.410 | ARS 49.527 |
  | K | ARS 126.610.838 | — |

  Fuentes: [Tiendanube blog](https://www.tiendanube.com/blog/categorias-monotributo/), [Mr. Factura](https://mrfactura.com.ar/monotributo/categorias); confianza media-alta.
- **Tipo de cambio:** mayorista ARS 1.524,50 (venta) y MEP ARS 1.555 al 28/09/2026
  ([La Noticia 1](https://www.lanoticia1.com/noticia/dolar-hoy-lunes-28-de-septiembre-de-2026-cuanto-cotizo-el-oficial-blue-y-mayorista), confianza media).

**Interpretación y estimaciones**

- A ~ARS 1.520 por dólar, el tope de la categoría A equivale a unos **USD 7.900/año** y el de la K a unos **USD 83.000/año**.
  Alcanza para cubrir los hitos de USD 1.000 y USD 5.000 MRR. Por encima de unos USD 7.000 MRR tendrías que pasar a
  Responsable Inscripto o constituir una sociedad.
- Vendés al exterior, así que se factura con **Factura E** (exportación de servicios). **El tratamiento de IVA, Ingresos Brutos
  (varía por provincia) y cómo documentar el ingreso de divisas lo tiene que confirmar un contador antes del primer cobro.**
  Esto no es un detalle: un error acá se paga caro.
- **No hace falta una LLC en EE.UU. al principio**, porque Shopify cobra al cliente final. Solo se justificaría si más adelante
  vendés fuera del marketplace (por encima de unos USD 2–3k MRR propios, **estimación**).

## 5. Costos de IA dentro del producto (precios de API vigentes)

**Hechos:** precios de la API de Claude al 25/09/2026, en USD por millón de tokens de entrada / salida:

| Modelo | Entrada | Salida |
|---|---|---|
| Haiku 4.5 | 1 | 5 |
| Sonnet 5.5 | 2 | 10 |
| Opus 5.5 | 4 | 20 |

El procesamiento por lotes (Batch API) cuesta un 50 % menos. Fuente: documentación de la API de Anthropic.

**Estimación:** una orden de compra típica de 1–2 páginas necesita unos 5.000–10.000 tokens de entrada (documento más
candidatos de SKU) y unos 1.000–2.000 de salida.

| Modelo | Costo por orden (**estimación**) |
|---|---|
| Sonnet 5.5 | ~USD 0,02–0,04 |
| Opus 5.5 | ~USD 0,04–0,12 (el razonamiento interno suma tokens) |

Frente a un precio de USD 1–3 por orden, **el costo de IA queda por debajo del 5 % del ingreso**. Qué modelo usar se decide
midiendo la precisión sobre un set de prueba de órdenes reales, no por precio.
