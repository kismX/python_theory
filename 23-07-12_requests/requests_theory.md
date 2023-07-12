# HTTP Requests
- requests library braucht man um infos einer source zu bekommen

## status codes
- 100: bearbeitung von anfragen.. evtl delay bei seite
- 2xx: source erreicht, datenabruf erfolgreich (alles ok)
- 3xx: umleitung von url auf andere
- 4xx: source nicht erreich bar (zb 404 seite nicht erreichbar)
- 5xx: serverseitige fehler - zb unerreichbarkeit / interne err
- 9xx: nicht server oder client sondern netwerk verursacht fehler (refresh kann helfen)
