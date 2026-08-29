# Track 2 — la tesis del informe

## El problema estratégico

El dossier técnico (`dossier_mecanismo_farmacos.md`) llega a la conclusión correcta y honesta:
**no existe un fármaco aprobado con evidencia defendible para MVA1.** Los mejores candidatos
(metformina, hidroxicloroquina, everolimus) son extrapolaciones de un screen en fibroblastos murinos
trisómicos, y los hits reales de ese screen — AICAR y 17-AAG — ni siquiera están aprobados.

Eso es rigor (35% de la nota). Pero entregado tal cual, un jurado lo lee como *"no encontraron nada"*
y se pierden **Impacto potencial (25%)** e **Innovación (25%)**.

Casi todos los equipos harán una de dos cosas: proponer metformina con entusiasmo injustificado, o
entregar exactamente esta conclusión negativa. Las dos pierden.

## La tesis: cambiar la pregunta

> No preguntamos *"¿qué medicamento le damos a este niño?"* — la respuesta honesta es ninguno todavía.
> Preguntamos *"¿qué hace falta para que esa pregunta se pueda contestar?"*, y entregamos las tres
> piezas que faltan.

### Pieza 1 — Lo accionable hoy (impacto real, sin fármaco)

Lo que más cambia el pronóstico de este niño **no es una molécula**: es la vigilancia tumoral
estructurada y la individualización de cualquier quimioterapia futura. El dossier ya tiene el
protocolo (ecografía cada 3 meses, examen clínico, criterios de consulta urgente) y la advertencia de
que los venenos mitóticos son una **precaución de alto nivel** en un checkpoint deficiente — sin caer
en el error de declarar la vincristina "contraindicada" y quitarle una quimioterapia curativa.

Esto es impacto verificable, no un "podría ser".

### Pieza 2 — El biomarcador que el campo no tiene ← *aquí está la innovación*

Cualquier terapia para MVA necesita un desenlace medible: la **carga de aneuploidía**. Nadie puede
evaluar un candidato sin poder medir si funcionó.

Nuestro análisis de `MOSAICISMO.md` demuestra empíricamente que **ese desenlace no es medible con
secuenciación bulk**: la variegación reparte la aneuploidía entre cromosomas distintos en células
distintas, de modo que cada cromosoma queda alterado en ~1–2% de las células. Probamos cuatro métodos
sobre el WGS del propio paciente y ninguno lo detecta; toda señal aparente resultó artefacto de
cobertura, duplicación segmental o contenido GC.

Ese es un resultado negativo **con datos del caso real**, no una opinión. Y de ahí sale la propuesta:

| Endpoint | Resolución | Costo | Veredicto |
|---|---|---|---|
| WGS bulk (BAF o dosis) | insuficiente — demostrado aquí | ya pagado | ❌ no sirve |
| Cariotipo de metafases | estándar diagnóstico, célula a célula | alto, manual, lento | referencia, no escalable |
| **scDNA-seq de baja cobertura** | por célula, todo el genoma | medio | ✅ el endpoint correcto |
| **Frecuencia de micronúcleos** | proxy de mis-segregación, por célula | **bajo**, microscopía | ✅ tamizaje barato |

Proponer el par *micronúcleos (tamizaje) → scDNA-seq (confirmación)* como endpoint estandarizado para
ensayos en trastornos de inestabilidad cromosómica es una contribución metodológica que hoy no existe,
y sale directamente de haber analizado estos datos.

### Pieza 3 — El criterio de avance (rigor convertido en producto)

El dossier ya define cuándo un candidato merece pasar a la siguiente fase: ventana ≥3× entre
aneuploide y corregido en ≥2 fondos isogénicos, reproducible en fibroblastos del paciente, **sin
aumentar la mis-segregación en las células supervivientes**, y a exposiciones humanas alcanzables.

Ese último criterio es el que descalifica a la mitad de las propuestas ingenuas: un compuesto que mata
células aneuploides pero incrementa la CIN en las que sobreviven **empeora la enfermedad**. Publicarlo
como regla de filtro es reutilizable por cualquier otro equipo.

## Escalabilidad (15%)

Nada de lo anterior es específico de este niño. El panel de 11 genes, el filtro de rareza+impacto, el
control de artefactos del mosaicismo, el endpoint de micronúcleos y el criterio de avance aplican a
cualquier síndrome de inestabilidad cromosómica: PCS/MVA por CEP57 o TRIP13, y en parte a las
anemias de Fanconi o el síndrome de Bloom.

## Lo que NO hacemos, y decirlo en voz alta

Un informe que proponga metformina como si fuera tratamiento gana entusiasmo y pierde credibilidad
ante un jurado que incluye clínicos y defensores de pacientes. **La familia de este niño está
leyendo.** Prometer una molécula sin evidencia es el peor resultado posible de este hackathon: no le
sirve al niño y erosiona la confianza que hizo posible que abrieran su genoma.

Nuestra postura: los candidatos entran al banco de pruebas, no al botiquín.

## Pendiente

- [ ] Redactar el informe final en inglés a partir de estas tres piezas
- [ ] Figura 1: mapa de dominios de BubR1 con Leu737Ter y Asn1002Lys ubicados
- [ ] Figura 2: el resultado negativo del mosaicismo (las 4 pruebas) — es la base de la Pieza 2
- [ ] Figura 3: árbol de decisión de vigilancia + precaución quimioterápica
- [ ] Video de pitch de 3 minutos
- [ ] Declarar uso de IA en el formulario de métodos (pregunta 23, obligatoria)
