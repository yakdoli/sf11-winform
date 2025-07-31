---
title: basiccorefeatures2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\basiccorefeatures2.md
created_at: 2025-07-03
---






#### Basic Core Features {#basic-core-features style="tab-stops: 0pt"}

AutoComplete supports basic core features which are listed below.

[·      ]SelectedIndex--- Used to set and get the index of the selected item.

[·      ]SelectedItem---Used to get which item of the AutoComplete has been selected.

[·      ]SelectedValue---Used to get the value of the selected item, the value of the **SelectedValue** property will be set based on the value of the **SelectedValuePath** property.

[·      ]SelectedValuePath---Used to set the value of the **SelectedValue** property of the AutoComplete.

[·      ]DisplayMemberPath---Used to set the value for the items displayed in the drop-down list.

[·      ]IsDropDownOpen---Used to open or close the Drop-down list by setting its value as True or False.

[·      ]SelectionChanged.

[·      ]TextChanged.

**[]** 

Using Basic Core Features in an Application

In the SelectionChanged event the **SelectedIndex**, **SelectedItem** & **SelectedValue** properties can be used in the application to get these property values. The properties and events listed can be used in the application as mentioned below.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                  |
| [List][\<[String]\> Products = [new] [List]\<[String]\>();] |
|                                                                                                                                                                                                                                                  |
| [Products.Add([\"Diagram\"]);]                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [Products.Add([\"Gauge\"]);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [Products.Add([\"Chart\"]);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [Products.Add([\"Business Intelligence\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [AutoComplete][ autoComplete1 = [new] [AutoComplete]();]                                                    |
|                                                                                                                                                                                                                                                  |
| [autoComplete1.CustomSource = Products;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [autoComplete1.SelectedIndex = 1;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [autoComplete1.IsDropDownOpen = [true];]                                                                                                                                                |
|                                                                                                                                                                                                                                                  |
| [autoComplete1.SelectionChanged += ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [new][ [SelectionChangedEventHandler](autoComplete1_SelectionChanged);]                                                             |
|                                                                                                                                                                                                                                                  |
| [autoComplete1.TextChanged += [new] [PropertyChangedCallback](autoComplete1_TextChanged);]                                                                      |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [void][ autoComplete1_TextChanged([DependencyObject] d, ]                                                                           |
|                                                                                                                                                                                                                                                  |
| [                                   DependencyPropertyChangedEventArgs][ e)]                                                                             |
|                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [      this][.textBlock.Text = [this].autoComplete1.Text;]                                                                             |
|                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [void][ autoComplete1_SelectionChanged([object] sender, ]                                                                              |
|                                                                                                                                                                                                                                                  |
| [                                            [SelectionChangedEventArgs] e)]                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [      [MessageBox].Show([\"SelectedItem: \"] +]                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [      [this].autoComplete1.SelectedItem.ToString()+ [\"\\n\"] + [\"SelectedValue: \"]]                                                 |
|                                                                                                                                                                                                                                                  |
| [      + [this].autoComplete1.SelectedValue.ToString())]                                                                                                                                |
|                                                                                                                                                                                                                                                  |
| [}][]                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for Properties, and Events

Properties[]

Table 1: Properties Table for Basic Features


  ------------------- --------------------------------------------------------- -------------------- -------------- -----------------
  Property            Description                                               Type                 Data Type      Reference links
  SelectedIndex       Gets or sets the SelectedIndex of the AutoComplete.       DependencyProperty   Int(-1)        
  SelectedValue       Gets or sets the SelectedValue of the AutoComplete.       DependencyProperty   Object(null)   
  SelectedItem        Gets or sets the SelectedItem of the AutoComplete.        DependencyProperty   Object(null)   
  SelectedValuePath   Gets or sets the SelectedValuePath of the AutoComplete.   DependencyProperty   String(null)   
  DisplayMemberPath   Gets or sets the DisplayMemberPath of the AutoComplete.   DependencyProperty   String(null)   
  ------------------- --------------------------------------------------------- -------------------- -------------- -----------------


**[]** 

Events

Table 2: Events Table for Basic Features


+------------------+-----------------------------------------------------------------------------------+------------------------------------+-------------------+---------------------------------+
| Event            | Description                                                                       | Arguments                          | Type              | Reference links                 |
+------------------+-----------------------------------------------------------------------------------+------------------------------------+-------------------+-------------------+-------------+
| SelectionChanged |  When the value of SelectedItem property is changed this event will be triggered. | Object,                            | SelectionChangedEventHandler          |             |
|                  |                                                                                   |                                    |                                       |             |
|                  | It cannot be cancelled.                                                           | SelectionChangedEventArgs          |                                       |             |
+------------------+-----------------------------------------------------------------------------------+------------------------------------+---------------------------------------+-------------+
| TextChanged      | When the value of the Text property is changed this event will be triggered.      | DependencyObject,                  | DependencyPropertyChangedCallBack     |             |
|                  |                                                                                   |                                    |                                       |             |
|                  | It cannot be cancelled.                                                           | DependencyPropertyChangedEventArgs |                                       |             |
+==================+===================================================================================+====================================+===================+===================+=============+
|                  |                                                                                   |                                    |                   |                   |             |
+------------------+-----------------------------------------------------------------------------------+------------------------------------+-------------------+-------------------+-------------+


 

Sample Link

WPF Sample Browser-\> Tools -\> Editors -\> AutoComplete Demo

 

[]{#related-topics}

