---
title: sizinggripsettings1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\sizinggripsettings1.md
created_at: 2025-07-03
---






##### SizingGrip Settings {#sizinggrip-settings style="tab-stops: 0pt"}

[] 

The StatusStripEx control has a sizing grip at its bottom right corner. This sizing grip can be shown or hidden using **SizingGrip** property. The below properties controls the appearance of the sizing grip.

[] 


  ------------ ----------------------------------------------
  Property     Description
  GripStyle    Specifies the style of the sizing grip.
  GripMargin   Gets or sets the margin for the sizing grip.
  ------------ ----------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                               |
| [this][.statusStripEx1.SizingGrip = [true];]                                                                        |
|                                                                                                                                                                                                                               |
| [this][.statusStripEx1.GripStyle = [ToolStripGripStyle].Visible;]                                                   |
|                                                                                                                                                                                                                               |
| [this][.statusStripEx1.GripMargin = [new] [Padding](5);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                            |
| [Me][.statusStripEx1.SizingGrip = [True]]                                                                        |
|                                                                                                                                                                                                                            |
| [Me][.statusStripEx1.GripStyle = [ToolStripGripStyle].Visible]                                                   |
|                                                                                                                                                                                                                            |
| [Me][.statusStripEx1.GripMargin = [New] [Padding](5)][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

