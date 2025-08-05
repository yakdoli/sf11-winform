---
title: howtosettransparentbackcolorforagridcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/howtosettransparentbackcolorforagridcontrol.md
created_at: 2025-08-05
---








  









### How to Set Transparent Backcolor for a GridControl {#how-to-set-transparent-backcolor-for-a-gridcontrol style="tab-stops: 0pt"}

[] 

Introduction

[] 

Setting the transparent [backcolor]{.UGHyperlink} for a **GridControl** can be done easily with simple code.

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                  |
| [// Set up Transparent Background.]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                  |
| [this][.gridControl1.SupportsTransparentBackColor = ][true][;\                                                                                               |
| ][this][.gridControl1.TransparentBackground = ][true][;] |
|                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                  |
| [// Set Color for the Transparent Background.\                                                                                                                                                                                                                                                                   |
| ][this][.gridControl1.Properties.BackgroundColor = Color.FromArgb(0, 1, 1, 1);\                                                                                                                               |
| ][this][.gridControl1.BackColor = Color.FromArgb(0, SystemColors.Window);]                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [\' Set up Transparent Background.]                                                                                                                                        |
|                                                                                                                                                                                                                              |
| [Me][.gridControl1.SupportsTransparentBackColor = ][True\                                                                 |
| Me][.gridControl1.TransparentBackground = ][True]                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [\' Set Color for the Transparent Background.\                                                                                                                                                                               |
| ][Me][.gridControl1.Properties.BackgroundColor = Color.FromArgb(0, 1, 1, 1)\                                              |
| ][Me][.gridControl1.BackColor = Color.FromArgb(0, SystemColors.Window)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p571} 

 

[]{#related-topics}

