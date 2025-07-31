---
title: bindingbetweenstaterangeandstateindicator3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\bindingbetweenstaterangeandstateindicator3.md
created_at: 2025-07-03
---






#### Binding between State Range and State Indicator {#binding-between-state-range-and-state-indicator style="tab-stops: 0pt"}

[] 

Essential Gauge WPF now provides support to bind between the State Range and State Indicator. This can be achieved by setting the **BindIndicator** property of the Linear Gauge to true. Default value of this property is set to false.

[] 

This feature is useful while working with multiple ranges. For example, while analyzing the performance of a gauge, set the range for each rating and enable the BindIndicator property. Once this is done, you can see the change in the indicator color depending upon the performance.

[] 

The **IndicatorColor** property is used to specify the color of the active indicator.

[] 


{border="0"}Note: Orange gradient is the default color of the active indicator.


[] 

The following code example illustrates this feature.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][my][:][LinearScale.Ranges][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    ][\<][my][:][LinearRange][ BorderWidth][=\"0.5\"][ EndValue][=\"100\"][ EndWidth][=\"10\"][ BindIndicator][=\"True\"][ IndicatorColor][=\"Red\"][ RangePosition][=\"Inside\"][          StartValue][=\"65\"][ StartWidth][=\"2\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][my][:][LinearScale.Ranges][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                 |
|                                                                                                                                                                                     |
| [LinearRange][ range = [new] [LinearRange]();] |
|                                                                                                                                                                                     |
| [range.BindIndicator = [true];]                                                                                            |
|                                                                                                                                                                                     |
| [range.StartValue = 70;]                                                                                                                        |
|                                                                                                                                                                                     |
| [range.EndValue = 100;]                                                                                                                         |
|                                                                                                                                                                                     |
| [range.IndicatorColor = [new] [SolidColorBrush]([Colors].Blue);]           |
|                                                                                                                                                                                     |
| [linearGauge1.Scales\[0\].Ranges.Add(range);]                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In the following screen shot, the pointer value lies outside the range value (70-100) and hence the Indicator is inactive (OFF state).

[] 

{border="0"}

[] 

Figure 65: Inactive Indicator (BindIndicator property set to True)

[] 

In the following screen shot, the pointer value lies inside the range value (70-100) and hence the Indicator is active (ON state).

[] 

{border="0"}

**[]** 

Figure 66: Active Indicator (BindIndicator property set to True)

 

[]{#related-topics}

