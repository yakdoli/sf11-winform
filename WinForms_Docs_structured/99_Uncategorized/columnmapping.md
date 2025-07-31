---
title: columnmapping.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\columnmapping.md
created_at: 2025-07-03
---








  









### Column Mapping {#column-mapping style="tab-stops: 0pt"}

The **MultiColumnDropDown** control also supports column mapping. Column mapping also includes setting the header text of the column, visibility of the column, width of the column, enabling and disabling sorting, formatting the text, and so on.

 

Use Case Scenarios

Column mapping allows you to filter columns in the bound table so that you can choose the columns that need to be displayed.

 

Column mapping can be performed in two ways:

[·      ]Using Builder

[·      ]Using MultiColumnDropDownModel

 

Through Builder

To perform column mapping using **Builder**:

Create a model in the application. Refer to [[Getting Started\>]]{.underline}[[Adding a Model to the Application]]{.underline}[.]

Create a strongly typed view. Refer to [[How to\>]]{.underline}[[Strongly Typed View]]{.underline}.

In the view, use the **Model** property **Datasource()** to bind the data source.

Map the columns using the **Columns** method and **Add** method and set the **HeaderText**, **Format**, **AllowSorting**, **Width**, and **Visible**, and so on.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View ][\[ASPX\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<%][=][Html.][Syncfusion().][MultiColumnDropDown\<[Student]\>([\"MultiColumnDropDown\"])] |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                .Datasource(Model)]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                .DisplayExpression(new int\[\] { 0,1,3 })]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                .AllowSorting(true)     ]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                .Columns(col =\> {]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    col.Add(m =\> m.UniversityCode).HeaderText(["UnivCode"]);]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    col.Add(m =\> m.Title).Width(150);]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    col.Add(m =\> m.CourseFees).AllowSorting(false);]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    col.Add(m =\> m.CGPA);    ]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                })]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [%\>]                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [@(][new][ [HtmlString](][Html.][Syncfusion().][MultiColumnDropDown\<[Student]\>([\"MultiColumnDropDown\"])] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                .Datasource(Model)]                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                .DisplayExpression(new int\[\] { 0,1,3 })]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                .AllowSorting(true)     ]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                .Columns(col =\> {]                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                    col.Add(m =\> m.UniversityCode).HeaderText(["UnivCode"]);]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                    col.Add(m =\> m.Title).Width(150);]                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                    col.Add(m =\> m.CourseFees).AllowSorting(false);]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                    col.Add(m =\> m.CGPA);       ]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [  })]                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [.ToString())[)]]**[]**                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Set its data source and render the view.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                    |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [ [///][ ][\<summary\>]]                                                                                                                  |
|                                                                                                                                                                                                                                               |
| [       [///][ Used for rendering the MultiColumnDropDown initially.]]                                                                                         |
|                                                                                                                                                                                                                                               |
| [       [///][ ][\</summary\>]]                                                                                                           |
|                                                                                                                                                                                                                                               |
| [       [///][ ][\<returns\>][View page; it displays the  MultiColumnDropDown.][\</returns\>]] |
|                                                                                                                                                                                                                                               |
| [       [public] [ActionResult] Index()]                                                                                                                     |
|                                                                                                                                                                                                                                               |
| [       {]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [            [var] Data = [new] [StudentDataContext]().AutoFormatStudent.Take(200);]                                                    |
|                                                                                                                                                                                                                                               |
| [           [return] View(Data);   ]                                                                                                                                                 |
|                                                                                                                                                                                                                                               |
| [       }]                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

In order to work with sorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code sample.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                             |
|                                                                                                                                                                                               |
| [        [public] [ActionResult] Index([PagingParams] args)]                         |
|                                                                                                                                                                                               |
| [        {]                                                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [                [var] Data = [new] [StudentDataContext]().AutoFormatStudent.Take(20);] |
|                                                                                                                                                                                               |
| [                [return] Data.GridActions\<[Student]\>();          ]                                        |
|                                                                                                                                                                                               |
| [        }]                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the application. The **MultiColumnDropDown** will appear as shown in the following screenshot.

 

 

{border="0"}

Figure 318: MultiColumnDropDown with HeaderText "UnivCode" and the Width of the Title Column Set to 150px

 

Through MultiColumnDropDownModel

To perform column mapping using **MultiColumnDropDownModel**:

 

Create a model in the application. Refer to [[Getting Started\>]]{.underline}[[Adding a Model to the Application]]{.underline}.

Add the following code[ in the **Index.aspx** file to create the **MultiColumnDropDown** control in the view.]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [\<%][=][ Html.Syncfusion().MultiColumnDropDown\<MvcSampleApplication.Models.[Student]\>([\"MulticolumnControl1\"], [\"DropDownModel\"], col =\>] |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [    col.Add(m =\> m.UniversityCode).HeaderText([\"UnivCode\"]);]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [    col.Add(m =\> m.Title).Width(150);]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [    col.Add(m =\> m.CourseFees).AllowSorting([false]);]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [    col.Add(m =\> m.CGPA);]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [})[%\>]]                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]      

 

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [@(][new][ [HtmlString](][Html.Syncfusion().MultiColumnDropDown\<MvcSampleApplication.Models.[Student]\>([\"MulticolumnControl1\"], [\"DropDownModel\"], col =\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    col.Add(m =\> m.UniversityCode).HeaderText([\"UnivCode\"]);]                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    col.Add(m =\> m.Title).Width(150);]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    col.Add(m =\> m.CourseFees).AllowSorting([false]);]                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    col.Add(m =\> m.CGPA);]                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [})][]                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [.ToString())[)]]**[]**                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Create a **MultiColumnDropDownModel** in **Index** action. Assign **MultiColumnDropDown** properties in this model and pass the model from the controller to the view using **ViewData** class as in step 6.

Set the **DataSource** and **DisplayExpression** as shown in the following code sample.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                 |
|                                                                                                                                                                                                                            |
| [        AcceptVerbs][([HttpVerbs].Post)\]]                                                                |
|                                                                                                                                                                                                                            |
| [        [public] [ActionResult] Index([MultiColumnDropDownModel]\<[Student]\> dropdown)] |
|                                                                                                                                                                                                                            |
| [        {]**[]**                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [                dropdown.DataSource = [new] [StudentDataContext]().AutoFormatStudent.Take(30);]                                          |
|                                                                                                                                                                                                                            |
| [                dropdown.DisplayExpression = [new] [int]\[2\] { 2, 3 };              ]                                                      |
|                                                                                                                                                                                                                            |
| [                ViewData\[[\"DropDownModel\"]\] = dropdown;]                                                                                                  |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [                [return] PartialView([\"MultiColumnDropDownPartialView\"]);]                                                             |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

         

In order to work with sorting actions, create a **Post** method for **Index** actions and bind the data source to **MultiColumnDropDown** as shown in the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                              |
| [        [public] [ActionResult] ][Index][ ([PagingParams] args)]                                           |
|                                                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                              |
| [       [IEnumerable] data =][new ][StudentDataContext][().AutoFormatStudent.Take(20);] |
|                                                                                                                                                                                                                                                                                              |
| [       [return] data.GridActions\<[Student]\>();]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

         

Run the application. The MultiColumnDropDown control will appear as shown in the following screenshot.

 

 

{border="0"}

Figure 319: MultiColumnDropDown with HeaderText "UnivCode" and Width of Title Column set to 150px

 

 

Properties

 

 


  Property       Description                                                                                                                                                                             Type          Type of the property   Value it accepts   Any other dependencies/sub-properties associated
  -------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ---------------------- ------------------ --------------------------------------------------
  Visible        Used to set the visibility of the column.                                                                                                                                               ServerSide    Boolean                True/False         NA
  Width          Used to set the width of the column.                                                                                                                                                    Server Side   Unit                   Numeric Value      NA
  AllowSorting   If AllowSorting property of MultiColumnDropDown is true, AllowSorting property of all the columns will be set to true. It is used to enable/disable sorting for the specified column.   Server Side   Boolean                True/False         AllowSorting property of MultiColumnDropDown
  HeaderText     Used to set the HeaderText of the column.                                                                                                                                               Server Side   String                 Any String         NA
  Format         Used to format the value of the column                                                                                                                                                  Server side   String                 Any string         NA
  IsUnbound      Used to check whether the column is bound or not.                                                                                                                                       Server Side   String                 Any string         NA


 

Sample Link

To access the samples:

1.   Go to **Grid MVC Demos** in SampleBrowser. Refer to Installation and Deployment\>Samples and Location.

2.   Select **MultiColumnDropDown** on the left side **Accordion**.

3.   Select the **Core Features** demo to view the **MultiColumnDropDown** full-fledged demo.

**[]** 

[]{#related-topics}

