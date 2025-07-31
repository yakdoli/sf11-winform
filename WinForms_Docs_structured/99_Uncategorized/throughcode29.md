---
title: throughcode29.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode29.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The following steps illustrate how to create the jQueryUITabs control programmatically.

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

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                               |
| []                                                                                           |
|                                                                                                                                               |
| [jQueryUITab Tab = [new] jQueryUITab();]                                             |
|                                                                                                                                               |
| [jQueryUITabItem TabItem = [new] jQueryUITabItem();]                                 |
|                                                                                                                                               |
| [TabItem.ID = [\"Item1\"];]                                                        |
|                                                                                                                                               |
| [TabItem.Text = [\"Header1\"];]                                                    |
|                                                                                                                                               |
| [HtmlGenericControl hgc=[new] HtmlGenericControl([\"div\"]);] |
|                                                                                                                                               |
| [hgc.InnerHtml = [\"This is the content of header1\"];]                            |
|                                                                                                                                               |
| [TabItem.Controls.Add(hgc);]                                                                              |
|                                                                                                                                               |
| [Tab.Items.Add(TabItem);]                                                                                 |
|                                                                                                                                               |
| [this][.form1.Controls.Add(Tab);]                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [Dim][ Tab [As] [New] jQueryUITab()]                                         |
|                                                                                                                                                                                                             |
| [Dim][ TabItem [As] [New] jQueryUITabItem()]                                 |
|                                                                                                                                                                                                             |
| [TabItem.ID = [\"Item1\"]]                                                                                                                      |
|                                                                                                                                                                                                             |
| [TabItem.Text = [\"Header1\"]]                                                                                                                  |
|                                                                                                                                                                                                             |
| [Dim][ hgc [As] [New] HtmlGenericControl([\"div\"])] |
|                                                                                                                                                                                                             |
| [hgc.InnerHtml = [\"This is the content of header1\"]]                                                                                          |
|                                                                                                                                                                                                             |
| [TabItem.Controls.Add(hgc)]                                                                                                                                             |
|                                                                                                                                                                                                             |
| [Tab.Items.Add(TabItem)]                                                                                                                                                |
|                                                                                                                                                                                                             |
| [Me][.form1.Controls.Add(Tab)]                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 461: jQueryUITabs Control

 

[]{#related-topics}

