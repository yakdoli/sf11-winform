---
title: throughcode50.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode50.md
created_at: 2025-07-03
---






#### Through Code {#through-code style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

To create a TabControlAdv programmatically,

[] 

1.     Add the Syncfusion assembly Tools.Windows to your application.

[] 

2.   Add the namespace Syncfusion.Windows.Forms.Tools.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| []                                                                            |
|                                                                                                                                |
| [using][ Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| **[]**                                                                        |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Declare the TabControlAdv and TabPageAdv.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| **[]**                                                                                                      |
|                                                                                                                                                               |
| [private][ Syncfusion.Windows.Forms.Tools.TabControlAdv tabControlAdv1;] |
|                                                                                                                                                               |
| [private][ Syncfusion.Windows.Forms.Tools.TabPageAdv tabPageAdv1;]       |
|                                                                                                                                                               |
| [private][ Syncfusion.Windows.Forms.Tools.TabPageAdv tabPageAdv2;]       |
|                                                                                                                                                               |
| [private][ Syncfusion.Windows.Forms.Tools.TabPageAdv tabPageAdv3;]       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| **[]**                                                                                                                               |
|                                                                                                                                                                                        |
| [Private][ tabControlAdv1 [As] Syncfusion.Windows.Forms.Tools.TabControlAdv] |
|                                                                                                                                                                                        |
| [Private][ tabPageAdv1 [As] Syncfusion.Windows.Forms.Tools.TabPageAdv]       |
|                                                                                                                                                                                        |
| [Private][ tabPageAdv2 [As] Syncfusion.Windows.Forms.Tools.TabPageAdv]       |
|                                                                                                                                                                                        |
| [Private][ tabPageAdv3 [As] Syncfusion.Windows.Forms.Tools.TabPageAdv]       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   The following code creates a TabControlAdv with three tabpages.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [private][ [void] Form1_Load([object] sender, System.EventArgs e)]                                                                          |
|                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [    [//Initialize the tabControlAdv and tabPageAdv]]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabControlAdv1 = [new] TabControlAdv();]                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabPageAdv1 = [new] TabPageAdv();]                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabPageAdv2 = [new] TabPageAdv();]                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabPageAdv3 = [new] TabPageAdv();]                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [    [//Add the TabPageAdv to the TabControlAdv.]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabControlAdv1.Controls.AddRange([new] Control\[\]{[this].tabPageAdv1, [this].tabPageAdv2, [this].tabPageAdv3});] |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [    [//Set the location of the TabContolAdv]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabControlAdv1.Location = [new] Point(16, 24);]                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [    [//Set the text of the TabPageAdv]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabPageAdv1.Text = [\"Tab1\"];]                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabPageAdv2.Text = [\"Tab2\"];]                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [    [this].tabPageAdv3.Text = [\"Tab3\"];]                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [    [//Add the TabControlAdv to your form                ]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [    [this].Controls.AddRange([new] Control\[\] { [this].tabControlAdv1});]                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\'Initialize the tabControlAdv and tabPageAdv]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabControlAdv1 = [New] TabControlAdv()]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabPageAdv1 = [New] TabPageAdv()]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabPageAdv2 = [New] TabPageAdv()]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabPageAdv3 = [New] TabPageAdv()]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\'Add the TabPageAdv to the TabControlAdv.]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabControlAdv1.Controls.AddRange([New] Control() {[Me].tabPageAdv1, [Me].tabPageAdv2, [Me].tabPageAdv3})]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\'Set the location of the TabContolAdv]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabControlAdv1.Location = [New] Point(16, 24)]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\'Set the text of the TabPageAdv]]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabPageAdv1.Text = [\"Tab1\"]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabPageAdv2.Text = [\"Tab2\"]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].tabPageAdv3.Text = [\"Tab3\"]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\'Add the TabControlAdv to your form                ]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Me].Controls.AddRange([New] Control() {[Me].tabControlAdv1})]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[[Through Designer]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Through_Designer_5)[]{.UGHyperlink}

 

 

                                  

 

[]{#related-topics}

