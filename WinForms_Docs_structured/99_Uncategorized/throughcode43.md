---
title: throughcode43.md
original_path: WinForms_Docs/99_Uncategorized/throughcode43.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

GroupView control can be created using the **GroupView** class. GroupView Items can be added to the GroupView control using the **GroupView.GroupViewItems collection** property.

[] 

1.   Include the required namespace.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| []                                                                           |
|                                                                                                                                |
| [using][ Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create instances of the GroupView control and GroupView Items.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [private][ Syncfusion.Windows.Forms.Tools.GroupView groupView1;]         |
|                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                               |
| [private][ Syncfusion.Windows.Forms.Tools.GroupViewItem groupViewItem1;] |
|                                                                                                                                                               |
| [private][ Syncfusion.Windows.Forms.Tools.GroupViewItem groupViewItem2;] |
|                                                                                                                                                               |
| [private][ Syncfusion.Windows.Forms.Tools.GroupViewItem groupViewItem3;] |
|                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                               |
| [this][.groupView1=[new] GroupView();]              |
|                                                                                                                                                               |
| [this][.groupViewItem1=[new] GroupViewItem();]      |
|                                                                                                                                                               |
| [this][.groupViewItem2=[new] GroupViewItem();]      |
|                                                                                                                                                               |
| [this][.groupViewItem3=[new] GroupViewItem();]      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [Private][ groupView1 [As] Syncfusion.Windows.Forms.Tools.GroupView]         |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [Private][ groupViewItem1 [As] Syncfusion.Windows.Forms.Tools.GroupViewItem] |
|                                                                                                                                                                                        |
| [Private][ groupViewItem2 [As] Syncfusion.Windows.Forms.Tools.GroupViewItem] |
|                                                                                                                                                                                        |
| [Private][ groupViewItem3 [As] Syncfusion.Windows.Forms.Tools.GroupViewItem] |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [Me][.groupView1 = [New] GroupView()]                                        |
|                                                                                                                                                                                        |
| [Me][.groupViewItem1 = [New] GroupViewItem()]                                |
|                                                                                                                                                                                        |
| [Me][.groupViewItem2 = [New] GroupViewItem()]                                |
|                                                                                                                                                                                        |
| [Me][.groupViewItem3 = [New] GroupViewItem()]                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Add GroupView Items to the GroupView control and specify the size of the GroupView control. Finally add a GroupView control to the Form.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.groupView2.GroupViewItems.AddRange([new] Syncfusion.Windows.Forms.Tools.[GroupViewItem]\[\] {]                                                                                   |
|                                                                                                                                                                                                                                                                                                                         |
| [new][ Syncfusion.Windows.Forms.Tools.[GroupViewItem]([\"Windows Forms\"], 0, [true], [null], [\"GroupViewItem0\"]),] |
|                                                                                                                                                                                                                                                                                                                         |
| [new][ Syncfusion.Windows.Forms.Tools.[GroupViewItem]([\"Components\"], 1, [true], [null], [\"GroupViewItem1\"]),]    |
|                                                                                                                                                                                                                                                                                                                         |
| [new][ Syncfusion.Windows.Forms.Tools.[GroupViewItem]([\"General\"], 2, [true], [null], [\"GroupViewItem2\"])});]     |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.groupView1.Size=[new] Size(192,120);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.Controls.Add([this].groupView1);]                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.groupView2.GroupViewItems.AddRange([New] Syncfusion.Windows.Forms.Tools.GroupViewItem() {[New] Syncfusion.Windows.Forms.Tools.GroupViewItem([\"Windows Forms\"], 0, [True], [Nothing], [\"GroupViewItem0\"]), [New] Syncfusion.Windows.Forms.Tools.GroupViewItem([\"Components\"], 1, [True], [Nothing], [\"GroupViewItem1\"]), [New] Syncfusion.Windows.Forms.Tools.GroupViewItem([\"General\"], 2, [True], [Nothing], [\"GroupViewItem2\"])})] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.groupView1.Size = [New] Size(192,120)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.Controls.Add([Me].groupView1)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 897: GroupView Items added to the GroupView Control

[] 

See Also

[] 

[[Concepts and Features]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Concepts_and_Features_2)[]{.UGHyperlink}

 

 

[]{#p638} 

[]{#related-topics}

