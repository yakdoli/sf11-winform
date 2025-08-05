---
title: throughcode6.md
original_path: WinForms_Docs/99_Uncategorized/throughcode6.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

To create the MultiSelectionDropDown control programmatically, follow the below given steps.

[] 

1.   Create a Web application.

2.   In the .cs file, include the following directives.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                     |
| []                                                                                                 |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI.WebControls.Tools;] |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI;]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI.WebControls.Tools] |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI]                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Then, instantiate the control and add it to the Web Form as given below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [MultiSelectionDropDown][ multiSelectionDropDown2 = [new] MultiSelectionDropDown();] |
|                                                                                                                                                                                                                                |
| [multiSelectionDropDown2.ID = [\"multiSelectionDropDown2\"];]                                                                                       |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [ListItem item1 = [new] ListItem();]                                                                                                                  |
|                                                                                                                                                                                                                                |
| [item1.Text = [\"Chai\"];]                                                                                                                          |
|                                                                                                                                                                                                                                |
| [ListItem item2 = [new] ListItem();]                                                                                                                  |
|                                                                                                                                                                                                                                |
| [item2.Text = [\"Chang\"];]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [ListItem item3 = [new] ListItem();]                                                                                                                  |
|                                                                                                                                                                                                                                |
| [item3.Text = [\"Chef Anton\'s Cajun Seasoning\"];]                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [multiSelectionDropDown2.Items.Add(item1);]                                                                                                                                |
|                                                                                                                                                                                                                                |
| [multiSelectionDropDown2.Items.Add(item2);]                                                                                                                                |
|                                                                                                                                                                                                                                |
| [multiSelectionDropDown2.Items.Add(item3);]                                                                                                                                |
|                                                                                                                                                                                                                                |
| [this][.form1.Controls.Add(multiSelectionDropDown2);]                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [Dim][ multiSelectionDropDown2 [As] MultiSelectionDropDown = [New] MultiSelectionDropDown()] |
|                                                                                                                                                                                                                                                             |
| [multiSelectionDropDown2.ID = [\"multiSelectionDropDown2\"]]                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [Dim][ item1 [As] ListItem = [New] ListItem()]                                               |
|                                                                                                                                                                                                                                                             |
| [item1.Text = [\"Chai\"]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [Dim][ item2 [As] ListItem = [New] ListItem()]                                               |
|                                                                                                                                                                                                                                                             |
| [item2.Text = [\"Chang\"]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [Dim][ item3 [As] ListItem = [New] ListItem()]                                               |
|                                                                                                                                                                                                                                                             |
| [item3.Text = [\"Chef Anton\'s Cajun Seasoning\"]]                                                                                                                               |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [multiSelectionDropDown2.Items.Add(item1)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [multiSelectionDropDown2.Items.Add(item2)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [multiSelectionDropDown2.Items.Add(item3)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [Me][.form1.Controls.Add(multiSelectionDropDown2)]                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

