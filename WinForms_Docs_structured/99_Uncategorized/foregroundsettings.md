---
title: foregroundsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\foregroundsettings.md
created_at: 2025-07-03
---








  









### Foreground Settings {#foreground-settings style="tab-stops: 0pt"}

[] 

Chart Title

**[]** 

The ChartControl provides properties to customize and align the text within the control. Below are the text properties.

Using the **ChartControl.Text** property, users can provide the title that appears at the top of the chart. **TextPosition** and **TextAlignment** further lets you control the relative positioning of this title.

Here are some properties that affect the title text in the chart.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Chart Control Properties          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Text                              | Specifies the title for the chart.                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------+
| TextPosition                      | Specifies the position of the chart. Possible values are,                                |
|                                   |                                                                                          |
|                                   | Top (**default setting**)                                                                |
|                                   |                                                                                          |
|                                   | Bottom                                                                                   |
|                                   |                                                                                          |
|                                   | Left                                                                                     |
|                                   |                                                                                          |
|                                   | Right                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------+
| TextAlignment                     | Specifies the alignment of the title with respect to the chart borders. Possible values: |
|                                   |                                                                                          |
|                                   | Near                                                                                     |
|                                   |                                                                                          |
|                                   | Center (**default setting**)                                                             |
|                                   |                                                                                          |
|                                   | Far                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Font                              | Indicates the font style of the title.                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ForeColor                         | Indicates the foreground color of the title.                                             |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                |
| [this][.ChartWebControl1.Text = [\"Illustrates Foreground Settings\"];]                                                                                                            |
|                                                                                                                                                                                                                                                                                                |
| [this][.ChartWebControl1.Font = [new] System.Drawing.[Font]([\"Arial\"], 11.25F, System.Drawing.[FontStyle].Bold);] |
|                                                                                                                                                                                                                                                                                                |
| [this][.ChartWebControl1.ForeColor = System.Drawing.[Color].Bisque;]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| [this][.ChartWebControl1.TextPosition = [ChartTextPosition].Top;]                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                             |
| [Me][.ChartWebControl1.Text = [\"Illustrates Foreground Settings\"]]                                                                                                            |
|                                                                                                                                                                                                                                                                                             |
| [Me][.ChartWebControl1.Font = [New] System.Drawing.[Font]([\"Arial\"], 11.25F, System.Drawing.[FontStyle].Bold)] |
|                                                                                                                                                                                                                                                                                             |
| [Me][.ChartWebControl1.ForeColor = System.Drawing.[Color].Bisque]                                                                                                                 |
|                                                                                                                                                                                                                                                                                             |
| [Me][.ChartWebControl1.TextPosition = [ChartTextPosition].Top]                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 301: Illustrates changes affecting the Title Text

**[]** 

General Text Related settings

**[]** 

The following text related properties affect all the text rendered in the chart.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Chart Control Properties          | Description                                                                                                                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TextRenderingHint                 | Specifies the way the text is drawn. Possible values:                                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                      |
|                                   | AntiAlias - each character is drawn using its anti-aliased glyph bitmap without hinting.                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                      |
|                                   | AntiAliasGridFit - each character is drawn using its antialiased glyph bitmap with hinting.                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                      |
|                                   | ClearTypeGridFit - each character is drawn using its glyph clear type bitmap with hinting.                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                      |
|                                   | SingleBitPerPixel - each character is drawn using its glyph bitmap.                                                                                                                                                                  |
|                                   |                                                                                                                                                                                                                                      |
|                                   | SingleBitPerPixelGridFit - each character is drawn using its glyph bitmap.                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                      |
|                                   | SystemDefault - each character is drawn using its glyph bitmap with the system default rendering hint. The text will be drawn using whatever the font-smoothing settings the user had selected for the system. (**default setting**) |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SmoothingMode                     | Specifies how chart elements should be rendered. Possible values:                                                                                                                                                                    |
|                                   |                                                                                                                                                                                                                                      |
|                                   | Antialias                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                      |
|                                   | HighQuality                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                      |
|                                   | HighSpeed                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                      |
|                                   | Invalid                                                                                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                      |
|                                   | None                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                      |
|                                   | Default(**default** **setting**)                                                                                                                                                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

See Also

[] 

[Axis Label Text Formatting]{.UGHyperlink}[, ]{.UGHyperlink}[Appearance and Positioning]{.UGHyperlink}, (for info on changing axis label text settings)

[Customizing Label Text]{.UGHyperlink}[, ]{.UGHyperlink}[Intersecting Labels]{.UGHyperlink}[, ]{.UGHyperlink}[Grouping Labels]{.UGHyperlink}[, ](for info on changing axis label text settings)

[Series Customization]{.UGHyperlink}[, ](for info on changing series text settings)

[Chart Legend]{.UGHyperlink}[ ](for info on changing legend text settings)

[]{#p209} 

[]{#related-topics}

