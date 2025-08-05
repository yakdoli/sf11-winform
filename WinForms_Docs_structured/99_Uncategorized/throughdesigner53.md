---
title: throughdesigner53.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner53.md
created_at: 2025-08-05
---






#### Through Designer {#through-designer style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

To create a TabbedMDIManager through designer,

[] 

1.      Drag-and-drop a TabbedMDIManager Control from the ToolBox onto the Form1.

[] 

2.   As soon as the control is dropped, the Form1\'s IsMDIContainer property will be set to True and it changes to an MDIContainer. Also, the AttachedTo property of the TabbedMDIManager will be set to Form1. Add a new Form (Form2) to your application.

[] 

3.   In the Form1_Load event, include the code snippet given below. This calls Form2 that is created and displays it in Form1.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [private][ [void] Form1_Load([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                   |
| [{]                                                                                                                                                           |
|                                                                                                                                                                                                   |
| [Form2 frm = [new] Form2();]                                                                                                             |
|                                                                                                                                                                                                   |
| [frm.MdiParent=[this];]                                                                                                                  |
|                                                                                                                                                                                                   |
| [frm.Show();]                                                                                                                                                 |
|                                                                                                                                                                                                   |
| [}]                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] System.Object, [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ frm As Form2 = [New] Form2]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [frm.MdiParent = [Me]]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [frm.[Show]()]                                                                                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Run the application. You will see Form2 tabbed inside Form1.

[] 

{border="0"}

[] 

Figure 1083: TabbedMDIManager Sample

[] 


{border="0"} Note: The DetachFromMdiContainer method is used to detach an MDIParent from the TabbedMDIManager.


[] 

See Also

[] 

[[Through Code]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Through_Code_6)[]{.UGHyperlink}

 

 

 

[]{#p902} 

[]{#related-topics}

