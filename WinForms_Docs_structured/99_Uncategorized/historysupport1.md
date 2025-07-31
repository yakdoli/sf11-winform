---
title: historysupport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\historysupport1.md
created_at: 2025-07-03
---






#### History Support {#history-support style="tab-stops: 0pt"}

History support in AutoComplete means, reusage of the items which are already used in the AutoComplete textbox. AutoComplete allows you to enable this history support by setting the value of the **IsHistory** property to True. AutoComplete guides you to select an item from the list of items which are added to the history, by using the drop-down button to open the drop-down list.

 

.Using History Support in an Application

Items can be added to the history using the **AddToHistory(String str)** and **AddToHistory(Object obj)** methods, only if that items are present in the data source used with the AutoComplete. Also it supports to save the history while closing the application and to load the history while opening the application using the **SaveHistory()** and **LoadHistory()** methods.

The below mentioned code snippet can be used to attain these functionalities.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [AutoComplete][ autoComplete1 = [new] [AutoComplete]();][]                                                      |
|                                                                                                                                                                                                                                                                                    |
| [autoComplete1][.Loaded += [new] [RoutedEventHandler]]                                                                                                        |
|                                                                                                                                                                                                                                                                                    |
| [(][autoComplete1][\_Loaded);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [void][ ][autoComplete1][\_Loaded([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
| [            [if] (][autoComplete1][!= [null])]                                                                              |
|                                                                                                                                                                                                                                                                                    |
| [                ][autoComplete1][.LoadHistory();]                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [autoComplete1][.SelectionChanged +=]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [   new][ [SelectionChangedEventHandler](][autoComplete1][\_SelectionChanged);]               |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [private][ [void] ][autoComplete1][\_SelectionChanged([object] sender, ]    |
|                                                                                                                                                                                                                                                                                    |
| [                                             [SelectionChangedEventArgs] e)]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
| [     ][autoComplete1][.AddHistory(][autoComplete1][.SelectedItem);]              |
|                                                                                                                                                                                                                                                                                    |
| [     ][autoComplete1][.SaveHistory();]                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [        }][]                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for properties, methods, and events

Properties

Table 14: Property Table for History support


  ----------- ---------------------------------------------------------- -------------------- ------------ -----------------
  Property    Description                                                Type                 Data Type    Reference links
  IsHistory   Gets or sets the value of IsHistory of the AutoComplete.   DependencyProperty   bool(true)   
  ----------- ---------------------------------------------------------- -------------------- ------------ -----------------


**[]** 

Methods

Table 15: MethodsTable for History


+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------+-------------+-----------------+
| Method            | Description                                                                                                                                                                                                     | Parameters                                                  | Type      | Return Type | Reference links |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------+-------------+-----------------+
| AddHistory()      | It should be called to add an item to the history.                                                                                                                                                              | (String str)                                                | NA.       | Void        |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | It can be called at any time.                                                                                                                                                                                   |                                                             |           |             |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | This method will add an input string to the history list if IsHistoryEnabled property is set as True and these items will only be displayed in the History list which can be opened using the drop-down button. | The input string must be there in the linked Custom Source. |           |             |                 |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------+-------------+-----------------+
| AddHistory()      | It should be called to add the item to history.                                                                                                                                                                 | (Object obj)                                                | NA.       | Void        |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | It can be called at any time.                                                                                                                                                                                   |                                                             |           |             |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | This method will add an input object to the history list if IsHistoryEnabled property is set as Ture and these items will only be displayed in the History list which can be opened using the drop-down button. | The input object must be there in the linked Custom Source. |           |             |                 |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------+-------------+-----------------+
| SaveHistory()     | It should be called if you want to save the history before closing the application.                                                                                                                             |                                                             | NA        | Void        |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | It can be called while closing the application.                                                                                                                                                                 |                                                             |           |             |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | This method will save the History list in an isolated storage.                                                                                                                                                  |                                                             |           |             |                 |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------+-------------+-----------------+
| LoadHistory()     | It should be called if you want to load the history while loading the application which is already saved.                                                                                                       |                                                             | NA        | Void        |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | It can be called while loading the application.                                                                                                                                                                 |                                                             |           |             |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | This method will load the history list from an isolated storage to be used in the application.                                                                                                                  |                                                             |           |             |                 |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------+-------------+-----------------+
| ClearAllHistory() | This should be called if you want to clear all the saved history.                                                                                                                                               |                                                             | NA        | Void        |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | It can be called at any time.                                                                                                                                                                                   |                                                             |           |             |                 |
|                   |                                                                                                                                                                                                                 |                                                             |           |             |                 |
|                   | This method will clear the entire history list loaded from an isolated storage.                                                                                                                                 |                                                             |           |             |                 |
+===================+=================================================================================================================================================================================================================+=============================================================+===========+=============+=================+


 

 

Sample Link

WPF Sample Browser-\> Tools -\> Editors -\> AutoComplete Demo

 

[]{#related-topics}

