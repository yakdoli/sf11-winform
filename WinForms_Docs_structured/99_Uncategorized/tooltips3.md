---
title: tooltips3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tooltips3.md
created_at: 2025-07-03
---






##### Tooltips {#tooltips style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Tooltip can be enabled for child windows or tabs using the below code snippet, where doc is the new child form that is created.

 

The **GetTooltip** method is used to set the Tooltips for the tabs.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Method                            | Description                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| GetTooltip                        | Gets the tooltips for the tabs associated with a form.                                                               |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   | [·      ]*mdiChild* - indicates the MDIChild form to which the tooltip should be added. |
|                                   |                                                                                                                      |
|                                   | [·      ]*tooltip* - indicates that the tooltip to be added is of type string.          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| SetTooltip                        | Sets the tooltips for the tabs associated with a form.                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [this][.TabbedMDIManager.GetTooltip(doc, \"Tooltip for \" + doc.Text);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [Me][.TabbedMDIManager.GetTooltip(doc, \"Tooltip for \" + doc.Text)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 1101: Tooltip Support Illustrated

[] 

See Also

[] 

[[Context Menu]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Context_Menu)[]{.UGHyperlink}

 

 

 

[]{#p921} 

[]{#related-topics}

