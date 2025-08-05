---
title: borderandmargins1.md
original_path: WinForms_Docs/99_Uncategorized/borderandmargins1.md
created_at: 2025-08-05
---








  









### Border and Margins {#border-and-margins style="tab-stops: 0pt"}

 

**Chart Area Border**

 

Borders of the chart area can be customized using the below border properties.

 


+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                          |
|                                     |                                                                                                                                          |
| **ChartArea Property**              | **Description**                                                                                                                          |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| BorderColor                         | Indicates the border color of the chart area.                                                                                            |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| BorderStyle                         | Indicates the border style.                                                                                                              |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| BorderWidth                         | Specifies the width of the border.                                                                                                       |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                |
|                                                                                                                                                                                |
| BorderAppearance                                                                                                                                                               |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| BaseColor                           | Gets or sets the color of the base.                                                                                                      |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| FrameThickness                      | Gets or sets the frame thickness. This property setting will be effective, when SkinStyle is **Frame**.                                  |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Interior                            | Sets the interior color of the border. This property settings will be effective when SkinStyle is **Sunken**, **Etched** and **Raised**. |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| SkinStyle                           | Specifies the border skin style.                                                                                                         |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+


 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.ChartArea.BorderColor = System.Drawing.[Color].Goldenrod;]                                                                         |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.ChartArea.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]                                                          |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.ChartArea.BorderWidth = 1;]                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.BorderAppearance.BaseColor = System.Drawing.[Color].DarkGray;]                                                                     |
|                                                                                                                                                                                                                                                                    |
| [//This property setting will be effective, when SkinStyle is \'Frame\'.]                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.BorderAppearance.FrameThickness = [new] Syncfusion.Windows.Forms.Chart.[ChartThickness](15F, 30F, 15F, 18F);] |
|                                                                                                                                                                                                                                                                    |
| [//This interior property settings will be effective when SkinStyle is Sunken, Etched and Raised.]                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.BorderAppearance.Interior.ForeColor = System.Drawing.[Color].Maroon;]                                                              |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.BorderAppearance.SkinStyle = Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Raised;]                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [Me][.ChartControl1.ChartArea.BorderColor = System.Drawing.[Color].Goldenrod]                                                   |
|                                                                                                                                                                                                                                           |
| [Me][.ChartControl1.ChartArea.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle]                                                            |
|                                                                                                                                                                                                                                           |
| [Me][.ChartControl1.ChartArea.BorderWidth = 1]                                                                                                       |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [Me][.chartControl1.BorderAppearance.BaseColor = System.Drawing.Color.DarkGray ]                                                                     |
|                                                                                                                                                                                                                                           |
| [\'This property setting will be effective, when SkinStyle is \'Frame\'. ]                                                                                                              |
|                                                                                                                                                                                                                                           |
| [Me][.chartControl1.BorderAppearance.FrameThickness = [New] Syncfusion.Windows.Forms.Chart.ChartThickness(15F, 30F, 15F, 18F) ] |
|                                                                                                                                                                                                                                           |
| [\'This interior property settings will be effective when SkinStyle is Sunken, Etched and Raised. ]                                                                                     |
|                                                                                                                                                                                                                                           |
| [Me][.chartControl1.BorderAppearance.Interior.ForeColor = System.Drawing.Color.Maroon ]                                                              |
|                                                                                                                                                                                                                                           |
| [Me][.chartControl1.BorderAppearance.SkinStyle = Syncfusion.Windows.Forms.Chart.ChartBorderSkinStyle.Raised ]                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Chart Area Shadow

 

The chart area can also be rendered with a shadow. Turn this feature on, by enabling the **ChartAreaShadow** property.

 


+-----------------------------------+--------------------------------------------+
|                                   |                                            |
|                                   |                                            |
| Chart control Property            | Description                                |
+-----------------------------------+--------------------------------------------+
| ChartAreaShadow                   | Indicates whether chart area has a shadow. |
+-----------------------------------+--------------------------------------------+
| ShadowColor                       | Specifies the color of the shadow.         |
+-----------------------------------+--------------------------------------------+
| ShadowWidth                       | Specifies the width of the shadow.         |
+-----------------------------------+--------------------------------------------+


**\
\**

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.chartControl1.ChartAreaShadow = [true];]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.chartControl1.ShadowColor = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].ForwardDiagonal, System.Drawing.[Color].AntiqueWhite, System.Drawing.[Color].Goldenrod);] |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.chartControl1.ShadowWidth = 7;]                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.ChartControl1.ChartAreaShadow = [True]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.ChartControl1.ShadowColor = [New] Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.[GradientStyle].ForwardDiagonal, System.Drawing.[Color].AntiqueWhite, System.Drawing.[Color].Goldenrod)] |
|                                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.chartControl1.ShadowWidth = 7]                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 319: ChartAreaShadow = \"True\"

 

