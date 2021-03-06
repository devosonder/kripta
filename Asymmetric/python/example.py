from KriptaRSA import KriptaRSA

k = KriptaRSA()

# You can generate KeyPairs here:
# print(k.generate_RSA())

# You can set/get PublicKey or Private key :
k.setPublicKey('-----BEGIN PUBLIC KEY-----\n'+
'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb8Jqk7U9RMEzb4bvO63EtDTHR\n'+
'LUQg8cJD5/0OQB1yx0Tro6sWNHScn40Px5+SHQYtH9VQPAcydJ+3wS/K7gA5D+r3\n'+
'RqqJMLWV1EkXQ6U0/3QR38twXN4eP9gqI1WaAW4Fad8kiuxfaVtEmmng9BN2ccg0\n'+
'RP80PMCLjDP0gv+umwIDAQAB\n'+
'-----END PUBLIC KEY-----')

k.setPrivateKey('-----BEGIN RSA PRIVATE KEY-----\n'+
'MIICXAIBAAKBgQCb8Jqk7U9RMEzb4bvO63EtDTHRLUQg8cJD5/0OQB1yx0Tro6sW\n'+
'NHScn40Px5+SHQYtH9VQPAcydJ+3wS/K7gA5D+r3RqqJMLWV1EkXQ6U0/3QR38tw\n'+
'XN4eP9gqI1WaAW4Fad8kiuxfaVtEmmng9BN2ccg0RP80PMCLjDP0gv+umwIDAQAB\n'+
'AoGBAJPhemYJfnyZ92lWCsrR0ERPDP03ljI/0mCfcgW/m62rd5qXXbnzCNs3G4jp\n'+
'YFQqHh9Q3vP12UVp/8U8+VvSlHYMSmWH0Tzcm2G894+V5WKfPAadYnTfRWIdhZs8\n'+
'eMpKmBL/R4ITprAIapz/2JkHoXMVVhjsmvSuR/UpXb4BfmYBAkEAtvITL7Z8z2tu\n'+
'Yi8Vn5dEvqlyha1my6hVeEvPI14RYfSSJUAVROGsjfz1Gfe6jJb53DBd7rylYcSZ\n'+
'62KwGjo6gQJBANo10imgQWjX0MurYen1kWWMIOx/DotPf39gB/vfWgOdm+8j72da\n'+
'iSSHUogPQX+fPYr8W55rFZfdjkEenAIsAxsCQED/72szZlL386c03XTvdQBdChCO\n'+
'1IgljgCIxtblFD3+fHJ5u1TW7c0hBCCu0PwkpC/ki2tIYWZESP/F95XJ/IECQEpy\n'+
'KERpV0eEsch6rQob7MH/X9AvvO+MbMwxICgvWE95exTIZsoVGkrrHB4tTkRTOLTt\n'+
'SfivQguw2/Kdlc4r49cCQEgULygEDSzkkz3FD0KCy9jprYs9Pdswc5Log19kW3Ih\n'+
'ELBTlo8/pPOqTVTgJ2XNCsXrZDtkM2j0e8MiFhXhDZ0=\n'+
'-----END RSA PRIVATE KEY-----')

print("\nWELCOME TO KRIPTA-RSA-PYTHON")
# message = "Mon message Secret Mon message Secret Mon message Secret Mon"
message = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
print("-----------------------------------------------------")
print("Message : ", message)
print("len(Message) : ", len(message))
print("-----------------------------------------------------")
print("PublicKey : ", k.getPublicKey().decode("utf-8"))
print("-----------------------------------------------------")
print("PrivateKey : ", k.getPrivateKey().decode("utf-8"))
print("-----------------------------------------------------")
encrypted_msg = k.encrypt(k.getPublicKey(), message.encode())
print("Encrypted-Message : ", encrypted_msg)
print("-----------------------------------------------------")
print("Decrypted-Message : ", k.decrypt(encrypted_msg))
print("-----------------------------------------------------")