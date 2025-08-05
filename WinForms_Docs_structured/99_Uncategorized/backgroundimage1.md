---
title: backgroundimage1.md
original_path: WinForms_Docs/99_Uncategorized/backgroundimage1.md
created_at: 2025-08-05
---








  









### Background Image {#background-image style="tab-stops: 0pt"}

 

Chart Settings

 

In Windows Forms, use the **BackgroundImage** property to specify a custom image as the background of the chart. The image layout can also be specified using the property below.

 


+-----------------------------------+------------------------------------------------------------------------------------+
| Chart control Property            | Description                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------+
| BackgroundImage                   | Indicates the background image used for the control.                               |
+-----------------------------------+------------------------------------------------------------------------------------+
| BackgroundImageLayout             | Indicates the background image layout used for the component. Possible values are: |
|                                   |                                                                                    |
|                                   | Tile **(default setting)**                                                         |
|                                   |                                                                                    |
|                                   | Center                                                                             |
|                                   |                                                                                    |
|                                   | Stretch                                                                            |
|                                   |                                                                                    |
|                                   | Zoom                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------+


 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| [this][.chartControl1.BackgroundImage = ((System.Drawing.[Image])(resources.GetObject([\"chartControl1.BackgroundImage\"])));] |
|                                                                                                                                                                                                                                                                 |
| [this][.chartControl1.BackgroundImageLayout = System.Windows.Forms.[ImageLayout].Stretch;]                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [Me][.ChartControl1.BackgroundImage = [CType]((Resources.GetObject([\"chartControl1.BackgroundImage\"])), System.Drawing.Image)] |
|                                                                                                                                                                                                                                                                   |
| [Me][.ChartControl1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch]                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 316: Background Image set for the Chart

 

ChartArea Background Image

 

The chart area can also be rendered with a custom background image and this can be set using the **ChartAreaBackImage** property.

 


  ------------------------ ---------------------------------------------------------------------
  Chart control Property   Description
  ChartAreaBackImage       Specifies the image to be used as the background in the chart area.
  ------------------------ ---------------------------------------------------------------------


 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                  |
|                                                                                                                                                 |
| **[]**                                                                                        |
|                                                                                                                                                 |
| [this][.chartControl1.ChartAreaBackImage = myCustomImage;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                           |
|                                                                                                                                              |
| **[]**                                                                                     |
|                                                                                                                                              |
| [Me][.ChartControl1.ChartAreaBackImage = myCustomImage] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 317: Background Image set for the Chart Area

 

Chart Interior Background Image

 

Chart Interior can be rendered with a custom background image using the **ChartInteriorBackImage** property.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                                     |
| **[]**                                                                                            |
|                                                                                                                                                     |
| [this][.chartControl1.ChartInteriorBackImage = myCustomImage;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                               |
|                                                                                                                                                  |
| **[]**                                                                                         |
|                                                                                                                                                  |
| [Me][.ChartControl1.ChartInteriorBackImage = myCustomImage] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**** 

Figure 318: Background Image set for the Chart Interior

 

[]{#p207} 

 

[]{#related-topics}

