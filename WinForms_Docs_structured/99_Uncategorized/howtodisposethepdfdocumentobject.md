---
title: howtodisposethepdfdocumentobject.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodisposethepdfdocumentobject.md
created_at: 2025-07-03
---






#### How To Dispose The Pdf document Object? {#how-to-dispose-the-pdf-document-object style="tab-stops: 0pt"}

 

You can dispose the Pdf object by using the **Close** method. Note that without closing this object, it is not possible to use the same document again for any other manipulation.

 

**Close** method releases the commonly used memory. Its overload with its parameter set to true \[Close(true)\], releases the entire document stream, enabling it to be reused.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                      |
|                                                                                                                     |
| []                                                                |
|                                                                                                                     |
| [// Release the common resources.        ]                        |
|                                                                                                                     |
| [pdfDoc.Close();]                                                               |
|                                                                                                                     |
| []                                                                              |
|                                                                                                                     |
| [// (or)]                                                         |
|                                                                                                                     |
| []                                                                |
|                                                                                                                     |
| [// Releases document stream. This releases the entire document.] |
|                                                                                                                     |
| [PdfDoc.Close([true]);]                                    |
+---------------------------------------------------------------------------------------------------------------------+

[                     ]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| [\' Release the common resources.  ][      ]                                              |
|                                                                                                                                                                                                                               |
| [pdfDoc.Close()]                                                                                                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [\' (or)]                                                                                                                                                   |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [\' Releases document stream. This releases the entire document.]                                                                                           |
|                                                                                                                                                                                                                               |
| [PdfDoc.Close(][True][)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

