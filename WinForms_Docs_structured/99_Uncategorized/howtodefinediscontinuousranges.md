---
title: howtodefinediscontinuousranges.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodefinediscontinuousranges.md
created_at: 2025-07-03
---








  









### How to define discontinuous ranges? {#how-to-define-discontinuous-ranges style="tab-stops: 0pt"}

 

You can set a discontinuous range by adding different ranges to the Range collection. The following code example illustrates this.

 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [// Create Range collection.]                                                              |
|                                                                                                                                              |
| [IRanges][ rangesOne = sheet.CreateRangesCollection();] |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [// Add different ranges to the Range collection.]                                         |
|                                                                                                                                              |
| [rangesOne.Add(sheet.Range\[[\"D2:D3\"]\]);]                                      |
|                                                                                                                                              |
| [rangesOne.Add(sheet.Range\[[\"D10:D11\"]\]);]                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [\' Create Range collection.  ]                                                                                                          |
|                                                                                                                                                                                            |
| [Dim][ rangesOne [As] Syncfusion.XlsIO.IRanges = sheet.CreateRangesCollection()] |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [\' Add different ranges to the Range collection.]                                                                                       |
|                                                                                                                                                                                            |
| [rangesOne.Add(sheet.Range([\"D2:D3\"]));]                                                                                      |
|                                                                                                                                                                                            |
| [rangesOne.Add(sheet.Range([\"D10:D11\"]));]                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

