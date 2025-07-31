---
title: vs2010designersupport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\vs2010designersupport1.md
created_at: 2025-07-03
---








  









### VS2010 Designer support  {#vs2010-designer-support style="tab-stops: 0pt"}

GridDataControl provides rich design time experience by associating a designer. This allows the users to modify the various grid settings to change the look and feel of the grid.

 

The grid designer is populated with numerous options when ItemsSource assigned to the grid. This enables the users to edit the basic grid properties and the properties of individual column. Changes in any of these properties in the designer will have an immediate impact on its XAML code and hence the designer makes the grid more user-friendly.

 

Activating Designer

1.   Open Design window.

2.   Right-click on the grid.


 

Note: An edit menu opens.


 

 

{border="0"}

Figure 245: *Edit Menu*

 

3.   Select Designer View -\> Show Designer.


{border="0"}Note: Ensure that the grid is assigned with an ItemsSource.


4.   Designer Window is displayed.

**[]** 

Designer Window has two options:

 

[·      ]Basic Properties - Modify the overall settings of the grid.

[·      ]Visible Columns - Automatically generates a property list for each visible column in the grid.

 

{border="0"}

Figure 246: Designer Window

[] 

Basic Properties

 

This option enables the users to modify the overall settings of the grid. The properties are categorized into three types:

 

[·      ]Column Properties

[·      ]Row Properties

[·      ]Cell Properties

 

{border="0"}

Figure 247: Basic Properties

 

 

Column Properties

 

This section explores the various column options such as Auto Populate Columns, Auto Populate Relations, Allow Sort, Allow Drag Columns, Allow Resize Columns, Show Column Options, Show Filters, Show Group Drop Area and Column Sizer combo box.

 

1.   Select as you require in this list.

 

{border="0"}

Figure 248: Column Properties

[] 

Row Properties

 

 This section explores the row-related properties such as Show Add New, Show Group Summaries, Show Row Header, Allow Resize Rows, Allow Delete and List Box Selection Modes combo box.

 

Select as you require in this list.

 

{border="0"}

Figure 249: Row Properties

 

Cell Properties

 

This section explores cell level properties such as Allow Edit, Show Error Tooltips, Show Tooltips, Allow Selection combo box, Activate Current Cell Behavior combo box and Visual Style combo box.

 

{border="0"}

Figure 250: Cell Properties

*[]* 

Select as you require in this list.

Visible Columns

 

This section automatically generates a property list for each visible column in the grid. Each list includes the column level properties such as Allow Filter, Allow Sort, Allow Drag, Allow Group, Allow Resize, Is Read Only, Auto fit, Width, Header Text field, Column Format combo box and Cell Type combo box.

 

[·      ]Click Visible Columns.

[·      ]Two options are displayed

[o  ]Generate Columns

[o  ]Clear Columns

 

{border="0"}

Figure 251: Visual Column Options

[] 

Generate Columns

1.   Click Generate Columns to populate the properties for each visible column.


[{border="0"}]Note: Property list for visible column in the grid displays.


 

{border="0"}

Figure 252: Property List of Visible Column In the Grid

 

2.   Select as you require.

 

{border="0"}

Figure 253: First Name Column Property List

 

 

Special Cell Types

This combo box lists the various possible cell types applicable to the column. It also automatically deducts the column type of the grid columns and sets the CellType of it. For example, if the column is of Boolean type, it will automatically have a CheckBox.

 

{border="0"}

Figure 254: Special Cell Types

 

Clear Columns

 

Click Clear Columns to clear the visible column settings.

**[]** 

[] 

[]{#related-topics}

