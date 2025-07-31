---
title: howtosuspendcalculationswhileaseriesofvaluesareupdated1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosuspendcalculationswhileaseriesofvaluesareupdated1.md
created_at: 2025-07-03
---








  









### How To Suspend Calculations While a Series Of Values Are Updated? {#how-to-suspend-calculations-while-a-series-of-values-are-updated style="tab-stops: 0pt"}

 

You can use the property CalcEngine.CalculatingSuspended to control the calculations that will be performed as values change in your ICalcData object.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [// Creates some data object that implements ICalcData.]                                                                                                   |
|                                                                                                                                                                                                              |
| [this][.data = [new] [ArrayCalcData](a);]                                     |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [// Creates a CalcEngine object using this ICalcData object.]                                                                                              |
|                                                                                                                                                                                                              |
| [CalcEngine][ engine = [new] [CalcEngine]([this].data);] |
|                                                                                                                                                                                                              |
| [//\...]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [// Turn off calculations.]                                                                                                                                |
|                                                                                                                                                                                                              |
| [engine.CalculatingSuspended = [true];]                                                                                                             |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [// Makes multiple updates to this.data somehow\...]                                                                                                       |
|                                                                                                                                                                                                              |
| [// Turn on calculations.]                                                                                                                                 |
|                                                                                                                                                                                                              |
| [ engine.CalculatingSuspended = [false];]                                                                                                           |
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
| [Dim][ engine ][As New ][CalcEngine(][Me][.data)] |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\'\...]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Turn off calculations.]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                            |
| [engine.CalculatingSuspended = ][True]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Makes multiple updates to this.data somehow\...]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Turn on calculations.]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                            |
| [engine.CalculatingSuspended = ][False]                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p229} 

[]{#related-topics}

