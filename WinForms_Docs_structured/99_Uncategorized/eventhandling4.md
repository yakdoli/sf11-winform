---
title: eventhandling4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\eventhandling4.md
created_at: 2025-07-03
---






##### Event Handling {#event-handling style="tab-stops: 0pt"}

Selection Events

**[]** 

The ComboBoxBase fires different events for the different user interaction scenarios. The occurrence and order of the events are tabulated below.

[] 


  ----------------------------------------------- -------------------------------------------------------- ---------------------- ---------------------- ----------------------
  Scenarios                                       SelectionChangedCommitted                                SelectedValueChanged   SelectedIndexChanged   Validating/Validated
  TextArea-Change Selection by Keys               Yes:1                                                    Yes:2                  Yes:3                  No
  TextArea-On AutoComplete                        No                                                       No                     No                     No
  Drop-Down List-Change Selection by Keys         No                                                       Yes:1                  Yes:2                  No
  Drop-Down List-Change Selection by Mouse Move   No                                                       No                     No                     No
  Drop-Down Close by Enter Key                    Yes:1                                                    No                     No                     No
  Drop-Down Close by Escape Key                   No                                                       No                     No                     No
  Drop-Down Close by Click                        Yes:1                                                    Yes:2                  Yes:3                  No
  Losing Focus                                    Yes:2 (in DropDownStyle.DropDown (editable) mode only)   No                     No                     Yes:1
  Changing Text Property in Code                  Yes:1                                                    No                     No                     No
  ----------------------------------------------- -------------------------------------------------------- ---------------------- ---------------------- ----------------------


[] 

[] 

###### []{#p414}[]{#_DropDownCloseOnClick_Event}3.3.5.3.4.1 DropDownCloseOnClick Event {#dropdowncloseonclick-event style="tab-stops: 0pt"}

[] 

This section deals with associating a CheckedListBox and handling the events. After the dropdown had closed, the checked items will be displayed on the dropdown text area. The steps are as follows.

[] 

1.   Create a CheckedListBox and populate it.

[] 

{border="0"}

[] 

Figure 365: Adding String Collection to CheckedListBox Control

[] 

2.   Associate it with the ComboBoxBase control.

[] 

{border="0"}

[] 

Figure 366: Associating CheckedListBox Control as Dropdown for ComboBoxBase

[] 

3.   To avoid the closing of dropdown when we are in checking the items, handle the **DropDownCloseOnClick** event and set **args.Cancel=true**.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [// Avoids the closing of dropdown.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [private void][ comboBoxBase1_DropDownCloseOnClick([object] sender, Syncfusion.Windows.Forms.Tools.MouseClickCancelEventArgs args) ] |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [args.Cancel=[true];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| [\' Avoids the closing of dropdown.]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [Private  Sub][ comboBoxBase1_DropDownCloseOnClick([ByVal] sender [As Object], [ByVal] args [As] Syncfusion.Windows.Forms.Tools.MouseClickCancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                      |
| [args.Cancel=[True]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                      |
| [End Sub]                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Handle **SelectedIndexChanged** event of the CheckedListBox and add the following code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                       |
| [// Sets the corresponding selected text in the ComboBoxBase TextBox.]                                                                              |
|                                                                                                                                                                                                       |
| [private void][ checkedListBox1_SelectedIndexChanged([object] sender, System.EventArgs e) ] |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [comboBoxBase1.TextBox.Text=\"\";]                                                                                                                                |
|                                                                                                                                                                                                       |
| [foreach][([object] s [in] checkedListBox1.CheckedItems ) ]            |
|                                                                                                                                                                                                       |
| [comboBoxBase1.TextBox.Text  += s.ToString();]                                                                                                                    |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [\' Sets the corresponding selected text in the ComboBoxBase TextBox.]                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [Private  Sub][ checkedListBox1_SelectedIndexChanged(ByVal sender [As Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                      |
| [comboBoxBase1.TextBox.Text=\"\"]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                      |
| [Dim][ s [As Object]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [For Each][ s [In] checkedListBox1.CheckedItems]                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [comboBoxBase1.TextBox.Text  += s.ToString()]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [Next]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [End Sub]                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 367: ComboBoxBase with selected options at Run Time

###### []{#p415}3.3.5.3.4.2 DropDown Event {#dropdown-event style="tab-stops: 0pt"}

[] 

In order to place ComboBoxBase within a PopupControlContainer, derive from our PopupControlContainer, override the **OnPopup** method and set the focus to the derived control. This ensures that the derived PopupControlContainer does not lose focus and close prematurely.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [// Derive from PopupControlContainer.]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [public class][ CustomPopupControlContainer : Syncfusion.Windows.Forms.PopupControlContainer\                                                                                                                                 |
| {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [public ][CustomPopupControlContainer()\                                                                                                                                                                                      |
| {\                                                                                                                                                                                                                                                                             |
| }]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                                                                             |
| ][public][ CustomPopupControlContainer(IContainer container):][this][()\ |
| {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [container.Add(][this][);]                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [protected override void][ OnPopup(EventArgs args)]                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [  ][ // Sets focus to the derived control.]                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [base.OnPopup(args);]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [this][.Focus();]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Derive from PopupControlContainer.]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Public Class][ CustomPopupControlContainer ][Inherits][ Syncfusion.Windows.Forms.PopupControlContainer]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Public Sub][ New()\                                                                                                                                                                                                                                                                                                                                                          |
| ][End Sub]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Public Sub][ New(][ByVal][ container ][As][ IContainer) : ][Me][()\ |
| container.Add(][Me][)\                                                                                                                                                                                                                                                                                                      |
| ][End Sub]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Sets focus to the derived control.\                                                                                                                                                                                                                                                                                                                                                                                        |
| ][Protected Overrides Sub][ OnPopup(][ByVal][ args ][As][ EventArgs)\                                                 |
| MyBase.OnPopup(args)\                                                                                                                                                                                                                                                                                                                                                                                                          |
| ][Me][.Focus()\                                                                                                                                                                                                                                                                                                             |
| ][End Sub]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                                                                                                                                                                                                                             |
| End Class]                                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here the specification of the parent-child relationship between the ComboBoxBase\'s popup and the PopupControlContainer is explained with the help of coding.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [private void][ comboBoxBase1_DropDown(][object][ sender, System.EventArgs e)\                                                                                                                  |
| {\                                                                                                                                                                                                                                                                                                                                                  |
|  ]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [/\* Setup the relationship between the ComboBoxBase\'s dropdown and it\'s parent PopupControlContainer, so that the popup will not close when the ComboBoxBase's dropdown is shown \*/]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [this][.comboBoxBase1.PopupContainer.PopupParent = ][this][.popupControlContainer1;\                                                                                                            |
| ][this][.popupControlContainer1.CurrentPopupChild = ][this][.comboBoxBase1.PopupContainer;] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private Sub][ comboBoxBase1_DropDown(][ByVal][ sender ][As Object][,][ ByVal][ e ][As][ System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [ \'Setup the relationship between the ComboBoxBase\'s dropdown and it\'s parent PopupControlContainer, so that the popup will not close when the ComboBoxBase's  dropdown is shown\                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ][\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ][Me][.comboBoxBase1.PopupContainer.PopupParent = ][Me][.popupControlContainer1\                                                                                                                                                                                                                                                                                                                                     |
| ][Me][.popupControlContainer1.CurrentPopupChild = ][Me][.comboBoxBase1.PopupContainer]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [End Sub]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

