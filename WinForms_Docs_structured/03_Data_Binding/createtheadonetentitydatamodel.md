---
title: createtheadonetentitydatamodel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\createtheadonetentitydatamodel.md
created_at: 2025-07-03
---








  









## Create the ADO.NET Entity Data Model {#create-the-ado.net-entity-data-model style="tab-stops: 0pt"}

In order to use the Entity Framework, you need to create an Entity Data Model. You can take advantage of the Visual Studio *Entity Data Model Wizard* to generate an Entity Data Model from a database automatically.

 

To create the ADO.NET Entity Data Model:

1.   Right-click the **Models** folder in the **Solution Explorer** window and select the menu option **Add New Item**.

2.   In the **Add New Item** dialog, select the **Data category** (see Figure 152).

[] 

[] 

{border="0"}

[Figure]{#_Ref316465816} 152: Creating a New Entity Data Model

[[]]{.MsoSubtleEmphasis} 

3.   Select the **ADO.NET Entity Data Model** template, give the Entity Data Model the name **DiagramDBModel.edmx**, and click **Add**. Clicking **Add** launches the **Data Model Wizard**.

4.   In the **Choose Model Contents** step, choose the **Generate from a database** option and click **Next** (see Figure 153).

[] 

{border="0"}

[]{#_Ref316465750}[Figure]{#_Ref316465757} 153: Choose Model Contents Step

[[]]{.MsoSubtleEmphasis} 

5.   In the **Choose Your Data Connection** step, select the **DiagramDB.mdf** database connection, enter the entities connection settings name **DiagramDBEntities**, and click N**ext** (see Figure 154).

[] 

{border="0"}

[Figure]{#_Ref316466133} 154: Choose Your Data Connection[]

[[]]{.MsoSubtleEmphasis} 

6.   In the **Choose Your Database Objects** step, select the database **DiagramTable** and click **Finish** (see Figure 155).

[] 

{border="0"}

[Figure]{#_Ref316466146} 155: Choose Your Database Objects

[[]]{.MsoSubtleEmphasis} 

**[]** 

When you have completed, you should have something like this:

[] 

{border="0"}

Figure 156: DiagramDBEntity Model

[]{#related-topics}

