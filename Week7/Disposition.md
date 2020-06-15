# Week 7 - OWASP A6: Security Misconfiguration + A9 Using Components with Known Vulnerabilities

### Explain briefly about the A6 Security Misconfiguration Risk, including topics from:
Atacker vil prøve at explote ikke opdaterede ting, defualt accounts, unprotected files and directories.
- Is the Application Vulnerable
    - Ja hvis ting ikke bliver opdateret eller filer ikke bliver beskyttet med privilegier.
- How to Prevent
    - En minimal platform, fjern biblioteker der ike bliver brugt. Og have en god CI (Continues Integration)
- Example Attack Scenarios
    - Serveren kommer med eksempel applicationer som ikke blvier fjernet eller opdateret. Hvis der findes et brud på en af disse er det nemt for hackere at bruge dem.

### Explain and demonstrate a number of the new Security Headers used by modern browsers, with emphasis on how they can increase security and the problem they protect against
- X-XSS-Protection (0/1)
    Stopper sider fra at loade hvis der detekteres cross-site scripting
- X-Frame-Options (DENY/SAMEORIGIN)
    Stopper brugen a I-Frames fra andre kilder på siden.
- X-Content-Type-Options
    Stopper browseren for at ændre MIME type på content

### Demonstrate shortly how many properties of a sample (misconfigured) application a hacker can discover.

### Explain, as many as you can come up with, Security Misconfigurations, made deliberately throughout this semester, to make it possible to demonstrate “real attacks”
- admin/test
- JWT token

### Explain briefly about the OWASP A9 threat

### Provide and demonstrate practical examples for how to ensure that our maven dependencies do not contain Known Vulnerabilities? (Feel free to replace Java/maven above with examples from other technologies such as JavaScript, Python …)
- https://snyk.io/vuln/?packageManager=all