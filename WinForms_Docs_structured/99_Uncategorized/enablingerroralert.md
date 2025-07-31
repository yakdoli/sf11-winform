---
title: enablingerroralert.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\enablingerroralert.md
created_at: 2025-07-03
---








  









### Enabling Error Alert {#enabling-error-alert style="tab-stops: 0pt"}

You can show an error icon or error message box as an alert for incorrect data.

 

Displaying Error Icon        

 

You can show the error icon in the cell and row header using the **ShowerrorIcon** and the **ShowRowHeaderErrorIcon** properties respectively.

 

To show the error icon in the cell, set the **ShowerrorIcon** property to **True**. By default this will be set to **True**. To show the error icon in the row header, set the **ShowRowHeaderErrorIcon** property to **True**. By default this will be set to **False**. 

You can display the error icon in the cell as well as a row header if needed.

The following code illustrates how to display the error icon on both the cell as well as the row header:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
|                                                                                                                                                                                                               |
|                                                                                                                                                                                                               |
| [this][.gridDataBoundGrid1.CurrentCell.ShowerrorIcon = [true];] |
|                                                                                                                                                                                                               |
| [this][.gridDataBoundGrid1.ShowRowHeaderErrorIcon = [true]; ]   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                        |
|                                                                                                                                                                        |
|                                                                                                                                                                        |
| [Me][.gridDataBoundGrid1.CurrentCell.ShowerrorIcon = [True]] |
|                                                                                                                                                                        |
| [Me][.gridDataBoundGrid1.ShowRowHeaderErrorIcon = [True]]    |
|                                                                                                                                                                        |
| []                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

*[Figure ][497][: Error Icon]*

 

 

Displaying Error Message Box

You can show an error dialog using the **ShowErrorMessageBox** property and specify the content to be displayed using the **ValidationErrorText** property.

 

The following code illustrates this:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [this][.gridDataBoundGrid1.CurrentCell.ShowErrorMessageBox= [false];]                    |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [this][.gridDataBoundGrid1.CurrentCell.ValidationErrorText = [\"this is the text\"];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [Me][.gridDataBoundGrid1.CurrentCell.ShowErrorMessageBox= [False]]                    |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [Me][.gridDataBoundGrid1.CurrentCell.ValidationErrorText = [\"this is the text\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

*[Figure ][498][: Error Message Box]*

Specifying Error Content

You can specify error conditions for individual cells using the **SetError()** method of the **GridCurrentCell**.

The following code illustrates this:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [this][.gridDataBoundGrid1.CurrentCell.SetError([\"Please enter valid number\"]);] |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| [Me][.gridDataBoundGrid1.CurrentCell.SetError([\"Please enter valid number\"])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

