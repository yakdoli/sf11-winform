---
title: howtoattachatemplate.md
original_path: WinForms_Docs/99_Uncategorized/howtoattachatemplate.md
created_at: 2025-08-05
---








  





## How to Attach a Template to a Word Document? {#how-to-attach-a-template-to-a-word-document style="tab-stops: 0pt"}

You can use the **AttachedTemplate** property to attach a template to a Word document using DocIO. The following code example illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                       |
|                                                                                                                                                                                                        |
| []                                                                                                                                     |
|                                                                                                                                                                                                        |
| [//Set the location of the template ]                                                                                                                |
|                                                                                                                                                                                                        |
| [document.AttachedTemplate.Path = [@\"D:\\Test.dot\"];]                                                                                    |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [//Set the UpdateStylesOnOpen to 'true' to automatically update the styles from the attached template each time the document is opened with MS Word] |
|                                                                                                                                                                                                        |
| [document.UpdateStylesOnOpen = [true];][]                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                     |
|                                                                                                                                                                                                        |
| [ ][//Set the location of the template document]                                     |
|                                                                                                                                                                                                        |
| [document.AttachedTemplate.Path = [@\"D:\\Test.dot\"]]                                                                                     |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [//Set the UpdateStylesOnOpen to 'true' to automatically update the styles from the attached template each time the document is opened with MS Word] |
|                                                                                                                                                                                                        |
| [document.UpdateStylesOnOpen = [true]][]                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

