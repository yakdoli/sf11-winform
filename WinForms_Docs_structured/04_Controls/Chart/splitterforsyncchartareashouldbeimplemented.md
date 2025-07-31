---
title: splitterforsyncchartareashouldbeimplemented.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\splitterforsyncchartareashouldbeimplemented.md
created_at: 2025-07-03
---






##### Splitter for SyncChartArea should be implemented {#splitter-for-syncchartarea-should-be-implemented style="tab-stops: 0pt"}

Essential Chart WPF is now enhanced with **Splitter for** **SyncChartArea**. This is useful to differentiate the implementation of more than one Chart Area.

 

Property Details

The following table contains the property details.

[] 

Table 11: Property Table


  -------------------- --------------------------------------- --------------------- -------------------------------------
  Name of Property     Description                             Type of Property      Value It Accepts
  SplitterVisibility   Sets the visibility for the splitter.   Dependency Property   Enum of the type SplitterVisibility
  SplitterWidth        Sets the width for the Splitter.        Dependency Property   Double
  SplitterStroke       Sets the stroke for the splitter.       Dependency Property   Brush
  SplitterColor        Sets the color for the splitter.        Dependency Property   Brush
  -------------------- --------------------------------------- --------------------- -------------------------------------


[] 

**[]** 

Adding Splitter for SyncChartArea

Add Splitter for SyncChartArea, by using the following code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\] ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][sfChart][:][SyncChartAreas][ Name][=\"syncChart\"][ SplitterVisiblity][=\"ShowAlways\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [SplitterStroke][=\"Red\"][ SplitterColor][=\"Blue\"][ [ SplitterWidth][=\"2\"][ ][/\>]]                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                           |
|                                                                                                                                                             |
| **[]**                                                                                                                  |
|                                                                                                                                                             |
| [this][.SyncChart.SplitterVisibility = SplitterVisibility.ShowAlways;] |
|                                                                                                                                                             |
| [            [this].SyncChart.SplitterStroke = [Brushes].Red;]             |
|                                                                                                                                                             |
| [            [this].SyncChart.SplitterColor = [Brushes].Blue;]             |
|                                                                                                                                                             |
| [            [this].SyncChart.SplitterWidth = 2;]                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p44} 

 

[]{#related-topics}

