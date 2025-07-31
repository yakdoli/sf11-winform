---
title: runtimesettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\runtimesettings.md
created_at: 2025-07-03
---






##### Runtime Settings {#runtime-settings style="tab-stops: 0pt"}

[] 

At run time a particular color group tab should be focussed or selected. Use **SelectedColorGroup** property of the ColorUI property for this purpose.

[] 

The options are as follows.

*[]* 

[·      ]CustomColors

[·      ]StandardColors

[·      ]SystemColors

[·      ]UserColors

[·      ]None (Default)

[] 

Use **SelectedColor** property to specify the initially selected color.

*[]* 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                          |
| [this][.colorUIControl1.SelectedColorGroup = Syncfusion.Windows.Forms.[ColorUISelectedGroup].StandardColors;] |
|                                                                                                                                                                                                                          |
| [this][.colorUIControl1.SelectedColor = System.Drawing.[Color].OrangeRed;]                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                        |
| [Me][.colorUIControl1.SelectedColorGroup = Syncfusion.Windows.Forms.[ColorUISelectedGroup].StandardColors;] |
|                                                                                                                                                                                                                        |
| [Me][.colorUIControl1.SelectedColor = System.Drawing.[Color].OrangeRed;]                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 298: SelectedColor = \"OrangeRed\"; SelectedColorGroup = \"StandardColors\"

[] 


{border="0"} Note: These property settings can be reset using ResetSelectedColorGroup() and ResetSelectedColor() methods.


[] 

See Also

[] 

[Color Groups]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

