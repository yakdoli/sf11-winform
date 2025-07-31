---
title: howtoforcecalculationstobeprocessedaftertheyhavebeensuspended1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoforcecalculationstobeprocessedaftertheyhavebeensuspended1.md
created_at: 2025-07-03
---








  









### How To Force Calculations To Be Processed After They Have Been Suspended? {#how-to-force-calculations-to-be-processed-after-they-have-been-suspended style="tab-stops: 0pt"}

 

The following code illustrates how to force calculations to be processed after Engine.CalculatingSuspended has been flipped back to true.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [// Creates some data object that implements ICalcData.]                                                                                                   |
|                                                                                                                                                                                                              |
| [this][.data = [new] [ArrayCalcData](a);]                                     |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [// Creates a CalcEngine object using this ICalcData object.]                                                                                              |
|                                                                                                                                                                                                              |
| [CalcEngine][ engine = [new] [CalcEngine]([this].data);] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [//Turn off calculations.]                                                                                                                                 |
|                                                                                                                                                                                                              |
| [engine.CalculatingSuspended = [true];      ]                                                                                                       |
|                                                                                                                                                                                                              |
| [      ]                                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [// Makes multiple updates to this.data.]                                                                                                                  |
|                                                                                                                                                                                                              |
| [// Turn on calculations.]                                                                                                                                 |
|                                                                                                                                                                                                              |
| [engine.CalculatingSuspended = [false];]                                                                                                            |
|                                                                                                                                                                                                              |
| [           ]                                                                                                                                                            |
|                                                                                                                                                                                                              |
| [// Calls RecalculateRange so any formulas in the data can be computed.][            ]                                 |
|                                                                                                                                                                                                              |
| [engine.RecalculateRange([RangeInfo].Cells(1, 1, nRows + 1, nCols + 1), data);            ]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Creates some data object that implements ICalcData.]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.data = ][New][ ArrayCalcData(a)]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Creates a CalcEngine object using this ICalcData object.]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ engine ][As New][ CalcEngine(][Me][.data)] |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\'\...]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Turn off calculations.]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                            |
| [engine.CalculatingSuspended = ][True]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Makes multiple updates to this.data.]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Turn on calculations.]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                            |
| [engine.CalculatingSuspended = ][False]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Calls RecalculateRange so any formulas in the data can be computed.]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| [engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), Data)]                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p227} 

[]{#related-topics}

