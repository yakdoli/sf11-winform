---
title: bitmapgeneration.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\bitmapgeneration.md
created_at: 2025-07-03
---








  









### Bitmap Generation {#bitmap-generation style="tab-stops: 0pt"}

 

The Edit Control has the ability to generate a bitmap image of itself. The bitmap image looks exactly like an actual snapshot of a live instance of Edit Control. This is achieved through the use of the **CreateBitmap** method.

 

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                              |
|                                                                                                             |
| []                                                        |
|                                                                                                             |
| [// Creates bitmap of the Edit Control.]                  |
|                                                                                                             |
| [Bitmap bmp = [this].editControl1.CreateBitmap();] |
+-------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [\' Creates bitmap of the Edit Control.]                                                                                                |
|                                                                                                                                                                                           |
| [Dim ][bmp [as ]Bitmap = [Me].editControl1.CreateBitmap()] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 45: Bitmap of a Live Instance of Edit Control

[]{#p67} 

[]{#related-topics}

