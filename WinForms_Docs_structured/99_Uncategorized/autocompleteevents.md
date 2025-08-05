---
title: autocompleteevents.md
original_path: WinForms_Docs/99_Uncategorized/autocompleteevents.md
created_at: 2025-08-05
---






##### AutoComplete Events {#autocomplete-events style="tab-stops: 0pt"}

 

The events of the AutoComplete control are as follows.

[] 


  ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------
  AutoComplete Events                 Description
  BeforeAddItem                       Handled when a new item is about to be added.
  AutoCompleteCustomize               Handled to customize the AutoCompletion.
  AutoCompleteItemBrowsed             Handled when the user selects an item from the list of possible matches when the AutoComplete is set to AutoSuggest.
  AutoCompleteItemSelected Event      Occurs when a new item has been selected by the user when the AutoComplete mode is set to AutoSuggest.
  DropDownClosed                      Occurs when the AutoComplete dropdown is closed.
  DropDownDisplayed                   Occurs when the AutoComplete dropdown is displayed.
  MatchItem[]   Enables you to provide a custom matching routine for the current value in the Edit control.
  PreMatchItem                        Handled before the AutoComplete control performs a matching operation for the current text content of the active Edit control.
  TargetChanging                      Occurs when the target control of the AutoComplete control changes.
  ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------


###### []{#p178}[]{#_AutoCompleteItemSelected_Event}3.3.1.1.4.1 AutoCompleteItemSelected Event {#autocompleteitemselected-event style="tab-stops: 0pt"}

[] 

AutoCompleteItemSelected Event is raised, when a new item has been selected by the user when the AutoComplete mode is set to AutoSuggest.

[] 

[This event is discussed in ]External DataSource[ topic.]

###### []{#_BeforeAddItem_Event}3.3.1.1.4.2 BeforeAddItem Event {#beforeadditem-event style="tab-stops: 0pt"}

[]{#p179}[] 

This event will be raised when new item is about to be added. New items can be added by calling AutoComplete.AddHistoryItem() method. The event handler receives an argument of type AutoCompleteAddItemCancelEventArgs containing data related to this event. The following are the properties associated with AutoCompleteAddItemCancelEventArgs argument.

[] 


  ------------------ -------------------------------------------------------------------------------------------------------
   Members           Description
  Cancel             Gets/Sets a value indicating whether the event should be canceled.
  ImageColumnIndex   Gets/Sets the ColumnIndex into the AutoComplete.ImageList property.
  RowItem            It is the System.Data.DataRow object that contains the value that is to be added to the history list.
  ------------------ -------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [private][ [void] autoComplete1_BeforeAddItem([object] sender, [AutoCompleteAddItemCancelEventArgs] e)] |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [//Cancels the item that is going to be added.]                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [    e.Cancel = [true];]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] autoComplete1_BeforeAddItem([ByVal] sender [As] [Object], [ByVal] e [As] AutoCompleteAddItemCancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [\'Cancels the item that is going to be added.][   ]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                   |
| [   e.Cancel = [True]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p180}[]{#_AutoCompleteItemBrowsed_Event}3.3.1.1.4.3 AutoCompleteItemBrowsed Event {#autocompleteitembrowsed-event style="tab-stops: 0pt"}

[] 

This event will be raised when the user selects an item from the list of possible matches when the AutoComplete is set to AutoSuggest. The event handler receives an argument of type AutoCompleteItemEventArgs. The event properties associated with the AutoCompleteItemEventArgs are as follows.

[] 


  ------------------ ---------------------------------------------------------------------------------------------------------------------------
  Members            Description
  SelectedValue      Gets/Sets the value selected.
  Handled            Specifies whether SelectedValue should be applied to target control. This can be used only with AutoCompleteItemSelected.
  ItemArray          Returns AutoComplete item as an object array.
  MatchColumnIndex   Returns the index of the item that was used for matching.
  ------------------ ---------------------------------------------------------------------------------------------------------------------------


[] 

When the user selects an item from the list of possible matches when the AutoComplete is set to AutoSuggest, we can display the selected URL in separate TextBox. The following code illustrate this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [private][ [void] autoComplete1_AutoCompleteItemBrowsed([object] sender, Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs args)] |
|                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [string][ itemText = args.ItemArray\[0\].ToString();]                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [string][ eventlogmessage = String.Format(\"Event: {0} Item: {1}\\r\\n\", \"AutoCompleteItemSelected\", itemText);]                                                                |
|                                                                                                                                                                                                                                                                         |
| [textBox1.Text = textBox1.Text + eventlogmessage;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] autoComplete1_AutoCompleteItemBrowsed([ByVal] sender [As] [Object], [ByVal] args [As] Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    [Dim] itemText [As] [String] = args.ItemArray(0).ToString()]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    [Dim] eventlogmessage [As] [String] = \[String\].Format([\"Event: {0} Item: {1}\"] & Chr(13) & [\"\"] & Chr(10) & [\"\"], [\"AutoCompleteItemSelected\"], itemText)]             |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    textBox1.Text = textBox1.Text + eventlogmessage]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p181}[]{#_MatchItem_Event}3.3.1.1.4.4 MatchItem Event {#matchitem-event style="tab-stops: 0pt"}

[] 

We can override the default matching of the current content of the target edit control using this event. The event handler receives an argument of type AutoCompleteMatchItemEventArgs. The following are the properties associated with AutoCompleteMatchItemEventArgs argument.

[] 


  --------------- -------------------------------------------------------------------------------------------------------------------------------------
   Members        Description
  Cancel          Gets/Sets a value indicating whether the event should be canceled.
  CurrentText     Returns the current text value to be matched.
  PossibleMatch   Returns the possible match value that needs to be compared against AutoCompleteMatchItemEventArgs.CurrentText by the event handler.
  --------------- -------------------------------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [private][ [void] autoComplete1_MatchItem([object] sender, [AutoCompleteMatchItemEventArgs] args)] |
|                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [   //Cancels the match operation]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [   e.Cancel = [true];]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] autoComplete1_MatchItem([ByVal] sender [As] [Object], [ByVal] args [As] [AutoCompleteMatchItemEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [   [//Cancels the match operation]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [   e.Cancel = [true];]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

