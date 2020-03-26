# Week-09 SSH + Crypto-1

### Explain conceptually all the following terms, and how/why they are needed for SSH and TLS/SSL.
* Symmetric Encryption
- En algoritme for kryptografi som bruger en kryptografiske nøgle for at enkryptere en plain tekst og dekryptering af en cipher tekst.
- Use case: Ex bluetooth.
* Asymmetric Encryption
- En algoritme for kryptografi som bruger et par af kryptografiske nøgler for at kunne enkryptere en plain tekst og dekryptere en cipher tekst. Den offentlige nøgle(public) er kendt af mange og den private nøgle(private) er kun kendt af egeren(ham der laver nøglen/kryptere teksten)
- Use case: Ex SSH / Dankort systemer.
* Hashing
- En særlig funktion som bruges til at omdanne data fra en stor definitionsmængde til en mindre værdimængde. Har så få kollisioner som muligt, En kollision er når to forskellige inddata giver samme funktionsværdi. Det er kun muligt at gå den ene vej.
- Use case: Sortering af nøgle/værdier(key/value) par i en database.

### Explain what it takes to safely log in to an SSH server, without having to provide a password.


### Explain the term SSH-tunnel, and provide a practical example for its use.


### Explain conceptually the purpose of Symmetrical Encryption, Asymmetrical Encryption and hashing for an SSH-connection.


### Explain the steps you have to go through to set up a server with MySQL,  as secure as possible →
* How can we limit the client IP's that can connect
* If set up to allow only localhost and a firewall that deny 3306, can we still connect “safely” from a remote server 
* how to set up an SSL connection that  anyone can use
* Demonstrate a client application (Java or whatever you prefer) running on a separate server that access the Database using SSL