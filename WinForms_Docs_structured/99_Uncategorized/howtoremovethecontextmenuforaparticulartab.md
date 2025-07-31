---
title: howtoremovethecontextmenuforaparticulartab.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoremovethecontextmenuforaparticulartab.md
created_at: 2025-07-03
---






#### How to remove the Context Menu for a particular tab {#how-to-remove-the-context-menu-for-a-particular-tab style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This can be achieved by handling the **BeforePopup** event of TabbedMDIManager.ContextMenuItem. Before that we should know which tab is currently active. To keep track of this, SelectedIndexChanged event of MDITabPanel can be used.

 

First handle the TabControlAdded event of TabbedMDIManager. Then subscribe to the args.TabControl.SelectedIndexChanged event (where args is the argument passed into this event). In the SelectedIndexChanged event handler, store the SelectedTab in a variable which is accessible by all the methods inside that class. In the BeforePopup event, check for the TabPageAdv and cancel the context menu by setting e.Cancel = true.

 

In this example, we are going to remove context menu for the pages which are having the text as \'New Document\'.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [// Declare the object st to store SelectedTab with enough scope. ]                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [TabPageAdv st =[new] TabPageAdv(); ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [// Handles the TabControlAdded event of TabbedMDIManager. ]                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [void][ tmm_TabControlAdded([object] sender, TabbedMDITabControlEventArgs args) ]                                                       |
|                                                                                                                                                                                                                                                   |
| [{ ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [args.TabControl.SelectedIndexChanged += [new] EventHandler(TabControl_SelectedIndexChanged); ]                                                                                          |
|                                                                                                                                                                                                                                                   |
| [} ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [// Handler for SelectedIndexChanged. ]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [void][ TabControl_SelectedIndexChanged([object] sender, EventArgs e) ]                                                                 |
|                                                                                                                                                                                                                                                   |
| [{ ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [// Store in a temporary variable.  ]                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [st = (sender [as] MDITabPanel).SelectedTab; ]                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [} ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [// Adding handler for the Context Menu Item. ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [tmm.ContextMenuItem.BeforePopup += [new] CancelEventHandler(ContextMenuItem_BeforePopup); ]                                                                                             |
|                                                                                                                                                                                                                                                   |
| [// Handler for BeforePopup event.]                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [void][ ContextMenuItem_BeforePopup([object] sender, CancelEventArgs e)]                                                                |
|                                                                                                                                                                                                                                                   |
| [//][ Cancelling][ if the Title is New Document. ][ ] |
|                                                                                                                                                                                                                                                   |
| [{ ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [if][ (st.Text == [\"New Document\"]) e.Cancel = [true];[ ]]                             |
|                                                                                                                                                                                                                                                   |
| [} ]                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Declare the object st to store SelectedTab with enough scope. ]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ st [As] TabPageAdv]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Handles the TabControlAdded event of TabbedMDIManager. ]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] tmm_TabControlAdded([ByVal] sender [As] [Object], [ByVal] args [As] TabbedMDITabControlEventArgs) [Handles] tmm.TabControlAdded] |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Subscribe to SelectedIndexChanged event. ]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [AddHandler][ args.TabControl.SelectedIndexChanged, [AddressOf] SelectedIndexChanged]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Handler for SelectedIndexChanged. ]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] SelectedIndexChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ mtp [As] MDITabPanel = [CType](sender, MDITabPanel)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Store in a temporary variable.  ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [st = mtp.SelectedTab]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Adding handler for the Context Menu Item. ]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [AddHandler][ tmm.ContextMenuItem.BeforePopup, [AddressOf] tmm_BeforePopup ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Handler for BeforePopup event. ]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] tmm_BeforePopup([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs)]                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Cancelling if the Title is New Document. ]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [If][ st.Text = [\"New Document\"] [Then] e.Cancel = [True]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p938} 

[]{#related-topics}

