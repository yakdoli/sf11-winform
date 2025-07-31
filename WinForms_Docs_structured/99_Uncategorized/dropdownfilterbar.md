---
title: dropdownfilterbar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\dropdownfilterbar.md
created_at: 2025-07-03
---






##### Dropdown FilterBar {#dropdown-filterbar style="tab-stops: 0pt"}

 

Dropdown FilterBar feature is similar to Text Box Filter instead of entering the key word the dropdown button can be used to filter the items.

 

To filter items using Dropdown Filter

The Dropdown button is used to filter the required items. We have to set the FilterBarStyle to change the FilterBar cell type.

 

**Xaml**


[ ][\<][syncfusion][:][GridDataVisibleColumn][ MappingName][=\"EmployeeID\"][ HeaderText][=\"Employee ID\"\>][]

[     ][\<][syncfusion][:][GridDataVisibleColumn.ColumnStyle][\>]

[\<][syncfusion][:][GridDataColumnStyle][ CellType][=\"IntegerEdit        \"][ HorizontalAlignment][=\"Right\"\>][]

[                  ][\</][syncfusion][:][GridDataColumnStyle][\>][]

[                  ][\</][syncfusion][:][GridDataVisibleColumn.ColumnStyle][\>][]

[                       ][\<][syncfusion][:][GridDataVisibleColumn.FilterBarStyle][\>][]

[                           ][\<][syncfusion][:][GridDataFilterBarStyle][ CellType][=\"ComboBox\" /\>][]

[                       ][\</][syncfusion][:][GridDataVisibleColumn.FilterBarStyle][\>][]

[ ][\</][syncfusion][:][GridDataVisibleColumn][\>][]


 

 

 

                                                


``` 
 <syncfusion:GridDataVisibleColumn MappingName="OrderID" HeaderText="Order ID">
```

``` 
                            <syncfusion:GridDataVisibleColumn.FilterBarStyle>
```

``` 
                                <syncfusion:GridDataFilterBarStyle CellType="ComboBox" ItemsSource="{Binding Source={StaticResource list}}" ValueMember="FirstName"  DisplayMember="LastName"  />
```

``` 
                            </syncfusion:GridDataVisibleColumn.FilterBarStyle>
```

``` 
                        </syncfusion:GridDataVisibleColumn>
```


 

 

{border="0"}

Figure 125: Dropdown FilterBar

 

Properties, Methods and Events tables

Properties

+--------------------+--------------------------------------------------------------------------------------------+-------------+------------------------+-----------------+
| Property           | Description                                                                                | Type        | Data Type              | Reference links |
+--------------------+--------------------------------------------------------------------------------------------+-------------+------------------------+-----------------+
| **CellType**       | Used to select ComboBox or TextBox                                                         | Dependency  | Enum                   | NA              |
+--------------------+--------------------------------------------------------------------------------------------+-------------+------------------------+-----------------+
| **ItemsSource**    | Used to bind the external item source                                                      | Dependency  | Object                 | NA              |
+--------------------+--------------------------------------------------------------------------------------------+-------------+------------------------+-----------------+
| **DisplayMember**  | This decides which member should be displayed.                                             | Dependency  | String                 | NA              |
+--------------------+--------------------------------------------------------------------------------------------+-------------+------------------------+-----------------+
| **ValueMember**    | Based on the value the items will be filtered.                                             | Dependency  | String                 | NA              |
+--------------------+--------------------------------------------------------------------------------------------+-------------+------------------------+-----------------+
| **FilterBarStyle** | This property used to set the style of the filterbar for the corresponding visible column. | Dependency  | GridDataFilterBarStyle | NA              |
|                    |                                                                                            |             |                        |                 |
|                    |                                                                                            |             |                        |                 |
+--------------------+--------------------------------------------------------------------------------------------+-------------+------------------------+-----------------+

 

 

[]{#related-topics}

