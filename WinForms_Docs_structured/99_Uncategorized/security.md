---
title: security.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\security.md
created_at: 2025-07-03
---








  









## Security {#security style="tab-stops: 0pt"}

 

DocIO provides support to protect a Word document. Here protection restricts the access to the elements present within the document. In MS Word, a document is protected through the **Protect Document** option in the **Tools** menu.

 

{border="0"}

Figure 80: Protect Document option in the Tools Menu

*[]* 

[]{#p85}{border="0"}

Figure 81: Protect Document Dialog Box

 

DocIO supports such protection while reading and writing Word documents for both **.doc** and **.docx** formats, and this can be provided through the following APIs.

*[]* 

[·      ]**AllowOnlyComments---**only comments are allowed.

[·      ]**AllowOnlyFormFields---**modification of form field value is allowed.

[·      ]**AllowOnlyRevisions---**only revisions are allowed.

[·      ]**AllowOnlyReading**---only reading is allowed.

[·      ]**NoProtection---**document has no protection.

 

You can also provide a password to restrict the user from editing documents. You can enable or disable document protection by using the **WordDocument.ProtectionType** property, when the document is opened with DocIO.

 

The following example illustrates the use of ProtectionType property.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [IWordDocument][ doc = [new] [WordDocument]( [\"sample.doc\"]);] |
|                                                                                                                                                                                                                        |
| [doc.Protect([ProtectionType].[AllowOnlyComments],[\"password\"]);]                                              |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [doc.Save( [\"Protection.doc\"] );]                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [Dim][ doc [As] IWordDocument = [New] WordDocument([\"sample.doc\"])] |
|                                                                                                                                                                                                                             |
| [doc.Protect([ProtectionType].[AllowOnlyComments],[\"password\"])]                                                   |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [doc.Save([\"Protection.doc\"])]                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

For More Information Refer:

[[[[Encryption and Decryption]]{.underline}]()]{.UGHyperlink}

[]{#_Encryption_and_Decryption} 

More:





