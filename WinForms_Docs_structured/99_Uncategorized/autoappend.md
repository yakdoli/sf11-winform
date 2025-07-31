---
title: autoappend.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\autoappend.md
created_at: 2025-07-03
---






##### AutoAppend {#autoappend style="tab-stops: 0pt"}

[] 

**Combo box controls** are commonly used to select from a particular value from a list of items. In several instances, the developer is not aware of the contents of the combo box before the application is being used.

 

For instance, in an FTP client application, if the user is allowed to enter the FTP address of the servers in a combo box, it is not possible to provide a complete list of all possible FTP servers. When the user enters a FTP server into a combo box, the value is lost unless the developer writes additional code to persist the user entries in the registry or in a file. Also, at initialization, the combo box should be reinitialized with the saved items from the registry or file into which the values were saved.

 

The **AutoAppend** class provides auto persisting of previously entered items in a Windows Forms combo box based on a category keyword and also populates the combo box control\'s items collection with the persisted list.

 

The AutoAppend class provides this service for any combo box control without the developer having to write any code for the persisting and reading of the values.

 

The following screen shot illustrates the usage of the AutoAppend class to persist items previously entered in a combo box and add them to the items collection of the combo box.

**[]** 

{border="0"}

Figure 144: AutoAppend functionality at RunTime

**[]** 

 

###### []{#p203}3.3.1.2.4.1 Features {#features style="tab-stops: 0pt"}

 

AutoAppend provides an auto persisting of previously entered items in a Windows Forms combo box based on a category keyword and also populates the combo box control\'s items collection with the persisted list. It has following features.

[] 

[·      ]New entries can be added to control\'s AutoAppend list programmatically.

[[·      ]]{.MsoHyperlink}It can be used with AutoComplete control.[[]]{.MsoHyperlink}

 

###### []{#p204}[]{#_Associating_AutoAppend_with}3.3.1.2.4.2 Associating AutoAppend with a control {#associating-autoappend-with-a-control style="tab-stops: 0pt"}

[] 

We can associate AutoAppend class to a ComboBox control by following the below steps.

[] 

1.   Open a Visual Studio project and include the required namespace.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                              |
| []                                                                                         |
|                                                                                                                                              |
| [using][ Syncfusion.Windows.Forms.Tools;] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                                                      |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Drag and drop a ComboBox control from the Toolbox onto the form.

3.   Create and instance of the AutoAppend class as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                          |
| []                                                                                               |
|                                                                                                                          |
| [// Creating an instance of the AutoAppend Class.]                     |
|                                                                                                                          |
| [private][ AutoAppend autoAppend1;] |
|                                                                                                                          |
| [autoappend1 = [new] AutoAppend();]                             |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                        |
| []                                                                                                                             |
|                                                                                                                                                        |
| [\' Creating an instance of the AutoAppend Class.]                                                   |
|                                                                                                                                                        |
| [Private][ autoAppend1 [As] AutoAppend]      |
|                                                                                                                                                        |
| [Private][ autoappend1 = [New] AutoAppend()] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   After creating the AutoAppend instance we need to associate it with an edit control. To achieve this use the **AutoAppend.SetAutoAppend** method. This method takes an object of **AutoAppendInfo** class which is used to hold the details of the data associated.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------+
| Method                            | Description                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| SetAutoAppend                     | Sets AutoAppend behavior for the control specified. The parameters are,              |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | *control* - control to which auto append class has to be associated.                 |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | *autoAppendInfo* - Initializes an AutoAppendInfo class which  has three parameters - |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | *AutoAppend* - specifies whether autoappend is enabled or not (true or false)        |
|                                   |                                                                                      |
|                                   | *categoryName* - category to which contents in this control belong to.               |
|                                   |                                                                                      |
|                                   | *items* - Reference to an item list.                                                 |
|                                   |                                                                                      |
|                                   | *maxItems* - specifies maximum number of items.                                      |
+-----------------------------------+--------------------------------------------------------------------------------------+
| GetAutoAppend                     | Returns the AutoAppend info associated with the control. The parameter is control.   |
+-----------------------------------+--------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                    |
| [// Calling this will enable AutoAppend behavior in the control.]                                                                                |
|                                                                                                                                                                                                    |
| [autoappend1.SetAutoAppend(cmbBox,[new] AutoAppendInfo(true,\"category name\", al, 10)); [//al is an IList object]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                  |
|                                                                                                                                                                                                     |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                     |
| [\' Calling this will enable AutoAppend behavior in the control.]                                                                                 |
|                                                                                                                                                                                                     |
| [autoappend1.SetAutoAppend(cmbBox,[New] AutoAppendInfo(True, \"category name\", al, 10)) [\' al is an IList object]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Adding New Entries Programmatically]{.UGHyperlink}[]{.UGHyperlink}

###### []{#_Adding_New_Entries}3.3.1.2.4.3 Adding New Entries Programmatically[]{#p205} {#adding-new-entries-programmatically style="tab-stops: 0pt"}

[] 

1.   To add or move an item to the top of controls\' AutoAppend list, call the method **InsertOrMoveToTop**. If the item is already present, it will be moved to the first place otherwise it will be added.

2.   It takes 2 arguments. First one is the associated control and the second is the value in string.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                                                 |
|                                                                                                                                                                                            |
| [this][.autoAppend1.InsertOrMoveToTop([this].comboBox1,\"www.syncfusion.com\");] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                    |
|                                                                                                                                                                                       |
| []                                                                                                                                                            |
|                                                                                                                                                                                       |
| [Me][.autoAppend1.InsertOrMoveToTop([Me].comboBox1,\"www.syncfusion.com\")] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 145: ComboBox added with AutoAppend Text

 

 

[]{#related-topics}