Chart Area Margins

 

Margin for the chart area can be controlled using ChartAreaMargins property. It indicates the margin that will be deduced from Chart Area\'s representation rectangle.

 


+-----------------------------------+---------------------------------------------------------------------------------------+
| Chart control Property            | Description                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------+
| ChartAreaMargins                  | Specifies the amount of pixels between the chart area border and the chart plot area. |
|                                   |                                                                                       |
|                                   |                                                                                       |
|                                   |                                                                                       |
|                                   | Default is **{10, 10, 10, 10}**.                                                      |
+-----------------------------------+---------------------------------------------------------------------------------------+


 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                               |
| [this][.chartControl1.ChartAreaMargins = [new] Syncfusion.Windows.Forms.Chart.[ChartMargins](10, 10, 10, 20);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                            |
|                                                                                                                                                                                                                     |
| [Me][.ChartControl1.ChartAreaMargins = [New] Syncfusion.Windows.Forms.Chart.ChartMargins(10, 10, 10, 20)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

ChartPlot Area Margins

 

The margins for ChartPlotArea is specified in **ChartPlotAreaMargins** property.

 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **ChartControl Property**         | **Description**                                                                                                                                                                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ChartPlotAreaMargins              | Indicates the margin of the axis labels. This  margin is supported for left, Top, Right and Bottom side of the chart. This property works only if **EdgeLabelsDrawingMode** property is set to **Shift**. |
|                                   |                                                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                           |
|                                   | Default is **{10, 10, 10, 10}**.                                                                                                                                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AdjustPlotAreaMargins             | Gets / sets the mode of drawing the edge labels. Default is **AutoSet**.                                                                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EdgeLabelsDrawingMode             | Gets or sets the edge labels drawing mode.                                                                                                                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                              |
| [this][.chartControl1.PrimaryYAxis.EdgeLabelsDrawingMode = Syncfusion.Windows.Forms.Chart.[ChartAxisEdgeLabelsDrawingMode].Shift;] |
|                                                                                                                                                                                                                                              |
| [this][.chartControl1.ChartArea.AdjustPlotAreaMargins = Syncfusion.Windows.Forms.Chart.[ChartSetMode].UserSet;]                    |
|                                                                                                                                                                                                                                              |
| [this][.chartControl1.ChartArea.ChartPlotAreaMargins.Left = 200;]                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [Me][.chartControl1.PrimaryYAxis.EdgeLabelsDrawingMode = Syncfusion.Windows.Forms.Chart.[ChartAxisEdgeLabelsDrawingMode].Shift] |
|                                                                                                                                                                                                                                            |
| [Me][.chartControl1.ChartArea.AdjustPlotAreaMargins = Syncfusion.Windows.Forms.Chart.[ChartSetMode].UserSet]                    |
|                                                                                                                                                                                                                                            |
| [Me][.chartControl1.ChartArea.ChartPlotAreaMargins.Left = 200]                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Spacing between elements**

 

The spacing between elements in the chart is specified using the **ElementsSpacing** property. For example, the space between the chart right border and legend right border if **LegendPosition** is set to **Right**.

 


  ------------------------ -----------------------------------------------------------------------------
  Chart control Property   Description
  ElementsSpacing          Specifies the spacing between the elements in the chart. Default is **20**.
  ------------------------ -----------------------------------------------------------------------------


 

[]{#p208} 

 

[]{#related-topics}

