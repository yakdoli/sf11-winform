---
title: howtoreleasethetabfocusfromgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoreleasethetabfocusfromgrid.md
created_at: 2025-07-03
---








  









### How To Release the Tab Focus from Grid {#how-to-release-the-tab-focus-from-grid style="tab-stops: 0pt"}

[] 

When you set the *ActiveControl* variable to *Grid control*, the focus will be on the *Grid control*. This may not allow you to navigate to other controls in the form. To overcome this difficulty, set the *ActiveControl* to the *Grid control*. Then set the *WantTabKey* property to false. This helps you navigate to the other controls in the form.

[] 

The following code illustrates how to release the tab focus from GridGroupingControl:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [private][ [void] FormMain_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                         |
|                                                                                                                                                                                                                         |
| [            [this].ActiveControl = [this].gridGroupingControl1.TableControl;]                                                            |
|                                                                                                                                                                                                                         |
| [            gridGroupingControl1.WantTabKey = [false];]                                                                                                       |
|                                                                                                                                                                                                                         |
| [            [return];]                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] FormMain_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                            |
| [                  [Me].ActiveControl = [Me].gridGroupingControl1.TableControl]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| [                  gridGroupingControl1.WantTabKey = [False]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [                  [Return]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                            |
| [ [End] [Sub]]                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

