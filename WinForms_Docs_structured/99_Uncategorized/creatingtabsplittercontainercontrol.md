---
title: creatingtabsplittercontainercontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingtabsplittercontainercontrol.md
created_at: 2025-07-03
---








  









### Creating TabSplitterContainer Control {#creating-tabsplittercontainer-control style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

TabSplitterContainer control can be easily created through designer by just dragging and dropping onto the form.

[] 

{border="0"}

[] 

Figure 1107: TabSplitterContainer in Toolbox

 

We can add primary or secondary pages using the below properties.

[] 

{border="0"}

[] 

Figure 1108: Adding Primary Pages to the Control

 

It can be created programmatically using the below steps.

[] 

1.              Create or open a Windows Forms project.

[] 

2.   Add Syncfusion\'s Tools.Windows and Shared.Base assemblies to the application.

[] 

3.   Add the Syncfusion.Windows.Forms.Tools namespace.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| **[]**                                                                       |
|                                                                                                                                |
| [using][ Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [Imports][ Syncfusion.Windows.Forms.Tools ] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Create and initialize the TabSplitterContainer control and TabSplitterPages.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [private][ Syncfusion.Windows.Forms.Tools.[TabSplitterPage] tabSplitterPage1;]                                       |
|                                                                                                                                                                                                                                |
| [private][ Syncfusion.Windows.Forms.Tools.[TabSplitterPage] tabSplitterPage2;]                                       |
|                                                                                                                                                                                                                                |
| [private][ Syncfusion.Windows.Forms.Tools.[TabSplitterContainer] tabSplitterContainer1;]                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [this][.tabSplitterPage1 = [new] Syncfusion.Windows.Forms.Tools.[TabSplitterPage]();]           |
|                                                                                                                                                                                                                                |
| [this][.tabSplitterPage2 = [new] Syncfusion.Windows.Forms.Tools.[TabSplitterPage]();]           |
|                                                                                                                                                                                                                                |
| [this][.tabSplitterContainer1 = [new] Syncfusion.Windows.Forms.Tools.[TabSplitterContainer]();] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [Private][ tabSplitterPage1 [As] Syncfusion.Windows.Forms.Tools.TabSplitterPage]           |
|                                                                                                                                                                                                      |
| [Private][ tabSplitterPage2 [As] Syncfusion.Windows.Forms.Tools.TabSplitterPage]           |
|                                                                                                                                                                                                      |
| [Private][ tabSplitterContainer1 [As] Syncfusion.Windows.Forms.Tools.TabSplitterContainer] |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [Me][.tabSplitterPage1 = [New] Syncfusion.Windows.Forms.Tools.TabSplitterPage() ]          |
|                                                                                                                                                                                                      |
| [Me][.tabSplitterPage2 = [New] Syncfusion.Windows.Forms.Tools.TabSplitterPage() ]          |
|                                                                                                                                                                                                      |
| [Me][.tabSplitterContainer1 = [New] Syncfusion.Windows.Forms.Tools.TabSplitterContainer()] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Add Splitter pages to the TabSplitterContainer.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [this][.tabSplitterContainer1.PrimaryPages.AddRange([new] Syncfusion.Windows.Forms.Tools.[TabSplitterPage]\[\] {[this].tabSplitterPage1});]   |
|                                                                                                                                                                                                                                                                                                   |
| [this][.tabSplitterContainer1.SecondaryPages.AddRange([new] Syncfusion.Windows.Forms.Tools.[TabSplitterPage]\[\] {[this].tabSplitterPage2});] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [Me][.tabSplitterContainer1.PrimaryPages.AddRange([New] Syncfusion.Windows.Forms.Tools.TabSplitterPage() {[Me].tabSplitterPage1}) ]   |
|                                                                                                                                                                                                                                                                      |
| [Me][.tabSplitterContainer1.SecondaryPages.AddRange([New] Syncfusion.Windows.Forms.Tools.TabSplitterPage() {[Me].tabSplitterPage2}) ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Set the size and location of the control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                                 |
| [this][.tabSplitterContainer2.Location = [new] System.Drawing.[Point](195, 29);] |
|                                                                                                                                                                                                                 |
| [this][.tabSplitterContainer2.Name = [\"tabSplitterContainer1\"];]                                  |
|                                                                                                                                                                                                                 |
| [this][.tabSplitterContainer2.Size = [new] System.Drawing.[Size](300, 250);]     |
|                                                                                                                                                                                                                 |
| [this][.tabSplitterContainer2.SplitterPosition = 50;]                                                                      |
|                                                                                                                                                                                                                 |
| [this][.tabSplitterPage3.Text = [\"Code\"];]                                                        |
|                                                                                                                                                                                                                 |
| [this][.tabSplitterPage4.Text = [\"Design\"];]                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [Me][.tabSplitterContainer2.Location = [New] System.Drawing.Point(195, 29) ] |
|                                                                                                                                                                                        |
| [Me][.tabSplitterContainer2.Name = [\"tabSplitterContainer1\"] ]           |
|                                                                                                                                                                                        |
| [Me][.tabSplitterContainer2.Size = [New] System.Drawing.Size(300, 250) ]     |
|                                                                                                                                                                                        |
| [Me][.tabSplitterContainer2.SplitterPosition = 50 ]                                               |
|                                                                                                                                                                                        |
| [Me][.tabSplitterPage3.Text = [\"Code\"] ]                                 |
|                                                                                                                                                                                        |
| [Me][.tabSplitterPage4.Text = [\"Design\"]]                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Add the control to the form.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| **[]**                                                                                                       |
|                                                                                                                                                                |
| [this][.Controls.Add([this].tabSplitterContainer2);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [Me][.Controls.Add([Me].tabSplitterContainer2)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1109: TabSplitterContainer Control

**[]** 

See Also

[] 

[[Concepts and Features]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Concepts_and_Features_8)[]{.UGHyperlink}

 

 

 

[]{#p947} 

[]{#related-topics}

