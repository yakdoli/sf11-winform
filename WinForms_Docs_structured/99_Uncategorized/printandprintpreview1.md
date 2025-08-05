---
title: printandprintpreview1.md
original_path: WinForms_Docs/99_Uncategorized/printandprintpreview1.md
created_at: 2025-08-05
---








  









### Print and Print Preview {#print-and-print-preview style="tab-stops: 0pt"}

Essential Grid for WPF provides an in-built support for printing and print preview.  This feature populates a print dialog that allows you to preview the output and make required modifications if necessary, before sending the grid content for printing.

 

The GridPrintDialog class plays a vital role in the implementation of printing support. It is built based on Microsoft PrintDialog class that will handle the internal operations for GridPrintDialog. The GridPrintDialog class defines the designer for the Print dialog and exposes a number of properties and APIs to handle the UI requirements and define the interaction logic for the Print Dialog. The users can use these properties to configure the Print and Print Preview options.

 

Example

 

Enabling the printing feature is like invoking an API -- ShowPrintDialog() on the instances of the grid.

 

+-----------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                            |
|                                                                                                                       |
| **[]**                                                               |
|                                                                                                                       |
| [this][.grid.ShowPrintDialog();] |
+-----------------------------------------------------------------------------------------------------------------------+

 

Output

 

       {border="0"}

Figure 88: Grid Print Dialog

 

*[]* 

*[]* 

More:







