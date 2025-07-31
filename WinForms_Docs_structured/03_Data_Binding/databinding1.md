---
title: databinding1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding1.md
created_at: 2025-07-03
---






##### Data Binding {#data-binding style="tab-stops: 0pt"}

[] 

The MultiColumnDropDownCombo control provides two properties to support data binding.

[] 

[·      ]To bind data to any object that implements the System.Collections.IEnumerable interface (such as System.Data.DataView, System.Collections.ArrayList, and System.Collections.Hashtable), or the IListSource interface, use the **DataSource** property to specify the data source. When you set the DataSource property, you must manually write the code to perform the data binding.

[·      ]To automatically bind a data listing control to a data source represented by a data source control, use the **DataSourceID** property and set its value to the **ID** property of the data source control to use. When you set the DataSourceID property, the MultiColumnDropDownCombo control automatically binds to the specified data source control. Therefore, you do not need to explicitly call the **DataBind** method.

[·      ]If the data source specified by the DataSource property contains multiple sources of data, use the **DataMember** property to specify the specific source to bind to the control. For example, if you have a System.Data.DataSet object with multiple tables, you must specify which table to bind to the control. After you have specified the data source, use the DataBind method to bind the data source to the control.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][ssw][:][MultiColumnDropDownCombo][ [ID][=\"MultiColumnDropDownCombo1\"] [runat][=\"server\" ] [Width][=\"200px\"] [PopupWidth][=\"300px\"] [AutoFormat][=\"Office2007 Luna Blue\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][HeaderStyle] [Font-Bold][=\"true\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][SelectedItemStyle] [BackColor][=\"#EEF6FF\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][ssw][:][MultiColumnDropDownCombo][\>]                                                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code snippet shows how to use the MultiColumnDropDownCombo control to display the items in the data source.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [ICollection][ CreateDataSource() ]                                                                                             |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [       [DataTable] dt = [new] [DataTable]();]                                                                                    |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [       dt.Columns.Add([new] [DataColumn]([\"IntegerValue\"], [typeof]([Int32])));]   |
|                                                                                                                                                                                                                                                      |
| [       dt.Columns.Add([new] [DataColumn]([\"StringValue\"], [typeof]([string])));]   |
|                                                                                                                                                                                                                                                      |
| [       dt.Columns.Add([new] [DataColumn]([\"CurrencyValue\"], [typeof]([double])));] |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [       [for]( [int] i = 0; i \< 5; i++ )]                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [       {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| [              [DataRow  ]dr = dt.NewRow();]                                                                                                                                |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [              dr\[0\] = i;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [              dr\[1\] = [\"Item\"] + i;]                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [              dr\[2\] = 1.23 \* (i+1);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [              dt.Rows.Add(dr);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [       }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [       [DataView] dv = [new] [DataView](dt);]                                                                                    |
|                                                                                                                                                                                                                                                      |
| [       [return] dv;]                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [void][ Page_Load([Object] sender, [EventArgs] e)]                                    |
|                                                                                                                                                                                                                                                      |
| [{ ]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [       [if]( !IsPostBack ) ]                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [       {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| [              MultiColumnDropDownCombo1.DataTextFormatField=[\"{StringValue}: {CurrencyValue}\"];]                                                                       |
|                                                                                                                                                                                                                                                      |
| [              [// Load this data only once.]]                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [              MultiColumnDropDownCombo1.DataSource = CreateDataSource();]                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| [              MultiColumnDropDownCombo1.DataBind();]                                                                                                                                            |
|                                                                                                                                                                                                                                                      |
| [       } ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 110

[] 

Data Binding to ArrayList

[] 

The following code example demonstrates how to bind data to an ArrayList.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [public][ [class] [Person]]                                                         |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [       [//fields]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [       [private] [int] m_nID = 0;]                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [       [private] [string] m_sLastName = [\"\"];]                                                                             |
|                                                                                                                                                                                                                                                    |
| [       [private] [string] m_sFirstName = [\"\"];        ]                                                                    |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [       [//constructor for Person class]]                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [       [public] Person( [int] nID, [string] sLastName, [string] sFirstName )]                             |
|                                                                                                                                                                                                                                                    |
| [       {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [              m_nID = nID;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [              m_sLastName = sLastName;]                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [              m_sFirstName = sFirstName;               ]                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [       }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [       ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [       [//Properties]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [       [public] [int] ID]                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [       {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [              [get]{ [return] m_nID;}]                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [              [set]{m_nID = [value];}]                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [       }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [       [public] [string] LastName]                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [       {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [              [get]{ [return] m_sLastName;}]                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [              [set]{m_sLastName = [value];}]                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [       }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [       [public] [string] FirstName]                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [       {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [              [get]{ [return] m_sFirstName;}]                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [              [set]{m_sFirstName = [value];}]                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [       }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [       MultiColumnDropDownCombo1.DataTextFormatField = [\"{LastName} {FirstName}\"];]                                                                                  |
|                                                                                                                                                                                                                                                    |
| [       ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [       [ArrayList] array = [new] [ArrayList]();]                                                                               |
|                                                                                                                                                                                                                                                    |
| [       array.Add( [new] [Person]( 0, [\"Davolio\"], [\"Nancy\"] ) );]                                 |
|                                                                                                                                                                                                                                                    |
| [       array.Add( [new] [Person]( 1, [\"Leverling\"], [\"Janet\"] ) );]                               |
|                                                                                                                                                                                                                                                    |
| [       array.Add( [new] [Person]( 2, [\"Peacock\"], [\"Margaret\"] ) );]                              |
|                                                                                                                                                                                                                                                    |
| [       array.Add( [new] [Person]( 3, [\"Buchanan\"], [\"Steven\"] ) );]                               |
|                                                                                                                                                                                                                                                    |
| [       array.Add( [new] [Person]( 4, [\"Suyama\"], [\"Michael\"] ) );]                                |
|                                                                                                                                                                                                                                                    |
| [       array.Add( [new] [Person]( 5, [\"King\"], [\"Robert\"] ) );]                                   |
|                                                                                                                                                                                                                                                    |
| [       ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [       MultiColumnDropDownCombo1.DataSource = array;]                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [       MultiColumnDropDownCombo1.DataBind();]                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

Figure 111

[] 

[]{#related-topics}

