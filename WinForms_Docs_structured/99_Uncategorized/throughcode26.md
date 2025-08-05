---
title: throughcode26.md
original_path: WinForms_Docs/99_Uncategorized/throughcode26.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

[] 

The following steps illustrate how to create the jQueryUIDialog control programmatically.

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

2.   Instantiate and add the control onto the form. Also set the required features and properties, if required.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                 |
| []                                                                                             |
|                                                                                                                                                 |
| [jQueryUIDialog dialog = [new] jQueryUIDialog();]                                      |
|                                                                                                                                                 |
| [dialog.ID = [\"jQueryUIDialog1\"];]                                                 |
|                                                                                                                                                 |
| [HtmlGenericControl hgc = [new] HtmlGenericControl([\"div\"]);] |
|                                                                                                                                                 |
| [hgc.InnerHtml = [\"This is dialog content.\"];]                                     |
|                                                                                                                                                 |
| [dialog.DialogContent = hgc;]                                                                               |
|                                                                                                                                                 |
| [dialog.AutoOpen = [true];]                                                            |
|                                                                                                                                                 |
| [this][.form1.Controls.Add(dialog);]                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [Dim][ dialog [As] [New] jQueryUIDialog()]                                   |
|                                                                                                                                                                                                             |
| [dialog.ID = [\"jQueryUIDialog1\"]]                                                                                                             |
|                                                                                                                                                                                                             |
| [Dim][ hgc [As] [New] HtmlGenericControl([\"div\"])] |
|                                                                                                                                                                                                             |
| [hgc.InnerHtml = [\"This is dialog content.\"]]                                                                                                 |
|                                                                                                                                                                                                             |
| [dialog.DialogContent = hgc]                                                                                                                                            |
|                                                                                                                                                                                                             |
| [dialog.AutoOpen = [True]]                                                                                                                         |
|                                                                                                                                                                                                             |
| [Me][.form1.Controls.Add(dialog)]                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 452: jQueryUIDialog Control

[]{#p626} 

[]{#related-topics}

