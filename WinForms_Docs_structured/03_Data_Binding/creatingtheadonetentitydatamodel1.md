---
title: creatingtheadonetentitydatamodel1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\creatingtheadonetentitydatamodel1.md
created_at: 2025-07-03
---








  









## Creating the ADO.NET Entity Data Model {#creating-the-ado.net-entity-data-model style="tab-stops: 0pt"}

In order to use the Entity Framework, you need to create an Entity Data Model. You can take advantage of the Visual Studio *Entity Data Model Wizard* to generate an Entity Data Model from a database automatically.

 

To create the ADO.NET Entity Data Model:

[] 

1.   Right-click the **Models** folder in the **Solution Explorer** window and select the menu option **Add New Item**.

2.   In the **Add New Item** dialog, select the **Data category** (see Figure 107).

[] 

{border="0"}

Figure 155[: Creating a new Entity Data Model]

*[]* 

3.   Select the **ADO.NET Entity Data Model** template, give the Entity Data Model the name ScheduleDBModel.edmx, and click **Add** . Clicking **Add,** launches the **Data Model Wizard**.

4.   In the **Choose Model Contents** step, choose the **Generate from a database** option and click **Next** (see Figure 108).

[] 

{border="0"}

Figure 156:[Choose Model Contents Step]

*[]* 

5.   In the **Choose Your Data Connection** step, select the Schedule_DB.mdf database connection, enter the entities connection settings name Schedule_DBEntities, and click **Next** (see Figure 109).

[] 

{border="0"}

Figure 157[: Choose Your Data Connection][]

*[]* 

6.   In the **Choose Your Database Objects** step, select  all the database appointment tables and click **Finish**  (see Figure110).

[] 

{border="0"}

Figure 158[: Choose Your Database Objects]

**[]** 

When you have completed you should have something like this:

[] 

{border="0"}

Figure 159[: ScheduleDbEntity Model]

*[]* 

[]{#related-topics}

