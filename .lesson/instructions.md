# Instruktioner


Om du behöver, använd följande fusklapp: [Flask Cheatsheet](https://www.codecademy.com/learn/learn-flask/modules/introduction-to-flask/cheatsheet).


## Konfiguera Flask-applikationen

**1.**

Börja med att, i toppen av filen **app.py**, importera klassen `Flask` från modulen `flask`.

Om du kör din kod i detta skede, kommer ett `NameError` att uppstå, men oroa dig inte, detta kommer vi att rätta till i nästa steg när du skapar din applikation!

**2.**

Skapa en instans av klassen `Flask`, där du passerar in `__name__` som argument, och tilldela denna instans till en variabel som heter `app`.

Om du kör din kod nu, kommer så ett felmeddelande om att URL:en inte kan hittas (Not Found) att visas, men detta kommer vi också att hantera i nästa steg när du definierar din första route (rutt)!

## Skapa startsidan

**3.**

För att skapa startsidan, börjar du med att definiera en vyfunktion med namnet `index()` som returnerar ett HTML-element `<h1>` med texten `Adopt a Pet!`. Tänk på att HTML kan returneras som en textsträng.

**4.**

Använd dekorationen `route()` för att koppla URL-vägen `'/'` till vyfunktionen `index()`.

Kör din kod nu, och du bör kunna se rubriken på sidan!

**5.**

Vi utökar sidan med fler element.

 Direkt efter `<h1>`-elementet, lägg till ett `<p>`-element som innehåller texten `Browse through the links below to find your new furry friend:`.

**6.** 

Efter `<p>`-elementet, skapa en punktlista med `<ul>`. Denna lista ska innehålla tre punkter: `Dogs`, `Cats` och `Kaniner`. Använd `<li>`-taggen för att skapa varje punkt i listan.

**Tips:** När du skriver HTML-kod inuti en Python-funktion, använd trippel citatstecken `'''` istället för enkla. Detta gör det enklare att skriva och läsa HTML-koden eftersom du kan placera varje element på en egen rad, vilket ökar kodens läsbarhet och underlättar underhåll. Dessutom kan du enkelt inkludera dubbelcitat inom HTML-koden utan att behöva oroa dig för att avsluta strängen av misstag.

## Skapa rutt för `animals`

**7.**

Visst börjar webbplatsen se bra ut! Nu är det dags att skapa separata sidor för varje djurtyp och länka dem från vår punktlista. Detta gör vi genom att lägga till en ny `animals`-rutt.

Först, skapa en vyfunktion kallad `animals()`. Inom denna funktion, skapa en sträng som innehåller ett `<h1>`-element med texten `List of pets`. Tilldela denna sträng till variabeln `html`. Slutligen, se till att funktionen returnerar `html`.

**8.**

Använd `route()`-dekorationen för att koppla `animals()`-funktionen till URL-mönstret `'/animals/X'`, där `X` representerar en variabel del av URL:en. Ge denna variabla namnet `pet_type`.

**9.** 

Därefter, modifiera `animals()`-funktionen så att den accepterar en parameter kallad `pet_type`. Inuti funktionen, uppdatera `<h1>`-rubriken till `List of X`, där `X` ska ersättas med värdet av `pet_type`.

**10.**

Nu är vi redo att skapa interaktiva länkar på vår startsida, vilka pekar mot varje specifik djursida! Inne i `index()`-funktionen, omvandla varje punkt i listan till en länk. Detta gör du genom att infoga ett `<a>`-element inuti varje `<li>`-element:

* `Dogs` ska länka till `'/animals/dogs'`
* `Cats` ska länka till `'/animals/cats'`
* `Rabbits` ska länka till `'/animals/rabbits'`

Starta din kod nu och testa att klicka på länkarna!

## Berika sidan med innehåll

**11.**

I Replit IDE, öppna filen **helper.py** som du hittar i filutforskaren på vänster sida.

Denna fil innehåller en ordbok (dictionary) vid namn `pets`, som innefattar data som vi kan använda för att fylla våra webbsidor med innehåll.

Ordboken `pets` består av tre element, ett för varje typ av djur. Nyckeln är djurtypen och värdet är en lista av ordböcker, var och en innehållande information om ett specifikt djur.

Börja med att importera `pets`-ordboken till början av din **app.py**-fil.

**12.**

Inuti `animals()`-funktionen kommer du att anpassa `html` så att det visar namnen på alla tillgängliga djur av typen `pet_type`.

Strax före `return`-satsen, skapa en for-loop som itererar igenom varje djur i listan. Du kan hitta den relevanta listan av djur i `pets`-ordboken genom att använda `pet_type` som nyckel. I varje iteration, skapa ett `<li>`-element för varje djurs namn och lägg till detta i `html`.

Kom också ihåg att lägga till en öppnande `<ul>`-tagg i `html` före loopen och en avslutande `</ul>`-tagg efter loopen. Detta ser till att dina `<li>`-element är korrekt inneslutna inom `<ul>`-elementet.

När du har startat din kod och besöker de olika djursidorna, bör du nu kunna se en lista med alla tillgängliga djur!

## Skapa rutt för `pets`

**13.**

Nu är det dags att ta nästa steg och skapa individuella profilsidor för varje djur, vilket vi åstadkommer genom att introducera en ny `pet`-rutt.

Skapa en vyfunktion med namnet `pet()` som kopplas till URL-mönstret `'/animals/X/#'`, där `X` och `#` utgör variabla delar av URL:en. Här ska `X` benämnas `pet_type` och `#` benämnas `pet_id`. Använd en konverterare för att försäkra att `pet_id` är ett positivt heltal.

Därefter, inkludera `pet_type` och `pet_id` som argument till `pet()`-funktionen.

**14.**

I funktionens kodblock, skapa en variabel med namnet `pet` som lagrar profildetaljerna för det djur som matchar `pet_type` och har indexpositionen `pet_id` i dess djurlista.

Detta innebär att du först ska hitta rätt lista i `pets`-ordboken med `pet_type` som nyckel. Sedan hittar du rätt ordbok i listan genom att använda `pet_id` som index.

Den skapade `pet`-ordboken kommer att innehålla följande:

```python
{
  'name': ...,
  'age': ...,
  'breed': ...,
  'description': ...,
  'url': ...
}
```

**15.**

Från `pet()`-funktionen, returnera ett HTML `<h1>`-element som visar djurets namn. Namnet hittar du i `pet`-ordboken som du skapade tidigare.

**16.**

Det är nu dags att skapa länkar på djursidan som leder till varje djurs individuella profilsida. Inuti `animals()`-funktionen, omvandla varje punkt i listan till en länk genom att infoga ett `<a>`-element i varje `<li>`-element.

Den önskade URL-strukturen ska följa mönstret `'/animals/X/#'`, där `X` representerar `pet_type` och `#` indexpositionen. För att uppnå detta behöver vi modifiera for-loopen så att `enumerate()` används för att loopa över både index och element.

När allt är klart, kör din kod och testa att navigera till de enskilda djurprofilssidorna.

**17.**

Till sist, för att ytterligare berika profilsidan, lägg till följande HTML-element inuti `pet()`-funktionen, strax efter `<h1>`-elementet, för att presentera profilinformationen från `pet`-ordboken:

- `<img>` för att visa bilden från den angivna URL:en.
- `<p>` som innehåller en beskrivning av djuret.
- `<ul>` med två `<li>`-element: ett för djurets ras och ett för dess ålder.