---
title: vs2010designersupport.md
original_path: WinForms_Docs/99_Uncategorized/vs2010designersupport.md
created_at: 2025-08-05
---








  









### VS2010 Designer support {#vs2010-designer-support style="tab-stops: 0pt"}

GridDataControl provides a rich design-time experience by utilizing a designer, which allows users to modify the various grid settings, affecting the look and feel of a grid.

Once the grid has an ItemsSource assigned, the grid designer populates with numerous options and allows you to edit the basic grid properties and the properties of individual columns. Any change in any of these properties in the designer will have an immediate impact on the XAML code, allowing the designer to make the grid easy to use and more user-friendly.

Activating Designer

1.   Open the design window, right-click on the grid and then select **Designer View, Show Designer**. Ensure that the grid has been assigned an ItemsSource; you will then see the Designer window.

[] 

{border="0"}

Figure 174: Activating Designer

[] 

[] 

{border="0"}

Figure 175: Designer

[] 

Basic Properties

The Basic Properties option lets you modify the overall settings of a grid. These properties are categorized into three types: Column Properties, Row Properties, and Cell Properties.

{border="0"}

Figure 176: Basic Properties

**[]** 

The **Column Properties** section provides various column options such as AutoPopulate Columns, AutoPopulate Relations, Allow Sort, Allow Drag Columns, Allow Resize Columns, Show Column Options, Show Filters, Show Group Drop Area, and Column Sizer options.

[] 

{border="0"}

Figure 177: Column Properties

The **Row Properties** section explores the row-related properties such as Show Add New, Show Group Summaries, Show Row Header, Allow Resize Rows, Allow Delete, and List Box Selection Modes.

{border="0"}

Figure 178: Row Properties

The **Cell Properties** section explores cell-level properties such as Allow Edit, Show Error ToolTips, Show ToolTips, Allow Selection options, Activate Current Cell Behavior options, and Visual Style options.

{border="0"}

Figure 179: Cell Properties

Visible Columns

This section automatically generates a property listing for each visible column in the grid. Each listing includes column-level properties such as Allow Filter, Allow Sort, Allow Drag, Allow Group, Allow Resize, Is Read Only, AutoFit, Width, Header Text, Column Format options, and Cell Type options.

Below is what you see when you click the Visible Columns button.

{border="0"}

Figure 180:Visible Columns

Click the Generate Columns button to populate the properties for each visible column. You can clear the visible column settings by clicking the Clear Columns button.

{border="0"}

Figure 181: Property listing for a column named FirstName

***[]*** 

{border="0"}

Figure 182: First Name

Special Cell Types

The Special Cell Types combo box lists the various cell types applicable to the column. It also automatically deducts the column type of the grid columns and sets the cell type. For example, if the column is a Boolean type, it will automatically have a check box.

{border="0"}

Figure 183: Special Cell Types

 

[]{#related-topics}

