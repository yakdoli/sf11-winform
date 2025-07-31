---
title: filename.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\filename.md
created_at: 2025-07-03
---






#### Filename {#filename style="tab-stops: 0pt"}

Filename with Path

You can also export Page as an image file with directory path and file name.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                 |
| [diagramview.Save([@\"D:\\ Diagram.jpeg\"]);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

  

Filename with Rect and Encoder

You can also specify the name of the file directly, specified portions of the DiagramPage, type of encoder such as TiffBitmapEncoder and GifBitmapEncoder.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                     |
| [TiffBitmapEncoder][ encoder = [new] [TiffBitmapEncoder]();]                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [ [Rect] rect = [new] [Rect]([new] [Point](100, 100), [new] [Point](300, 300));] |
|                                                                                                                                                                                                                                                                                     |
| [ [string] filename = [\" Diagram.jpeg\"];[]]                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [diagramview.Save(filename, rect, encoder);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

