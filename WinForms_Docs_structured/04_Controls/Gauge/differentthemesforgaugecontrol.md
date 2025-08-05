---
title: differentthemesforgaugecontrol.md
original_path: WinForms_Docs/04_Controls/Gauge/differentthemesforgaugecontrol.md
created_at: 2025-08-05
---








  









### Different themes for gauge control {#different-themes-for-gauge-control style="tab-stops: 0pt"}

The OLAP Gauge control allows you to present your data using different built-in-skins. These skins allow you to theme and style the look and feel of the control in various rich color schemes. You can use the *Skin Manager Framework* to apply a wide range of skins to the *Essential OLAP Gauge*. These skins have been designed to suit the needs of a wide range of audience. The following are the types of skins available:

**** 

***Default***-The visual style of this skin depends upon the Operating System used.

***Office2007Blue***-This skin is similar to the Microsoft Office2007Blue skin.

***Office2007Black***-This skin is similar to the Microsoft Office2007Black skin.

***Office2007Silver***-This skin is similar to the Microsoft Office2007Silver skin.

***Office2003Blue***-This skin is similar to the Microsoft Office2003 skin.

***Blend***-This skin is similar to the Microsoft Blend skin.

***Metro:*** This skin is similar to the Metro Skin.

 

[] 

{border="0"}

 

Figure 18: Office 2007 default theme[]

[] 

{border="0"}

 

Figure 19: Office2007Blue Theme[]

***[]*** 

{border="0"}

 

Figure 20: Office2007Black Theme[]

[] 

{border="0"}

 

Figure 21: Office2007Silver Theme[]

[] 

{border="0"}

 

Figure 22: Blend Theme[]

[] 

{border="0"}

 

Figure 23: Office2003Blue Theme[]

{border="0"}

Figure 24: Metro Theme[]

 

 

Applying Skins

 

The various skin themes available can be applied to the control using the *SkinStorage.VisualStyle* property.

To set the visual style for the controls, use the following code:

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<!---To set Office2007Blue ][visual][ style for OLAP Gauge\--\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][gauge][:][OlapGauge][ Name][=\"olapGauge1\"][ Radius][=\"120\"][ syncfusion][:][SkinManager.VisualStyle][=\"Default\"/\>][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [//To set Office2007Blue visual style for Olap Gauge]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [SkinManager][.SetVisualStyle(olapGauge1, ][VisualStyle][.Default);][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [\'To set Office2007Blue visual style for Olap Gauge]                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [SkinManager][.SetVisualStyle(olapGauge1, ][VisualStyle][.Default);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the code. The following output is obtained:

[] 

{border="0"}

 

Figure 25: Office2007 default theme[]

[]{#related-topics}

