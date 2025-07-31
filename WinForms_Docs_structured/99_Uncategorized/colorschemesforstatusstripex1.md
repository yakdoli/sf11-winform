---
title: colorschemesforstatusstripex1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\colorschemesforstatusstripex1.md
created_at: 2025-07-03
---






##### ColorSchemes for StatusStripEx {#colorschemes-for-statusstripex style="tab-stops: 0pt"}

[]{#p1177}[] 

StatusStripEx supports all the three color schemes, i.e., Silver, Blue and Black schemes of Office2007. It can be changed using **OfficeColorScheme** property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Tooltips][\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [this][.statusStripEx1.OfficeColorScheme = Syncfusion.Windows.Forms.Tools.[ToolStripEx].[ColorScheme].Silver;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [Me][.statusStripEx1.OfficeColorScheme = Syncfusion.Windows.Forms.Tools.[ToolStripEx].[ColorScheme].Silver] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1407: Color Scheme = \"Silver\"

[] 

{border="0"}

[] 

***[]*** 

Figure 1408: Color Scheme = \"Blue\"

**[]** 

{border="0"}

**[]** 

Figure 1409: Color Scheme = \"Black\"

**[]** 

Custom Colors

[] 

We can also apply custom colors to the StatusStripEx by setting OfficeColorScheme to \"Managed\" and specifying the custom color through the **ApplyManagedColors** method as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [this][.statusStripEx1.OfficeColorScheme = Syncfusion.Windows.Forms.Tools.[ToolStripEx].[ColorScheme].Managed;] |
|                                                                                                                                                                                                                                                |
| [Office2007Colors][.ApplyManagedColors([this], [Color].DarkGreen);]                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                       |
| [Me][.statusStripEx1.OfficeColorScheme = Syncfusion.Windows.Forms.[Tools.ToolStripEx.ColorScheme.Managed]] |
|                                                                                                                                                                                                                       |
| [Office2007Colors.][ApplyManagedColors([Me], [Color].DarkGreen)]                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1410: Custom Color = \"DarkGreen\"

**[]** 

See Also

[] 

[[Creating a StatusStripEx]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Creating_a_StatusStripEx)[, ]{.UGHyperlink}[[Smart Tag Options]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Smart_Tag_Options)[, ]{.UGHyperlink}[[SizingGrip Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_SizingGrip_Settings)[]{.UGHyperlink}

 

 

[]{#related-topics}

