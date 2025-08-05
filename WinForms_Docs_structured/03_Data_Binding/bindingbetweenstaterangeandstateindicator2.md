---
title: bindingbetweenstaterangeandstateindicator2.md
original_path: WinForms_Docs/03_Data_Binding/bindingbetweenstaterangeandstateindicator2.md
created_at: 2025-08-05
---






#### Binding between State Range and State Indicator {#binding-between-state-range-and-state-indicator style="tab-stops: 0pt"}

[] 

Essential Gauge WPF now provides support to bind between the State Range and State Indicator. This can be achieved by setting the **BindIndicator** property of the Circular Gauge to *true*. Default value of this property is set to *false*.

[] 

This feature is useful while working with multiple ranges. For example, while analyzing the performance of a gauge, set the range for each rating and enable the BindIndicator property. Once this is done, you can see the change in the indicator color depending upon the performance.

[] 

The **IndicatorColor** property is used to specify the color of the active indicator.

[] 


{border="0"}Note: Orange gradient is the default color of the active indicator.

 


The following code example illustrates this feature.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][my][:][CircularScale.Ranges][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\<][my][:][CircularRange][ BorderWidth][=\"1\"][ DistanceFromScale][=\"23\"][ BindIndicator][=\"True\"][ EndValue][=\"100\"][ EndWidth][=\"20\"][ IndicatorColor][=\"Red\"][ RangePosition][=\"Inside\"][ StartValue][=\"70\"][ StartWidth][=\"2\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\</][my][:][CircularRange][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][my][:][CircularScale.Ranges][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                     |
|                                                                                                                                                                                         |
| [CircularRange][ range = [new] [CircularRange]();] |
|                                                                                                                                                                                         |
| [range.BindIndicator = [true];]                                                                                                |
|                                                                                                                                                                                         |
| [range.StartValue = 70;]                                                                                                                            |
|                                                                                                                                                                                         |
| [range.EndValue = 100;]                                                                                                                             |
|                                                                                                                                                                                         |
| [range.IndicatorColor = [new] [SolidColorBrush]([Colors].Blue);]               |
|                                                                                                                                                                                         |
| [circularGauge1.Scales\[0\].Ranges.Add(range);]                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In the following screen shot, the pointer value lies outside the range value (70-100) and hence the Indicator is inactive (OFF state).

[] 

{border="0"}

Figure 44: Inactive Indicator (BindIndicator property set to True)

[] 

[] 

In the following screen shot, the pointer value lies inside the range value (70-100) and hence the Indicator is active (ON state).

[] 

{border="0"}

[] 

Figure 45: Active Indicator (BindIndicator property set to True)

[] 

Events

[] 

The following table lists the events associated with this feature.

[] 

[] 


  ----------------------- -------------------------------- ------------------------ ------------------------------------ ------------------------------------------------------------------------------
  Event                   Event Trigger                    Method Handling Event    Event Argument                       Purpose
  BindIndicatorChanged    BindIndicatorChanged             OnBindIndicatorChanged   DependencyPropertyChangedEventArgs   To set the binding between the two indicators.
  IndicatorColorChanged   ValueChanged for the Indicator   OnValueChanged           KeyEventArgs                         Indicator color changes, if the pointer value falls between the range value.
  ----------------------- -------------------------------- ------------------------ ------------------------------------ ------------------------------------------------------------------------------


Table 7: Events for Binding between State Range and State Indicator

 

[]{#related-topics}

