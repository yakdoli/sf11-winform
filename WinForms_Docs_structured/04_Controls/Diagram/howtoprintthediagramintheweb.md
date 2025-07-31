---
title: howtoprintthediagramintheweb.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\howtoprintthediagramintheweb.md
created_at: 2025-07-03
---








  









## How to print the diagram in the Web?[] {#how-to-print-the-diagram-in-the-web style="tab-stops: 0pt"}

[] 

We can print the diagram by saving the diagram as an image and navigating to that image in a new window. We need to use the Syncfusion Window control for this purpose. We can store the diagram image inside the Window control using the**window.navigate**(\'image.jpg\') method. In the new window, you could find options for printing the image.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [\<][script][  [type][=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                  |
| [   ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                  |
| [  [function] Print()]                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [  {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                  |
| [   window.navigate([\'image.jpg\']);]                                                                                                                                |
|                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [\</][script][\>]                                                           |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [// Code snippet for save Diagram as image.]                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                        |
|                                                                                                                                                                                                            |
| [// Export to image.]                                                                                                                                    |
|                                                                                                                                                                                                            |
| [System.Drawing.[Image] img = [this].DiagramWebControl1.View.ExportDiagramAsImage([true]);            ] |
|                                                                                                                                                                                                            |
| [img.Save(Server.MapPath([\"Image.jpg\"]), System.Drawing.Imaging.[ImageFormat].Jpeg);]                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [\' Export to image.]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [Dim][ img [As] System.Drawing.Image = [Me].DiagramWebControl1.View.ExportDiagramAsImage([True])] |
|                                                                                                                                                                                                                                                       |
| [img.Save(Server.MapPath([\"Image.jpg\"]), System.Drawing.Imaging.ImageFormat.Jpeg)]                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

