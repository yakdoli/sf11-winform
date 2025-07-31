---
title: bordersettings2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\bordersettings2.md
created_at: 2025-07-03
---






##### Border Settings {#border-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section discusses the border settings of the ProgressBarAdv control.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------+
| ProgressBarAdv Property           | Description                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Border3DStyle                     | Determines the style of the 3D border. It includes the following options.                         |
|                                   |                                                                                                   |
|                                   |                                                                                                   |
|                                   |                                                                                                   |
|                                   | [·      ]*RaisedOuter,*                                              |
|                                   |                                                                                                   |
|                                   | [·      ]*SunkenOuter,*                                              |
|                                   |                                                                                                   |
|                                   | [·      ]*RaisedInner,*                                              |
|                                   |                                                                                                   |
|                                   | [·      ]*Raised,*                                                   |
|                                   |                                                                                                   |
|                                   | [·      ]*Etched,*                                                   |
|                                   |                                                                                                   |
|                                   | [·      ]*SunkenInner,*                                              |
|                                   |                                                                                                   |
|                                   | [·      ]*Bump,*                                                     |
|                                   |                                                                                                   |
|                                   | [·      ]*Sunken,*                                                   |
|                                   |                                                                                                   |
|                                   | [·      ]*Adjust and*                                                |
|                                   |                                                                                                   |
|                                   | [·      ]*Flat.*                                                     |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| BorderColor                       | Indicates the color of the border.                                                                |
|                                   |                                                                                                   |
|                                   |                                                                                                   |
|                                   |                                                                                                   |
|                                   | This will be applied to the control only when the BorderStyle property is set to \'FixedSingle\'. |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| BorderSingle                      | Determines the style of the 2D border. The options included are as follows.                       |
|                                   |                                                                                                   |
|                                   |                                                                                                   |
|                                   |                                                                                                   |
|                                   | [·      ]Dashed,                                                     |
|                                   |                                                                                                   |
|                                   | [·      ]Dotted,                                                     |
|                                   |                                                                                                   |
|                                   | [·      ]Solid,                                                      |
|                                   |                                                                                                   |
|                                   | [·      ]Inset,                                                      |
|                                   |                                                                                                   |
|                                   | [·      ]Outset and                                                  |
|                                   |                                                                                                   |
|                                   | [·      ]None.                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| BorderStyle                       | Determines the style of the border. It includes the following options.                            |
|                                   |                                                                                                   |
|                                   |                                                                                                   |
|                                   |                                                                                                   |
|                                   | [·      ]FixedSingle,                                                |
|                                   |                                                                                                   |
|                                   | [·      ]Fixed3D and                                                 |
|                                   |                                                                                                   |
|                                   | [·      ]None.                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [this][.progressBarAdv1.Border3DStyle = System.Windows.Forms.[Border3DStyle].RaisedOuter;] |
|                                                                                                                                                                                                      |
| [this][.progressBarAdv1.BorderColor = System.Drawing.[Color].Black;]                       |
|                                                                                                                                                                                                      |
| [this][.progressBarAdv1.BorderSingle = System.Windows.Forms.[ButtonBorderStyle].Dashed;]   |
|                                                                                                                                                                                                      |
| [this][.progressBarAdv1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                          |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
| [Me][.progressBarAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.RaisedOuter ] |
|                                                                                                                                                                             |
| [Me][.progressBarAdv1.BorderColor = System.Drawing.Color.Black ]                       |
|                                                                                                                                                                             |
| [Me][.progressBarAdv1.BorderSingle = System.Windows.Forms.ButtonBorderStyle.Dashed ]   |
|                                                                                                                                                                             |
| [Me][.progressBarAdv1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle ]     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 974: Border Settings of ProgressBarAdv

 

 

 

[]{#p718} 

[]{#related-topics}

