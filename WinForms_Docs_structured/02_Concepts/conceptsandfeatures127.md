---
title: conceptsandfeatures127.md
original_path: WinForms_Docs/02_Concepts/conceptsandfeatures127.md
created_at: 2025-08-05
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

[] 

This section will take you in detail about the concepts and features available for the gradient panel and guides you to customize the control using the features available.

[] 

###### []{#p458}[]{#_GradientPanel_Appearance}3.3.6.2.4.1 GradientPanel Appearance {#gradientpanel-appearance style="tab-stops: 0pt"}

[] 

The background of the GradientPanel can be customized using the below properties.

[] 


  -------------------------- ------------------------------------------------------------------------
  GradientPanel Properties   Description
  BackColor                  Background color used to display the text and graphics in the control.
  BackgroundColor            Sets a gradient style background for the control.
  -------------------------- ------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.gradientPanel1.BackColor = System.Drawing.Color.LightCoral;]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.gradientPanel1.BackgroundColor = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].PathRectangle, System.Drawing.[Color].AliceBlue, System.Drawing.[Color].SteelBlue);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                       |
| [Me][.gradientPanel1.BackColor = System.Drawing.Color.LightCoral]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [Me][.gradientPanel1.BackgroundColor = [New] Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathRectangle, System.Drawing.Color.AliceBlue, System.Drawing.Color.SteelBlue) ] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 392: Gradient Panel with Gradient Background

**[]** 

Foreground Settings

[] 

The foreground text in the control can be customized using the below properties.

[] 


  -------------------------- --------------------------------------------------------------
  GradientPanel Properties   Description
  Font                       Indicates the Font style of the text in the control.
  ForeColor                  Indicates the color of the text and graphics in the control.
  -------------------------- --------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                               |
