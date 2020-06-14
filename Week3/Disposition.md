# Week 3 - Logging and monitoring

### Explain the difference between prevention, detection and recovery for systems you develop.
- Prevention
    - Her forbygger du systemet til at modstå de ting der kan ske, ved at sikre de velkendte 10 OWASP ting.
- Detection
    - Her bruger du logs og monitorering til at se om der er sket et brud.
- Recovery
    - Hvis der er sket et brud så fikses det og der lukkes ned for bruddet.

### Discuss how a firewall can produce log files.
Hver gang en forspørgelse bliver lavet til serveren vil den komme forbi firwallen, her bliver den enten godkendt og sendt videre ind eller ikke. Når forspørgelsen rammer kan der laves en log på det, med information såsom IP og tid.

### Explain how to set up a remote logging server, and use that to register logins to an ubuntu server.
Først sættes en HTTP server op med en context path f.eks. /logger, her efter akn vores firewall på den anden server sende et POST request til denne context hvorefter det kan skrives ind i en log fil.

### Explain how to use a cloud-based logging service to enable anomaly detection.
Fleste store cloud-based logging services såsom f.eks. Azure Stream, har veltrænede AI som kan detektere anomaly i real-time. Derfor er det en god ide at bruge disse services, da det vil tage lang tid at træne dem selv.