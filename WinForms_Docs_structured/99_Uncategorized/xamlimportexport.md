---
title: xamlimportexport.md
original_path: WinForms_Docs/99_Uncategorized/xamlimportexport.md
created_at: 2025-08-05
---






#####  XAML Import/Export {#xaml-importexport style="tab-stops: 0pt"}

The XAML import feature allows users to import a .xaml file into the RichTextBoxAdv. It renders the XAML elements as XamlReader and displays the text in the format of RichTextBoxAdv's content model. The XAML export feature actually exposes the RichTextBoxAdv's document as a .xaml file. The following methods clearly show this use case.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [RichTextBox.Document=[XAMLImporting].ConvertToDocumentAdv(xamlStream)]                                                                                                                |
|                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| **[\[C#\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| **[         ]**[string][ xaml = [XAMLExporting].ConvertToXAML(RichTextBox.Document, xamlstream);] |
|                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Methods

  ------------------------ ------------------------------------------- ------------ ------ -------------
  Method                   Description                                 Parameters   Type   Return Type
  ConvertToDocumentAdv()   It converts XAML stream into DocumentAdv.   NA           NA     DocumentAdv
  ConvertToXaml()          It returns the RichText content as XAML.    NA           NA     Void
  ------------------------ ------------------------------------------- ------------ ------ -------------

[]{#related-topics}

