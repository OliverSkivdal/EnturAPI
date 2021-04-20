# EnturAPI
En enkel måte å hente ut sanntidsdata fra Entur

Denne kan for eksempel brukes til å vise sanntidsdata for nærmeste stopp på en liten tekstskjerm som vist på bildet 
![Sanntidsskjerm](https://user-images.githubusercontent.com/63880823/115404858-000be500-a1ee-11eb-8160-c1fb37445f89.jpg)

Denne kan også benyttes for å enkelt vise tider på ditt nærmeste busstopp rett i terminalen.

# Oppsett
For å komme i gang med denne må du først gjøre noen endringer i API.py filen.
1. Erstatt DITTKLIENTNAVN-HER i linje 3 med navnet på ditt prosjekt.
2. Fyll inn NSR:StopPlace IDen for stoppet du ønsker data for på linje 17
3. Du kan velge hvor mange resultater du ønsker ved å endre tallet etter "numberOfDepartures:" på linje 20

Det er også mulig å endre konfigurasjonen for 'sed' i Start.sh filen om du ønsker å ikke vise enkelte linjer eller innhold i output.
