---
title: builtinerrorprovidersupport.md
original_path: WinForms_Docs/99_Uncategorized/builtinerrorprovidersupport.md
created_at: 2025-08-05
---








  









## Built-in Error Provider Support {#built-in-error-provider-support style="tab-stops: 0pt"}

Essential Grid for Windows Forms now provides a built-in error provider for error alerts. This feature enables you to display an error icon in a specific cell and row header when incorrect data is entered in a cell. This also enables you to specify the error conditions.

 

Use Case Scenarios

This feature is useful when you want to set that only numeric values can be entered in a cell.

 

Properties


  ------------------------ -------------------------------------------------------------- ---------- ---------------
  **Property**             **Description**                                                **Type**   **Data Type**
  ShowerrorIcon            Specifies whether to show error icon.                          NA         Boolean
  ShowRowHeaderErrorIcon   Specifies whether to show error icon in the row header.        NA         Boolean
  ShowErrorMessageBox      Specifies whether to show error message box.                   NA         Boolean
  ValidationErrorText      Specifies the text to be displayed in the error message box.   NA         Boolean
  ------------------------ -------------------------------------------------------------- ---------- ---------------


[] 

Methods

  **[Method ]**[]   **[Description ]**[]   **[Parameters ]**[]   **[Type ]**[]   **[Return Type ]**[]
  ------------------------------------------------------------- ------------------------------------------------------------------ ----------------------------------------------------------------- ----------------------------------------------------------- ------------------------------------------------------------------
  SetError()[]                                                                                             Method (string)                                                   Method                                                      String

[] 

Sample Link

A sample of this feature is available in the following location:

**GridDataBoundGrid**

***{Installed Path}\\Syncfusion\\EssentialStudio\\{Version}\\Windows\\GridDataBound.Windows\\Samples\\2.0\\Appearance\\Error Provider Demo***

 

**GridGroupingGrid**

***{Installed Path}\\Syncfusion\\EssentialStudio\\{Version}\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Grouping Grid Layout\\Error Provider Demo***

 

**GridControl**

***{Installed Path}\\Syncfusion\\EssentialStudio\\{Version}\\Windows\\Grid.Windows\\Samples\\2.0\\Grid Layout\\Error Provider Demo***

***[]*** 

More:





