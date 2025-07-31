---
title: encryptworkbook3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\encryptworkbook3.md
created_at: 2025-07-03
---








  









### Encrypt workbook {#encrypt-workbook style="tab-stops: 0pt"}

Encryption

Encryption is used to protect the workbook data with password. It converts the data into an encrypted format (unreadable). This restricts anonymous users to access the data. You can achieve this by two methods. They are:

[·      ]Using method

[·      ]Using command

 

Method

To encrypt a workbook, pass the password in the EncryptWorkBook method. The following code illustrates this:

 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                         |
| []                                                                     |
|                                                                                                                         |
| [spreadControl.EncryptWorkBook([\"asd123\"]);] |
+-------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                       |
|                                                                                                                        |
| [spreadControl.EncryptWorkBook([\"asd123\"])] |
+------------------------------------------------------------------------------------------------------------------------+

 

Encrypt workbook using the Commands

You can also encrypt the workbook using the *Encrypt Document* dialog box. You can open the Encrypt Document dialog using the *EncryptCommand.*

 

{border="0"}

Figure 37: Encrypt Document dialog box

 

The following code illustrates how to bind the *EncryptCommand* to a button:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Button][ Command][=\"{][Binding][ Path][=] [EncryptCommand}\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Button][\>]                                                                                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Open Encrypted Document

When you open encrypted document Password dialog box will open. Enter password to decrypt the data.

 

{border="0"}

Figure 38: Password Dialog

 

[]{#related-topics}

