# Respuesta de Claude — íntegra

Consulta de solo lectura del 6 de septiembre de 2026. Texto conservado sin correcciones;
la evaluación de sus observaciones está en `../REVISION-2026-09-06.md`.

---

**1) Mayor debilidad competitiva (verificable hoy):** el reporte va por detrás de sus propios archivos y de lo primero que ve el juez. `CONTINUAR-AQUI.md` L14-17 lo declara; L167-183 documenta que el `README.md` del repo (la URL es parte del envío) sigue en la ronda 6 con dos afirmaciones refutadas por el propio benchmark; L222-235: cinco PMID sin abstract guardado, y el 39264246 sostiene 8 usos, el §7 entero y el veredicto MVA2. Con Rigor al 35% y tres citas falsas en el historial, eso es lo que un panel encuentra en la primera hora. Agravante interno: `track2/REPORT_track2_EN.md` L93 dice del salto cáncer→constitucional *"it did not survive"*, y L432-435 dice *"we do not withdraw… the direction survives"*. Juicio propio: la honestidad suma, pero el resumen ejecutivo y el §3.5 tienen que decir lo mismo.

**2) Dos mejoras sin laboratorio**

- **Impacto:** correr `replay/mva_replay.py` para TRIP13 (MVA3) sobre un fondo GIAB público, pre-registrado, y anexarlo a `TRANSFER_MVA2_MVA3.md`. Hoy la herramienta solo está demostrada en el gen para el que se construyó, y `replay/README_TOOL.md` L57-59 admite que el set de control por defecto sigue contaminado para BUB1B. Aceptación: commit del pre-registro con fecha anterior al run; `out_tool/TRIP13.json` con `alleles_ingested` verdadero y `technical_failure` falso; ninguna advertencia de HPO anotado al gen; L29 del README corregido a 21 asserts. Datos públicos, sin GPU.
- **Reproducibilidad:** un script `verificar_numeros.py` que lea `potencia/resultados.json`, `depmap/`, `mosaico/` y `replay/out*/` e imprima cada número citado en §3.5, §5 y §6 junto al valor del archivo fuente; añadir el sexto par a `VERIFY.md` (CONTINUAR L268-270). Aceptación: exit 0 con cero discrepancias en un clon limpio en menos de 5 minutos, y **falla** si se altera un número del reporte, el mismo control positivo que ya se le aplicó al self-check (CONTINUAR L244-246).

**3) Afirmación demasiado fuerte, fuera de los tres errores conocidos:** `REPORT_track2_EN.md` L177-178: la segregación parental *"is not merely the cheapest route to this variant — it is the only practical one"*. Se contradice con L190-193 y L592, donde el brazo de destino alélico del §6 (RT-PCR alelo-específica, western N/C) *"tests it directly"*. Y la segregación en trans aporta solo PM3 sobre PM2_Supporting + PP4_Moderate + BP1 (L132): la variante sigue VUS. Debe decir "el más barato y el que fija la fase", no "el único". Relacionado y menor: `video/GUION.md` L34 dice *"five verified ones… still ranked first"*, mientras README_TOOL L57-59 reconoce el set contaminado y CONTINUAR L140 da rank 1 en 1 de 3 fondos.
