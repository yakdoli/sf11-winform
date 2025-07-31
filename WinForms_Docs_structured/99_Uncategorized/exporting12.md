---
title: exporting12.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exporting12.md
created_at: 2025-07-03
---








  









## Exporting {#exporting style="tab-stops: 0pt"}

When creating OLAP Report in OLAP Client, the report will be previewed in the OLAP Chart and OLAP Grid. OLAP Client has the option to export the current visual of the Grid to various forms.

Export Options in Grid

The Grid can be exported to the following form:

[·      ]Word

[·      ]PDF

[·      ]Excel

Users can perform these exports in two ways:

[·      ]Through OLAPGrid Tool Bar menu

[·      ]Through APIs

Using OLAPGrid Tool Bar Menu

The OLAPGrid Toolbar provides the menu to perform export operations. By clicking any one of the Export buttons, the user can export the grid to the corresponding format.

 

{border="0"}

 

Figure 37: Export Menus in OLAP Grid Tool Bar

 

Export menus in OlapGrid Toolbar

Table 8: Export Options in Grid

 


  ------------------------------------------- ----------------- --------------------------
  Icon                                        Name              Description
  {border="0"}   Export to Excel   Export the Grid to Excel
  {border="0"}   Export to Word    Export the Grid to Word
  {border="0"}   Export to PDF     Export the Grid to PDF
  ------------------------------------------- ----------------- --------------------------


 

Using APIs

You can achieve the Export feature of OLAPGrid, using the following APIs.

The code snippet for the Export feature of OLAPGrid in OLAP Client is shown below:

 

+----------------------------------------------------------------------------------+
| **[\[C#\]]**                                 |
|                                                                                  |
| []                                           |
|                                                                                  |
| [// Export an OlapGrid into an Excel Format] |
|                                                                                  |
| [this.OlapClient.OlapGrid.ExportToExcel();]  |
|                                                                                  |
| []                                           |
|                                                                                  |
| [// Export an OlapGrid into a Word Format]   |
|                                                                                  |
| [this.OlapClient.OlapGrid.ExportToWord();]   |
|                                                                                  |
| []                                           |
|                                                                                  |
| [// Export an OlapGrid into a PDF Format]    |
|                                                                                  |
| [this.OlapClient.OlapGrid.ExportToPdf();]    |
|                                                                                  |
| []                                           |
+----------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------+
| **[\[VB\]]**                                 |
|                                                                                  |
| []                                           |
|                                                                                  |
| [\' Export an OlapGrid into an Excel Format] |
|                                                                                  |
| [Me.OlapClient.OlapGrid.ExportToExcel()]     |
|                                                                                  |
| []                                           |
|                                                                                  |
| [\' Export an OlapGrid into a Word Format]   |
|                                                                                  |
| [Me.OlapClient.OlapGrid.ExportToWord()]      |
|                                                                                  |
| []                                           |
|                                                                                  |
| [\' Export an OlapGrid into a PDF Format]    |
|                                                                                  |
| [Me.OlapClient.OlapGrid.ExportToPdf()]       |
|                                                                                  |
| []                                           |
+----------------------------------------------------------------------------------+

 

[]{#related-topics}

