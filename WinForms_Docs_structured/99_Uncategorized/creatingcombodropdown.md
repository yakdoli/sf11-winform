---
title: creatingcombodropdown.md
original_path: WinForms_Docs/99_Uncategorized/creatingcombodropdown.md
created_at: 2025-08-05
---






##### Creating ComboDropDown[]{#p372} {#creating-combodropdown style="tab-stops: 0pt"}

[] 

In this section, ComboDropDown is used to host TreeView control and this can be achieved in the following ways.

[] 

###### []{#p373}3.3.5.1.2.1 Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

This section will guide you to create a ComboDropDown control through designer and associate a TreeView control as its popup.

 

The below steps will guide you with this.

[] 

1.   Create a new Visual C# application or VB.NET application in Visual Studio .NET.

[] 

{border="0"}

[] 

Figure 330: ComboDropDown in Toolbox

[] 

2.   Drag and drop a ComboDropDown control, TreeView control from the toolbox onto the form.

[] 

{border="0"}

[] 

Figure 331: ComboDropDown and TreeView Control in the Windows Form

[] 

3.   Add nodes to the TreeView control and set HideSelection property to false. The HideSelection property specifies whether the selected tree node remains highlighted even when the tree view has lost the focus.

[] 

{border="0"}

[] 

Figure 332: Setting TreeView Control HideSelection Property

[] 

4.   Now set the ComboDropDown\'s **PopupControl** property to be the above TreeView instance.

[] 

{border="0"}

[] 

Figure 333: Associating TreeView control as Popup of ComboDropDown Control

**[]** 


{border="0"} Note: We can also include code to set up the interaction between the combo and the treeview control. Refer Setting Interaction between ComboDropDown and TreeView.[]


[] 

See also[ ]

[] 

[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

 

###### []{#p374}3.3.5.1.2.2 Through Code {#through-code style="tab-stops: 0pt"}

[] 

Drag and drop the TreeView control which will be used in the drop-down portion of ComboDropDown control.

[] 

1.   Include the required namespace.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| []                                                                                                     |
|                                                                                                                                |
| [using ][Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                                                      |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an instance of the ComboDropDown control class.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                              |
|                                                                                                                                                                                         |
| [private][ Syncfusion.Windows.Forms.Tools.ComboDropDown comboDropDown1;]                           |
|                                                                                                                                                                                         |
| [this][.comboDropDown1=[new] Syncfusion.Windows.Forms.Tools.ComboDropDown();] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                                             |
|                                                                                                                                                                                        |
| [Private][ comboDropDown1 [As] Syncfusion.Windows.Forms.Tools.ComboDropDown] |
|                                                                                                                                                                                        |
| [Me][.comboDropDown1 = [New] Syncfusion.Windows.Forms.Tools.ComboDropDown()] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Add TreeView in the drop-down portion of ComboDropDown. Finally add ComboDropDown to the Form.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                                                       |
|                                                                                                                                                                  |
| [this][.comboDropDown1.PopupControl=[this].treeView1;] |
|                                                                                                                                                                  |
| [this][.Controls.Add([this].comboDropDown1);]          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                                                  |
|                                                                                                                                                             |
| [Me][.comboDropDown1.PopupControl=[Me].treeView1] |
|                                                                                                                                                             |
| [Me][.Controls.Add([Me].comboDropDown1)]          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note:[ ]Refer Setting Interaction between ComboDropDown and TreeView[ ]to set the interaction between the ComboDropDown and Treeview.


[] 

See also

[] 

[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

