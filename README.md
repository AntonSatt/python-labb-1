
# Python Labb 1 – Studentregister
## Syfte

- Träna på att använda variabler, input/print, loopar, listor och dictionaries.
- Bygga ett program steg för steg och se hur olika koncept samverkar.
### Del A – Grundläggande meny (ca 30–45 min)
1. Skapa ett Pythonprogram som vid start visar en meny:
1. Lägg till student
    - När man väljer 'Lägg till student', ska programmet fråga efter namn och ålder.
2. Lista alla studenter
3. Avsluta
2. Använd en while-loop så att menyn visas om och om igen tills användaren väljer att avsluta.
- Spara studenten i en lista som en dictionary, t.ex.: {"namn": "Ada", "ålder": 36}

### Del B – Fler funktioner (ca 45–60 min)
1. Utöka menyn med fler alternativ:
1. Lägg till student
2. Lista alla studenter
3. Sök student
    - Sök student: Fråga efter namn och skriv ut om studenten finns i registret.
4. Räkna genomsnittsålder
    - Räkna genomsnittsålder: Beräkna medelåldern för alla studenter i listan.
5. Avsluta
### Del C – Fördjupning och robusthet (ca 60–90 min)
1. Lägg till möjlighet att ta bort en student genom att skriva in namnet.
2. Se till att programmet hanterar felaktig input (t.ex. om ålder inte är en siffra,
eller om man väljer ett menyval som inte finns).
3. Extra utmaning:
- Låt varje student även ha en lista med favoritämnen.
- När man listar studenter, skriv ut både ålder och favoritämnen.
### Tips till studenterna
- Börja enkelt – få grundloopen att fungera först.
- Testa ofta i REPL innan du lägger till mer kod.
- Använd funktioner om koden blir lång – varje menyval kan vara en egen funktion.
### Inlämning / Redovisning
- Programfil (studentregister.py).
- Körbar demonstration där man kan lägga till, lista, söka och ta bort studenter.
- Kort reflektion (några meningar): Vilken del var svårast? Vad lärde du dig?
