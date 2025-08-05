---
title: creatingtemplates.md
original_path: WinForms_Docs/99_Uncategorized/creatingtemplates.md
created_at: 2025-08-05
---








  









### Creating Templates {#creating-templates style="tab-stops: 0pt"}

[] 

Creating Templates through Code Behind

[] 

Using the class called ITemplates, you can create templates through code behind. Using **QueryCellStyleInfo** event, you can access the particular column and apply the templates for it. Refer the below code snippet, which illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [protected][ [void] GridGroupingControl1_QueryCellStyleInfo([object] sender, GridTableCellStyleInfoEventArgs e)] |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [    [//Look for the RecordField and AlternateField Cell.]]                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [    [if] (e.TableCellIdentity.TableCellType == GridTableCellType.RecordFieldCell \|\| e.TableCellIdentity.TableCellType == GridTableCellType.AlternateRecordFieldCell)]               |
|                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        [//Look for the Column Name \"Name of the Column specified\" in the GridGroupingControl when it get rendered]]                                                               |
|                                                                                                                                                                                                                                                 |
| [        [if] (e.TableCellIdentity.Column.MappingName == [\"City\"])]                                                                                           |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            [//Changes the EditItem template of the column specified as DropDownListBox ]]                                                                                           |
|                                                                                                                                                                                                                                                 |
| [            DropDownList dropdown = [new] DropDownList();]                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            dropdown.Items.Add([\"USA\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            dropdown.Items.Add([\"UK\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            [//Here add the DropDownListBox programmatically using ITemplate Interface]]                                                                                             |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            [TemplateClass] mytemp = [new] [TemplateClass](dropdown);]                                                                      |
|                                                                                                                                                                                                                                                 |
| [            e.TableCellIdentity.Column.ItemTemplate = mytemp;]                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [public][ [class] [TemplateClass] : [ITemplate]]                                            |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [    [private] [Control] m_ctrlChildControl = [null];]                                                                                       |
|                                                                                                                                                                                                                                                 |
| [    [public] TemplateClass([Control] ctrlChildControl)]                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        m_ctrlChildControl = ctrlChildControl;]                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [    [public] [void] InstantiateIn([Control] container)]                                                                                     |
|                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        container.Controls.Add(m_ctrlChildControl);]                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Sub] GridGroupingControl1_QueryCellStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridTableCellStyleInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [\'Look for the RecordField and AlternateField Cell.]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [If] e.TableCellIdentity.TableCellType = GridTableCellType.RecordFieldCell [OrElse] e.TableCellIdentity.TableCellType = GridTableCellType.AlternateRecordFieldCell [Then]]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [\'Look for the Column Name \"Name of the Column specified\" in the GridGroupingControl when it get rendered]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [If] e.TableCellIdentity.Column.MappingName = [\"City\"] [Then]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [\'Changes the EditItem template of the column specified as DropDownListBox ]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [Dim] dropdown [As] DropDownList = [New] DropDownList()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            dropdown.Items.Add([\"USA\"])]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            dropdown.Items.Add([\"UK\"])]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [\'Here add the DropDownListBox programmatically using ITemplate Interface]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [Dim] mytemp [As] TemplateClass = [New] TemplateClass(dropdown)]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.TableCellIdentity.Column.ItemTemplate = mytemp]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [End] [If]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [End] [If]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Class] TemplateClass]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [Implements] ITemplate]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [Private] m_ctrlChildControl [As] Control = [Nothing]]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [Public] [Sub] [New]([ByVal] ctrlChildControl [As] Control)]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        m_ctrlChildControl = ctrlChildControl]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [End] [Sub]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [Public] [Sub] InstantiateIn([ByVal] container [As] Control)]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        container.Controls.Add(m_ctrlChildControl)]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [End] [Sub]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Class]]                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 109

[]{#p93} 

[]{#related-topics}

