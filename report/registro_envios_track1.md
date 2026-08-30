# Registro de envíos — Track 1, MVA Hackathon 2026

Equipo: ciberpty · Cuenta HF: cpu-16 · Fecha: 30-ago-2026

## Envío 1 (~15:22 UTC) — reporte original
```
Submission received ✓
ciberpty (cpu-16) | Submission: 1 | Proband: PROBAND01
Rank points 100.0 / 100 · F-max 1.000 · F-max EPCR threshold 0.85
✅ Full match at rank 1
```

## Envío 2 (~16:33 UTC) — reporte corregido (control HPO re-corrido)
```
Submission received ✓
ciberpty (cpu-16) | Submission: 2 | Proband: PROBAND01
Rank points 100.0 / 100 · F-max 1.000 · F-max EPCR threshold 0.85
✅ Full match at rank 1
```

## Verificación por canal independiente
Cuota leída del DOM de la pestaña Submit — Track 1 (se calcula listando
los archivos realmente guardados vía HfApi().list_repo_files, no del caché):
```
2 / 6 submissions used  ·  4 remaining
```

## ⚠️ El leaderboard público está desactualizado
Al 30-ago 16:4x UTC el leaderboard muestra 25 equipos y su marca de tiempo
más reciente es **2026-08-26 18:50 UTC** — cuatro días atrás. No muestra
ningún envío del 27 al 30 de agosto, ni el nuestro ni el de nadie más.
Causa probable: `load_leaderboard()` en utils.py usa `snapshot_download`
y, si falla, devuelve el caché anterior (`except: return _leaderboard_cache or []`).
Es un problema del Space, no del envío. La cuota lo confirma: nuestros dos
archivos están guardados.

Timestamps más recientes vistos en el leaderboard:
```
2026-08-26 16:07 UTC / 16:15 UTC / 17:01 UTC / 18:50 UTC (el más nuevo)
```
