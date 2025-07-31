---
title: eventhandling5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\eventhandling5.md
created_at: 2025-07-03
---






##### Event Handling {#event-handling style="tab-stops: 0pt"}

[] 

The events of ComboBoxAdv present in the MultiColumnComboBox.

[] 

Selection Events

[] 

The MultiColumnComboBox fires different events for the different user interaction scenarios. The occurrence and order of the events are tabulated below:

[] 


  ----------------------------------------------- -------------------------------------------------------- ------------------------ ------------------------ ----------------------
  Scenarios                                       Selection Changed Committed                              Selected Value Changed   Selected Index Changed   Validating/Validated
  TextArea-Change Selection by Keys               Yes:1                                                    Yes:2                    Yes:3                    No
  TextArea-On AutoComplete                        No                                                       No                       No                       No
  Drop-Down List-Change Selection by Keys         No                                                       Yes:1                    Yes:2                    No
  Drop-Down List-Change Selection by Mouse Move   No                                                       No                       No                       No
  Drop-Down Close by Enter Key                    Yes:1                                                    No                       No                       No
  Drop-Down Close by Escape Key                   No                                                       No                       No                       No
  Drop-Down Close by Click                        Yes:1                                                    Yes:2                    Yes:3                    No
  Losing Focus                                    Yes:2 (in DropDownStyle.DropDown (editable) mode only)   No                       No                       Yes:1
  Changing Text Property in Code                  Yes:1                                                    No                       No                       No
  ----------------------------------------------- -------------------------------------------------------- ------------------------ ------------------------ ----------------------


[] 

You can refer the following topics which gives you an idea on implementing the above events.

[] 

[[·      ]]{.UGHyperlink}[How to display multiple members in a MultiColumnComboBox?]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[How to retrieve the columns other than Display and Value members in a MultiColumnComboBox?]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p427}[]{#_SelectedValueChanged_Event}3.3.5.4.4.1 SelectedValueChanged Event {#selectedvaluechanged-event style="tab-stops: 0pt"}

[] 

This event is handled when the selected value is changed in the combobox. This section discusses a use case illustrating the event.

[] 

Setting Text According to Selection

[] 

The process of accessing the selected item is a complex one. We need to access DataRowView from the control and then to get the values. Include the below code in the **SelectedValueChanged** event handler to set the text of MultiColumnComboBox to the text in the first column of the selected row.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [private void][ multiColumnComboBox1_SelectedValueChanged(object sender, System.EventArgs e) ]                                 |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [ComboBoxBaseDataBound c=multiColumnComboBox1 ][as][ ComboBoxBaseDataBound;] |
|                                                                                                                                                                                                                                   |
| [if ][(c.SelectedIndex!=-1)        ]                                                                                           |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [       // Sets the text of MultiColumnComboBox to the text in the first column of selected row.]                                                                               |
|                                                                                                                                                                                                                                   |
| [       DataRowView drv=c.Items\[c.SelectedIndex\] ][as][ DataRowView;]      |
|                                                                                                                                                                                                                                   |
| [       c.Text=drv.Row\[1\].ToString();]                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private Sub][ multiColumnComboBox1_SelectedValueChanged(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ System.EventArgs) ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ c ][As][ ComboBoxBaseDataBound = ][CType][(multiColumnComboBox1, ComboBoxBaseDataBound) ]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [If Not][ (c.SelectedIndex = -1) ][Then][ ]                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [       \' Sets the text of MultiColumnComboBox to the text in the first column of selected row.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [       Dim][ drv ][As][ DataRowView = ][CType][(c.Items(c.SelectedIndex), DataRowView) ]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [       c.Text = drv.Row(1).ToString ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End If ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End Sub]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 376: Second Column Value of the Selected Row Displayed in the ComboBox

###### []{#p428}[]{#_SelectedIndexChanged_Event}3.3.5.4.4.2 SelectedIndexChanged Event {#selectedindexchanged-event style="tab-stops: 0pt"}

[] 

[This event is illustrated in ]How to retrieve the columns other than Display and Value members in a MultiColumnComboBox?[ topic.]

[]{#related-topics}

