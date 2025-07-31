---
title: addingamodeltotheapplication4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingamodeltotheapplication4.md
created_at: 2025-07-03
---








  









## Adding a Model to the Application {#adding-a-model-to-the-application style="tab-stops: 0pt"}

After an MVC application is created, a model has to be added. A Model is a place from where the data can be fetched by the controller (Refer to "Understanding ASP.NET MVC"). This section guides you with the step-by-step procedure on adding a model.

34.  On the **Solution Explorer**, right-click the **Models** folder.


 

{border="0"} Note: A context menu will be displayed.


{border="0"}

Figure 34: Context Menu displayed on clicking the Models Folder

 

35.  On the **Context** menu, point to **Add** and click **New Item**.


 

{border="0"}Note:The Add New Item {Application Name} is displayed. The Categories window displays the components available under Visual C# program. The Templates window displays the templates under the selected elements.


{border="0"}

Figure 35: Add New Item Dialog Box

***[]*** 

36.  Click **Data** under **Visual C#***.*


 

{border="0"}Note: - The Visual Studio installed templates are displayed in the Templates window.


{border="0"}

Figure 36: Connecting a Database to the Application

[] 


{border="0"}Note: - This step is optional and should be performed only when you want to attach a database with the model. For details, see [[http://weblogs.asp.net/scottgu/archive/2007/05/29/linq-to-sql-part-2-defining-our-data-model-classes.aspx]{.UGHyperlink}](http://weblogs.asp.net/scottgu/archive/2007/05/29/linq-to-sql-part-2-defining-our-data-model-classes.aspx)[ ]{.UGHyperlink}[.]{.UGHyperlink}


37.  In the **Name** field, enter **NorthwindDataClasses***.*

38.  Click **Linq to SQL Classes** under **Templates**.

39.  Finally click **Add**.

{border="0"}***[Note :The data classes are added under the Model folder.]***

40.  In the **Name** box, enter **NorthwindDataClasses.dbml** and click the **Add** button.****

Now northwind linq to sql classes are created in your application and the **Object Relational Designer** appears.

41.  Drag and drop the tables from the server explorer window onto the Object Relational Designer to create LINQ to SQL Classes that represent particular database tables. We need to add the all northwind database tables onto the Object Relational Designer.

When completed, you should have the following:

{border="0"}

Figure 37: NorthwindDataContext.dbml

**[]** 

[]{#related-topics}

