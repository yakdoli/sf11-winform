---
title: backgroundsettings1.md
original_path: WinForms_Docs/99_Uncategorized/backgroundsettings1.md
created_at: 2025-08-05
---






##### Background Settings {#background-settings style="tab-stops: 0pt"}

[] 

The background settings of the CommandBar control are discussed below.

[] 

BackColor

**[]** 

CommandBarController

[] 

The back color of the CommandBarController can be set using the property given below.

[] 


  ------------------------------- ----------------------------------------------------------------------
  CommandBarController Property   Description
  BackColor                       The background color used to draw the host form\'s dockable regions.
  ------------------------------- ----------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [this][.commandBarController1.BackColor = System.Drawing.[Color].RosyBrown;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [Me][.CommandBarController1.BackColor = System.Drawing.Color.RosyBrown] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

CommandBar

[] 

The back color of the CommandBar can be set using the property given below.

[] 


  --------------------- --------------------------------------------------
  CommandBar Property   Description
  BackColor             The background color used to draw the component.
  --------------------- --------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [this][.commandBar1.BackColor = System.Drawing.[Color].Wheat;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                             |
|                                                                                                                                                |
| []                                                                                           |
|                                                                                                                                                |
| [Me][.commandBar1.BackColor = System.Drawing.Color.Wheat] |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 27: BackColor of CommandBarController and CommandBar Set

[] 


{border="0"} Note: The ResetBackColor() method of the CommandBarController can be used to reset it\'s BackColor property to the default value. Similarly, the ResetBackColor() method of the CommandBar can be used to reset it\'s BackColor property to the default value.


[]{#related-topics}

