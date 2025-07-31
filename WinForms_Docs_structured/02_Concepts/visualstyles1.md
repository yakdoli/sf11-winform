---
title: visualstyles1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\visualstyles1.md
created_at: 2025-07-03
---






##### Visual Styles {#visual-styles style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Visual Styles

[] 

It determines the painting scheme to be used for drawing the control.

 

The Visual Styles supported are given below.

[] 

[·      ]**Office XP Style -** It specifies the standard colors and it can enabled by setting the Visual Style to OfficeXP and ThemesEnabled property to \'True\'.

[·      ]**Office 2003 Style -** It specifies the Office 2003 look and it can enabled by setting the Visual Style to Office2003 and ThemesEnabled property to \'False\'.

[·      ]**Office 2007 Style -** It specifies the new Office 2007 look and it can enabled by setting the Visual Style to Office2007 and ThemesEnabled property to \'False\'.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [this][.groupBar1.ThemesEnabled = [true];]                                          |
|                                                                                                                                                                                               |
| [this][.groupBar1.VisualStyle = Syncfusion.Windows.Forms.[VisualStyle].OfficeXP;]   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [this][.groupBar1.ThemesEnabled = [false];]                                         |
|                                                                                                                                                                                               |
| [this][.groupBar1.VisualStyle = Syncfusion.Windows.Forms.[VisualStyle].Office2003;] |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [this][.groupBar1.ThemesEnabled = [false];]                                         |
|                                                                                                                                                                                               |
| [this][.groupBar1.VisualStyle = Syncfusion.Windows.Forms.[VisualStyle].Office2007;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [Me][.groupBar1.ThemesEnabled = [True]]                                            |
|                                                                                                                                                                                              |
| [Me][.groupBar1.VisualStyle = Syncfusion.Windows.Forms.VisualStyle.OfficeXP]                            |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [Me][.groupBar1.ThemesEnabled = [False]]                                           |
|                                                                                                                                                                                              |
| [Me][.groupBar1.VisualStyle = Syncfusion.Windows.Forms.[VisualStyle].Office2003;] |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [Me][.groupBar1.ThemesEnabled = [False]]                                           |
|                                                                                                                                                                                              |
| [Me][.groupBar1.VisualStyle = Syncfusion.Windows.Forms.VisualStyle.Office2007]                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 886: Visual Styles

[] 

GroupBar control supports Office 2007 Style with the color themes Blue, Black and Silver which gives the application a perfect look and feel. This can be set using the **Office2007Theme** property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                          |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [this][.groupBar1.Office2007Theme = [Office2007Theme].Black;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                            |
|                                                                                                                                               |
| []                                                                                          |
|                                                                                                                                               |
| [Me][.groupBar1.Office2007Theme = Office2007Theme.Black] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 887: Office 2007 Color Themes

[] 


{border="0"} Note : The Visual Style property must be set to Office2007 to enable the color themes.


[] 

Custom Colors

[] 

We can also apply custom colors to the GroupBar control by setting Office2007Theme to \"Managed\" and specifying the custom color through the ApplyManagedColors method as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                    |
| [this][.groupBar1.Office2007Theme = Syncfusion.Windows.Forms.[Office2007Theme].Managed;] |
|                                                                                                                                                                                                    |
| [Office2007Colors][.ApplyManagedColors([this], [Color].CadetBlue);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                   |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                   |
| [Me][.groupBar1.Office2007Theme = Syncfusion.Windows.Forms.[Office2007Theme].Managed;]  |
|                                                                                                                                                                                                   |
| [Office2007Colors.][ApplyManagedColors([Me], [Color].CadetBlue)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 888: Custom Color = \"CadetBlue\"

 

 

 

[]{#p615} 

 

[]{#related-topics}

