---
title: howtocopypastenodesinessentialdiagram.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\howtocopypastenodesinessentialdiagram.md
created_at: 2025-07-03
---








  









## How To Copy / Paste Nodes In Essential Diagram {#how-to-copy-paste-nodes-in-essential-diagram style="tab-stops: 0pt"}

[] 

The following code snippet illustrates how you can copy / paste nodes (symbol, shape, or link) in Essential Diagram.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [//Copy Code]                                                                                                                                           |
|                                                                                                                                                                                                           |
| [this][.diagram1.Controller.Copy();]                                                                                 |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [//Paste Code]                                                                                                                                          |
|                                                                                                                                                                                                           |
| [//If the data in the clipboard is of the type ClipboardNodeCollection, paste it onto the Diagram.]                                                     |
|                                                                                                                                                                                                           |
| [IDataObject][ clipboardData = [Clipboard].GetDataObject();]                                    |
|                                                                                                                                                                                                           |
| [if][ (clipboardData.GetDataPresent([typeof]([ClipboardNodeCollection])))] |
|                                                                                                                                                                                                           |
| [{]                                                                                                                                                                   |
|                                                                                                                                                                                                           |
| [this][.diagram1.Controller.Paste();]                                                                                |
|                                                                                                                                                                                                           |
| [}]                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [\'Copy Code]                                                                                                                             |
|                                                                                                                                                                                             |
| [Me][.diagram1.Controller.Copy()]                                                                      |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [\'Paste Code]                                                                                                                            |
|                                                                                                                                                                                             |
| [\'If the data in the clipboard is of the type ClipboardNodeCollection, paste it onto the Diagram.]                                       |
|                                                                                                                                                                                             |
| [Dim][ clipboardData [As] IDataObject = Clipboard.GetDataObject()]                |
|                                                                                                                                                                                             |
| [If][ clipboardData.GetDataPresent(Type.GetType(ClipboardNodeCollection)) [Then]] |
|                                                                                                                                                                                             |
| [Me][.diagram1.Controller.Paste()]                                                                     |
|                                                                                                                                                                                             |
| [End][ [If]]                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p76} 

 

[]{#related-topics}

