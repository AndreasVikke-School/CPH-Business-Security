# Week 5 - Security+Penetration-Testing, Tools + how to practice 

### Explain briefly about the concept of Security Testing, and more thoroughly about Penetration Testing
Security Testing er en metode til altid at teste systemer undervejs i forløbet, "Test Early and Test Often".
    - Manuel inspection og anmeldelser
    - Threat Modeling
    - Code Review
    - Penetration Testing

En af metoderne der kan bruges er Penetration Testing, hvor en attacker for et bruger loggin og skal derfra finde en vej ind i systemet. Attackeren kender ikke til hvordan programmet virker (black box) men prøver at finde vulnerabilities ved at agere som en hacker.

### Explain the pros & cons related to Penetration Testing
#### Pros
- Det er hurtigt og derved billigt
- Kræver mindre skill-set end source code review.
- Koden der bliver testet er koden der vil udsat

#### Cons
- Det sker for sent i SDLC (Systems development life cycle)
- Tester kun fra fronten

### Explain a few (one or two) of the tools meant for Penetration Testing
- NMAP (netdiscover)
    - Kan scanne netværker, finde åbne porte eller gætte OS brugt.
- WireShark
    - Network Protocol analyzer, bruges til at catche indgående og udgående traffik på systemet. HTTP, DNS, IP osv.
- BurpSuite
    - Tool til at intercepte requests, og ændre på dem inden de bliver sent

### Explain the purpose of NMap and what can be discovered with the tool, using one or more prepared samples
1. NMAP kan finde åbne porte på et netværk.
    - nc -lvp 2222
    - nmap 127.0.0.1
|PORT|STATE|SERVICE|
|---|---|---|---|
|21/tcp|filtered|ftp|
|53/tcp|open|domain|
|80/tcp|filtered|http|
|3333/tcp|open|dec-notes|
|5555/tcp|filtered|freeciv|
2. NMAP kan også finde hvilket OS systemt kører
    - nmap 91.100.104.27 -O
        - Running: Linux 2.6.X

### Explain “ways” to legally practice Penetration Tester Skills
### Explain the concepts (where do they fit in) Kali Linux, Metasploitable 2 (and 3) OWASP Juice Shop.
### Explain a possible test-setup using Kali Linux and Metasploitable x (or similar) and why testing/practising in this way “makes sense”
