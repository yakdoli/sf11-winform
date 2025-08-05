---
title: conceptsandfeatures122.md
original_path: WinForms_Docs/02_Concepts/conceptsandfeatures122.md
created_at: 2025-08-05
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

[] 

The following topics will help you become more familiar in using the ComboDropDown control.

[] 

###### []{#p376}[]{#_ComboDropDown_Text}3.3.5.1.3.1 ComboDropDown Text {#combodropdown-text style="tab-stops: 0pt"}

[] 

ComboDropDown control supports the properties which can change the appearance and behavior of the control\'s edit portion.

[] 

{border="0"}

[] 

Figure 334: Control\'s Edit Portion

[] 


  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------
  ComboDropDown Properties   Description
  CharacterCasing            Specifies the ComboDropDown control modifies the case of characters when they are typed in the edit portion.
  NumberOnly                 Specifies whether the user should be forced to enter only numbers in the edit portion of ComboDropDown.
  ReadOnly                   Specifies whether the text in the edit portion of ComboDropDown should be set to read-only or can be changed. By default it will be set to false.
  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                        |
|                                                                                                                                                                            |
| [this][.comboDropDown1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;] |
|                                                                                                                                                                            |
| [this][.comboDropDown1.NumberOnly = [true];]                     |
|                                                                                                                                                                            |
| [this][.comboDropDown1.ReadOnly = [true];]                       |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [this][.comboDropDown1.CaseSensitiveAutocomplete = [false];]     |
|                                                                                                                                                                            |
| [this][.comboDropDown1.MatchFirstCharacterOnly = [false];]       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                     |
|                                                                                                                                                                         |
| [Me][.comboDropDown1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper] |
|                                                                                                                                                                         |
| [Me][.comboDropDown1.NumberOnly = [True]]                     |
|                                                                                                                                                                         |
| [Me][.comboDropDown1.ReadOnly = [True]]                       |
|                                                                                                                                                                         |
| []                                                                                                                     |
|                                                                                                                                                                         |
| [Me][.comboDropDown1.CaseSensitiveAutocomplete = [False]]     |
|                                                                                                                                                                         |
| [Me][.comboDropDown1.MatchFirstCharacterOnly = [False]]       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Banner Text Support

[] 

We can set banner text for the ComboBoxDropDown control. Refer [[BannerTextProvider Component]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/D2H/ui/windows/tools/Documents/Tools%20-%20Part%202.docx#BannerTextProviderComponent) topic for more details.

 

{border="0"}

[] 

Figure 335: Banner Text set for ComboDropDown

###### []{#p377}[]{#_ComboDropDown_Appearance}3.3.5.1.3.2 ComboDropDown Appearance {#combodropdown-appearance style="tab-stops: 0pt"}

[] 

This section discusses the appearance settings for ComboDropDown control.

[] 

Border Styles

[] 

The below properties lets you set 3D border style for the control.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------+
| Properties                        | Description                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Border3DStyle                     | Sets the 3D border style for the control. The options are,                           |
|                                   |                                                                                      |
|                                   | *[]*                                                           |
|                                   |                                                                                      |
|                                   | [·      ]*RaisedOuter*                                  |
|                                   |                                                                                      |
|                                   | [·      ]*RaisedInner*                                  |
|                                   |                                                                                      |
|                                   | [·      ]*SunkenOuter*                                  |
|                                   |                                                                                      |
|                                   | [·      ]*SunkenInner*                                  |
|                                   |                                                                                      |
|                                   | [·      ]*Raised*                                       |
|                                   |                                                                                      |
|                                   | [·      ]*Sunken*                                       |
|                                   |                                                                                      |
|                                   | [·      ]*Etched*                                       |
|                                   |                                                                                      |
|                                   | [·      ]*Flat*                                         |
|                                   |                                                                                      |
|                                   | [·      ]*Adjust*                                       |
|                                   |                                                                                      |
|                                   | [·      ]*Bump*                                         |
|                                   |                                                                                      |
|                                   | *[]*                                                           |
|                                   |                                                                                      |
|                                   | FlatStyle property should be set to Standard to effect this settings.                |
+-----------------------------------+--------------------------------------------------------------------------------------+
| BorderSides                       | Specifies the sides of the control which should have border.                         |
+-----------------------------------+--------------------------------------------------------------------------------------+
| FlatStyle                         | Specifies the flat style to be applied to the ComboDropDown control. The styles are, |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | Flat - The control and the button appear flat.                                       |
|                                   |                                                                                      |
|                                   | System - Appearance based on the OS used and                                         |
|                                   |                                                                                      |
|                                   | Standard - The control and button appears three-dimensional.                         |
+-----------------------------------+--------------------------------------------------------------------------------------+
| FlatBorderColor                   | Specifies the border color for the control, when FlatStyle is set to \"Flat\".       |
+-----------------------------------+--------------------------------------------------------------------------------------+


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.comboDropDown1.Border3DStyle = System.Windows.Forms.[Border3DStyle].RaisedInner;] |
|                                                                                                                                                                                                     |
| [this][.comboDropDown1.BorderSides = System.Windows.Forms.[Border3DSide].All;]            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [Me][.comboDropDown1.Border3DStyle = System.Windows.Forms.[Border3DStyle].RaisedInner] |
|                                                                                                                                                                                                   |
| [Me][.comboDropDown1.BorderSides = System.Windows.Forms.[Border3DSide].All]            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 336: Border3DStyle = \"RaisedInner\"; BorderSides = \"All\"

**[]** 


{border="0"} Note: ComboDropDown.Style property should be set to Default to effect the above settings. See Themes and Styles topic.


