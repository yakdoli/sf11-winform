---
title: tabsizesettings.md
original_path: WinForms_Docs/99_Uncategorized/tabsizesettings.md
created_at: 2025-08-05
---






#### TabSize Settings {#tabsize-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

SizeMode

[] 

The SizeMode of the tabstrip allows to position the tabitems according to the selected options.

[] 


+-----------------------------------+--------------------------------------------------------------------------+
| TabControlAdv property            | Description                                                              |
+-----------------------------------+--------------------------------------------------------------------------+
| SizeMode                          | Specifies how the tabs should be sized and aligned. The options include: |
|                                   |                                                                          |
|                                   |                                                                          |
|                                   |                                                                          |
|                                   | [·      ]Normal,                            |
|                                   |                                                                          |
|                                   | [·      ]Fixed,                             |
|                                   |                                                                          |
|                                   | [·      ]FillToRight,                       |
|                                   |                                                                          |
|                                   | [·      ]ShrinkToFit.                       |
+-----------------------------------+--------------------------------------------------------------------------+


[] 

[·      ]In **Normal** mode, the size of each tab depends on the text and image settings of the tab.

[·      ]In **Fixed** mode, the size of each tab is the same and is the value specified in the **ItemSize** property.

[·      ]In **ShrinkToFit** mode, the width of each tab is shrunk so that all the tabs are visible (this is only applicable to the tabcontrols in the single-line mode).

[·      ]In **FillToRight** mode, the width of each tab is sized so that each row of tabs occupies the entire width of the ContainerControl (this is only applicable to tabcontrols with more than one row).

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| **[]**                                                                                                                        |
|                                                                                                                                                                                 |
| [this][.tabControlAdv1.SizeMode = Syncfusion.Windows.Forms.Tools.TabSizeMode.Normal;]      |
|                                                                                                                                                                                 |
| [this][.tabControlAdv1.SizeMode = Syncfusion.Windows.Forms.Tools.TabSizeMode.Fixed;]       |
|                                                                                                                                                                                 |
| [this][.tabControlAdv1.SizeMode = Syncfusion.Windows.Forms.Tools.TabSizeMode.ShrinkToFit;] |
|                                                                                                                                                                                 |
| [this][.tabControlAdv1.SizeMode = Syncfusion.Windows.Forms.Tools.TabSizeMode.FillToRight;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                              |
| **[]**                                                                                                                     |
|                                                                                                                                                                              |
| [Me][.tabControlAdv1.SizeMode = Syncfusion.Windows.Forms.Tools.TabSizeMode.Normal]      |
|                                                                                                                                                                              |
| [Me][.tabControlAdv1.SizeMode = Syncfusion.Windows.Forms.Tools.TabSizeMode.Fixed]       |
|                                                                                                                                                                              |
| [Me][.tabControlAdv1.SizeMode = Syncfusion.Windows.Forms.Tools.TabSizeMode.ShrinkToFit] |
|                                                                                                                                                                              |
| [Me][.tabControlAdv1.SizeMode = Syncfusion.Windows.Forms.Tools.TabSizeMode.FillToRight] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

**[                      ][       ][]**

Figure 1056: TabControlAdv with Various Size Modes

**                 \**
 The below methods are raised when the tabcontroladv is resized.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Methods                           | Description                                                                                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether a control should automatically resize itself to fit it\'s contents. The default value is set to False. |
|                                   |                                                                                                                          |
|                                   |                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| AutoSizeMode                      | Specifies the mode by which the user interface element automatically resizes itself. The options include:                |
|                                   |                                                                                                                          |
|                                   |                                                                                                                          |
|                                   |                                                                                                                          |
|                                   | [·      ]GrowOnly - This is used only when the controls have to be expanded.                |
|                                   |                                                                                                                          |
|                                   | [·      ]GrowAndShrink - This is used when the controls have to be expanded and shrunk.     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+


 

 

 

 

[]{#related-topics}

