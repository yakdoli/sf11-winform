---
title: howtoprovideinputdataofdatetimetype1.md
original_path: WinForms_Docs/03_Data_Binding/howtoprovideinputdataofdatetimetype1.md
created_at: 2025-08-05
---








  









## How to provide input data of DateTime type {#how-to-provide-input-data-of-datetime-type style="tab-stops: 0pt"}

 

The Start Date and Time can be expressed using an instance of the **DateTime** class. If you want to add days, the **AddDays()** method can be used along with that instance. **AddHours()** and **AddMinutes()** can be used for adding any number of hours and minutes.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [DateTime][ start = [new] [DateTime](2006, 11, 1);] |
|                                                                                                                                                                                          |
| [ChartSeries][ series = [this].chartControl1.Model.NewSeries("");]          |
|                                                                                                                                                                                          |
| [series.Points.Add(start.AddDays(7), 363);]                                                                                                          |
|                                                                                                                                                                                          |
| [series.Points.Add(start.AddDays(14), 417);]                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [Dim][ start [As] DateTime = [New] DateTime(2006, 11, 1)] |
|                                                                                                                                                                                          |
| [ChartSeries series = [Me].chartControl1.Model.NewSeries([""])]                                         |
|                                                                                                                                                                                          |
| [series.Points.Add(start.AddDays(7), 363)]                                                                                                           |
|                                                                                                                                                                                          |
| [series.Points.Add(start.AddDays(14), 417)]                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p291} 

[]{#related-topics}

