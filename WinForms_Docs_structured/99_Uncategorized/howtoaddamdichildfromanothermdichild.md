---
title: howtoaddamdichildfromanothermdichild.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaddamdichildfromanothermdichild.md
created_at: 2025-07-03
---






#### How to add a MDI Child from another MDIChild {#how-to-add-a-mdi-child-from-another-mdichild style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

You should set the MDIParent of the new child form as follows:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                                                        |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                          |
| [private][ [void] buttonAdv1_Click([object] sender, System.EventArgs e) ] |
|                                                                                                                                                                                                          |
| [{ ]                                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [Form3 child1 = [new] Form3(); ]                                                                                                                |
|                                                                                                                                                                                                          |
| [// Set the new form\'s MDIParent to the main form. ]                                                                                                  |
|                                                                                                                                                                                                          |
| [child1.MdiParent = (Form1) [this].Parent.Parent; ]                                                                                             |
|                                                                                                                                                                                                          |
| [child1.Text = [\"Document\"]; ]                                                                                                              |
|                                                                                                                                                                                                          |
| [child1.Show(); ]                                                                                                                                                    |
|                                                                                                                                                                                                          |
| [} ]                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] buttonAdv1_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] buttonAdv1.Click] |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ f1 [As] Form3 = [New] Form3()]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Set the new form\'s MDIParent to the main form. ]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [f1.MdiParent = [CType]([Me].Parent.Parent, Form1)]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [f1.Text = [\"Document\"]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [f1.Show()]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p932} 

[]{#related-topics}

