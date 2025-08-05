---
title: throughcode11.md
original_path: WinForms_Docs/99_Uncategorized/throughcode11.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The TreeView provides a rich and flexible server side API which allows you to easily populate the treeview. To add nodes programmatically, follow the below steps.

[] 

1.   To the application, add TreeView control.

42.  In .cs file, include the following directives.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                     |
| **[]**                                                                                                          |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI.WebControls.Tools;] |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI;]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                                      |
| **[]**                                                                                                           |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI.WebControls.Tools] |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI]                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

43.  Create an instance of the TreeView and add it to the form. Then create nodes, sub-nodes, and add it as child to the root node.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [Syncfusion.Web.UI.WebControls.Tools.[TreeView] tree = [new] Syncfusion.Web.UI.WebControls.Tools.[TreeView]();] |
|                                                                                                                                                                                                                                    |
| [form1.Controls.Add(tree);]                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [TreeViewNode][ rootNode = [new] [TreeViewNode]();]                 |
|                                                                                                                                                                                                                                    |
| [rootNode.Text = [\"MailBox\"];]                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [rootNode.Expanded = [true];]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [rootNode.ImagePath = [\"root.gif\"];]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [rootNode.Look = [\"look\"];]                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [tree.Items.Add(rootNode);]                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [TreeViewNode][ firstChild = [new] [TreeViewNode]();]               |
|                                                                                                                                                                                                                                    |
| [firstChild.Text = [\"Calendar\"];]                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [firstChild.ImagePath = [\"calendar.gif\"];]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [firstChild.Look = [\"look\"];]                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [rootNode.Items.Add(firstChild);]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [TreeViewNode][ secondChild = [new] [TreeViewNode]();]              |
|                                                                                                                                                                                                                                    |
| [secondChild.Text = [\"DeletedItems\"];]                                                                                                                |
|                                                                                                                                                                                                                                    |
| [secondChild.ImagePath = [\"deleted.gif\"];]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [secondChild.Look = [\"look\"];]                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [rootNode.Items.Add(secondChild);]                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [TreeViewNode][ secondChildSubNodes = [new] [TreeViewNode]();]      |
|                                                                                                                                                                                                                                    |
| [secondChildSubNodes.ImagePath = [\"folder.gif\"];]                                                                                                     |
|                                                                                                                                                                                                                                    |
| [secondChildSubNodes.Text = [\"Folder1\"];]                                                                                                             |
|                                                                                                                                                                                                                                    |
| [secondChildSubNodes.Look = [\"look\"];]                                                                                                                |
|                                                                                                                                                                                                                                    |
| [secondChild.Items.Add(secondChildSubNodes);]                                                                                                                                  |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [secondChildSubNodes = [new] [TreeViewNode]();]                                                                                      |
|                                                                                                                                                                                                                                    |
| [secondChildSubNodes.ImagePath = [\"folder.gif\"];]                                                                                                     |
|                                                                                                                                                                                                                                    |
| [secondChildSubNodes.Text = [\"Folder2\"];]                                                                                                             |
|                                                                                                                                                                                                                                    |
| [secondChildSubNodes.Look = [\"look\"];]                                                                                                                |
|                                                                                                                                                                                                                                    |
| [secondChild.Items.Add(secondChildSubNodes);]                                                                                                                                  |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [TreeViewNode][ thirdChild = [new] [TreeViewNode]();]               |
|                                                                                                                                                                                                                                    |
| [thirdChild.ImagePath = [\"inbox.gif\"];]                                                                                                               |
|                                                                                                                                                                                                                                    |
| [thirdChild.Text = [\"Inbox\"];]                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [thirdChild.ShowCheckBox = [true];]                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [thirdChild.Look = [\"look\"];]                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [rootNode.Items.Add(thirdChild);]                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                          |
| [Private][ tree [As] Syncfusion.Web.UI.WebControls.Tools.TreeView = [New] Syncfusion.Web.UI.WebControls.Tools.TreeView()] |
|                                                                                                                                                                                                                                                                                          |
| [form1.Controls.Add(tree)]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Private][ rootNode [As] TreeViewNode = [New] TreeViewNode()]                                                             |
|                                                                                                                                                                                                                                                                                          |
| [Private][ rootNode.Text = [\"MailBox\"]]                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| [Private][ rootNode.Expanded = [True]]                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| [Private][ rootNode.ImagePath = [\"root.gif\"]]                                                                                              |
|                                                                                                                                                                                                                                                                                          |
| [Private][ rootNode.Look = [\"look\"]]                                                                                                       |
|                                                                                                                                                                                                                                                                                          |
| [tree.Items.Add(rootNode)]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Private][ firstChild [As] TreeViewNode = [New] TreeViewNode()]                                                           |
|                                                                                                                                                                                                                                                                                          |
| [Private][ firstChild.Text = [\"Calendar\"]]                                                                                                 |
|                                                                                                                                                                                                                                                                                          |
| [Private][ firstChild.ImagePath = [\"calendar.gif\"]]                                                                                        |
|                                                                                                                                                                                                                                                                                          |
| [Private][ firstChild.Look = [\"look\"]]                                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| [rootNode.Items.Add(firstChild)]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChild [As] TreeViewNode = [New] TreeViewNode()]                                                          |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChild.Text = [\"DeletedItems\"]]                                                                                            |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChild.ImagePath = [\"deleted.gif\"]]                                                                                        |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChild.Look = [\"look\"]]                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| [rootNode.Items.Add(secondChild)]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChildSubNodes [As] TreeViewNode = [New] TreeViewNode()]                                                  |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChildSubNodes.ImagePath = [\"folder.gif\"]]                                                                                 |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChildSubNodes.Text = [\"Folder1\"]]                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChildSubNodes.Look = [\"look\"]]                                                                                            |
|                                                                                                                                                                                                                                                                                          |
| [secondChild.Items.Add(secondChildSubNodes)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChildSubNodes = [New] TreeViewNode()]                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChildSubNodes.ImagePath = [\"folder.gif\"]]                                                                                 |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChildSubNodes.Text = [\"Folder2\"]]                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| [Private][ secondChildSubNodes.Look = [\"look\"]]                                                                                            |
|                                                                                                                                                                                                                                                                                          |
| [secondChild.Items.Add(secondChildSubNodes)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Private][ thirdChild [As] TreeViewNode = [New] TreeViewNode()]                                                           |
|                                                                                                                                                                                                                                                                                          |
| [Private][ thirdChild.ImagePath = [\"inbox.gif\"]]                                                                                           |
|                                                                                                                                                                                                                                                                                          |
| [Private][ thirdChild.Text = [\"Inbox\"]]                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| [Private][ thirdChild.ShowCheckBox = [True]]                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Private][ thirdChild.Look = [\"look\"]]                                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| [rootNode.Items.Add(thirdChild)]                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

44.  Build and run the application. The treeview control with the nodes will be displayed.

 

[]{#related-topics}

