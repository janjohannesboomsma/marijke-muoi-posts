# Richtlijnen dagelijkse post – Marijke Muoi Odd Fellows Leeuwarden

## Buffer
- Organisatie: "My organization" – `6ace30f6cfe865a2dc6fb4bf`
- Facebook-pagina "Odd Fellows Leeuwarden" – `6ace3669778b240e2ff7800a` (metadata `{"facebook":{"type":"post"}}`)
- Instagram "@marijkemuoioddfellows" – `6ad4c701778b240e2f48b7ec` (metadata `{"instagram":{"type":"post","shouldShareToFeed":true}}`)
- `schedulingType`: `automatic`
- Afbeelding-URL: `https://raw.githubusercontent.com/janjohannesboomsma/marijke-muoi-posts/main/images/<JJJJ-MM-DD>.jpg`
- Altijd alt-tekst meegeven (beschrijving + de zin op de afbeelding).

## Modus
- Zie `MODUS.txt` in deze map: `concept` = posts opslaan als concept (`saveToDraft: true`);
  `live` = posts inplannen met `mode: customScheduled` en `dueAt` vandaag 09:30 Europe/Amsterdam.

## Afbeelding
`python3 make_image.py --titel "<kernzin>" --thema <thema> --uit images/<JJJJ-MM-DD>.jpg`
- Kernzin: 3–9 woorden, eigen formulering, geen citaten van anderen.
- Thema per seizoen: dec–feb `winter`, mrt–mei `lente`, jun–aug `zomer`, sep–nov `herfst`.
  Af en toe (±1 op 4 dagen) `nacht` of `goud` voor afwisseling.
- Commit en push de afbeelding naar `main` vóór de Buffer-post wordt aangemaakt.

## Tekst
- Nederlands, warm, uitnodigend, niet zweverig of prekerig. Spreek de lezer aan met "je".
- Kern: de drie schakels Vriendschap, Liefde, Waarheid, en hoe je die in het dagelijks leven oefent.
- Wissel onderwerpen af: luisteren, praktische zorg voor een ander, eerlijkheid, dankbaarheid,
  samen zijn in donkere dagen, het seizoen, Leeuwarden/Friesland, wat een loge is,
  nieuwsgierigheid naar lidmaatschap, een kleine "oefening voor vandaag", een vraag aan de lezer.
- Facebook: 80–150 woorden, 3–5 korte alinea's.
- Instagram: 30–60 woorden, korte regels.
- Beide eindigen met: marijke-muoi-odd-fellows.nl (Facebook ook: info@marijke-muoi-odd-fellows.nl)
- Hashtags: #OddFellows #Leeuwarden #Vriendschap #Liefde #Waarheid #MarijkeMuoi (+ max. 1 seizoenstag).
- Verzin GEEN data, bijeenkomsten, evenementen, namen of feiten over de loge.
- Herhaal geen onderwerp of openingszin uit de posts van de afgelopen 14 dagen (check met list_posts).
