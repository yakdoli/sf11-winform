---
title: howtoovercomesendkeyexceptionincurrencycell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoovercomesendkeyexceptionincurrencycell.md
created_at: 2025-07-03
---








  









### How to Overcome SendKey Exception in Currency Cell {#how-to-overcome-sendkey-exception-in-currency-cell style="tab-stops: 0pt"}

The *CurrentCellKeyDown* event cannot be handled for CurrencyTextbox, when the Windows Forms application is hosted into Internet Explorer. It will throw an error message as,"SendKeys cannot run inside this application." To overcome this exemption, set the *ActivateSendKey* property to false.

The following code illustrates this: []

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                              |
|                                                                                                                                                                                                |
| [//GridGroupingControl: ][]                                                                              |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [this][.[Grid].TableModel.Option.ActivateSendKey = [false];] |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [//GridControl/GridDataBound:][]                                                                         |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [this][.[Grid].Model.Option. ActivateSendKey = [false];]     |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [//GridListControl:][]                                                                                   |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [this][.GridList.Grid.Model.Option.ActivateSendKey = [false];]                       |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                      |
|                                                                                                                                                                       |
| **[]**                                                                                                                            |
|                                                                                                                                                                       |
| [\'GridGroupingControl: ][]                                                     |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [Me][.Grid.TableModel.Option.ActivateSendKey = [False]]     |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\'GridControl/GridDataBound:][]                                                |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [Me][.Grid.Model.Option.ActivateSendKey = [False]]          |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\'GridListControl:][]                                                          |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [Me][.GridList.Grid.Model.Option.ActivateSendKey = [False]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

[]{#related-topics}

