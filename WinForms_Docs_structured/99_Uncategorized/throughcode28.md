---
title: throughcode28.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode28.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The following steps illustrate how to create the jQueryUIAccordion control programmatically.

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
| [jQueryUIAccordion Accordion = [new] jQueryUIAccordion();]                           |
|                                                                                                                                               |
| [jQueryUIAccordionItem AccordionItem = [new] jQueryUIAccordionItem();]               |
|                                                                                                                                               |
| [AccordionItem.ID = [\"Item1\"];]                                                  |
|                                                                                                                                               |
| [AccordionItem.Text = [\"Header1\"];]                                              |
|                                                                                                                                               |
| [HtmlGenericControl hgc=[new] HtmlGenericControl([\"div\"]);] |
|                                                                                                                                               |
| [hgc.InnerHtml=[\"This is the content of header1\"];]                              |
|                                                                                                                                               |
| [AccordionItem.Controls.Add(hgc);]                                                                        |
|                                                                                                                                               |
| [Accordion.Items.Add(AccordionItem);]                                                                     |
|                                                                                                                                               |
| [this][.form1.Controls.Add(Accordion);]                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [Dim][ Accordion [As] [New] jQueryUIAccordion()]                             |
|                                                                                                                                                                                                             |
| [Dim][ AccordionItem [As] [New] jQueryUIAccordionItem()]                     |
|                                                                                                                                                                                                             |
| [AccordionItem.ID = [\"Item1\"]]                                                                                                                |
|                                                                                                                                                                                                             |
| [AccordionItem.Text = [\"Header1\"]]                                                                                                            |
|                                                                                                                                                                                                             |
| [Dim][ hgc [As] [New] HtmlGenericControl([\"div\"])] |
|                                                                                                                                                                                                             |
| [hgc.InnerHtml = [\"This is the content of header1\"]]                                                                                          |
|                                                                                                                                                                                                             |
| [AccordionItem.Controls.Add(hgc)]                                                                                                                                       |
|                                                                                                                                                                                                             |
| [Accordion.Items.Add(AccordionItem)]                                                                                                                                    |
|                                                                                                                                                                                                             |
| [Me][.form1.Controls.Add(Accordion)]                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 458: jQueryUIAccordion Control

 

[]{#related-topics}

