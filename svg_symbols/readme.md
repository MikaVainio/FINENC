# SVG-symboleja sähköisiin merikarttoihin

QGIS käyttää kartoissa SVG-grafiikkaa symbolien esittämiseen. Karttamerkin keskipiste piirretään arkin keskelle. Esimerkeissä on käytetty A4-arkkia (210 x 297 mm). Piirto-ohjelmana voi käyttää mitä tahansa vektorigrafiikkasovellusta, joka tukee SVG-muotoon tallentamista.

Merimerkkien keskipiste on merkin alareunassa olevan ympyrän keskellä. Täyttöväri ja viivojen väri voidaan muuttaa QGIS-ohjelmasta käsin. Värien ja viivapaksuuksien muuttaminen edellyttää parametrointia. Sen voi tehdä muokkaamalla SVG-tiedostoa XML-editorilla.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="210mm" height="297mm" version="1.1" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd"
viewBox="0 0 21000 29700"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <g id="huippumerkki">
  <polygon fill="param(fill) #FFF" stroke="param(outline) #000" stroke-width="param(outline-width) 1" points="-8205,2834 -9156,4322 -10107,5811 -8205,5811 -6303,5811 -7254,4322 "/>
  <polygon fill="param(fill) #FFF" stroke="param(outline) #000" stroke-width="param(outline-width) 1" points="10545,227 9595,1715 8644,3204 10545,3204 12447,3204 11496,1715 "/>
  <polygon fill="param(fill) #FFF" stroke="param(outline) #000" stroke-width="param(outline-width) 1" points="-8205,-378 -9156,1111 -10107,2599 -8205,2599 -6303,2599 -7254,1111 "/>
  <polygon fill="param(fill) #FFF" stroke="param(outline) #000" stroke-width="param(outline-width) 1" points="27667,9390 28618,7902 29569,6414 27667,6414 25765,6414 26716,7902 "/>
 </g>
</svg>
```

Kiinteät värit ja viivaleveys, esim.  `polygon fill="black" stroke="black" stroke-width="7.62" ` muutetaan parametroituun muotoon
`polygon fill="param(fill) #FFF" stroke="param(outline) #000" stroke-width="param(outline-width) 1"`
