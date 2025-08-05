---
title: encryptionanddecryption.md
original_path: WinForms_Docs/99_Uncategorized/encryptionanddecryption.md
created_at: 2025-08-05
---








  









### Encryption and Decryption {#encryption-and-decryption style="tab-stops: 0pt"}

 

**Encryption** is a method of protecting the Word document. It is based on a password, which converts it into a form that cannot be understood. It restricts anonymous users from accessing a document.

 

**Decryption** is the process of converting encrypted data, back into its original form so that data can be read from the document. A password for encrypting a Word document is set in Microsoft Word through the **Security** tab in the **Options** dialog box.

 

The following example illustrates how to encrypt and decrypt a Word document.

 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                             |
|                                                                                                                            |
| []                                                                                     |
|                                                                                                                            |
| [//Encrypting the Word document with password.]                          |
|                                                                                                                            |
| [document.EncryptDocument(password);]                                                  |
|                                                                                                                            |
| []                                                                                     |
|                                                                                                                            |
| [// Opening the encrypted Workbook.]                                     |
|                                                                                                                            |
| [WordDocument document = [new] WordDocument(filename, password);] |
+----------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                             |
| [\'Encrypting the Word document with password.]                                                                                           |
|                                                                                                                                                                                             |
| [document.EncryptDocument(password)]                                                                                                                    |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [\'Opening the encrypted Workbook.]                                                                                                       |
|                                                                                                                                                                                             |
| [Dim][ document [As] [New] WordDocument(filename, password)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

Encryption and Decryption Samples Installation Location:

To Locate the Encrypt and Decrypt samples:

\\DocIO.WPF\\Samples\\3.5\\WindowsSamples\\Prepare\\Encrypt and Decrypt

 

Viewing Encryption and Decryption samples:

 

1.   Click **Start**\--\>**All Programs**\--\>**Syncfusion**\--\>**Essential Studio \<version number\>** \--\>**Dashboard**.

2.   Open **Reporting** edition samples. Click the drop-down button of **WPF** platform and select the **Explore samples** option.

 

For more information refer to section .

 

[]{#related-topics}

