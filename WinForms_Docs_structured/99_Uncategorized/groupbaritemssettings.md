---
title: groupbaritemssettings.md
original_path: WinForms_Docs/99_Uncategorized/groupbaritemssettings.md
created_at: 2025-08-05
---






##### GroupBar Items Settings {#groupbar-items-settings style="tab-stops: 0pt"}

[] 

This section discusses the various settings that can be applied to the GroupBar Items of the GroupBar control.

 

It includes the below given topics.

[] 

[] 

 

###### 3.6.1.4.2.1 Text Settings {#text-settings style="tab-stops: 0pt"}

[] 

This section describes how text alignment can be done for the GroupBar Items.

[] 

Through Designer

[] 

The **TextAlign** property specifies the horizontal alignment of the GroupBar Item text[. ]The text can be aligned to the Center, Left and Right. The default alignment is set to Center.

[] 

{border="0"}[]

 

Figure 865: GroupBar with TextAlign = \"Left\"

[] 

Through Code

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [this][.groupBar1.TextAlign = Syncfusion.Windows.Forms.Tools.TextAlignment.Left;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [Me][.groupBar1.TextAlign = Syncfusion.Windows.Forms.Tools.TextAlignment.Left] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In-Place Renaming

[] 

Users are allowed to rename GroupBar Items at run-time using the code snippet given below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                                   |
| []                                                                              |
|                                                                                                                                   |
| [// index: index of the GroupBar Item to be renamed.]                           |
|                                                                                                                                   |
| [this][.groupBar1.InplaceRenameItem(index);] |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                             |
|                                                                                                                                |
| []                                                                           |
|                                                                                                                                |
| [\' index: index of the GroupBar Item to be renamed.]                        |
|                                                                                                                                |
| [Me][.groupBar1.InplaceRenameItem(index)] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

The method associated with this property is given below.

[] 


  ------------------------- -----------------------------------------------
  Method                    Description
  CancelInplaceRenameItem   Cancels an in-place edit that is in progress.
  ------------------------- -----------------------------------------------


 

 

[]{#p601} 

 

###### 3.6.1.4.2.2 Image Settings {#image-settings style="tab-stops: 0pt"}

[] 

This section describes the image settings available for GroupBar Items.

[] 

Large images can be set for GroupBar Items using the following properties.

[] 


  ----------------------- ------------------------------------------------------------------------------------
  GroupBarItem Property   Description
  LargeImageMode          Specifies whether large images can be set for the GroupBar Item\'s client control.
  Image                   Specifies the image for the GroupBar Item\'s client control.
  ----------------------- ------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [this][.groupBarItem1.LargeImageMode = [true];]                                                                                        |
|                                                                                                                                                                                                                                                  |
| [this][.groupBarItem1.Image = ((System.Drawing.Image)(resources.GetObject(\"groupBarItem1.Image\")));   ][            ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [Me][.groupBarItem1.LargeImageMode = [True]]                                                                                        |
|                                                                                                                                                                                                                                               |
| [Me][.groupBarItem1.Image = ([CType](resources.GetObject([\"groupBarItem1.Image\"]), System.Drawing.Image))] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

 

Figure 866: Large Images displayed on the Headers of GroupBar Items

[] 

Users can also display the selected GroupBar Item\'s image on the header of the Stacked GroupBar. This can be achieved by setting the **ShowItemImageInHeader** property to \'True\'.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [this][.groupBar1.ShowItemImageInHeader = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [Me][.groupBar1.ShowItemImageInHeader = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

 

Figure 867: Image displayed on the Header of the Stacked GroupBar

 

 

[]{#p602} 

 

###### 3.6.1.4.2.3 GroupBar Items Customization {#groupbar-items-customization style="tab-stops: 0pt"}

[] 

The following table lists the properties related to the GroupBar Items.

[] 


  ------------------- ------------------------------------------------------------------------------------------------------------------
  GroupBar Property   Description
  BarHighlight        Specifies the value which indicates whether to highlight the GroupBar Item when the mouse cursor hovers over it.
  FlatLook            Specifies whether to draw GroupBar Items with the control\'s borders without a 3-dimensional edge.
  ------------------- ------------------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [this][.groupBar1.BarHighlight = [true];] |
|                                                                                                                                                     |
| [this][.groupBar1.FlatLook = [true];]     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                               |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [Me][.groupBar1.BarHighlight = [True]] |
|                                                                                                                                                  |
| [Me][.groupBar1.FlatLook = [True]]     |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The control provides highlighting effect for the GroupBar Item when the mouse is hovered over it by setting the **BarHighlight** property to \'True\'.

[] 

{border="0"}[]

 

Figure 868: \'Components\' Item Highlighted in the GroupBar

[] 

 The border of the GroupBar Items can be changed by drawing the border without 3-dimensional edge which can be attained by setting the **FlatLook** property to \'True\'.

[] 

{border="0"}[]

 

Figure 869: Flat Look of GroupBar Items

 

 

[]{#p603} 

 

###### 3.6.1.4.2.4 Integrating Child Controls to the GroupBar Items {#integrating-child-controls-to-the-groupbar-items style="tab-stops: 0pt"}

[] 

GroupBar Item can host any control in it\'s client area. To host more than one control, place the controls in the panel and then drop the panel inside the GroupBar Item container.

[] 

In this section, the following controls are added as Child controls to the GroupBar Items.

[] 

[] 

[]{#p604} 

3.6.1.4.2.4.1      TreeView as Child Control

[] 

You can add a TreeView control to the GroupBar by clicking on a particular group say GroupBarItem1 by activating it and then dragging-and-dropping the TreeView control onto the GroupBar\'s client region. You can repeat this process for all groups in the control.

 

Individual GroupBar Item properties such as Text, Image and ForeColor can be set using the **GroupBar Item Collection Editor**. To do this, first select the **GroupBar.GroupBarItems** to bring up the collection editor and select each item to assign the property values.

 

The default GroupBar properties will display the control in the regular mode using the standard visual style. You can now use the property browser to set the appropriate Appearance and Behavior settings to tailor the GroupBar\'s interface to suit the application\'s requirement.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [this][.groupBar1 = [new] Syncfusion.Windows.Forms.Tools.GroupBar();]                  |
|                                                                                                                                                                                                  |
| [this][.groupBarItem1 = [new] Syncfusion.Windows.Forms.Tools.GroupBarItem();]          |
|                                                                                                                                                                                                  |
| [this][.groupBarItem2 = [new] Syncfusion.Windows.Forms.Tools.GroupBarItem();]          |
|                                                                                                                                                                                                  |
| [this][.treeView1 = [new] System.Windows.Forms.TreeView();]                            |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// groupBarItem1 has no client control.]                                                                                                      |
|                                                                                                                                                                                                  |
| [this][.groupBarItem1.Client = [null];]                                                |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// TreeView control attached as a client control to groupBarItem2.]                                                                           |
|                                                                                                                                                                                                  |
| [this][.groupBarItem2.Client = [this].treeView1;]                                      |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// Nodes are added to the TreeView Control.]                                                                                                  |
|                                                                                                                                                                                                  |
| [this][.treeView1.Nodes.AddRange([new] System.Windows.Forms.TreeNode\[\]{treeNode2});] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [Me][.groupBar1 = [New] Syncfusion.Windows.Forms.Tools.GroupBar()]                 |
|                                                                                                                                                                                              |
| [Me][.groupBarItem1 = [New] Syncfusion.Windows.Forms.Tools.GroupBarItem()]         |
|                                                                                                                                                                                              |
| [Me][.groupBarItem2 = [New] Syncfusion.Windows.Forms.Tools.GroupBarItem()]         |
|                                                                                                                                                                                              |
| [Me][.treeView1 = [New] System.Windows.Forms.TreeView()]                           |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\' groupBarItem1 has no client control.]                                                                                                  |
|                                                                                                                                                                                              |
| [Me][.groupBarItem1.Client = [Nothing]]                                            |
|                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                              |
| [\' TreeView control attached as a client control to groupBarItem2.]                                                                       |
|                                                                                                                                                                                              |
| [Me][.groupBarItem2.Client = [Me].treeView1]                                       |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\' Nodes are added to the TreeView Control.]                                                                                              |
|                                                                                                                                                                                              |
| [Me][.treeView1.Nodes.AddRange([New] System.Windows.Forms.TreeNode() {treeNode2})] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

 

Figure 870: Adding a TreeView Control to the GroupBar

[] 

{border="0"}

[] 

Figure 871: TreeView Control added to GroupBarItem1

 

 

 

[]{#p605} 

 

3.6.1.4.2.4.2      GroupView as Child Control

[] 

GroupView control can be added as a Child control to the GroupBar Item by dragging-and-dropping the control onto the GroupBar\'s client region and adding GroupView Items using the **GroupView Item Collection Editor**.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [this][.groupBar1 = [new] Syncfusion.Windows.Forms.Tools.GroupBar();]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                      |
| [this][.groupBarItem1 = [new] Syncfusion.Windows.Forms.Tools.GroupBarItem();]                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [this][.groupBarItem2 = [new] Syncfusion.Windows.Forms.Tools.GroupBarItem();]                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [this][.groupView1 = [new] Syncfusion.Windows.Forms.Tools.GroupView();]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                      |
| [                   ]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                      |
| [// groupBarItem1 has no client control.]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [this][.groupBarItem1.Client = [null];]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [// GroupView control attached as a client control to groupBarItem2.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [this][.groupBarItem2.Client = [this].groupView1;]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [// Items are added to the GroupView Control and their text is edited.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                      |
| [this][.groupView1.GroupViewItems.AddRange([new] Syncfusion.Windows.Forms.Tools.GroupViewItem\[\] {]                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [new][ Syncfusion.Windows.Forms.Tools.GroupViewItem([\"GroupViewItem0\"], -1, [true], [null], [\"GroupViewItem0\"]),]   |
|                                                                                                                                                                                                                                                                                                      |
| [new][ Syncfusion.Windows.Forms.Tools.GroupViewItem([\"GroupViewItem1\"], -1, [true], [null], [\"GroupViewItem1\"])});] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.groupBar1 = [New] Syncfusion.Windows.Forms.Tools.GroupBar()]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.groupBarItem1 = [New] Syncfusion.Windows.Forms.Tools.GroupBarItem()]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.groupBarItem2 = [New] Syncfusion.Windows.Forms.Tools.GroupBarItem()]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.groupView1 = [New] Syncfusion.Windows.Forms.Tools.GroupView()]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' groupBarItem1 has no client control. ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.groupBarItem1.Client = [Nothing]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' GroupView control attached as a client control to groupBarItem2.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.groupBarItem2.Client = [Me].groupView1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Items are added to the GroupView Control and their text is edited.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.groupView1.GroupViewItems.AddRange([New] Syncfusion.Windows.Forms.Tools.GroupViewItem() {[New] Syncfusion.Windows.Forms.Tools.GroupViewItem([\"GroupViewItem0\"], -1, [True], [Nothing], [\"GroupViewItem0\"]), [New] Syncfusion.Windows.Forms.Tools.GroupViewItem([\"GroupViewItem1\"], -1, [True], [Nothing], [\"GroupViewItem1\"])})] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

 

Figure 872: GroupView control added to the GroupBarItem0

 

 

 

[]{#p606} 

 

3.6.1.4.2.4.3      GroupBar as Child Control

[] 

GroupBar control itself can be placed in the client region of the GroupBar Item. This is called **Nested GroupBar**.

[] 

The following step-by-step procedure helps you to create Nested GroupBars.

[] 

1.   Drag and drop the GroupBar1 control from the toolbox onto the form, add GroupBar Items using the **GroupBar Item Collection Editor**, drag and drop the GroupView control and add GroupView Items using the **GroupView Item Collection Editor**. Associate the GroupView control inside the client area of the GroupBar Item.

[] 

The below screen shot shows the GroupBar with four GroupBar Items named as Windows Forms, Components, General and Nested GroupBar.

[] 

{border="0"}[]

 

Figure 873: GroupBar1 with Four GroupBar Items

[] 

2.   Drag and drop another GroupBar2 control from the toolbox and add the GroupBar Items (Personal, Work and Contacts) using the **GroupBar Item Collection Editor** and add the GroupView control with GroupView Items (Vendors, Metrics, Trend, Sales and Sales 2 for the GroupBar Item Work) to each GroupBar Item using the **GroupView Item Collection Editor**.

[] 

{border="0"}[]

 

Figure 874: GroupBar2 with Three GroupBar Items

[] 

3.   Add GroupBar2 as child control to the GroupBar1 by doing a drag and drop operation.

[] 

{border="0"}[]

 

Figure 875: Adding GroupBar2 as Child Control to GroupBar1

[] 

The following screen shot shows the Nested GroupBars.

[] 

{border="0"}[]

 

Figure 876: Nested GroupBars

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [this][.groupBar1 = [new] Syncfusion.Windows.Forms.Tools.GroupBar();]                             |
|                                                                                                                                                                                                             |
| [this][.groupBarItem1 = [new] Syncfusion.Windows.Forms.Tools.GroupBarItem();]                     |
|                                                                                                                                                                                                             |
| [this][.groupBarItem2 = [new] Syncfusion.Windows.Forms.Tools.GroupBarItem();]                     |
|                                                                                                                                                                                                             |
| [this][.groupBar2 = [new] Syncfusion.Windows.Forms.Tools.GroupBar();]                             |
|                                                                                                                                                                                                             |
| [this][.groupBarItem3 = [new] Syncfusion.Windows.Forms.Tools.GroupBarItem();]                     |
|                                                                                                                                                                                                             |
| [this][.groupBarItem4 = [new] Syncfusion.Windows.Forms.Tools.GroupBarItem();]                     |
|                                                                                                                                                                                                             |
| [         ]                                                                                                                                                             |
|                                                                                                                                                                                                             |
| [// groupBarItem1 has no client control.]                                                                                                                 |
|                                                                                                                                                                                                             |
| [this][.groupBarItem1.Client = [null];]                                                           |
|                                                                                                                                                                                                             |
| [            ]                                                                                                                                                          |
|                                                                                                                                                                                                             |
| [// GroupBar control attached as a client control to groupBarItem2.]                                                                                      |
|                                                                                                                                                                                                             |
| [this][.groupBarItem2.Client = [this].groupBar2;]                                                 |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [// Items are added to the GroupBar Control.]                                                                                                             |
|                                                                                                                                                                                                             |
| [this][.groupBar2.GroupBarItems.AddRange([new] Syncfusion.Windows.Forms.Tools.GroupBarItem\[\] {] |
|                                                                                                                                                                                                             |
| [this][.groupBarItem3,]                                                                                                |
|                                                                                                                                                                                                             |
| [this][.groupBarItem4});]                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBar1 = [New] Syncfusion.Windows.Forms.Tools.GroupBar()]                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBarItem1 = [New] Syncfusion.Windows.Forms.Tools.GroupBarItem()]                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBarItem2 = [New] Syncfusion.Windows.Forms.Tools.GroupBarItem()]                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBar2 = [New] Syncfusion.Windows.Forms.Tools.GroupBar()]                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBarItem3 = [New] Syncfusion.Windows.Forms.Tools.GroupBarItem()]                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBarItem4 = [New] Syncfusion.Windows.Forms.Tools.GroupBarItem()]                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [     ]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [\' groupBarItem1 has no client control.]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBarItem1.Client = [Nothing]]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [\' GroupBar control attached as a client control to groupBarItem2.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBarItem2.Client = [Me].groupBar2]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [\' Items are added to the GroupBar Control.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [Me][.groupBar2.GroupBarItems.AddRange([New] Syncfusion.Windows.Forms.Tools.GroupBarItem() {[Me].groupBarItem3, [Me].groupBarItem4})] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p607} 

 

###### 3.6.1.4.2.5 GroupBarItem Popup {#groupbaritem-popup style="tab-stops: 0pt"}

[] 

The below properties controls the appearance and behavior of the GroupBarItem popup.

[] 


  ------------------- --------------------------------------------------------------------------------------
  GroupBar Property   Description
  PopupAutoClose      Indicates whether popup is closed after clicking an item.
  PopupClientSize     Indicates the initial size of the popup for the GroupBarItem client.
  PopupResizeMode     Gets or sets the popup\'s resize mode. It can be horizontal, vertical, Both or None.
  ShowPopupGripper    Specifies whether to show or hide the popup gripper.
  ------------------- --------------------------------------------------------------------------------------


[] 

[] 


  ------------------- ------------------------------------------
  GroupBar Property   Description
  HidePopup           Calling this method will hide the popup.
  ------------------- ------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [this][.groupBar1.PopupClientSize = [new] System.Drawing.[Size](5, 6);]    |
|                                                                                                                                                                                                           |
| [this][.groupBar1.PopupResizeMode = Syncfusion.Windows.Forms.Tools.[PopupResizeMode].Vertical;] |
|                                                                                                                                                                                                           |
| [this][.groupBar1.PopupAutoClose = [true];]                                                     |
|                                                                                                                                                                                                           |
| [this][.groupBar1.ShowPopupGripper = [true];]                                                   |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [this][.groupBar1.HidePopup();]                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [Me][.groupBar1.PopupClientSize = [New] System.Drawing.Size(5, 6) ]    |
|                                                                                                                                                                                  |
| [Me][.groupBar1.PopupResizeMode = Syncfusion.Windows.Forms.Tools.PopupResizeMode.Vertical ] |
|                                                                                                                                                                                  |
| [Me][.groupBar1.PopupAutoClose = [True] ]                              |
|                                                                                                                                                                                  |
| [Me][.groupBar1.ShowPopupGripper = [True] ]                            |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [Me][.groupBar1.HidePopup()]                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p608} 

 

[]{#related-topics}

