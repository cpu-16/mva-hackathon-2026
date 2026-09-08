# Subida a YouTube — título, descripción y ajustes

⚠️ **v5 lista para subir (8-sep-2026). La v4 sigue en línea en https://youtu.be/QGYHK0Ihs1c** y contradice
al reporte actual (dice «clears filter three» e «inverts»). YouTube no permite reemplazar el archivo de un
video: hay que **subir la v5 como video nuevo**, copiar la URL nueva y ponerla en el campo *Pitch video URL*
del tercer envío del Track 2 (y en `submission/ciberpty_track1_report.md`, `NOTAS_ENVIO.md`,
`ENVIAR-PASO-A-PASO.md`). No borrar la v4 hasta que el envío 3 esté confirmado.

Archivo a subir: `~/datos/HACKATHON-MVA-2026/video/pitch_MVA2026.mp4` (v5, corte documental)
(duración, tamaño y sha256 de la v5: ver `README.md` de esta carpeta, sección «Build record»)

## Ajustes de YouTube

| Campo | Valor | Por qué |
|---|---|---|
| Visibilidad | **No listado** | El formulario solo necesita una URL que el jurado pueda abrir. No listado la abre sin exponerla en búsquedas |
| Audiencia | **No, no es contenido para niños** | Si marcas "para niños", YouTube desactiva funciones y puede complicar la revisión |
| Idioma del video | Inglés | La narración es en inglés |
| Categoría | Ciencia y tecnología | |
| Comentarios | Desactivados | Es un envío a concurso, no un canal |

⚠️ **No pongas el nombre del niño, su ciudad, ni nada de la familia en el título, la descripción, las
etiquetas ni la miniatura.** El reto lo prohíbe expresamente y no aparece en el video.

## Título

```
A prepared answer, not a prescription — MVA Hackathon 2026 (team ciberpty)
```

## Descripción

La herramienta de voz **no hace falta nombrarla aquí**. El reglamento la pide en la descripción de
métodos (Q23 del Track 1 y Q3 del Track 2), y ahí ya está declarada con el modelo exacto. En YouTube
basta decir que la voz es sintética, que es lo que un espectador necesita saber.

```
Three-minute pitch for "Rare Disease, Real Kid" (Sage Bionetworks, MVA Society, Hugging Face and
BEACON). Team: ciberpty. Track 2, drug repurposing.

The case is a child with mosaic variegated aneuploidy type 1, with two BUB1B variants (presumed
compound heterozygous; phase not established). We were asked which already-approved drug could help
him. Our answer is that no drug should be started today, and the useful part is the evidence behind
that answer and what would change it.

Chapters:

I    The variant — two BUB1B alleles, a pre-registered retrieval benchmark on 37 healthy public
     genomes, and the control of our own that came back against us
II   Five filters — approval, mechanism, exposure, safety in this child, direction of effect;
     metformin is unevaluable on the mechanism proposed for it
III  Against ourselves — bortezomib is not excluded by the exposure check (free-drug margin unknown);
     our pre-registered test on public cancer data found no significant proteasome-inhibitor
     association in 444 solid-tumour lines and an attenuated target association in solid tumours;
     it fails the safety filter for this child (neuropathy 18% of children, on existing muscle
     atrophy); the experiment that could refute the premise needs 12 cultures per arm, not 3
IV   What helps, what scales — consensus surveillance, eight pre-registrations, a five-filter
     worksheet reusable as questions, and a replay tool transferred to a second MVA gene

Eight analyses were pre-registered in git — hypothesis, statistic and stopping rules committed
before each run. Where a result came back against our own argument, it is in the report.

Code, pre-registrations, results and the full report:
https://github.com/cpu-16/mva-hackathon-2026
(private during the hackathon, made public for the final evaluation as the challenge rules require)

This is a research submission, not medical advice, and no drug is recommended for any patient. No
patient data appears in this video or in that repository. The narration is synthetic speech, generated
locally.
```

## Etiquetas (opcional)

```
rare disease, mosaic variegated aneuploidy, BUB1B, drug repurposing, bioinformatics,
Sage Bionetworks, hackathon, aneuploidy, precision medicine
```

## Después de subir

Copia la URL corta (`https://youtu.be/…`) — es el campo **Pitch video URL** del formulario del Track 2,
y es obligatorio.
