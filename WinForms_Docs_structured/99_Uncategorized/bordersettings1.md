---
title: bordersettings1.md
original_path: WinForms_Docs/99_Uncategorized/bordersettings1.md
created_at: 2025-08-05
---






##### Border Settings {#border-settings style="tab-stops: 0pt"}

**[]** 

GroupBar Settings

[] 

The border style of the GroupBar can be set using the below given property.

[] 


  ------------------- -------------------------------------------------------
  GroupBar Property   Description
  BorderStyle         Gets / sets the border style of the GroupBar control.
  ------------------- -------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [this][.groupBar1.BorderStyle = System.Windows.Forms.[BorderStyle].Fixed3D;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [Me]**[.]**[groupBar1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

 

Figure 880: Border is drawn with BorderStyle = \"Fixed3D\"

[] 

GroupBar Item Client Area Border Settings

[] 

The border of the GroupBar Item client area can be set and customized using the following properties.

[] 


  -------------------- -----------------------------------------------------------------------------------------------------------------------------
  GroupBar Property    Description
  DrawClientBorder     Specifies whether a border is drawn around the GroupBar\'s client window.
  ClientBorderColors   Specifies the value which determines whether the border for the client area of the GroupBar control should be drawn or not.
  -------------------- -----------------------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.groupBar1.DrawClientBorder = [true];]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.groupBarItem2.ClientBorderColors = [new] Syncfusion.Windows.Forms.Tools.BorderColors(System.Drawing.Color.Red, System.Drawing.Color.Aqua, System.Drawing.Color.Lime, System.Drawing.Color.Magenta);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [Me][.groupBar1.DrawClientBorder = [True]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [Me][.groupBarItem2.ClientBorderColors = [New] Syncfusion.Windows.Forms.Tools.BorderColors(System.Drawing.Color.Red, System.Drawing.Color.Aqua, System.Drawing.Color.Lime, System.Drawing.Color.Magenta)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

 

Figure 881:GroupBar with ClientBorderColors = \"Red, Aqua, Lime, Magenta\"

 

 

 

[]{#p612} 

 

[]{#related-topics}

