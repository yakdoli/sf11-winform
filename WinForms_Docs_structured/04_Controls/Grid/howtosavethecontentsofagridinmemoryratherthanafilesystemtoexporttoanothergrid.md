---
title: howtosavethecontentsofagridinmemoryratherthanafilesystemtoexporttoanothergrid.md
original_path: WinForms_Docs/04_Controls/Grid/howtosavethecontentsofagridinmemoryratherthanafilesystemtoexporttoanothergrid.md
created_at: 2025-08-05
---








  









### How to save the contents of a Grid in memory rather than a file system to export to another grid {#how-to-save-the-contents-of-a-grid-in-memory-rather-than-a-file-system-to-export-to-another-grid style="tab-stops: 0pt"}

[] 

 You can save the contents of a grid in memory rather than writing to a file system. This can be done using the **SaveSoap** or **SaveBinary** method of GridControl. The below code snippet illustrates how this can be done.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                       |
| [MemoryStream s = [new] MemoryStream();]                                     |
|                                                                                                                                       |
| [gridControl1.Model.SaveSoap(s); [// or gridControl1.Model.SaveBinary(s);]] |
|                                                                                                                                       |
| [s.Position = 0;]                                                                                 |
|                                                                                                                                       |
| [gridControl1.Model = [GridModel].LoadSoap(s);]                              |
|                                                                                                                                       |
| [gridControl2.Model = [GridModel].LoadSoap(s);]                              |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [Dim][ s [As] MemoryStream = [New] MemoryStream()] |
|                                                                                                                                                                                   |
| [gridControl1.Model.SaveSoap(s) [\' or gridControl1.Model.SaveBinary(s);]]                                              |
|                                                                                                                                                                                   |
| [s.Position = 0]                                                                                                                              |
|                                                                                                                                                                                   |
| [gridControl1.Model = GridModel.LoadSoap(s)]                                                                                                  |
|                                                                                                                                                                                   |
| [gridControl2.Model = GridModel.LoadSoap(s)]                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p563} 

 

[]{#related-topics}

