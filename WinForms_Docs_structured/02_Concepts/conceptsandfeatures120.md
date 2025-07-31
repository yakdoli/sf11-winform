---
title: conceptsandfeatures120.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\conceptsandfeatures120.md
created_at: 2025-07-03
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

 

The following topics will help you become more familiar in using the ColorUI control.

[] 

###### []{#_Color_Groups}3.3.4.1.3.1 Color Groups {#color-groups style="tab-stops: 0pt"}

[]{#p339}[] 

ColorUI control has three in-built color groups which are CustomColors, StandardColor, and SystemColors. This section gives you an idea of the color groups available.

[] 

{border="0"}

[] 

Figure 291: In-Built Color Groups

[] 

Displaying the Color Groups

[] 

We can control the display of the color groups using **ColorGroups** property.

[] 

{border="0"}

**[]** 

Figure 292: ColorGroups Property

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                              |
| [this][.colorUIControl1.ColorGroups = ((Syncfusion.Windows.Forms.[ColorUIGroups])((Syncfusion.Windows.Forms.[ColorUIGroups].CustomColors \| Syncfusion.Windows.Forms.[ColorUIGroups].StandardColors)));] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                               |
| [Me][.colorUIControl1.ColorGroups = [DirectCast](((Syncfusion.Windows.Forms.ColorUIGroups.CustomColors [Or] Syncfusion.Windows.Forms.ColorUIGroups.StandardColors)), Syncfusion.Windows.Forms.ColorUIGroups) ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 293: Color Groups = \"CustomColors\" and \"StandardColor Groups\"

[] 

User Groups

[] 

ColorGroups property also let you add user groups in addition to the standard groups. The color palette for the UserGroups will be CustomColors, by default.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [this][.colorUIControl1.ColorGroups = ((Syncfusion.Windows.Forms.[ColorUIGroups])(((Syncfusion.Windows.Forms.[ColorUIGroups].CustomColors \| Syncfusion.Windows.Forms.[ColorUIGroups].StandardColors)\| Syncfusion.Windows.Forms.[ColorUIGroups].UserColors)));] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.colorUIControl1.ColorGroups = [DirectCast]((((Syncfusion.Windows.Forms.ColorUIGroups.CustomColors [Or]  Syncfusion.Windows.Forms.ColorUIGroups.StandardColors) [Or] Syncfusion.Windows.Forms.ColorUIGroups.UserColors)),  Syncfusion.Windows.Forms.ColorUIGroups) ] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 294: User Group added to ColorUIControl

**[]** 


{border="0"} Note: We can add custom text for the tabs of the Color groups. See Tab Text for details.


[] 


{border="0"} Note: The Custom Color Panels and User Color Panels can be stretched according to the size of the control. Refer ColorUIControl Appearance for details.


[] 

See Also

[] 

[Runtime Settings]{.UGHyperlink}[]{.UGHyperlink}

###### []{#_Tab_Text}3.3.4.1.3.2 Tab Text {#tab-text style="tab-stops: 0pt"}

[]{#p340}[] 

The default tab text of the ColorGroups can be set using the below properties.

[] 


+-----------------------------------+----------------------------------------------------------------+
| ColorUIControl Properties         | Description                                                    |
+-----------------------------------+----------------------------------------------------------------+
| CustomTabName                     | Set the text displayed on the custom colors tab.               |
|                                   |                                                                |
|                                   | The tab name can be reset using ResetCustomTabName() method.   |
+-----------------------------------+----------------------------------------------------------------+
| StandardTabName                   | Set the text displayed on the Standard colors tab.             |
|                                   |                                                                |
|                                   | The tab name can be reset using ResetStandardTabName() method. |
+-----------------------------------+----------------------------------------------------------------+
| SystemTabName                     | Set the text displayed on the System colors tab.               |
|                                   |                                                                |
|                                   | The tab name can be reset using ResetSystemTabName() method.   |
+-----------------------------------+----------------------------------------------------------------+
| UserTabName                       | Set the text displayed on the User colors tab.                 |
|                                   |                                                                |
|                                   | The tab name can be reset using ResetUserTabName() method.     |
+-----------------------------------+----------------------------------------------------------------+


**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                           |
| []                                                                                                                                                |
|                                                                                                                                                                           |
| [this][.colorUIControl1.StandardTabName = [\"Web Layout\"];]  |
|                                                                                                                                                                           |
| [this][.colorUIControl1.SystemTabName = [\"System Colors\"];] |
|                                                                                                                                                                           |
| [this][.colorUIControl1.UserTabName = [\"User Defined\"];]    |
|                                                                                                                                                                           |
| [this][.colorUIControl1.CustomTabName = [\"Palettes\"];]      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
| []                                                                                                                                             |
|                                                                                                                                                                        |
| [Me][.colorUIControl1.StandardTabName = [\"Web Layout\"]]  |
|                                                                                                                                                                        |
| [Me][.colorUIControl1.SystemTabName = [\"System Colors\"]] |
|                                                                                                                                                                        |
| [Me][.colorUIControl1.UserTabName = [\"User Defined\"]]    |
|                                                                                                                                                                        |
| [Me][.colorUIControl1.CustomTabName = [\"Palettes\"]]      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 295: Custom Text for Color Group Tabs

**[]** 


{border="0"} Note: We can also change the font style of the tab text using ColorUIControl.Font property.


[]{#related-topics}

