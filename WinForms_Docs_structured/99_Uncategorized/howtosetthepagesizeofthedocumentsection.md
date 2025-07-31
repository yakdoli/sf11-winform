---
title: howtosetthepagesizeofthedocumentsection.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthepagesizeofthedocumentsection.md
created_at: 2025-07-03
---








  









## How to set the Page Size of the Document Section? {#how-to-set-the-page-size-of-the-document-section style="tab-stops: 0pt"}

 

The page size of the document section is set by using the **PageSize** property of the PageSetup object. The following code snippet illustrates how to set this property.

 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [document.Sections\[0\].PageSetup.PageSize = [PageSize].B6;] |
+-----------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                          |
|                                                                                             |
| []                                        |
|                                                                                             |
| [document.Sections(0).PageSetup.PageSize = PageSize.B6] |
+---------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

