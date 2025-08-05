---
title: keyperformanceindicatorkpielement.md
original_path: WinForms_Docs/99_Uncategorized/keyperformanceindicatorkpielement.md
created_at: 2025-08-05
---








  









### Key Performance Indicator (KPI) Element {#key-performance-indicator-kpi-element style="tab-stops: 0pt"}

Key Performance Indicator(KPI) is a collection of calculations that are associated with a measure group in a cube that are used to evaluate business success. Typically, these calculations are a combination of Multidimensional Expressions (MDX) or calculated members. The KPIs also have an additional metadata that provides information about how client applications should display the results of the KPI\'s calculations.

The different types of KPI Indicators are:

[·      ]KPI Goal

[·      ]KPI Status

[·      ]KPI Trend

[·      ]KPI Value

We can create a KPI element by specifying its name and giving details of the indicator that are included in the element.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]               ]**                                                                                                                          |
|                                                                                                                                                                                          |
| [KpiElements][ kpiElement = [new] [KpiElements]();] |
|                                                                                                                                                                                          |
| [// Specifying the KPI Element name and configuring its Indicators]                                                                    |
|                                                                                                                                                                                          |
| [kpiElement.Elements.Add([new] [KpiElement] { Name = [\"Internet Revenue\"],  ] |
|                                                                                                                                                                                          |
| [ShowKPIGoal = [true], ShowKPIStatus = [true], ShowKPIValue = [true], ]               |
|                                                                                                                                                                                          |
| [ShowKPITrend = [true] });][]                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| [Dim][ kpiElement [As] KpiElements = [New] KpiElements()]                     |
|                                                                                                                                                                                                              |
| [\' Specifying the KPI Element name and configuring its Indicators][]                                                  |
|                                                                                                                                                                                                              |
| [kpiElement.Elements.Add([New] KpiElement [With] {.Name =  ]                                                                   |
|                                                                                                                                                                                                              |
| [\"Internet Revenue\"][, .ShowKPIGoal = [True], .ShowKPIStatus = [True], ] |
|                                                                                                                                                                                                              |
| [ .ShowKPIValue = [True], .ShowKPITrend = [True]})]                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

