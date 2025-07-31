---
title: addingcelltypestoanapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingcelltypestoanapplication.md
created_at: 2025-07-03
---






##### Adding CellTypes to an Application {#adding-celltypes-to-an-application style="tab-stops: 0pt"}

There are more than ten CellTypes that are currently available. The following are the cell types:

[] 

[·      ]Basic Cells

[·      ]TextBox Cells

[·      ]CheckBox Cells

[·      ]Data Template Cells

[·      ]ComboBox Cells

[·      ]MaskEdit Cells

[·      ]IntegerEdit Cells

[·      ]DoubleEdit Cells

[·      ]PercentEdit Cells

[·      ]UpDownEdit Cells

[·      ]Currency Cells

 

###### []{#_Basic_Cell_Types}4.1.1.2.1.1 Basic Cell Types {#basic-cell-types style="tab-stops: 0pt"}

Basic controls like Check Boxes can be implemented within a grid cell. The list of cell types and their usages are tabulated in the following table. The table also lists the format string for the individual cell types.

 Table 1: Basic Cell Types Property Table


  ----------- ------------------ --------------------------------
  Cell Type   Cell Type String   Cell Usage
  Header      "Header"           Used as row and column headers
  Static      "Static"           Cannot be edited
  Check Box   "CheckBox"         Used for toggling options
  Image       "ImageCell"        Used to display pictures
  TextBlock   "TextBlock"        Used to display text
  ----------- ------------------ --------------------------------


 

To set up the desired cell type, the Style.CellType property must be assigned with the corresponding format string. For instance, if you want to display a Check box control in the cell (2, 2), then you have to use the following code.

 

Displaying a Check Box Control in a Cell:

 

