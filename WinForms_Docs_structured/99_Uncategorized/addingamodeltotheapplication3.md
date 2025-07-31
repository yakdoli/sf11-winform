---
title: addingamodeltotheapplication3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingamodeltotheapplication3.md
created_at: 2025-07-03
---








  









## Adding a Model to the Application {#adding-a-model-to-the-application style="tab-stops: 0pt"}

After the  MVC application is created, a model has to be added. Model is a place from where the data can be fetched by the controller (Refer to the Understanding ASP.NET MVC). This section guides you with a  step-by-step procedure on adding a model.

[] 

1.   On the **Solution Explorer**, right-click **Models** folder.


 {border="0"}Note: A context menu will be displayed.


[] 

{border="0"}

[] 

Figure 36: Context Menu displayed on clicking the Models Folder

[] 

2.   On the context menu, point to **Add** and click **New Item**.


{border="0"}Note: The Add New Item {Application Name} is displayed. The Categories window displays the components available under Visual C# program. The Templates window displays the templates under the selected elements.


[] 

{border="0"}

[] 

Figure 37: Add New Item Dialog Box

[] 

3.   Click Data under Visual C#.

[] 

{border="0"}[Note: The Visual Studio installed templates are displayed in the Templates window.]{.NoteChar}

[] 

{border="0"}

[] 

Figure 38: Connecting a Database to the Application


{border="0"}Note: This step is optional and should be performed only when you want to attach a database with the model. For details, see[[ http://weblogs.asp.net/scottgu/archive/2007/05/29/linq-to-sql-part-2-defining-our-data-model-classes.aspx]{.UGHyperlink}](http://weblogs.asp.net/scottgu/archive/2007/05/29/linq-to-sql-part-2-defining-our-data-model-classes.aspx)[.]


4.   In the **Name** box, enter **NorthwindDataClasses**.

5.   Click **Linq to SQL** Classes under **Templates**.

6.   Finally, click **Add**.


{border="0"}Note: The data classes are added under the Model folder.


7.   In the **Name** box, enter NorthwindDataClasses.dbml and click **Add**.

8.   Now northwind linq to sql classes are created in your application and the **Object Relational Designer** appears.

9.   Drag and drop the tables from the server explorer window onto the Object Relational Designer to create LINQ to SQL Classes that represent particular database tables. All the northwind database tables should be added to the Object Relational Designer.

[] 

When you\'re done, you should have something like this:

[] 

{border="0"}

[] 

Figure 39: NorthwindDataContext.dbml

[] 

[]{#_Adding_Essential_Schedule}[] 

[]{#related-topics}

