---
title: creatingmonthcalendaradv.md
original_path: WinForms_Docs/99_Uncategorized/creatingmonthcalendaradv.md
created_at: 2025-08-05
---






##### Creating MonthCalendarAdv {#creating-monthcalendaradv style="tab-stops: 0pt"}

 

We can just drag and drop the MonthCalendarAdv onto the form through designer and can access their properties through the property grid.

[] 

{border="0"}

[] 

Figure 207: MonthCalendarAdv in Toolbox

[] 

To create the control programmatically, follow the below steps.

[] 

1.   Include the required namespace.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| []                                                                                                     |
|                                                                                                                                |
| [using ][Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                                                      |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an instance of the MonthCalendarAdv control.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                                          |
|                                                                                                                                                                     |
| [private][ Syncfusion.Windows.Forms.Tools.MonthCalendarAdv monthCalendarAdv1;] |
|                                                                                                                                                                     |
| [this][.monthCalendarAdv1=[new] MonthCalendarAdv();]      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                                                   |
|                                                                                                                                                                                              |
| [Private][ monthCalendarAdv1 [As] Syncfusion.Windows.Forms.Tools.MonthCalendarAdv] |
|                                                                                                                                                                                              |
| [Me][.monthCalendarAdv1 = [New] MonthCalendarAdv()]                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Set the visual style for the control. Add that instance to the Form.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                 |
| [this][.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.[VisualStyle].Office2007;] |
|                                                                                                                                                                                                 |
| [this][.Controls.Add([this].monthCalendarAdv1);]                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                                    |
|                                                                                                                                                                                               |
| [Me][.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.[VisualStyle].Office2007] |
|                                                                                                                                                                                               |
| [Me][.Controls.Add([Me].monthCalendarAdv1)]                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Run the application.

[] 

{border="0"}

[] 

Figure 208: MonthCalendarAdv Created Programmatically

[] 

See Also

**[]** 

[[Concepts and Features]]{.UGHyperlink}

[]{#related-topics}