###### []{#_Themes_And_Styles_1}3.3.5.1.3.3 Themes And Styles {#themes-and-styles style="tab-stops: 0pt"}

[]{#p378}[] 

The below given properties enhances the look and feel of the ComboDropDown.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ComboDropDown Properties          | Description                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| IgnoreThemeBackground             | Specifies whether the control will ignore the theme\'s background color and draw the backcolor instead.             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Style                             | Specifies advanced appearance and behavior of the ComboDropDown. The default value is \'Default\'. The options are, |
|                                   |                                                                                                                     |
|                                   |                                                                                                                     |
|                                   |                                                                                                                     |
|                                   | *Default,*                                                                                                          |
|                                   |                                                                                                                     |
|                                   | *OfficeXP,*                                                                                                         |
|                                   |                                                                                                                     |
|                                   | *Office2003,*                                                                                                       |
|                                   |                                                                                                                     |
|                                   | *VS2005 and*                                                                                                        |
|                                   |                                                                                                                     |
|                                   | *Office2007.*                                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                              |
| [this][.comboDropDown1.IgnoreThemeBackground = [true];]                                                                            |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                              |
| [//To set Default Visual Style]                                                                                                                                                            |
|                                                                                                                                                                                                                                              |
| [this][.comboDropDown1.Style = Syncfusion.Windows.Forms.[VisualStyle].Default;]                                                    |
|                                                                                                                                                                                                                                              |
| [//To set Office2003 Visual Style]                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [this][.comboDropDown1.Style = Syncfusion.Windows.Forms.[VisualStyle].Office2003;]                                                 |
|                                                                                                                                                                                                                                              |
| [//To set OfficeXP Visual Style]                                                                                                                                                           |
|                                                                                                                                                                                                                                              |
| [this][.comboDropDown1.Style = Syncfusion.Windows.Forms.[VisualStyle].OfficeXP;]                                                   |
|                                                                                                                                                                                                                                              |
| [//To set VS2005 Visual Style]                                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| [this][.comboDropDown1.Style = Syncfusion.Windows.Forms.[VisualStyle].VS2005;]                                                     |
|                                                                                                                                                                                                                                              |
| [//To set Office2007 Visual Style]                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [this][.comboDropDown1.Style = Syncfusion.Windows.Forms.[VisualStyle].Office2007;][          ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [Me][.comboDropDown1.IgnoreThemeBackground = [True]]     |
|                                                                                                                                                                    |
| []                                                                                                                |
|                                                                                                                                                                    |
| [\'To set Default Visual Style]                                                                                  |
|                                                                                                                                                                    |
| [Me][.comboDropDown1.Style = Syncfusion.Windows.Forms.VisualStyle.Default]    |
|                                                                                                                                                                    |
| [\'To set Office2003 Visual Style]                                                                               |
|                                                                                                                                                                    |
| [Me][.comboDropDown1.Style = Syncfusion.Windows.Forms.VisualStyle.Office2003] |
|                                                                                                                                                                    |
| [\'To set OfficeXP Visual Style]                                                                                 |
|                                                                                                                                                                    |
| [Me][.comboDropDown1.Style = Syncfusion.Windows.Forms.VisualStyle.OfficeXP]   |
|                                                                                                                                                                    |
| [\'To set VS2005 Visual Style]                                                                                   |
|                                                                                                                                                                    |
| [Me][.comboDropDown1.Style = Syncfusion.Windows.Forms.VisualStyle.VS2005]     |
|                                                                                                                                                                    |
| [\'To set Office2007 Visual Style]                                                                               |
|                                                                                                                                                                    |
| [Me][.comboDropDown1.Style = Syncfusion.Windows.Forms.VisualStyle.Office2007] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 337: Styles for ComboDropDown Control

[] 

Office Color Schemes

**[]** 

The ComboDropDown control supports blue, silver and black office colors scheme. It is set using **Office2007ColorTheme** property. **Style** property should be set to Office2007.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| [//To set Blue Color scheme]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| [this][.comboDropDown1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme].Blue;]                                                        |
|                                                                                                                                                                                                                                                                  |
| [//To set Silver Color scheme]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| [this][.comboDropDown1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme.]Silver;]                                                      |
|                                                                                                                                                                                                                                                                  |
| [//To set Black Color scheme]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
| [this][.comboDropDown1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme].Black;][                ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                    |
|                                                                                                                                                                                   |
| **[]**                                                                                                                          |
|                                                                                                                                                                                   |
| [\'To set Blue Color scheme]                                                                                                    |
|                                                                                                                                                                                   |
| [Me][.comboDropDown1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Blue]   |
|                                                                                                                                                                                   |
| [\'To set Silver Color scheme]                                                                                                  |
|                                                                                                                                                                                   |
| [Me][.comboDropDown1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Silver] |
|                                                                                                                                                                                   |
| [\'To set Black Color scheme]                                                                                                   |
|                                                                                                                                                                                   |
| [Me][.comboDropDown1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Black]  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 338: Blue, Silver and Black OfficeColorSchemes

**[]** 

Custom Colors

[] 

We can also apply custom colors to the ComboDropDown control by setting Office2007ColorTheme to \"Managed\" and specifying the custom color through the ApplyManagedColors method as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [this][.comboDropDown1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme].Managed;] |
|                                                                                                                                                                                                              |
| [Office2007Colors][.ApplyManagedColors([this], [Color].Orchid);]              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [Me][.comboDropDown1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme].Managed;] |
|                                                                                                                                                                                                            |
| [Office2007Colors.][ApplyManagedColors([Me], [Color].Orchid)]             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 339: Custom Color = \"Orchid\"

[]{#related-topics}

