---
title: howtoconvertoffsetvaluesintotextrangeintheeditcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoconvertoffsetvaluesintotextrangeintheeditcontrol.md
created_at: 2025-07-03
---








  









## How To Convert Offset Values Into Text Range In the Edit Control {#how-to-convert-offset-values-into-text-range-in-the-edit-control style="tab-stops: 0pt"}

[] 

This section explains how to get the associated CoordinatePoint values from text offset values. This can be done as follows.

[] 

You have to convert offset values into VirtualPoints, and then VirtualPoints to ParsePoints before converting them to CoordinatePoints.

[] 

The following code snippet illustrates this:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [// Starting offset converted to virtual point.]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| [Point][ startVirtualPoint = [this].editControl1.ConvertOffsetToVirtualPosition(startOffsetValue);]                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [// Ending offset converted to virtual point.]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [Point][ endVirtualPoint = [this].editControl1.ConvertOffsetToVirtualPosition(endOffsetValue);]                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [// Converting the VirtualPoints to ParsePoints.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [ParsePoint startParsePoint = [new] ParsePoint(startVirtualPoint.Y, startVirtualPoint.X, 0);]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [ParsePoint endParsePoint = [new] ParsePoint(endVirtualPoint.Y, endVirtualPoint.X, 0);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [// Creating the associated CoordinatePoints that indicate the text range. ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [CoordinatePoint startCoordinatePoint = [new] CoordinatePoint([this].editControl1.Parser [as] ILexemParser, startParsePoint, startVirtualPoint.Y, startVirtualPoint.X, [true]);] |
|                                                                                                                                                                                                                                                                                                          |
| [CoordinatePoint endCoordinatePoint = [new] CoordinatePoint([this].editControl1.Parser [as] ILexemParser, endParsePoint, endVirtualPoint.Y, endVirtualPoint.X, [true]);]         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Starting offset converted to virtual point. ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ startVirtualPoint [As] Point = [Me].EditControl1.ConvertOffsetToVirtualPosition(startOffsetValue)]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Ending offset converted to virtual point. ]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ endVirtualPoint [As] Point = [Me].EditControl1.ConvertOffsetToVirtualPosition(endOffsetValue)]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Converting the VirtualPoints to ParsePoints. ]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ startParsePoint [As] [New] ParsePoint(startVirtualPoint.Y, startVirtualPoint.X, 0)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ endParsePoint [As] [New] ParsePoint(endVirtualPoint.Y, endVirtualPoint.X, 0)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Creating the associated CoordinatePoints that indicate the text range. ]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ startCoordinatePoint [As] [New] CoordinatePoint([TryCast]([Me].editControl1.Parser, ILexemParser), startParsePoint, startVirtualPoint.Y, startVirtualPoint.X, [True])] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ endCoordinatePoint [As] [New] CoordinatePoint([TryCast]([Me].editControl1.Parser, ILexemParser), endParsePoint, endVirtualPoint.Y, endVirtualPoint.X, [True])]         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p186} 

[]{#related-topics}

