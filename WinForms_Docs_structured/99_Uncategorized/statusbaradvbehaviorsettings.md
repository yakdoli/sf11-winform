---
title: statusbaradvbehaviorsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\statusbaradvbehaviorsettings.md
created_at: 2025-07-03
---






##### StatusBarAdv - Behavior Settings {#statusbaradv---behavior-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section discusses the properties that determine the behavior of the StatusBarAdv control.

 

**AutoSize Settings**

[] 

This includes the properties that enable auto sizing of the StatusBarAdv control.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| StatusBarAdv Property             | Description                                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether a control will automatically resize itself to fit it\'s contents.                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| AutoSizeMode                      | Specifies the mode by which the control automatically resizes itself. The options included are given below. |
|                                   |                                                                                                             |
|                                   |                                                                                                             |
|                                   |                                                                                                             |
|                                   | [·      ]GrowAndShrink and                                                     |
|                                   |                                                                                                             |
|                                   | [·      ]GrowOnly.                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+


[] 

If the \'GrowAndShrink\' option is selected, then the control grows and shrinks to fit it\'s contents to a size that may be a little more or less than the value specified in the Size property of the control.

 

If the \'GrowOnly\'*[ ]*option is selected, the control grows as much as necessary to fit it\'s contents, but doesn\'t shrink smaller than the value specified in the Size property of the control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                               |
| [this][.statusBarAdv1.AutoSize = [true];]                                           |
|                                                                                                                                                                                               |
| [this][.statusBarAdv1.AutoSizeMode = System.Windows.Forms.[AutoSizeMode].GrowOnly;] |
|                                                                                                                                                                                               |
| [this][.statusBarAdv1.AutoHeightControls = [true];]                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                         |
|                                                                                                                                                                                            |
| **[]**                                                                                                                                   |
|                                                                                                                                                                                            |
| [Me][.statusBarAdv1.AutoSize = [True]]                                           |
|                                                                                                                                                                                            |
| [Me][.statusBarAdv1.AutoSizeMode = System.Windows.Forms.[AutoSizeMode].GrowOnly] |
|                                                                                                                                                                                            |
| [Me][.statusBarAdv1.AutoHeightControls = [True]]                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

AutoHeight Settings

[] 

The height of the panels can be made to change automatically when the height of the StatusBarAdv control changes. This can be accomplished using the property given below.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------+
| StatusBarAdv Property             | Description                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| AutoHeightControls                | Determines if the StatusBarAdv will resize the height of the panels according to it\'s height. |
|                                   |                                                                                                |
|                                   |                                                                                                |
|                                   |                                                                                                |
|                                   | The default value will be set to \'True\'.                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| **[]**                                                                                                      |
|                                                                                                                                                               |
| [this][.statusBarAdv1.AutoHeightControls = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                         |
|                                                                                                                                                            |
| **[]**                                                                                                   |
|                                                                                                                                                            |
| [Me][.statusBarAdv1.AutoHeightControls = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The methods associated with the above properties are given below.

[] 


  ------------------ -----------------------------------------------------------------
  Methods            Description
  GetPreferredSize   Returns the preferred size of the specified control.
  SetPreferredSize   Sets the preferred size in the layout of the specified control.
  ------------------ -----------------------------------------------------------------


 

 

 

 

[]{#related-topics}

