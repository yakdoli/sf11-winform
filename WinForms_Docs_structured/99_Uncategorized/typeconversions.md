---
title: typeconversions.md
original_path: WinForms_Docs/99_Uncategorized/typeconversions.md
created_at: 2025-08-05
---






#### Type Conversions {#type-conversions style="tab-stops: 0pt"}

[] 

You will notice that in the **GridSaveCellInfo** method, you had made use of the **int.Parse** method to convert the string value in the **GridStyleInfo** object to the integer you needed for the external data source. You can instead make use of the more general **Convert** class provided by Essential Grid, to handle conversions between various data types. This class, for example, can convert the value in a **CellValue** property to a **DataTime** object, or to a **Color** object, depending upon the need. The following code example illustrates how to use this Convert class.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [// Convert a value in CellValue property to \'int\' (as required by our data source) by using Convert class.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                               |
| [this][.\_extData\[e.RowIndex - 1, e.ColIndex - 1\] = ([int])[GridCellValueConvert].ChangeType(e.Style.CellValue, [typeof]([int]), [null]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                         |
| [\' Convert a value in CellValue property to \'int\' (as required by our data source) by using Convert class.]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                         |
| [Me][.\_extData(e.RowIndex - 1, e.ColIndex - 1) = [CInt](GridCellValueConvert.ChangeType(e.Style.CellValue, [GetType]([Integer]), [Nothing]))] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: This conversion problem may occur when the value that is stored in the style object is a string. This happens when the CellValueType property is not explicitly set on the style object in your GridQueryCellInfo method. But when this is set to \"int\", then you can cast the CellValue in SaveCellInfo to an int, and do not have to worry about conversions.


 

[]{#p28} 

 

[]{#related-topics}

