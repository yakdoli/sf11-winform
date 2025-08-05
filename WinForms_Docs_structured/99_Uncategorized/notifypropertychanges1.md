---
title: notifypropertychanges1.md
original_path: WinForms_Docs/99_Uncategorized/notifypropertychanges1.md
created_at: 2025-08-05
---






#### Notify Property changes {#notify-property-changes style="tab-stops: 0pt"}

You can keep the grid notified of the underlying data source changes by setting a Boolean property called NotifyPropertyChanges. When it is set to true, the grid continues to listen to the data source changes and gets its field values updated accordingly. For this feature to take effect, the data source should implement the INotifyPropertyChanged interface.

 

The following code illustrates this property:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][GridDataControl][ x][:][Name][=\"grid\"][ [AutoPopulateColumns][=\"True\"] [AutoPopulateRelations][=\"False\"] [NotifyPropertyChanges][=\"True\"\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following image corresponds to the output of the above given code:

 

{border="0"}

Figure 150: NotifyPropertyChanges

[]{#related-topics}

