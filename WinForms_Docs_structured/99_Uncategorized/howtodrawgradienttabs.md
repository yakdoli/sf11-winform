---
title: howtodrawgradienttabs.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodrawgradienttabs.md
created_at: 2025-07-03
---






#### How to draw Gradient Tabs {#how-to-draw-gradient-tabs style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

You can handle the **DrawItem** Event of TabControlAdv and then set the gradient by using the **LinearGradientBrush**.

 

This can be done programmatically using the code snippet given below.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [private][ [void] tabControlAdv1_DrawItem([object] sender, Syncfusion.Windows.Forms.Tools.[DrawTabEventArgs] drawItemInfo)] |
|                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [    [// Use LinearGradientBrush to set gradient. ]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [    [// Use GetTabRect to get the rectangle of the tabs. ]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [    [if] (drawItemInfo.Index != [this].tabControlAdv1.SelectedIndex)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [        [// For the non-selected tabs. ]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [        lgb = [new] System.Drawing.Drawing2D.[LinearGradientBrush](]                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [        [this].tabControlAdv1.GetTabRect(drawItemInfo.Index), [Color].FromArgb(197, 197, 173), [Color].FromArgb(228, 228, 212), LinearGradientMode.Horizontal);]            |
|                                                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [    [else]]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [        [// For the selected tab. ]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [        lgb = [new] System.Drawing.Drawing2D.[LinearGradientBrush](]                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [        [this].tabControlAdv1.GetTabRect(drawItemInfo.Index), [Color].White, [Color].WhiteSmoke, LinearGradientMode.Horizontal);]                                           |
|                                                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [    [float]\[\] positions = { 0.0f, 0.05f, 0.95f, 1.0f };]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [    [float]\[\] factors = { 0.4f, 1.0f, 0.05f, 0.04f };]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [    [// Blend Settings]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [    Blend blend = [new] Blend();]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [    blend.Factors = factors;]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [    blend.Positions = positions;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [    lgb.Blend = blend;]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                 |
| [    drawItemInfo.Graphics.FillRectangle(lgb, [this].tabControlAdv1.GetTabRect(drawItemInfo.Index));]                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [    lgb.Dispose();]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [    [// Draw the default borders and interior (text and image). ]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                 |
| [    drawItemInfo.DrawBorders();]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                 |
| [    drawItemInfo.DrawInterior();]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [} ]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        [private] [void] Form1_Load([object] sender, [EventArgs] e)]                                                                                   |
|                                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [            [this].tabControlAdv1.Padding = [new] [Point](12, 12); ]                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        [private] [void] tabPageAdv1_Click([object] sender, [EventArgs] e)]                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [           ]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        [private] [void] tabControlAdv1_SelectedIndexChanged([object] sender, [EventArgs] e)]                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        [private] [void] tabPageAdv1_Click_1([object] sender, [EventArgs] e)]                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [            ]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        [private] [void] autoLabel1_Click([object] sender, [EventArgs] e)]                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p892} 

[]{#related-topics}

