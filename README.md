# MILLONES — Qué negocio construir desde Argentina con la mayor automatización posible por IA

> Fecha del análisis: 29/09/2026. Todo dato de mercado tiene fuente en [`docs/01-investigacion.md`](docs/01-investigacion.md).
> Las estimaciones propias están marcadas como **estimación** para no mezclarlas con hechos.

## Veredicto en 30 segundos

**Negocio elegido:** un **micro-SaaS de back-office para comerciantes de Shopify**, distribuido por el **Shopify App Store**,
donde la IA hace el trabajo central del producto. **Nicho inicial:** *carga automática de órdenes de compra B2B*.
Los mayoristas que venden por Shopify reciben pedidos de sus clientes (tiendas, distribuidores) en PDF, email, Excel o foto.
La app lee el documento, reconoce productos y cantidades, los cruza con los SKUs del catálogo y deja un
**draft order** listo para que el comerciante lo apruebe con un clic.

**Por qué este y no otro (resumen):**

1. **El canal resuelve lo más difícil para vos, que es conseguir clientes sin vender en persona.** Según datos de la industria,
   alrededor del 70 % de las apps se descubren buscando dentro del App Store. Es tráfico de gente que ya está buscando una solución.
2. **El cobro no pasa por vos.** Shopify cobra al comerciante, no te quita comisión sobre el primer millón de dólares y te paga en USD.
   Así evitás el problema de Stripe en Argentina.
3. **El nicho tiene demanda con precio a la vista y poca competencia.** Encontré 2 competidores directos. El principal cobra
   USD 50, 250 y 750 por mes. Además, desde abril de 2026 las funciones B2B de Shopify están disponibles en todos los planes,
   así que el mercado se está ampliando.
4. **La IA hace el trabajo real.** Leer documentos desordenados y cruzarlos con un catálogo es justo lo que la IA hace bien
   y antes no se podía automatizar. El costo de IA por orden (**estimación**: USD 0,02–0,15) es muy chico frente al precio (USD 1–3 por orden).

**Lo que no es realista, dicho sin vueltas:**

- **No existe un negocio que funcione solo desde el día uno.** Los primeros 3 a 6 meses te piden entre 30 y 50 horas por semana,
  incluyendo hablar con 20 a 50 comerciantes. Con suerte y buena ejecución, eso baja a unas 5–10 h/semana a los 12–18 meses.
  Nunca llega a cero: Shopify cambia su API cada trimestre, hay escalamientos de soporte y cambia la plataforma.
- **La distribución de resultados es muy desigual.** La mediana de las apps publicadas factura menos de USD 1.000 por mes.
  **Estimación subjetiva** para este plan ejecutado con disciplina:

  | Hito | Probabilidad |
  |---|---|
  | Primeros USD 100 | 60–70 % |
  | USD 1.000 MRR a 12 meses | 25–35 % |
  | USD 5.000 MRR a 18 meses | 8–15 % |
  | USD 10.000 MRR a 24–30 meses | 4–8 % |

  No son datos: son juicios apoyados en benchmarks.
- **La elección del nicho es una hipótesis con fecha de vencimiento.** Si en el día 10 no pasa los umbrales de validación
  ([`docs/04-plan-de-ejecucion.md`](docs/04-plan-de-ejecucion.md)), el mismo procedimiento elige el siguiente nicho.
  El modelo de negocio no se vuelve a discutir.

## Estructura

| Archivo | Contenido |
|---|---|
| [`docs/01-investigacion.md`](docs/01-investigacion.md) | Evidencia de mercado por modelo de negocio, con fuentes y nivel de confianza. Pagos e impuestos desde Argentina. |
| [`docs/02-scoring.md`](docs/02-scoring.md) | Sistema de puntuación, justificación de cada puntaje, sensibilidad a los pesos y prueba de robustez. |
| [`docs/03-negocio-elegido.md`](docs/03-negocio-elegido.md) | Las 27 preguntas: qué es, quién paga, precios, costos, competencia, IA vs. humano, riesgos, métricas, criterios de abandono. |
| [`docs/04-plan-de-ejecucion.md`](docs/04-plan-de-ejecucion.md) | Plan día por día hasta tener el negocio funcionando y las fases 1 a 5 con tareas tuyas y de la IA. |
| [`scoring/`](scoring/) | Matrices de decisión en CSV y script reproducible (`python3 scoring/score.py scoring/modelos.csv`). |

## Cómo usar el scoring

Los puntajes son juicios míos justificados en `docs/02-scoring.md`. Si no estás de acuerdo con alguno, cambiá el CSV y volvé a correr:

```bash
python3 scoring/score.py scoring/modelos.csv   # modelos de negocio
python3 scoring/score.py scoring/nichos.csv    # nichos dentro del modelo elegido
```

El script muestra el ranking ponderado, cómo cambia el ganador con otros pesos y cuántas veces sigue ganando cuando
se le agrega ruido de ±1 punto a cada puntaje.