| [this][.gradientPanel1.Font = [new] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Bold);] |
|                                                                                                                                                                                                                                                                                               |
| [this][.gradientPanel1.ForeColor = System.Drawing.[Color].Blue;]                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                            |
| [Me][.GradientPanel1.Font = [New] System.Drawing.Font(\"Comic Sans MS\", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, [CType](0, [Byte]))] |
|                                                                                                                                                                                                                                                                                                                            |
| [this][.gradientPanel1.ForeColor = System.Drawing.Color.Blue;]                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 393: Gradient Panel with FontStyle

**[]** 

Image Settings

[] 

Background image for the GradientPanel control is set using below properties.

[] 


  -------------------------- --------------------------------------------
  GradientPanel Properties   Description
  BackgroundImage            Sets the background image for the control.
  BackgroundImageLayout      Specifies the layout of the image.
  -------------------------- --------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [this][.gradientPanel1.BackgroundImage = ((System.Drawing.[Image])(resources.GetObject([\"gradientPanel1.BackgroundImage\"])));] |
|                                                                                                                                                                                                                                                                   |
| [this][.gradientPanel1.BackgroundImageLayout = System.Windows.Forms.[ImageLayout].Stretch;     ][      ]            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [Me][.gradientPanel1.BackgroundImage = [CType]((resources.GetObject([\"gradientPanel1.BackgroundImage\"])),System.Drawing.Image) ] |
|                                                                                                                                                                                                                                                                     |
| [Me][.gradientPanel1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch]                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 394: Background Image for GradientPanel

**[]** 

See Also

**[]** 

[Border Settings]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p459}[]{#_Border_Settings}3.3.6.2.4.2 Border Settings {#border-settings style="tab-stops: 0pt"}

[] 

GradientPanel can have 2D and 3D borders. The properties which sets the border style are as follows.

**[]** 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| GradientPanel Property            | Description                                                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| BorderStyle                       | Sets the 2D or 3D border for the GradientPanel. The options are,                                                              |
|                                   |                                                                                                                               |
|                                   |                                                                                                                               |
|                                   |                                                                                                                               |
|                                   | FixedSingle and                                                                                                               |
|                                   |                                                                                                                               |
|                                   | Fixed3D.                                                                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Border3DStyle                     | Sets the style of the 3D border. The options are,                                                                             |
|                                   |                                                                                                                               |
|                                   |                                                                                                                               |
|                                   |                                                                                                                               |
|                                   | RaisedOuter,                                                                                                                  |
|                                   |                                                                                                                               |
|                                   | RaisedInner,                                                                                                                  |
|                                   |                                                                                                                               |
|                                   | SunkenOuter,                                                                                                                  |
|                                   |                                                                                                                               |
|                                   | SunkenInner,                                                                                                                  |
|                                   |                                                                                                                               |
|                                   | Raised,                                                                                                                       |
|                                   |                                                                                                                               |
|                                   | Etched,                                                                                                                       |
|                                   |                                                                                                                               |
|                                   | Bump,                                                                                                                         |
|                                   |                                                                                                                               |
|                                   | Sunken,                                                                                                                       |
|                                   |                                                                                                                               |
|                                   | Adjust and                                                                                                                    |
|                                   |                                                                                                                               |
|                                   | Flat.                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| BorderSingle                      | Indicates the 2D border style. The options are,                                                                               |
|                                   |                                                                                                                               |
|                                   |                                                                                                                               |
|                                   |                                                                                                                               |
|                                   | Solid,                                                                                                                        |
|                                   |                                                                                                                               |
|                                   | Dotted,                                                                                                                       |
|                                   |                                                                                                                               |
|                                   | Dashed,                                                                                                                       |
|                                   |                                                                                                                               |
|                                   | Inset,                                                                                                                        |
|                                   |                                                                                                                               |
|                                   | Outset and                                                                                                                    |
|                                   |                                                                                                                               |
|                                   | None.                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| BorderColor                       | Sets the color for the 2D border. The BorderColor will be effective only when the BorderStyle property is set to FixedSingle. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| BorderSides                       | Specifies the sides of the control which should have a border.                                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [//Sets the 3D border style ]                                                                                                                   |
|                                                                                                                                                                                                   |
| [this][.gradientPanel1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]   |
|                                                                                                                                                                                                   |
| [this][.gradientPanel1.Border3DStyle = System.Windows.Forms.Border3DStyle.Etched;]                           |
|                                                                                                                                                                                                   |
| []                                                                                                                                               |
|                                                                                                                                                                                                   |
| [//Sets the 2D Border style]                                                                                                                    |
|                                                                                                                                                                                                   |
| [this][.gradientPanel1.BorderColor = System.Drawing.Color.Blue;]                                             |
|                                                                                                                                                                                                   |
| [this][.gradientPanel1.BorderSingle = System.Windows.Forms.[ButtonBorderStyle].Dashed;] |
|                                                                                                                                                                                                   |
| [this][.gradientPanel1.BorderSides = System.Windows.Forms.[Border3DSide].All;]          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [\'Sets the 3D border style]                                                                                                                 |
|                                                                                                                                                                                                |
| [Me][.gradientPanel1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle]   |
|                                                                                                                                                                                                |
| [Me][.gradientPanel1.Border3DStyle = System.Windows.Forms.Border3DStyle.Etched]                           |
|                                                                                                                                                                                                |
| [Me][.gradientPanel1.BorderColor = System.Drawing.Color.Blue]                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [\'Sets the 2D Border style]                                                                                                                 |
|                                                                                                                                                                                                |
| [Me][.gradientPanel1.BorderSingle = System.Windows.Forms.[ButtonBorderStyle].Dashed] |
|                                                                                                                                                                                                |
| [Me][.gradientPanel1.BorderSides = System.Windows.Forms.[Border3DSide].All]          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 395: Border3DStyle = \"Etched\"

**[]** 

{border="0"}

Figure 396: BorderSingle = \"Dashed\"; BorderColor = \"Crimson\"

[] 

See Also

**[]** 

[GradientPanel Appearance]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p460}[]{#_Scroll_Settings}3.3.6.2.4.3 Scroll Settings {#scroll-settings style="tab-stops: 0pt"}

[] 

When the contents inside the gradient panel exceeds the visible area, the scroll bars appears. AutoScroll property should be set to true for this purpose. Margin width for the control during auto scroll is set through **AutoScrollMargin** property. The minimum logical size for the auto scroll region is specified using the **AutoScrollMinSize**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                                 |
| [this][.gradientPanel1.AutoScroll = [true];]                                                          |
|                                                                                                                                                                                                                 |
| [this][.gradientPanel1.AutoScrollMargin = [new] System.Drawing.[Size](5, 5);]    |
|                                                                                                                                                                                                                 |
| [this][.gradientPanel1.AutoScrollMinSize = [new] System.Drawing.[Size](20, 20);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                           |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                     |
|                                                                                                                                                                                                              |
| [Me][.gradientPanel1.AutoScroll = [True]]                                                          |
|                                                                                                                                                                                                              |
| [Me][.gradientPanel1.AutoScrollMargin = [New] System.Drawing.[Size](5, 5)]    |
|                                                                                                                                                                                                              |
| [Me][.gradientPanel1.AutoScrollMinSize = [New] System.Drawing.[Size](20, 20)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Size properties

**[]** 

The GradientPanel can automatically size itself based on the contents available in the control by enabling the **AutoSize** property. The mode of this resizing can be specified through **AutoSizeMode** property. There are two options provided for the AutoSizeMode.

[] 

[·      ]GrowOnly - the control grows as much as necessary to fit its contents but doesn\'t shrink smaller than the value specified in Size property of the control.

[·      ]GrowAndShrink - the control grows and shrinks to fit its contents to a size may be less than that specified in Size property.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [this][.gradientPanel1.AutoSize = [true];]                                           |
|                                                                                                                                                                                                |
| [this][.gradientPanel1.AutoSizeMode = System.Windows.Forms.[AutoSizeMode].GrowOnly;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [Me][.gradientPanel1.AutoSize = [True]]                                           |
|                                                                                                                                                                                             |
| [Me][.gradientPanel1.AutoSizeMode = System.Windows.Forms.[AutoSizeMode].GrowOnly] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

