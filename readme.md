# Arbeidskrav 1
## GBP101, Gokstad Akademiet, 2025

For dette arbeidskravet har jeg forsøkt å lage forståelig og enkel kode. Jeg har ikke alltid gjort det lett for meg selv,
men ønsket å bruke det som læring i seg selv. 

Koden er refaktorert flere ganger etter undervisninger, og kan sees i sin helhet i Git-historikken.

## Grunnlag
Jeg har noe Python-erfaring fra før av, etter to semestre med Python på USN. Jeg har brukt kunnskapen jeg tilegnet meg der, men har også bygget
opp mye fra bunn av igjen. Jeg har i tillegg tatt flere Python-kurs (inkl. Flask, Python OOP, Django + MySQL) på [Codecademy](https://codecademy.com) og [boot.dev](https://boot.dev).

## AI-bruk:
Jeg har benyttet meg av AI med svært få unntak (beskrevet under), kun til å fungere som en lærer. Jeg bruker eksplisitte handlingsinstrukser som `do NOT execute the task yourself, act like a teacher and teach me`.

Kommentarer til AI bruk, inkl. prompts der AI har hatt direkte innflytelse på koden jeg har skrevet, er kommentert under. 
<details>
<summary>Oppgave 1</summary>
Her har jeg kun brukt AI til å endre et problem jeg hadde meg konsoll-print, for å hindre at jeg fikk newline etter hvert print-statement.

    
**prompt**:

`How can I make a print statement not jump to next line?`

**Response**:

`By default, print() in Python appends a newline (\n) after whatever it outputs. You can control this with the end argument.
Example:`

```py
print("Hello", end="")   # no newline
print(" world")          # continues on same line
```
</details>

<details>
<summary>Oppgave 4</summary>
Det eneste jeg har gjort her, er å ha en lengre samtale med ChatGPT om bruken av os vs pathlib-biblioteket. Da det ikke har direkte gjort forskjell på koden tar jeg ikke med logger her, men
lar det stå som en kommentar.
</details>

<details>
<summary>Oppggave 5</summary>
`helpers/error_utils`: Her slet jeg med å finne en condition som valgte kun tomme kolonner, men ikke 0 (som er en faktisk verdi, ikke falsy). Her brukte jeg ChatGPT til å hjelpe meg med condition.

Relevant kodelinje:

```py
if any(row[col] is None or row[col] == "" for col in headers):
```

**prompt**:

`I want to jump over any row with empty cells from this DictRead loop, but not those with the number 0, as I would like to parse that. Explain how I can make this work.`

**Response**:
```
Good catch 👀 — that’s an important edge case.
In Python, 0 is treated as False in a boolean context. So with this code:

if any(not line[h] for h in headers):
    continue

a cell containing 0 would be seen as “missing” (because not 0 == True).
But often in CSV data, 0 is a perfectly valid value (e.g. age = 0, quantity = 0).

Safer check

If you want to only skip truly empty cells (not 0), be more explicit:

if any(line[h] is None or line[h] == "" for h in headers):
    continue

Now:

None → considered missing
"" (empty string) → considered missing
"0" (string from CSV) → not missing
" " (just spaces) → still counts as not missing unless you also strip:

if any(line[h] is None or line[h].strip() == "" for h in headers):
    continue
```
</details>