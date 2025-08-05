---
title: databindinginchartthroughchartwizard.md
original_path: WinForms_Docs/04_Controls/Chart/databindinginchartthroughchartwizard.md
created_at: 2025-08-05
---








  









### Data Binding in Chart Through Chart Wizard {#data-binding-in-chart-through-chart-wizard style="tab-stops: 0pt"}

 

You can easily implement data binding technique at design-time, using Chart Wizard.

 

The below steps lets you bind a database table with the ChartControl.

 

1.   Open the **Chart Wizard** tool, Click **Series** button and go to the **Data Source** tab as shown in the image below.

 

{border="0"}

 

Figure 28: Data Source Tab

 

2.   First step is to select the chart data source from the drop-down list. All data sources available with the form will be shown in the list. If there is no data source in the list, click the **new BindingSource** option from the drop-down list.

 

{border="0"}

**** 

Figure 29: Selecting \"new BindingSource\....\" from the drop-down list in the Data Source Tab

**** 

3.   This opens a **Data Source Configuration Wizard**. Choose the Data source Type as **Database**, and click **Next**.

 

{border="0"}

**** 

Figure 30: Selecting the Data Source Type

 

4.   Then click **New Connection**.

 

{border="0"}

**** 

Figure 31: Creating a New Connection

 

5.   In the Choose Data Source dialog box, select the data source as MS SQL server database or MS Access database, and then click Continue button.

 

{border="0"}

**** 

Figure 32: Choose Data Source Dialog Box

 

6.   This opens the **Add Connection** dialog box. Click the **Browse** button and select the database file from any location. Click **OK** to make this connection available to the Data source Configuration Wizard.

 

{border="0"}

**** 

Figure 33: Selecting the Database file by clicking on the Browse Button in the Add Connection Dialog Box

 

7.   You will be directed to the Data Source Configuration Wizard after completing the above steps. Click **Next**.

 

{border="0"}

**** 

Figure 34: Next button in the Data Source Configuration Wizard is Clicked

 

8.   Tables and Views that are available in the selected database will be listed in the Wizard. Select the appropriate table, required columns and then click **Finish**.

 

{border="0"}

**** 

Figure 35: Finish button in the Data Source Configuration Wizard is clicked after selecting the required Table and Columns

 

9.   You will be directed back to the Chart Wizard now. Select the database from the **Data Source** list as shown in the image below.

 

{border="0"}

**** 

Figure 36: Selecting the Database from the drop-down List in the Data Source Tab

 

10.  Once the source is selected, the selected table will be visible as in the below image.

 

{border="0"}

**** 

Figure 37: Selected Table

 

Binding the Table Data with Chart Series

 

1.   Click the \'Series Data\' option in the wizard to select the series to which the data is to be bound. In \'Series Data\' page, select the series using the **Series Data** box.

 

{border="0"}

**** 

Figure 38: Selecting the Series to which the data is to be Bound

 

2.   To assign the retrieved database column to X and Y values of the series, use **X Value** box and **Y Value** box as shown in the below screen shots.

 

{border="0"}

**** 

Figure 39: Assigning the retrieved database column to X value of the Series

**** 

{border="0"}

 

Figure 40: Assigning the retrieved database column to Y value of the Series

 

3.   Click **Finish** to apply these data binding settings to the Chart. The below image illustrates the Chart bound with custom data.

 

{border="0"}

 

Figure 41: Data Source bound to the Chart by using the Chart Wizard

 

[]{#p25} 

 

[]{#related-topics}

