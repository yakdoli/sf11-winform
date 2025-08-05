---
title: constructorsforpdfandword.md
original_path: WinForms_Docs/99_Uncategorized/constructorsforpdfandword.md
created_at: 2025-08-05
---






##### Constructors for PDF and Word {#constructors-for-pdf-and-word style="tab-stops: 0pt"}

This table illustrates the constructors (along with their arguments) to be used for the export of Grid to PDF and Word:

+------------------+-----------------------------------------------------------------+------------------------------------------------------+--------------------------------------------------------+
| Type of Document | Name                                                            | Description                                          | Parameters                                             |
+------------------+-----------------------------------------------------------------+------------------------------------------------------+--------------------------------------------------------+
| For PDF          | [GridPdfExport]  | This constructor can be used to export Grid to PDF.  | [·      ]GridObject       |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]FileName         |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]ConverterOptions |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]ShowHeader       |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]ShowFooter       |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]StartRange       |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]EndRange         |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]FormatType       |
+------------------+-----------------------------------------------------------------+------------------------------------------------------+--------------------------------------------------------+
| **For Word**     | [GridWordExport] | This constructor can be used to export Grid to Word. | [·      ]GridObject       |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]FileName         |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]ConverterOptions |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]ShowHeader       |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]ShowFooter       |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]StartRange       |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]EndRange         |
|                  |                                                                 |                                                      |                                                        |
|                  |                                                                 |                                                      | [·      ]FormatType       |
+------------------+-----------------------------------------------------------------+------------------------------------------------------+--------------------------------------------------------+

 


Notes:  



***[·    ]***You can choose and customize the parameters of these constructors to suit your needs.

***[·    ]***ConverterOptions refer to the choice of content that you would like to export to PDF or Word- Visible content, All content, or Custom content.


[]{#related-topics}

