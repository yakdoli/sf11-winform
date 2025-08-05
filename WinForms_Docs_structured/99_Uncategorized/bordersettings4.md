---
title: bordersettings4.md
original_path: WinForms_Docs/99_Uncategorized/bordersettings4.md
created_at: 2025-08-05
---






##### Border Settings {#border-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section illustrates the border settings available for the StatusBarAdvPanel control.

 

The border settings for the StatusBarAdvPanel control can be set through the properties listed below.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------+
| StatusBarAdvPanel Property        | Description                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| Border3DStyle                     | Indicates the style of the 3D border. The options included are as follows.              |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | [·      ]RaisedOuter,                                      |
|                                   |                                                                                         |
|                                   | [·      ]SunkenOuter,                                      |
|                                   |                                                                                         |
|                                   | [·      ]RaisedInner,                                      |
|                                   |                                                                                         |
|                                   | [·      ]SunkenInner,                                      |
|                                   |                                                                                         |
|                                   | [·      ]Raised,                                           |
|                                   |                                                                                         |
|                                   | [·      ]Etched,                                           |
|                                   |                                                                                         |
|                                   | [·      ]Bump,                                             |
|                                   |                                                                                         |
|                                   | [·      ]Sunken,                                           |
|                                   |                                                                                         |
|                                   | [·      ]Adjust and                                        |
|                                   |                                                                                         |
|                                   | [·      ]Flat.                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderColor                       | Indicates the color of the 2D border.                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderSingle                      | Indicates the 2D border style. The options included are as follows.                     |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | [·      ]Dotted,                                           |
|                                   |                                                                                         |
|                                   | [·      ]Dashed,                                           |
|                                   |                                                                                         |
|                                   | [·      ]Solid,                                            |
|                                   |                                                                                         |
|                                   | [·      ]Inset,                                            |
|                                   |                                                                                         |
|                                   | [·      ]Outset and                                        |
|                                   |                                                                                         |
|                                   | [·      ]None.                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderSides                       | Indicates the border sides of the control. The options included are given below.        |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | [·      ]Left,                                             |
|                                   |                                                                                         |
|                                   | [·      ]Top,                                              |
|                                   |                                                                                         |
|                                   | [·      ]Right,                                            |
|                                   |                                                                                         |
|                                   | [·      ]Bottom,                                           |
|                                   |                                                                                         |
|                                   | [·      ]Middle and                                        |
|                                   |                                                                                         |
|                                   | [·      ]All.                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderStyle                       | Indicates whether the panel should have a border. The options included are given below. |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | [·      ]FixedSingle,                                      |
|                                   |                                                                                         |
|                                   | [·      ]Fixed3D and                                       |
|                                   |                                                                                         |
|                                   | [·      ]None.                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+


 


{border="0"} Note: The BorderColor and BorderSingle properties will have effect only when the BorderStyle property is set to \'FixedSingle\'.


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [this][.statusBarAdv1.Border3DStyle = System.Windows.Forms.[Border3DStyle].RaisedInner;] |
|                                                                                                                                                                                                    |
| [this][.statusBarAdv1.BorderColor = System.Drawing.[Color].DarkRed;]                     |
|                                                                                                                                                                                                    |
| [this][.statusBarAdv1.BorderSingle = System.Windows.Forms.[ButtonBorderStyle].Dashed;]   |
|                                                                                                                                                                                                    |
| [this][.statusBarAdv1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]     |
|                                                                                                                                                                                                    |
| [this][.statusBarAdv1.BorderSides = System.Windows.Forms.[Border3DSide].All;]            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                       |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [Me][.statusBarAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.RaisedInner] |
|                                                                                                                                                                          |
| [Me][.statusBarAdv1.BorderColor = System.Drawing.Color.DarkRed]                     |
|                                                                                                                                                                          |
| [Me][.statusBarAdv1.BorderSingle = System.Windows.Forms.ButtonBorderStyle.Dashed]   |
|                                                                                                                                                                          |
| [Me][.statusBarAdv1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle]     |
|                                                                                                                                                                          |
| [Me][.statusBarAdv1.BorderSides = System.Windows.Forms.Border3DSide.All]            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

User can also set the other options available to the properties and monitor the difference in appearance.

[] 

{border="0"}

[] 

Figure 1025: StatusBarAdvPanel with Border Set

 

 

 

 

[]{#related-topics}

