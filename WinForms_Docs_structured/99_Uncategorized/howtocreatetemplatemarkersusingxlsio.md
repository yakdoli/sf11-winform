---
title: howtocreatetemplatemarkersusingxlsio.md
original_path: WinForms_Docs/99_Uncategorized/howtocreatetemplatemarkersusingxlsio.md
created_at: 2025-08-05
---








  









### How to Create Template Markers Using XlsIO? {#how-to-create-template-markers-using-xlsio style="tab-stops: 0pt"}

[] 

Report created in Excel provides ordered and rich look for large datasets. This article focuses on creating an Excel report using template markers. A template marker is a special marker symbol created in an Excel template which will be bound the required user data. Essential XlsIO allows you to create and bind the template markers to data from various sources, such as data table, variables and arrays. This allows the user to control the data formats for the data bound to the template document.

[] 

How Does it Work?

[] 

Markers are applied in the template to the required cells. This will include the data source name and field name of interest. During data binding a search is conducted for the data source name and the field name in the Excel workbook and the corresponding data from the data source is bound to the marker. Cells in the worksheet can be filled with single data source or with multiple records. Format of these data can be changed using the arguments of the markers.

[] 

What is the Syntax of the Markers in Template?

[] 

Each marker starts with some prefix (by default it is "%" character) and followed by the variable name and properties. There could be several arguments after a variable which are delimited by some character (by default it is semicolon ";".)

[] 

{border="0"}

Figure 164: Marker Syntax

[] 

What are the Various Sources of Binding Data to Markers?

 

Essential XlsIO allows data binding from following data sources.

 

1\. Data Source

This includes data tables, datasets, data readers and data views. A data source can be used to bind large number records to the template document. This will add the rows for each record and fields to be bound are identified through the field name in the template.

[] 

Syntax: %DataSource.FieldName

[] 

2\. Variable Name

This option will allow you to bind a single data stored in a variable to the marker in the template.

 

Syntax: %VariableName

 

**3. Variable Array**

This option will allow you to bind array of data stored in an array to the marker in the template.

 

Syntax: %VariableArray

 

**4. Formulas**

This option will allow you to create formulas for each row when multiple records comprising formula in the cells are bound to the marker. If a cell contains formula, by default it will be stretched to the rows/columns for any of the above sources of data binding.

[] 

{border="0"}

Figure 165: Formulas[]

***[]*** 

What are the Various Arguments for the Marker?

 

The following arguments can be used with the marker to control the formatting while binding the data:

[·      ]**Horizontal**-This argument specifies the horizontal direction of the data import for complex variables.

[·      ]**Vertical**-This argument specifies the vertical direction of the data import for complex variables.

[·      ]**Insert**-This argument inserts new row or column depending on the direction argument for each new cell. By default, the rows can't be added.

[·      ]**insert:copystyles**-This argument copies style from the row above or left column.

[·      ]**jump:\[cell reference in R1C1 notation\]**-This argument binds the data to the cell at the specified reference. Cell reference address can be relative or absolute.

[·      ]**copyrange:\[top-left cell reference in R1C1\]:\[bottom-right cell reference in R1C1\]**-Copies the specified cells after each cell import.

 

Following code snippet illustrates processing and binding the marker with data.

 

+-----------------------------------------------------------------------------------------------------------------------------------+
| [// Create marker processor]                                                    |
|                                                                                                                                   |
| [ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();] |
|                                                                                                                                   |
| []                                                                              |
|                                                                                                                                   |
| [// Bind the data from the data table]                                          |
|                                                                                                                                   |
| [marker.AddVariable(\"Customers\",northwindDt);]                                |
|                                                                                                                                   |
| []                                                                              |
|                                                                                                                                   |
| [// Process the markers in the template]                                        |
|                                                                                                                                   |
| [marker.ApplyMarkers();]                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

Here, **CreateTemplateMarkerProcessor** returns **ITemplateMarkersProcessor** interface which creates and manipulates the marker data. **ApplyMarkers** method of **ITemplateMarkersProcessor** is the special method that processes the markers in the template.

 

Here is a screen shot after binding data with marker variable.

***[]*** 

{border="0"}

Figure 166: Marker Syntax

 

[Here is a screen shot after binding the data with the marker that retains the formula.]

[] 

{border="0"}

Figure 167: Marker Syntax**[]**

**[]** 

Summary

This article demonstrates about how Essential XlsIO can be used to generate rich reports in Excel format using template markers. You can create and format user specific information in a large report with few lines of coding and great performance[. ]

[] 

[]{#related-topics}