+-----------------------------------------------------------------------------------------+
| **[\[C#\]]**                                        |
|                                                                                         |
| []                                                  |
|                                                                                         |
| [GridStyleInfo style = gridControl1.Model\[2, 2\];] |
|                                                                                         |
| [style.CellType = \"CheckBox\";]                    |
+-----------------------------------------------------------------------------------------+

 

 

Displaying a Cell as a Header Cell:

 

+-----------------------------------------------------------------------------------------+
| **[\[C#\]]**                                        |
|                                                                                         |
| []                                                  |
|                                                                                         |
| [GridStyleInfo style = gridControl1.Model\[2, 2\];] |
|                                                                                         |
| [style.CellType = \"Header\";]                      |
+-----------------------------------------------------------------------------------------+

 

Displaying a Cell as a Static Cell:

 

+-----------------------------------------------------------------------------------------+
| **[\[C#\]]**                                        |
|                                                                                         |
| []                                                  |
|                                                                                         |
| [GridStyleInfo style = gridControl1.Model\[2, 2\];] |
|                                                                                         |
| [style.CellType = \"Static\";]                      |
+-----------------------------------------------------------------------------------------+

 

Displaying a Cell as the Image Cell:

 

+-----------------------------------------------------------------------------------------+
| **[\[C#\]]**                                        |
|                                                                                         |
|                                                                                         |
|                                                                                         |
| [GridStyleInfo style = gridControl1.Model\[2, 2\];] |
|                                                                                         |
| [style.CellType = \"ImageCell\";]                   |
+-----------------------------------------------------------------------------------------+

 

Displaying a Cell as the TextBlock Cell:

[] 

+-----------------------------------------------------------------------------------------+
| **[\[C#\]]**                                        |
|                                                                                         |
|                                                                                         |
|                                                                                         |
| [GridStyleInfo style = gridControl1.Model\[2, 2\];] |
|                                                                                         |
| [style.CellType = \"TextBlock\";]                   |
+-----------------------------------------------------------------------------------------+

 

A sample output is shown in the following screenshot:

{border="0"}

Figure 23: Basic Cell Types

 

###### 4.1.1.2.1.2 TextBlock Cells {#textblock-cells style="tab-stops: 0pt"}

TextBlock cells enable the grid cell as TextBlock so that it displays text that cannot be edited further. The following table consists of properties that are used to customize these cells.

[] 

Table 2: TextBlock Cell Type Property Table


  ----------- -------------------------------------------- -------- ------------------ ------------------------------------------------
  Property    Description                                  Type     Value It Accepts   Property Syntax
  CellType    Set to "TextBlock".                          Normal   String             grid.Model\[6, 2\].CellType = \" TextBlock \";
  CellValue   Sets the value to be displayed in the cell   Normal   String             grid.Model\[6, 2\].CellValue =  "Textblock1";
  ----------- -------------------------------------------- -------- ------------------ ------------------------------------------------


 

Creating a TextBlock Cell

The following code illustrates the implementation of  TextBlock Control in the grid cells.

 

+--------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                       |
|                                                                                                        |
| [grid.Model\[rowIndex, colIndex\].Text = \"TextBlock Cells \";]    |
|                                                                                                        |
| [rowIndex++;]                                                      |
|                                                                                                        |
| [grid.Model\[rowIndex, colIndex\].CellType = \"TextBlock\";]       |
|                                                                                                        |
| [grid.Model\[rowIndex, colIndex\].CellValue = \"TextBlock1\";]     |
|                                                                                                        |
| [grid.Model\[rowIndex, colIndex + 2\].CellType = \"TextBlock\";]   |
|                                                                                                        |
| [grid.Model\[rowIndex, colIndex + 2\].CellValue = \"TextBlock2\";] |
+--------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output is displayed:

 

{border="0"}***[]***

***[]*** 

***[]*** 

Figure 24: TextBlock Cells

 

###### 4.1.1.2.1.3 TextBox Cells {#textbox-cells style="tab-stops: 0pt"}

TextBox cells enable the grid cell as TextBox so that any text can be typed inside the control. It is the default type for grid cells. The following table consists of properties that are used to customize these cells.

 

Table 3: TextBox Cell Type Property Table

  ----------- -------------------------------------------- -------- ------------------- ---------------------------------------------
  Property    Description                                  Type     Value it  Accepts   Property Syntax
  CellType    Set to "TextBox".                            Normal   String              grid.Model\[6, 2\].CellType = \"TextBox\";
  CellValue   Sets the value to be displayed in the cell   Normal   String              grid.Model\[6, 2\].CellValue =  "Textbox1";
  ----------- -------------------------------------------- -------- ------------------- ---------------------------------------------

[] 

Creating a TextBox cell

The following code illustrates the implementation of  TextBox Control in the grid cells.

.

+------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                      |
| [grid.Model\[rowIndex, colIndex\].CellType = \"TextBox\";]       |
|                                                                                                      |
| [grid.Model\[rowIndex, colIndex\].CellValue = \"TextBox1\";]     |
|                                                                                                      |
| [grid.Model\[rowIndex, colIndex + 2\].CellType = \"TextBox\";]   |
|                                                                                                      |
| [grid.Model\[rowIndex, colIndex + 2\].CellValue = \"TextBox2\";] |
+------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output is displayed:

[] 

{border="0"}***[]***

***[]*** 

Figure 25: TextBox cells

***[]*** 

###### []{#_CheckBox_Cells}4.1.1.2.1.4 CheckBox Cells {#checkbox-cells style="tab-stops: 0pt"}

The CheckBox cells enable the grid cell as a checkbox. The following table consists of properties used to customize these cells.

Table 4: CheckBox Cell Type Property Table

  ------------- ---------------------------------------------------------------------------------- -------- ------------------ ----------------------------------------------
  Property      Description                                                                        Type     Value It Accepts   Property Syntax
  CellType      Set to "CheckBox".                                                                 Normal   String             grid.Model\[6, 2\].CellType = \"CheckBox\";
  CellValue     Sets true or false for the checkbox in order to select and deselect respectively   Normal   Boolean            grid.Model\[6, 2\].CellValue = true;
  Description   Sets options for the control namely Enable, Disable and TriState                   Normal   String             grid.Model\[6, 2\].Description= \"Enabled\";
  Enabled       Shows whether the control is enabled or disabled (by default it is true)           Normal   Boolean            grid.Model\[6, 2\].Enabled = true;
  ------------- ---------------------------------------------------------------------------------- -------- ------------------ ----------------------------------------------

[] 

Creating a CheckBox Cell

The following code illustrates the implementation of  CheckBox Control in the grid cells.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                 |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex\].CellValue = [false];]                 |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex\].CellType = [\"CheckBox\"];]        |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex\].Description = [\"Enabled\"];]      |
|                                                                                                                                  |
| [           ]                                                                                |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex + 1\].CellValue = [true];]              |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex + 1\].CellType = [\"CheckBox\"];]    |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex + 1\].Description = [\"TriState\"];] |
|                                                                                                                                  |
| []                                                                                           |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex + 2\].CellValue = [true];]              |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex + 2\].Description = [\"Disabled\"];] |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex + 2\].CellType = [\"CheckBox\"];]    |
|                                                                                                                                  |
| [grid.Model\[rowIndex, colIndex + 2\].Enabled = [false];]               |
|                                                                                                                                  |
| []                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------+

 

When the code runs, the following output is displayed:

[] 

{border="0"}***[]***

Figure 26: CheckBox cells

***[]*** 

 

###### 4.1.1.2.1.5 Data Template Cells {#data-template-cells style="tab-stops: 0pt"}

 

This cell builds a custom data template that can be used to set enriched styles for associated cells. To achieve this, you need to create custom data templates and by making use of QueryCellInfo event, you can assign the CellType, CellEditTemplateKey, CellItemTemplateKey to display the enriched styles. CellEditTemplateKey specifies the CellRenderer while editing and the CellItemTemplateKey specifies the CellRenderer on cell load time. The following is the sample code to set two different styles inside a cell. It includes a TextBlock cell type and a TextBox cell type while editing (CellEditTemplateKey). While loading the cell, it loads as two TextBlocks (CellItemTemplateKey).

[] 

Data Template Definition

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| [       ][\<[DataTemplate][ x]:[Key]=\"editableEmployee\"\>]                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| [            ][\<[StackPanel][ Orientation]=\"Horizontal\"[ Background]=\"Transparent\"\>]                                                  |
|                                                                                                                                                                                                                                                                                                     |
| [                [\<]TextBlock[ FontWeight][=\"Bold\"]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [                          [ Text][=\"{][Binding][ Path][=CellBoundValue.Name}\"] ]                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| [                          [ Width][=\"70\" /\>]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| [               ][\<[TextBox][ Text]=\"{[Binding][ Path]=CellBoundValue.Title,[Mode]=TwoWay}\"] |
|                                                                                                                                                                                                                                                                                                     |
| [                         syncfusion[:]BindingHelper.UpdateSourceOnChange[=\"True\"]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [                        [ BorderThickness][=\"0\"]  ]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [                        [ Padding][=\"0\"] ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [                        [ Margin][=\"0\"] ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [                        [ Width][=\"130\"]   [ /\>]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [            [\</]StackPanel[\>]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| [        [\</]DataTemplate[\>]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [        ][\<[DataTemplate][ x]:[Key]=\"nonEditableEmployee\"\>]                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [            ][\<[StackPanel][ Orientation]=\"Horizontal\"[ Background]=\"Transparent\"\>]                                                  |
|                                                                                                                                                                                                                                                                                                     |
| [                [\<]TextBlock[ FontWeight][=\"Bold\"] ]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [                          [ Text][=\"{][Binding][ Path][=CellBoundValue.Name}\"] ]                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| [                          [ Width][=\"70\"/\>]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                     |
| [                [\<]TextBlock[ Text][=\"{]Binding[ Path][=CellBoundValue.Title}\"] [ /\>]]                                         |
|                                                                                                                                                                                                                                                                                                     |
| [            [\</]StackPanel[\>]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| [        [\</]DataTemplate[\>]]                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Setting Up the Data Template Cell and Assigning the Cell Template

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [this.grid.QueryCellInfo += new Syncfusion.Windows.Controls.Grid.GridQueryCellInfoEventHandler(grid_QueryCellInfo); ]                                     |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [        void grid_QueryCellInfo(object sender, Syncfusion.Windows.Controls.Grid.GridQueryCellInfoEventArgs e)]                                           |
|                                                                                                                                                                                               |
| [        {]                                                                                                                                               |
|                                                                                                                                                                                               |
| [            if (e.Cell.RowIndex \> 1 && e.Cell.ColumnIndex == 2)]                                                                                        |
|                                                                                                                                                                                               |
| [            {]                                                                                                                                           |
|                                                                                                                                                                                               |
| [                e.Style.CellType = \"DataBoundTemplate\";]                                                                                               |
|                                                                                                                                                                                               |
| [                e.Style.CellEditTemplateKey = \"editableEmployee\";]                                                                                     |
|                                                                                                                                                                                               |
| [                e.Style.CellItemTemplateKey = \"nonEditableEmployee\";]                                                                                  |
|                                                                                                                                                                                               |
| [                e.Style.CellValue = employeesSource.Employees\[e.Cell.RowIndex % employeesSource.Employees.Count\];//Values to be displayed in the cell] |
|                                                                                                                                                                                               |
| [            }]                                                                                                                                           |
|                                                                                                                                                                                               |
| [               }]                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Output

The following output is generated using code above:

 

 {border="0"}

***[]*** 

Figure 27: Data Template with Cell Template Assigned

 

***[]*** 

###### []{#_ComboBox_Cells}4.1.1.2.1.6 ComboBox Cells {#combobox-cells style="tab-stops: 0pt"}

A combo box is a component with a drop-down arrow that users click to display an associated list of choices. The user displays the list by clicking or dragging the drop-down arrow. This cell type allows you to choose the cell value from a drop-down list.

The following table lists various properties that can affect combo box cells.

Table 5 : ComboBox Cell Type Property Table


+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+
| Property        | Description                                                                                              | Value It Accepts                                                     | Property Syntax                                                    |
+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+
| CellType        | Set to "ComboBox" for a Combo box control                                                                | String                                                               | grid.Model\[6, 2\].CellType                                        |
|                 |                                                                                                          |                                                                      |                                                                    |
|                 |                                                                                                          |                                                                      | = \"ComboBox\";                                                    |
+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+
| ChoiceList      | Not Applicable                                                                                           | Not Applicable                                                       | Not Applicable                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+
| DropDownStyle   | Determines the drop-down cell behavior.                                                                  | GridDropDownStyle Enumeration                                        | grid.Model\[6, 2\].DropDownStyle = GridDropDownStyle.AutoComplete; |
|                 |                                                                                                          |                                                                      |                                                                    |
|                 | [·      ]Editable( Not Applicable)                                          |                                                                      |                                                                    |
|                 |                                                                                                          |                                                                      |                                                                    |
|                 | [·      ]Autocomplete                                                       |                                                                      |                                                                    |
|                 |                                                                                                          |                                                                      |                                                                    |
|                 | [·      ]Exclusive ( Not Applicable)                                        |                                                                      |                                                                    |
+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+
| ItemsSource     | Specifies the binding source for the Combo box.                                                          | Collection                                                           | grid.Model\[6, 2\].ItemsSource = employeesSource.Employees;        |
+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+
| Display Member  | String that names the public property from the data source object to be displayed in the cell.           | String                                                               | grid.Model\[6, 2\].DisplayMember = \"Name\";                       |
+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+
| CellValue       | String that names the public property from the data source object to be used as the value for this cell. | The value to be displayed in the ComboBox from the given data source | grid.Model\[6, 2\].ValueMember                                     |
|                 |                                                                                                          |                                                                      |                                                                    |
|                 |                                                                                                          |                                                                      |  = employeesSource.Employees\[0\];                                 |
+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+
| ValueMember     | Not Applicable                                                                                           | Not Applicable                                                       | Not Applicable                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+--------------------------------------------------------------------+


 

 

Using ItemsSource

The combo boxes created using ItemsSource class ensure that the options available in the drop-down list are populated from the data source the combo box is bound to. The combo boxes in the following examples are bound to ObservableCollection employees. The following code shows the implementation of ObservableCollection for EmployeesSource class. It has two properties namely Name and Title of the employees.

**[]** 

Setting Up ItemsSource to the Combo Box

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ [class] [EmployeesSource]]                                                      |
|                                                                                                                                                                                                                             |
| [    {]                                                                                                                                                                                 |
|                                                                                                                                                                                                                             |
| [        [private] [ObservableCollection]\<[Employee]\> employees;]                                                |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [        [public] [ObservableCollection]\<[Employee]\> Employees]                                                  |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [            [get] { [return] employees; }]                                                                                                   |
|                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [        [public] EmployeesSource()]                                                                                                                               |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [            employees = [new] [ObservableCollection]\<[Employee]\>();]                                            |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [                employees.Add([new] [Employee]([\"Matt\"], [\"Program Manager\"]));]      |
|                                                                                                                                                                                                                             |
| [                employees.Add([new] [Employee]([\"Joan\"], [\"Developer\"]));]            |
|                                                                                                                                                                                                                             |
| [                employees.Add([new] [Employee]([\"Mark\"], [\"Programming Writer\"]));]   |
|                                                                                                                                                                                                                             |
| [                employees.Add([new] [Employee]([\"Mary\"], [\"Test Lead\"]));]            |
|                                                                                                                                                                                                                             |
| [                employees.Add([new] [Employee]([\"Karen\"], [\"Developer\"]));]           |
|                                                                                                                                                                                                                             |
| [                employees.Add([new] [Employee]([\"George\"], [\"Programming Writer\"]));] |
|                                                                                                                                                                                                                             |
| [                employees.Add([new] [Employee]([\"Peter\"], [\"Program Manager\"]));]     |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [        }    }]                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [    [public] [class] [Employee] : [INotifyPropertyChanged]]                                  |
|                                                                                                                                                                                                                             |
| [    {]                                                                                                                                                                                 |
|                                                                                                                                                                                                                             |
| [        [private] [string] name;]                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [        [public] [string] Name]                                                                                                              |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [            [get] { [return] name; }]                                                                                                        |
|                                                                                                                                                                                                                             |
| [            [set]]                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [                name = [value];]                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [                OnPropertyChanged([\"Name\"]);]                                                                                                                |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [        [private] [string] title;]                                                                                                           |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [        [public] [string] Title]                                                                                                             |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [            [get] { [return] title; }]                                                                                                       |
|                                                                                                                                                                                                                             |
| [            [set]]                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [                title = [value];]                                                                                                                                 |
|                                                                                                                                                                                                                             |
| [                OnPropertyChanged([\"Title\"]);]                                                                                                               |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [        [public] Employee([string] name, [string] title)]                                                               |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [            [this].name = name;]                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [            [this].title = title;]                                                                                                                                |
|                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [        [public] [event] [PropertyChangedEventHandler] PropertyChanged;]                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [        [private] [void] OnPropertyChanged([string] propertyName)]                                                      |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [            [if] (PropertyChanged != [null])]                                                                                                |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [                PropertyChanged([this], [new] [PropertyChangedEventArgs](propertyName));]                            |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [    }]                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code sets the ItemSource values from the ObservableCollection.

 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [var][ style = grid.Model\[rowIndex,colIndex\];] |
|                                                                                                                                       |
| [style.ItemsSource = employeesSource.Employees;]                                                  |
|                                                                                                                                       |
| [style.CellType = [\"ComboBox\"];]                                        |
|                                                                                                                                       |
| [style.CellValue = employeesSource.Employees\[0\];]                                               |
|                                                                                                                                       |
| [style.DisplayMember = **[\"Name\"];**]                                   |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

In the above sample code the "Name" is used as the DisplayMember. Therefore, the Combo box will be filled with the Name as the CellValue.

[] 

Output

The following output is generated using code above:

 

 {border="0"}

***[]*** 

Figure 28: Combo Box using DisplayMember as Name

 

If we set the DisplayMember to the "Title", the combobox will be filled with the Title object. The following code explains the same.

 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [var][ style = grid.Model\[rowIndex,colIndex\];] |
|                                                                                                                                       |
| [style.ItemsSource = employeesSource.Employees;]                                                  |
|                                                                                                                                       |
| [style.CellType = [\"ComboBox\"];]                                        |
|                                                                                                                                       |
| [style.CellValue = employeesSource.Employees\[0\];]                                               |
|                                                                                                                                       |
| [style.DisplayMember = **[\"Title\"];**]                                  |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated from the above code:

 

 {border="0"}

 

Figure 29: Combo Box using DisplayMember as Title

***[]*** 

ComboBox with DataTemplate

DataTemplate can be used to format the view of the Combo box. The following code shows the definition of the DataTemplate in XAML.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\<[DataTemplate][ x]:[Key]=\"editableEmployee\"\>]                                                        |
|                                                                                                                                                                                                                |
| [                    \<StackPanel[ Orientation]=\"Horizontal\"\>]                                                                                      |
|                                                                                                                                                                                                                |
| [                        \<TextBlock [ Width]=\"150\"[ Text]=\"{Binding[ Path]=Name}\"[ ]] |
|                                                                                                                                                                                                                |
| [                                    VerticalAlignment=\"Center\" FontSize=\"14\"/\>]                                                                                      |
|                                                                                                                                                                                                                |
| [                        \<TextBlock[ Text]=\"{Binding[ Path]=Title}\"[ ]]                                     |
|                                                                                                                                                                                                                |
| [                                   HorizontalAlignment=\"Right\" ]                                                                                                        |
|                                                                                                                                                                                                                |
| [                                   VerticalAlignment=\"Center\" FontSize=\"12\"  /\>]                                                                                     |
|                                                                                                                                                                                                                |
| [                    \</StackPanel\>]                                                                                                                                      |
|                                                                                                                                                                                                                |
| [\</DataTemplate\>]                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code shows the implementation of the above DataTemplate.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [var][ style = grid.Model\[rowIndex,colIndex\];] |
|                                                                                                                                       |
| [style.CellItemTemplateKey = [\"editableEmployee\"];]                     |
|                                                                                                                                       |
| [style.CellType = [\"ComboBox\"];]                                        |
|                                                                                                                                       |
| [style.ItemsSource   = employeesSource.Employees;]                                                |
|                                                                                                                                       |
| [style.CellValue = employeesSource.Employees\[0\];]                                               |
|                                                                                                                                       |
| [style.DisplayMember = [\"Name\"];]                                       |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using code above:

[] 

{border="0"}

 

Figure 30: ComboBox is displayed with DataTemplate

 

###### 4.1.1.2.1.7 MaskEdit Cells {#maskedit-cells style="tab-stops: 0pt"}

The MaskEdit cells enable the grid cell to customize the way values are displayed. Masking can be achieved using this cell type. The MaskEdit cells do not accept the values more than the masked type. The following table consists of properties that are used to customize these cells.

 

Table 6: MaskEdit Cell Type Property Table

+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------+---------------------------------------------------------------------------------------------+
| Property    | Description                                                                                               | Type        | Value It Accepts      | Property Syntax                                                                             |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------+---------------------------------------------------------------------------------------------+
| CellType    | Set to "MaskEdit".                                                                                        | Normal      | String                | grid.Model\[6, 2\].CellType = \"MaskEdit\";                                                 |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------+---------------------------------------------------------------------------------------------+
| CellValue   | Sets the value to be displayed in the cell                                                                | Normal      | Number (only)         | grid.Model\[6, 2\].CellValue =  08192010;                                                   |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------+---------------------------------------------------------------------------------------------+
| MaskEdit    | Sets the mask edit style                                                                                  | Normal      | GridMaskEditStyleInfo |             this.grid.Model\[rowIndex, colIndex\].MaskEdit = GridMaskEditStyleInfo.Default; |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------+---------------------------------------------------------------------------------------------+
| Mask        | Formats the number and masks according to the given Mask string. See the Property syntax for sample code. | Normal      | String                | this.grid.Model\[rowIndex, colIndex\].MaskEdit.Mask                                         |
|             |                                                                                                           |             |                       |                                                                                             |
|             |                                                                                                           |             |                       |  = \"00/00/0000\";                                                                          |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------+---------------------------------------------------------------------------------------------+

 

Creating a MaskEdit Cell

**[]** 

The following code describes the implementation of  MaskEdit Control in the grid cells.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                          |
| [            [this].grid.Model\[rowIndex, colIndex\].CellType = [\"MaskEdit\"];]        |
|                                                                                                                                                                          |
| [            [this].grid.Model\[rowIndex, colIndex\].MaskEdit = ]                                               |
|                                                                                                                                                                          |
| [            GridMaskEditStyleInfo][.Default;]                                   |
|                                                                                                                                                                          |
| [            [this].grid.Model\[rowIndex, colIndex\].MaskEdit.Mask = [\"00/00/0000\"];] |
|                                                                                                                                                                          |
| [            [this].grid.Model\[rowIndex, colIndex\].CellValue = 08192010;]                                     |
|                                                                                                                                                                          |
| [            rowIndex++;]                                                                                                            |
|                                                                                                                                                                          |
| [            [var] maskStyleInfo1 = [this].grid.Model\[rowIndex, colIndex\];]              |
|                                                                                                                                                                          |
| [            maskStyleInfo1.CellType = [\"MaskEdit\"];]                                                      |
|                                                                                                                                                                          |
| [            maskStyleInfo1.MaskEdit = [GridMaskEditStyleInfo].Default;]                                     |
|                                                                                                                                                                          |
| [            maskStyleInfo1.MaskEdit.Mask = [\"00:00:00\"];]                                                 |
|                                                                                                                                                                          |
| [            maskStyleInfo1.CellValue = 043549;]                                                                                     |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

###### 4.1.1.2.1.8 IntegerEdit Cells {#integeredit-cells style="tab-stops: 0pt"}

 

IntegerEdit is a specialized cell type that restricts the data entry to integers. The following table consists of GridStyleInfo properties that are used to customize these cells.

 

Table 7:IntegerEdit Cell Type Property Table


  ---------------------- ------------------------------------------------- -------- ------------------ ---------------------------------------------------------------------------------------------------------------------
  Property               Description                                       Type     Value it Accepts   Property Syntax
  CellType               Set to "IntegerEdit"                              Normal   String             grid.Model\[6, 2\].CellType = \"IntegerEdit\";
  NumberGroupSeparator   Sets the string that separates groups of digits   Normal   String             grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberGroupSeparator = \";\" };
  NumberGroupSizes       Sets the number of digits in each group           Normal   int\[\]            grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberGroupSizes = new int\[\] { 2, 3, 4 }};
  ---------------------- ------------------------------------------------- -------- ------------------ ---------------------------------------------------------------------------------------------------------------------


 

Creating Integer Edit Cells

[] 

The following code illustrates the creation of three different Integer Edit Cells.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| [            int][\[\] sizes = { 2, 3, 4 };]                                                                                     |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].CellType = [\"IntegerEdit\"];]                                                                                            |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].IsEditable = [true];]                                                                                                        |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].NumberFormat = [new] [NumberFormatInfo] { NumberGroupSeparator = [\"@\"] };] |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                                           |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].CellValue = 1000; ]                                                                                                                               |
|                                                                                                                                                                                                                       |
| [            ]                                                                                                                                                                    |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].CellType = [\"IntegerEdit\"];]                                                                                            |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].IsEditable = [true];]                                                                                                        |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].NumberFormat = [new] [NumberFormatInfo] { NumberGroupSeparator = [\",\"] };] |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                                           |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].CellValue = 1;]                                                                                                                                   |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].CellType = [\"IntegerEdit\"];]                                                                                            |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].IsEditable = [true];]                                                                                                        |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].NumberFormat = [new] [NumberFormatInfo] { NumberGroupSeparator = [\";\"] };] |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                                           |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].CellValue = 222222;]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays:

[] 

{border="0"}

***[]*** 

Figure 31: Integer Edit Cells

***[]*** 

 

###### 4.1.1.2.1.9 DoubleEdit Cells {#doubleedit-cells style="tab-stops: 0pt"}

**[]** 

**DoubleEdit** cell restricts you to enter only double (value type) values into the cell. This is useful to display System.Double type values. The following table consists of **GridStyleInfo** properties that are used to customize these cells.

[] 

[] 

Table 8:DoubleEdit Cell Type Property Table

  Property                 Description                                                                   Type     Value It Accepts   Property Syntax
  ------------------------ ----------------------------------------------------------------------------- -------- ------------------ ----------------------------------------------------------------------------------------------------------------------
  Cell Type                Set to "DoubleEdit"                                                           Normal   String             grid.Model\[6, 2\].CellType = \"DoubleEdit\";
  NumberGroupSeparator     Sets the string that separates groups of digits to the left of the decimal.   Normal   String             grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberGroupSeparator = \"@\" };
  NumberDecimalSeparator   Sets the string to use as decimal separator.                                  Normal   String             grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberDecimalSeparator = \".\" };
  NumberDecimalDigits      Sets the number of decimal places.                                            Normal   int                grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberDecimalDigits = 0};
  NumberGroupSizes         Sets the number of digits in each group to the left of the decimal.           Normal   Int\[\]             grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberGroupSizes = new int\[\] { 2, 3, 4 }};

 

Creating DoubleEdit Cells

[] 

The following code illustrates the creation of three double edit cells using different group separators and different decimal digits.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [grid.Model\[6, 2\].CellType = [\"DoubleEdit\"];]                                                                                  |
|                                                                                                                                                                                                |
| [            [this].grid.Model.CoveredCells.Add([new] [CoveredCellInfo](6, 2, 6, 3));]   |
|                                                                                                                                                                                                |
| [            grid.Model\[6, 2\].NumberFormat = [new] [NumberFormatInfo]]                                      |
|                                                                                                                                                                                                |
| [            {]                                                                                                                                            |
|                                                                                                                                                                                                |
| [                NumberGroupSeparator = [\"@\"],]                                                                                  |
|                                                                                                                                                                                                |
| [                NumberDecimalSeparator = [\".\"],]                                                                                |
|                                                                                                                                                                                                |
| [                NumberDecimalDigits = 0,]                                                                                                                 |
|                                                                                                                                                                                                |
| [                NumberGroupSizes = [new] [int]\[\] { 2, 3, 4 }]                                                 |
|                                                                                                                                                                                                |
| [            };]                                                                                                                                           |
|                                                                                                                                                                                                |
| [            grid.Model\[6, 2\].CellValue = 12345678.00;]                                                                                                  |
|                                                                                                                                                                                                |
| [            grid.Model\[8, 2\].CellType = [\"DoubleEdit\"];]                                                                      |
|                                                                                                                                                                                                |
| [            [this].grid.Model.CoveredCells.Add([new] [CoveredCellInfo](8, 2, 8, 8));]   |
|                                                                                                                                                                                                |
| [            grid.Model\[8, 2\].NumberFormat = [new] [NumberFormatInfo]]                                      |
|                                                                                                                                                                                                |
| [            {]                                                                                                                                            |
|                                                                                                                                                                                                |
| [                NumberGroupSeparator = [\",\"],]                                                                                  |
|                                                                                                                                                                                                |
| [                NumberDecimalSeparator = [\".\"],]                                                                                |
|                                                                                                                                                                                                |
| [                NumberDecimalDigits = 4,]                                                                                                                 |
|                                                                                                                                                                                                |
| [                NumberGroupSizes = [new] [int]\[\] { 2, 3, 4 }]                                                 |
|                                                                                                                                                                                                |
| [            };]                                                                                                                                           |
|                                                                                                                                                                                                |
| [            grid.Model\[8, 2\].CellValue = 12;]                                                                                                           |
|                                                                                                                                                                                                |
| [            grid.Model\[10, 2\].CellValue = 2345.00;]                                                                                                     |
|                                                                                                                                                                                                |
| [            grid.Model\[10, 2\].CellType = [\"DoubleEdit\"];]                                                                     |
|                                                                                                                                                                                                |
| [            [this].grid.Model.CoveredCells.Add([new] [CoveredCellInfo](10, 2, 10, 3));] |
|                                                                                                                                                                                                |
| [            grid.Model\[10, 2\].NumberFormat = [new] [NumberFormatInfo]]                                     |
|                                                                                                                                                                                                |
| [            {]                                                                                                                                            |
|                                                                                                                                                                                                |
| [                NumberGroupSeparator = [\";\"],]                                                                                  |
|                                                                                                                                                                                                |
| [                NumberDecimalSeparator = [\".\"],]                                                                                |
|                                                                                                                                                                                                |
| [                NumberDecimalDigits = 4,]                                                                                                                 |
|                                                                                                                                                                                                |
| [                NumberGroupSizes = [new] [int]\[\]{2, 3, 4}]                                                    |
|                                                                                                                                                                                                |
| [            };]                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays:

[] 

{border="0"}[]

***[]*** 

Figure 32: DoubleEdit Cells

***[]*** 

###### 4.1.1.2.1.10        PercentEdit Cells {#percentedit-cells style="tab-stops: 0pt"}

**[]** 

The PercentEdit cell type restricts you in data entry. This accepts only percentage values. The following table consists of GridStyleInfo properties that are used to customize these cells.

[] 

Table 9:PercentEdit Cell Type Property Table[]


+-----------------------+--------------------------------------------------------------------------------+-------------+------------------+--------------------------------------------------------------------------------------------------------------+
| Property              | Description                                                                    | Type        | Value It Accepts | Property Syntax                                                                                              |
+-----------------------+--------------------------------------------------------------------------------+-------------+------------------+--------------------------------------------------------------------------------------------------------------+
| CellType              | Set to "PercentEdit".                                                          | Normal      | String           | grid.Model\[6, 2\].CellType = \"PercentEdit\";                                                               |
+-----------------------+--------------------------------------------------------------------------------+-------------+------------------+--------------------------------------------------------------------------------------------------------------+
| PercentSymbol         | Allows to set any String as PercentSymbol                                      | Normal      | String           | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                                                      |
|                       |                                                                                |             |                  |                                                                                                              |
|                       |                                                                                |             |                  | PercentSymbol = \"%\"};                                                                                      |
+-----------------------+--------------------------------------------------------------------------------+-------------+------------------+--------------------------------------------------------------------------------------------------------------+
| PercentGroupSizes     | Sets the number of digits in each group to the left of the decimal.            | Normal      | int\[\]          | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                PercentGroupSizes = new int\[\] {3}}; |
+-----------------------+--------------------------------------------------------------------------------+-------------+------------------+--------------------------------------------------------------------------------------------------------------+
| PercentGroupSeparator | Sets the string that separates the group of digits to the left of the decimal. | Normal      | String           | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                PercentGroupSeparator = \",\"};       |
+-----------------------+--------------------------------------------------------------------------------+-------------+------------------+--------------------------------------------------------------------------------------------------------------+
| PercentDecimalDigits  | Sets the number of digits that appear after the decimal.                       | Normal      | int              | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                PercentDecimalDigits = 4};            |
+-----------------------+--------------------------------------------------------------------------------+-------------+------------------+--------------------------------------------------------------------------------------------------------------+


**[]** 

**[]** 

Creating PercentEdit cell

[] 

The following code illustrates the creation of two Percent Edit cells with different group sizes and decimal digits.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                 |
| [var][ percentStyleInfo = [this].grid.Model\[7, 2\];] |
|                                                                                                                                                                 |
| [            percentStyleInfo.CellType = [\"PercentEdit\"];]                                        |
|                                                                                                                                                                 |
| [            percentStyleInfo.NumberFormat = [new] [NumberFormatInfo]()]       |
|                                                                                                                                                                 |
| [            {]                                                                                                             |
|                                                                                                                                                                 |
| [                PercentSymbol = [\"%\"],]                                                          |
|                                                                                                                                                                 |
| [                PercentGroupSizes = [new] [int]\[\] { 1, 2, 3 },]                |
|                                                                                                                                                                 |
| [                PercentDecimalDigits = 2,]                                                                                 |
|                                                                                                                                                                 |
| [                PercentGroupSeparator = [\",\"],]                                                  |
|                                                                                                                                                                 |
| [            };]                                                                                                            |
|                                                                                                                                                                 |
| [            percentStyleInfo.CellValue = 19;]                                                                              |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [            [var] percentStyleInfo2 = [this].grid.Model\[9, 2\];]                |
|                                                                                                                                                                 |
| [            percentStyleInfo2.CellType = [\"PercentEdit\"];]                                       |
|                                                                                                                                                                 |
| [            percentStyleInfo2.NumberFormat = [new] [NumberFormatInfo]()]      |
|                                                                                                                                                                 |
| [            {]                                                                                                             |
|                                                                                                                                                                 |
| [                PercentSymbol = [\"%\"],]                                                          |
|                                                                                                                                                                 |
| [                PercentGroupSizes = [new] [int]\[\] { 3 },]                      |
|                                                                                                                                                                 |
| [                PercentDecimalDigits = 4,]                                                                                 |
|                                                                                                                                                                 |
| [                PercentGroupSeparator = [\",\"],]                                                  |
|                                                                                                                                                                 |
| [            };]                                                                                                            |
|                                                                                                                                                                 |
| [            percentStyleInfo2.CellValue = 91;]                                                                             |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| []                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

When the code runs, the following output displays:

[] 

{border="0"}[]

***[]*** 

Figure 33: Percent Edit Cells

 

###### 4.1.1.2.1.11        RichTextBox CellType {#richtextbox-celltype style="tab-stops: 0pt"}

 

RichTextBox CellType is used to format the cells, where each character, word or a line can be given different formats. RichTextBox Cell Type also supports Printing, copy/paste operation, Importing from Excel and Exporting to Excel. 

RichTextBox CellType can be defined in Grid using the following code snippet.

To set a cell as RichTextBox Cell type:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [              ][//Cell type as RichText and Cell Value as Paragraph Format][]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                   |
| [              ][this][.grid.Model\[rowIndex, colIndex\].CellType = ][\"RichText\"][;] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [              ][this][.grid.Model\[rowIndex, colIndex\].CellValue = \_paragraph;]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The Cell value of RichTextBox must be Paragraph as given in the following code snippet:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ][// Paragraph Format is supported for Rich Text Cell Type.][]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ][Paragraph][ \_paragraph = ][new][ ][Paragraph][();] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ][Run][ \_run1 = ][new][ ][Run][();]                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_run1.Text = ][\"This is RichText box Cell Type\"][;]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_run1.TextDecorations = ][TextDecorations][.Underline;]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ][Run][ \_run2 = ][new][ ][Run][();]                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_run2.Text = ][\"Various formatting can be done in Single Cell.\"][;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_run1.FontWeight = ][FontWeights][.Bold;]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_run2.Foreground = ][Brushes][.Green;]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ][Run][ \_run3 = ][new][ ][Run][();]                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_run3.Text = ][\"Rich Text cell type also supports Images\"][;]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_run3.FontSize = 16;]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_run3.FontStyle = ][FontStyles][.Italic;]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_paragraph.Inlines.Add(\_run1);]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_paragraph.Inlines.Add(\_run2);]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \_paragraph.Inlines.Add(\_run3);]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ]                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ][//Cell type as RichText and Cell Value as Paragraph Format.][]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ][this][.grid.Model\[rowIndex, colIndex\].CellType = ][\"RichText\"][;]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              ][this][.grid.Model\[rowIndex, colIndex\].CellValue = \_ paragraph;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 34: RichTextBox CellType

 

 

 

###### 4.1.1.2.1.12        UpDownEdit Cells {#updownedit-cells style="tab-stops: 0pt"}

**[]** 

UpDownEdit cell enables you to increase or decrease the cell value with a pair of arrow buttons in the cell. The following table consists of GridStyleInfo properties that are used to customize these cells.

[] 

Table 10:UpDownEdit Cell Type Property Table

  ---------- ----------------------------------------------------------------------------------- -------- ------------------ ------------------------------------------------
  Property   Description                                                                         Type     Value It Accepts   Property Syntax
  CellType   Set to "UpDownEdit".                                                                Normal   String             grid.Model\[6, 2\].CellType = \"UpDownEdit\";
  MaxValue   Sets the upper limit in the range of applicable values.                             Normal   Double             grid.Model\[6, 2\].UpDownEdit.MaxValue = 1000;
  MinValue   Sets the lower limit in the range of applicable values.                             Normal   Double             grid.Model\[6, 2\].UpDownEdit.MinValue = 500;
  Step       Sets the unit value to be increased /decreased when the spin buttons are clicked.   Normal   Double             grid.Model\[6, 2\].UpDownEdit.Step = 50;
  ---------- ----------------------------------------------------------------------------------- -------- ------------------ ------------------------------------------------

 

Creating UpDownEdit cell

The following code illustrates the creation of three different Up and Down controls in grid cells.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].CellType = [\"UpDownEdit\"];]                       |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].UpDownEdit.MinValue = 500;]                                                 |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].UpDownEdit.MaxValue = 1000;]                                                |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].UpDownEdit.Step = 50;]                                                      |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].HorizontalAlignment = [HorizontalAlignment].Right;] |
|                                                                                                                                                 |
| []                                                                                                          |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].CellType = [\"UpDownEdit\"];]                       |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].UpDownEdit.MinValue = 5;]                                                   |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].UpDownEdit.MaxValue = 100;]                                                 |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].UpDownEdit.Step = 5;]                                                       |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].HorizontalAlignment = [HorizontalAlignment].Right;] |
|                                                                                                                                                 |
| []                                                                                                          |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].CellType = [\"UpDownEdit\"];]                       |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].UpDownEdit.MinValue = 10;]                                                  |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].UpDownEdit.MaxValue = 18;]                                                  |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].UpDownEdit.Step = 2;]                                                       |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].HorizontalAlignment = [HorizontalAlignment].Right;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays:

[] 

 

{border="0"}

***[]*** 

Figure 35: UpDown Edit cells

 

 

###### []{#_Currency_Cells}4.1.1.2.1.13        Currency Cells {#currency-cells style="tab-stops: 0pt"}

[] 

Currency cell is useful to represent monetary values to achieve accuracy in calculations. This stripes the currency sign in the cell and attempts to parse only the number from the input.

The following table consists of GridStyleInfo properties that are used to customize these cells:

[] 

Table 11:Currency Cell Type Property Table

+-------------------------+---------------------------------------------------------------------+-------------+------------------+-------------------------------------------------------------------------------------------------------+
| Property                | Description                                                         | Type        | Value It Accepts | Property Syntax                                                                                       |
+=========================+=====================================================================+=============+==================+=======================================================================================================+
| CellType                | Set to "CurrencyEdit".                                              | Normal      | string           | grid.Model\[6, 2\].CellType = \"CurrencyEdit\";                                                       |
+-------------------------+---------------------------------------------------------------------+-------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencyDecimalDigits   | Sets the number of decimal places in currency value.                | Normal      | Int              | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                                               |
|                         |                                                                     |             |                  |                                                                                                       |
|                         |                                                                     |             |                  | CurrencyDecimalDigits = 2               };                                                            |
+-------------------------+---------------------------------------------------------------------+-------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencyNegativePattern | Sets the format pattern for negative currency values.               | Normal      | Int              | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                                               |
|                         |                                                                     |             |                  |                                                                                                       |
|                         |                                                                     |             |                  | CurrencyNegativePattern = 11 };                                                                       |
+-------------------------+---------------------------------------------------------------------+-------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencyPositivePattern | Sets the format pattern for positive currency values.               | Normal      | Int              | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                                               |
|                         |                                                                     |             |                  |                                                                                                       |
|                         |                                                                     |             |                  | CurrencyPositivePattern = 1 };                                                                        |
+-------------------------+---------------------------------------------------------------------+-------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencySymbol          | Sets the string to use as currency symbol.                          | Normal      | String           | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{CurrencySymbol = \"\$\"};                      |
+-------------------------+---------------------------------------------------------------------+-------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencyGroupSizes      | Sets the number of digits in each group to the left of the decimal. | Normal      | int\[\]          | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{CurrencyGroupSizes = new int\[\] { 2, 3, 4 }}; |
+-------------------------+---------------------------------------------------------------------+-------------+------------------+-------------------------------------------------------------------------------------------------------+

**[]** 

Creating a Currency Cell

[] 

Create a Currency Cell with a negative currency value and '\$' as the currency symbol. The negative values are automatically converted into positive values and displayed.

The following code illustrates this:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                               |
| [grid.Model\[6, 2\].CellType = [\"CurrencyEdit\"];]                               |
|                                                                                                                                               |
| [grid.Model\[6, 2\].CurrencyEdit.MinValue = 5;]                                                           |
|                                                                                                                                               |
| [grid.Model\[6, 2\].CurrencyEdit.MaxValue = 1000;]                                                        |
|                                                                                                                                               |
| [grid.Model\[6, 2\].NumberFormat = [new] [NumberFormatInfo]] |
|                                                                                                                                               |
| [            {]                                                                                           |
|                                                                                                                                               |
| [                CurrencyPositivePattern = 0,]                                                            |
|                                                                                                                                               |
| [                CurrencyDecimalDigits = 4,]                                                              |
|                                                                                                                                               |
| [                CurrencyNegativePattern = 0,]                                                            |
|                                                                                                                                               |
| [                CurrencySymbol = "\$",]                                                                  |
|                                                                                                                                               |
| [                CurrencyGroupSizes = new int\[\]{2, 3, 4}]                                               |
|                                                                                                                                               |
| [            };]                                                                                          |
|                                                                                                                                               |
| [grid.Model\[6, 2\].CellValue = **-4.0**;]                                                                |
|                                                                                                                                               |
| []                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

 

 Refer to [[CurrencyNegativePattern]](http://msdn.microsoft.com/en-us/library/system.globalization.numberformatinfo.currencynegativepattern.aspx) Codes from the following link:

[] 

When the code runs, the following output displays.

[] 

{border="0"}

***[]*** 

Figure 36: Currency Cell with Negative Value

***[]*** 

[] 

Create a Currency Cell with a positive value with '\$' as the currency symbol and with a different positive pattern.

The following code illustrates this:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                |
| **[]**                                                                                                     |
|                                                                                                                                                |
| [grid.Model\[10, 2\].CellType = [\"CurrencyEdit\"];]                               |
|                                                                                                                                                |
| [grid.Model\[10, 2\].CurrencyEdit.MinValue = 5;]                                                           |
|                                                                                                                                                |
| [grid.Model\[10, 2\].CurrencyEdit.MaxValue = 1000;]                                                        |
|                                                                                                                                                |
| [grid.Model\[10, 2\].NumberFormat = [new] [NumberFormatInfo]] |
|                                                                                                                                                |
| [            {]                                                                                            |
|                                                                                                                                                |
| [                CurrencyPositivePattern = 1,]                                                             |
|                                                                                                                                                |
| [                CurrencyDecimalDigits = 2,]                                                               |
|                                                                                                                                                |
| [                CurrencyNegativePattern = 11,]                                                            |
|                                                                                                                                                |
| [                CurrencySymbol = [\"\$\"],]                                       |
|                                                                                                                                                |
| [                CurrencyGroupSizes = [new] [int]\[\]{2, 3, 4}]  |
|                                                                                                                                                |
| [            };]                                                                                           |
|                                                                                                                                                |
| [grid.Model\[10, 2\].CellValue = 36.0;]                                                                    |
|                                                                                                                                                |
| []                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------+

 

Refer to [[CurrencyPositivePattern]](http://msdn.microsoft.com/en-us/library/system.globalization.numberformatinfo.currencypositivepattern.aspx) Codes from the following link:

[] 

When the code runs, the following output displays:

 

{border="0"}

***[]*** 

Figure 37: Currency Cell with Positive Value

 

**[]** 

[]{#_DoubleEdit_Cells}[]{#_IntegerEdit_Cells}[]{#_Data_Template_Cells}[]{#_TextBlock_Cells}[]{#_UpDownEdit_Cells} 

[]{#related-topics}

