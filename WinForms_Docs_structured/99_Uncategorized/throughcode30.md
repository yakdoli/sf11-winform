---
title: throughcode30.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode30.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The following steps illustrate how to create the jQueryUIDatePicker control programmatically.

[] 

1.   Add the required namespace.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                     |
|                                                                                                                                      |
| []                                                                                  |
|                                                                                                                                      |
| [using][ Syncfusion.Web.UI.WebControls.Shared;] |
+--------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                      |
|                                                                                                                                       |
| []                                                                                   |
|                                                                                                                                       |
| [Imports][ Syncfusion.Web.UI.WebControls.Shared] |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Instantiate and add the control to the form. Also set the required features and properties, if required.

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                               |
| []                                                                           |
|                                                                                                                               |
| [jQueryUIDatePicker datepicker = [new] jQueryUIDatePicker();]        |
|                                                                                                                               |
| [datepicker.ID = [\"jQueryUIDatePicker1\"];]                       |
|                                                                                                                               |
| [this][.form1.Controls.Add(datepicker);] |
+-------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                       |
|                                                                                                                        |
| []                                                                    |
|                                                                                                                        |
| [jQueryUIDatePicker datepicker = [new] jQueryUIDatePicker();] |
|                                                                                                                        |
| [datepicker.ID = [\"jQueryUIDatePicker1\"];]               |
|                                                                                                                        |
| [this.form1.Controls.Add(datepicker);]                                             |
+------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 464: jQueryUIDatePicker Control

[]{#related-topics}

