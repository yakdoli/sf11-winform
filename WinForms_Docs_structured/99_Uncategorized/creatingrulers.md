---
title: creatingrulers.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingrulers.md
created_at: 2025-07-03
---








  









### Creating Rulers {#creating-rulers style="tab-stops: 0pt"}

[] 

Rulers display the coordinates of elements on the diagram page. At any point, the ruler value always indicates the exact coordinates of the page and its elements. By default, labels of the major lines in rulers will represent the pixel values using a label.

 

 

The Horizontal and Vertical ruler can be initialized for DiagramView in two ways namely:

[] 

[·      ]Through XAML

[·      ]Through Code Behind

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][DiagramView][ [IsPageEditable][=\"True\"] [Bounds][=\"0,0,12,12\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Name][=\"diagramView\"\>]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][DiagramView.HorizontalRuler][\>]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    [\<][syncfusion][:][HorizontalRuler] [Name][=\"horizontalRuler\"] [Background][=\"#FFC6C6C6\"] [LabelFontColor][=\"Green\"/\>]]                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][DiagramView.HorizontalRuler][\>]                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][DiagramView.VerticalRuler][\>]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    [\<][syncfusion][:][VerticalRuler] [Name][=\"verticalRuler\"] [Background][=\"#FFC6C6C6\"] [LabelFontColor][=\"Green\"/\>]]                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][DiagramView.VerticalRuler][ [\>]]                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][DiagramView][\>]                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [DiagramView][ diagramView = [new] [DiagramView]();]         |
|                                                                                                                                                                                                   |
| [(diagramView.HorizontalRuler [as] [HorizontalRuler]).LabelFontColor = [Brushes].Green;] |
|                                                                                                                                                                                                   |
| [(diagramView.VerticalRuler [as] [VerticalRuler]).LabelFontColor = [Brushes].Green;]     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [Dim][ diagramView [As] [New] [DiagramView]()]           |
|                                                                                                                                                                                                                 |
| [TryCast][(diagramView.HorizontalRuler, HorizontalRuler).LabelFontColor = Brushes.Green]                                   |
|                                                                                                                                                                                                                 |
| [TryCast][(diagramView.VerticalRuler, VerticalRuler).LabelFontColor = Brushes.Green][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

{border="0"}

Figure 105: Rulers**[]**

**[]** 

Several customizable options have been provided for the horizontal and vertical rulers. These are common for both the rulers.\
\

Properties

[] 

  Property              Description                                  Type of the property   Value it accepts   Any other dependencies/ sub properties associated
  --------------------- -------------------------------------------- ---------------------- ------------------ ---------------------------------------------------
  Background            Get or sets the ruler\'s background color.   Dependency property    Brush              No
  MarkerBrush           Gets or sets the MarkerBrush.                Dependency property    Brush              No
  LabelFontColor        Gets or sets the LabelFontColor.             Dependency property    Brush              No
  MinorLinesStroke      Gets or sets the MinorLinesStroke.           Dependency property    Brush              No
  MajorLinesStroke      Gets or sets the MajorLinesStroke.           Dependency property    Brush              No
  MajorLinesThickness   Gets or sets the MajorLinesThickness.        Dependency property    Double             No
  MinorLinesThickness   Gets or sets the MinorLinesThickness.        Dependency property    Double             No
  MarkerThickness       Gets or sets the MarkerThickness.            Dependency property    Double             No

[] 

[] 

[] 

{border="0"}

Figure 106: Ruler Terminology**[]**

[[[]]]{.underline} 

[[[]]]{.underline} 

The following code shows how the properties that can be set.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:][DiagramView][ [IsPageEditable][=\"True\"] [Bounds][=\"0,0,12,12\"] [Name][=\"diagramView\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:][DiagramView.HorizontalRuler][\>]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [\<][syncfusion][:][HorizontalRuler] [Name][=\"horizontalRuler\"] [Background][=\"#FFC6C6C6\"] [LabelFontColor][=\"Green\"/\>]]                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][syncfusion][:][DiagramView.HorizontalRuler][\>]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:][DiagramView.VerticalRuler][\>]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [\<][syncfusion][:][VerticalRuler] [Name][=\"verticalRuler\"] [Background][=\"#FFC6C6C6\"] [LabelFontColor][=\"Green\"/\>]]                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][syncfusion][:][DiagramView.VerticalRuler][ [\>]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][syncfusion][:][DiagramView][\>]                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [DiagramView][ diagramView = [new] [DiagramView]();]         |
|                                                                                                                                                                                                   |
| [(diagramView.HorizontalRuler [as] [HorizontalRuler]).LabelFontColor = [Brushes].Green;] |
|                                                                                                                                                                                                   |
| [(diagramView.VerticalRuler [as] [VerticalRuler]).LabelFontColor = [Brushes].Green;]     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [Dim][ diagramView [As] [New] [DiagramView]()]           |
|                                                                                                                                                                                                                 |
| [TryCast][(diagramView.HorizontalRuler, HorizontalRuler).LabelFontColor = Brushes.Green]                                   |
|                                                                                                                                                                                                                 |
| [TryCast][(diagramView.VerticalRuler, VerticalRuler).LabelFontColor = Brushes.Green][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 107: Custom Ruler[]{#p76}

[]{#related-topics}

