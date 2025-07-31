---
title: settingcornerradiusforthegroupbaritem.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingcornerradiusforthegroupbaritem.md
created_at: 2025-07-03
---






#### Setting Corner Radius for the GroupBar Item {#setting-corner-radius-for-the-groupbar-item style="tab-stops: 0pt"}

 

It is now possible to set the corner radius of GroupBar Items in the GroupBar by using the **GroupBarItemCornerRadius** property. This helps the user to specify the degree of roundness at the tip of the GroupBar.

 

The following code examples illustrate how to set this property.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][syncfusion][:][GroupBarItem][ HeaderText][=\"Mailbox\"][ GroupBarItemCornerRadius][=\"20\"][ ShowInGroupBar][=\"True\"\>] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [// Creating an instance of GroupBar.]                                                                                                                     |
|                                                                                                                                                                                                                              |
| [GroupBar groupBar = [new] GroupBar();]                                                                                                             |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [// Creating an instance of GroupBar Item.]                                                                                                                |
|                                                                                                                                                                                                                              |
| [GroupBarItem][ groupBarItem = [new] [GroupBarItem]();] |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [// Setting Header Text for GroupBar Item.]                                                                                                                |
|                                                                                                                                                                                                                              |
| [groupBarItem.HeaderText = [\"Mailbox\"];]                                                                                                       |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [// Setting Corner Radius For GroupBar Item.]                                                                                                              |
|                                                                                                                                                                                                                              |
| [groupBarItem.GroupBarItemCornerRadius = [new] [CornerRadius](20d);]                                                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [// Setting ShowInGroupBar propety for GroupBar Item.]                                                                                                     |
|                                                                                                                                                                                                                              |
| [groupBarItem.ShowInGroupBar = [true];]                                                                                                             |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [// Adding GroupBar Item to GroupBar.]                                                                                                                     |
|                                                                                                                                                                                                                              |
| [groupBar.Items.Add(groupBarItem);]                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the code. The following output is displayed.

 

{border="0"}

Figure 530: Corner Radius of GroupBar Items in GroupBar set to 20

 

[]{#p330} 

[]{#related-topics}

