---
title: howtoprovideinputdataofdatetimetype.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\howtoprovideinputdataofdatetimetype.md
created_at: 2025-07-03
---








  









## How to provide input data of DateTime type? {#how-to-provide-input-data-of-datetime-type style="tab-stops: 0pt"}

[] 

The Start Date and Time can be expressed using an instance of the **DateTime** class. If you want to add days, the **AddDays()** method can be used along with that instance. **AddHours()** and **AddMinutes()** can be used for adding any number of hours and minutes.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [DateTime][ start = [new] [DateTime](2006, 11, 1);] |
|                                                                                                                                                                                          |
| [ChartSeries][ series = [this].ChartWebControl1.Model.NewSeries("");]       |
|                                                                                                                                                                                          |
| [series.Points.Add(start.AddDays(7), 363);]                                                                                                          |
|                                                                                                                                                                                          |
| [series.Points.Add(start.AddDays(14), 417);]                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [Dim][ start [As] DateTime = [New] DateTime(2006, 11, 1)] |
|                                                                                                                                                                                          |
| [ChartSeries series = [Me].ChartWebControl1.Model.NewSeries([""])]                                      |
|                                                                                                                                                                                          |
| [series.Points.Add(start.AddDays(7), 363)]                                                                                                           |
|                                                                                                                                                                                          |
| [series.Points.Add(start.AddDays(14), 417)]                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p283} 

[]{#related-topics}

