---
title: creatingmulticolumndropdownandbindingthevalues.md
original_path: WinForms_Docs/03_Data_Binding/creatingmulticolumndropdownandbindingthevalues.md
created_at: 2025-08-05
---






#### Creating MultiColumnDropDown and Binding the values[] {#creating-multicolumndropdown-and-binding-the-values style="tab-stops: 0pt"}

[] 

This topic discusses how to bind the dropdown list to the data source.

[] 

{border="0"}

**[]** 

Figure 108: MultiColumnDropDownCombo bound to the Access Data Source

[] 

1.   Create a new **ASP.NET Web** application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}.

2.   Drag the **MultiColumnDropDownCombo** control onto the Web Form.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][ssw][:][MultiColumnDropDownCombo][ [ID][=\"MultiColumnDropDownCombo1\"] [runat][=\"server\"] [Width][=\"150px\"\>\</][ssw][:][MultiColumnDropDownCombo][\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 109

[] 

3.   Drag the AccessDataSource from the **Data** tab in the VS.NET ToolBox onto the Web Form.

3.   Right-click **AccessDataSource** and click **Configure DataSource**.

4.   In the **Configure Data Source** screen, click **Browse** to select the \'.mdb\' file name.

[] 

{border="0"}

[] 

5.   Select the appropriate datasource and click **Next**, which opens the following screen.

[] 

{border="0"}

[] 

6.   Select the required columns to display and click **Finish**.

[] 

Setting the DataSourceID property

[] 

The **DataSourceID** property shows the list of available datasources and allows you to select the appropriate data source.

[] 

1.   Set the DataSourceID property by selecting the appropriate datasource.

[] 


  --------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property              Description
  DataMember            Specifies the data member in a data source to bind to the data listing control.
  DataSourceID          Specifies the ID of the datasource.
  DataTextFormatField   Specifies the format string to use when formatting on client side via the value retrieved from selected grid item text. For ex: \"Text1 {ID}, Text2 {Name}\"
  --------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

{border="0"}

[] 

2.   Build and run the application.

 

[]{#related-topics}

