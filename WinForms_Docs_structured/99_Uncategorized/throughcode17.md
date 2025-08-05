---
title: throughcode17.md
original_path: WinForms_Docs/99_Uncategorized/throughcode17.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

[] 

The Groupbar structure can be created from XML file or by building the items in code. This procedure below shows how to add group bar items and to look for an item programmatically.

[] 

Creating GroupBar Structure Programmatically

[] 

1.   Open a Web application.

9.   In the design view, drag the Groupbar from the toolbox.

10.  Add the following sample code snippet to the code view of the project.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                           |
| []                                                                                       |
|                                                                                                                                                           |
| [if][ (!IsPostBack)]                 |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  Syncfusion.Web.UI.WebControls.Tools.GroupBar gbar = Groupbar1;]                                    |
|                                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                                           |
| [  gbar.Width = 175;]                                                                                 |
|                                                                                                                                                           |
| [  gbar.DefaultTopItemSpacing = 10;]                                                                  |
|                                                                                                                                                           |
| [  gbar.ControlRootCSSClass = [\"TopGroup\"];]                                 |
|                                                                                                                                                           |
| [  gbar.ExpandSingleGroup = [true];]                                             |
|                                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                                           |
| [  [//create sub items look]]                                                   |
|                                                                                                                                                           |
| [  GroupBarItemLook subPanel = [new] GroupBarItemLook();]                        |
|                                                                                                                                                           |
| [  subPanel.ID = [\"subPanelLook\"];]                                          |
|                                                                                                                                                           |
| [  subPanel.TextPaddingLeft = 5;]                                                                     |
|                                                                                                                                                           |
| [  subPanel.ImageHeight = 16;]                                                                        |
|                                                                                                                                                           |
| [  subPanel.ImageWidth = 16;]                                                                         |
|                                                                                                                                                           |
| [  subPanel.StateDataDefault.ItemCSSClass = [\"DefChild_ItemCss\"];]           |
|                                                                                                                                                           |
| [  subPanel.StateDataDefault.TextContainerCSSClass = [\"DefChild_TextCont\"];] |
|                                                                                                                                                           |
| [  subPanel.StateDataHover.ItemCSSClass = [\"HovChild_ItemCss\"];]             |
|                                                                                                                                                           |
| [  subPanel.StateDataHover.TextContainerCSSClass = [\"HovChild_TextCont\"];]   |
|                                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                                           |
| [  [//create top items look]]                                                   |
|                                                                                                                                                           |
| [  GroupBarItemLook topItem = [new] GroupBarItemLook();]                         |
|                                                                                                                                                           |
| [  topItem.ID = [\"topItemLook\"];]                                            |
|                                                                                                                                                           |
| [  topItem.StateDataDefault.ItemCSSClass = [\"DefRoot_ItemCss\"];]             |
|                                                                                                                                                           |
| [  topItem.StateDataDefault.TextContainerCSSClass = [\"DefRoot_TextCont\"];]   |
|                                                                                                                                                           |
| [  topItem.StateDataHover.ItemCSSClass = [\"HovRoot_ItemCss\"];]               |
|                                                                                                                                                           |
| [  topItem.StateDataHover.TextContainerCSSClass = [\"HovRoot_TextCont\"];]     |
|                                                                                                                                                           |
| [  topItem.StateDataExpanded.ItemCSSClass = [\"DefRoot_ItemCss\"];]            |
|                                                                                                                                                           |
| [  topItem.StateDataExpanded.TextContainerCSSClass = [\"DefRoot_TextCont\"];]  |
|                                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                                           |
| [  [//add item looks to the groupbar]]                                          |
|                                                                                                                                                           |
| [  gbar.ItemLooks.Add(subPanel);]                                                                     |
|                                                                                                                                                           |
| [  gbar.ItemLooks.Add(topItem);]                                                                      |
|                                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                                           |
| [  [//create groupbar items]]                                                   |
|                                                                                                                                                           |
| [  GroupBarItem networkTasks = [new] GroupBarItem();]                            |
|                                                                                                                                                           |
| [  networkTasks.Expanded = [true];]                                              |
|                                                                                                                                                           |
| [  networkTasks.Text = [\"File and Folder Tasks\"];]                           |
|                                                                                                                                                           |
| [  networkTasks.ControlSubPanelCSSClass = [\"Level2Group\"];]                  |
|                                                                                                                                                           |
| [  networkTasks.Look = [\"topItemLook\"];]                                     |
|                                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                                           |
| [  GroupBarItem networkPlace = [new] GroupBarItem();]                            |
|                                                                                                                                                           |
| [  networkPlace.Text = [\"Email this folder\'s file\"];]                       |
|                                                                                                                                                           |
| [  networkPlace.Look = [\"subPanelLook\"];]                                    |
|                                                                                                                                                           |
| [  networkPlace.ExpandImageURL = [\"email.gif\"];]                             |
|                                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                                           |
| [  GroupBarItem viewConnection = [new] GroupBarItem();]                          |
|                                                                                                                                                           |
| [  viewConnection.Text = [\"View network \"];]                                 |
|                                                                                                                                                           |
| [  viewConnection.Look = [\"subPanelLook\"];]                                  |
|                                                                                                                                                           |
| [  viewConnection.ExpandImageURL = [\"publish.gif\"];]                         |
|                                                                                                                                                           |
| [  gbar.Items.Add(networkTasks);]                                                                     |
|                                                                                                                                                           |
| [  networkTasks.Items.Add(networkPlace);]                                                             |
|                                                                                                                                                           |
| [  networkTasks.Items.Add(viewConnection);]                                                           |
|                                                                                                                                                           |
| [}]                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [If][ ([Not] IsPostBack) [Then]]                                  |
|                                                                                                                                                                                                                                  |
| [Dim][ gbar [As] Syncfusion.Web.UI.WebControls.Tools.GroupBar = Groupbar1]             |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  gbar.Width = 175]                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  gbar.DefaultTopItemSpacing = 10]                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  gbar.ControlRootCSSClass = [\"TopGroup\"]]                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  gbar.ExpandSingleGroup = [True]]                                                                                                                     |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [\'create sub items look]                                                                                                                                      |
|                                                                                                                                                                                                                                  |
| [Dim][ subPanel [As] GroupBarItemLook = [New] GroupBarItemLook()] |
|                                                                                                                                                                                                                                  |
| [  subPanel.ID = [\"subPanelLook\"]]                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [  subPanel.TextPaddingLeft = 5]                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [  subPanel.ImageHeight = 16]                                                                                                                                                |
|                                                                                                                                                                                                                                  |
| [  subPanel.ImageWidth = 16]                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [  subPanel.StateDataDefault.ItemCSSClass = [\"DefChild_ItemCss\"]]                                                                                   |
|                                                                                                                                                                                                                                  |
| [  subPanel.StateDataDefault.TextContainerCSSClass = [\"DefChild_TextCont\"]]                                                                         |
|                                                                                                                                                                                                                                  |
| [  subPanel.StateDataHover.ItemCSSClass = [\"HovChild_ItemCss\"]]                                                                                     |
|                                                                                                                                                                                                                                  |
| [  subPanel.StateDataHover.TextContainerCSSClass = [\"HovChild_TextCont\"]]                                                                           |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| [\'create top items look]                                                                                                                                      |
|                                                                                                                                                                                                                                  |
| [Dim][ topItem [As] GroupBarItemLook = [New] GroupBarItemLook()]  |
|                                                                                                                                                                                                                                  |
| [  topItem.ID = [\"topItemLook\"]]                                                                                                                    |
|                                                                                                                                                                                                                                  |
| [  topItem.StateDataDefault.ItemCSSClass = [\"DefRoot_ItemCss\"]]                                                                                     |
|                                                                                                                                                                                                                                  |
| [  topItem.StateDataDefault.TextContainerCSSClass = [\"DefRoot_TextCont\"]]                                                                           |
|                                                                                                                                                                                                                                  |
| [  topItem.StateDataHover.ItemCSSClass = [\"HovRoot_ItemCss\"]]                                                                                       |
|                                                                                                                                                                                                                                  |
| [  topItem.StateDataHover.TextContainerCSSClass = [\"HovRoot_TextCont\"]]                                                                             |
|                                                                                                                                                                                                                                  |
| [  topItem.StateDataExpanded.ItemCSSClass = [\"DefRoot_ItemCss\"]]                                                                                    |
|                                                                                                                                                                                                                                  |
| [  topItem.StateDataExpanded.TextContainerCSSClass = [\"DefRoot_TextCont\"]]                                                                          |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| [\'add item looks to the groupbar]                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [  gbar.ItemLooks.Add(subPanel)]                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [  gbar.ItemLooks.Add(topItem)]                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [\'create groupbar items]                                                                                                                                      |
|                                                                                                                                                                                                                                  |
| [Dim][ networkTasks [As] GroupBarItem = [New] GroupBarItem()]     |
|                                                                                                                                                                                                                                  |
| [  networkTasks.Expanded = [True]]                                                                                                                      |
|                                                                                                                                                                                                                                  |
| [  networkTasks.Text = [\"File and Folder Tasks\"]]                                                                                                   |
|                                                                                                                                                                                                                                  |
| [  networkTasks.ControlSubPanelCSSClass = [\"Level2Group\"]]                                                                                          |
|                                                                                                                                                                                                                                  |
| [  networkTasks.Look = [\"topItemLook\"]]                                                                                                             |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| [Dim][ networkPlace [As] GroupBarItem = [New] GroupBarItem()]     |
|                                                                                                                                                                                                                                  |
| [  networkPlace.Text = [\"Email this folder\'s file\"]]                                                                                               |
|                                                                                                                                                                                                                                  |
| [  networkPlace.Look = [\"subPanelLook\"]]                                                                                                            |
|                                                                                                                                                                                                                                  |
| [  networkPlace.ExpandImageURL = [\"email.gif\"]]                                                                                                     |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| [Dim][ viewConnection [As] GroupBarItem = [New] GroupBarItem()]   |
|                                                                                                                                                                                                                                  |
| [  viewConnection.Text = [\"View network \"]]                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  viewConnection.Look = [\"subPanelLook\"]]                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  viewConnection.ExpandImageURL = [\"publish.gif\"]]                                                                                                 |
|                                                                                                                                                                                                                                  |
| [  gbar.Items.Add(networkTasks)]                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [  networkTasks.Items.Add(networkPlace)]                                                                                                                                     |
|                                                                                                                                                                                                                                  |
| [  networkTasks.Items.Add(viewConnection)]                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [End][ [If]]                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

11.  Build and run the application.

[] 

{border="0"}

**[]** 

Figure 327: Programmatically created GroupBar

[]{#p433} 

[]{#related-topics}

