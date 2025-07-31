---
title: backcolorsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\backcolorsettings.md
created_at: 2025-07-03
---






##### BackColor Settings {#backcolor-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

BackColor Settings for the TabControl

[] 

The look and feel of the tabcontrols can be customized using the below **Tab** and **Panel** properties.

[] 


  ------------------------ ------------------------------------------------------------------------
  TabControlAdv Property   Description
  ActiveTabColor           Specifies the backcolor for the selected tab.
  BackColor                Specifies the backcolor for all the tabpages.
  InactiveTabColor         Specifies the backcolor to be used for the inactive tabs.
  TabPanelBackColor        Specifies the color for the tabpanel over which the tabitems are laid.
  ------------------------ ------------------------------------------------------------------------


[] 

BackColor Settings for the TabItems

[] 

The backcolor of the individual tabitems can be customized by setting the **TabBackColor** property of the corresponding tabpages.

[] 


  ------------------------ ------------------------------------------
  TabControlAdv Property   Description
  TabBackColor             Specifies the backcolor for the tabitem.
  ------------------------ ------------------------------------------


[           ]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| **[]**                                                                                                                            |
|                                                                                                                                                                                     |
| [this][.tabControlAdv1.ActiveTabColor = System.Drawing.[Color].Ivory;]    |
|                                                                                                                                                                                     |
| [this][.tabControlAdv1.InactiveTabColor = System.Drawing.[Color].Silver;] |
|                                                                                                                                                                                     |
| [this][.tabControlAdv1.TabPanelBackColor = System.Drawing.[Color].White;] |
|                                                                                                                                                                                     |
| [this][.tabControlAdv1.BackColor = System.Drawing.[Color].Yellow;]        |
|                                                                                                                                                                                     |
| [this][.tabPageAdv1.TabBackColor = System.Drawing.[Color].Pink;]          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [Private][ [Me].tabControlAdv1.ActiveTabColor = System.Drawing.Color.Ivory]    |
|                                                                                                                                                                                          |
| [Private][ [Me].tabControlAdv1.InactiveTabColor = System.Drawing.Color.Silver] |
|                                                                                                                                                                                          |
| [Private][ [Me].tabControlAdv1.TabPanelBackColor = System.Drawing.Color.White] |
|                                                                                                                                                                                          |
| [Private][ [Me].tabControlAdv1.BackColor = System.Drawing.Color.Yellow]        |
|                                                                                                                                                                                          |
| [Private][ [Me].tabPageAdv1.TabBackColor = System.Drawing.Color.Pink]          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1062: TabControl with various BackColor Settings

**[]** 

{border="0"}

**[]** 

Figure 1063: TabControl with TabPanelBackColor for Various TabStyles

 

 

 

 

[]{#related-topics}

