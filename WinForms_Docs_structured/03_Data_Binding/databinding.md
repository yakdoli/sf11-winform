---
title: databinding.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding.md
created_at: 2025-07-03
---








  









## Data Binding {#data-binding style="tab-stops: 0pt"}

The Data Binding feature enables to bind the Schedule control with external data sources like MS Access, SQL, XML, GenericList, and so on. While creating the data source, there are a few constraints on its structure. The data type of the column must match with the data type of the Schedule Appointments, Resources and Categories properties. This is the minimal set of requirements. If any of these requirements are not met, the Schedule control will throw an error when the data source is bound.

 

The Database always reflects the state of the schedule. This means that when the user operates on an appointment by adding, removing, dragging, or deleting appointments, the database is updated. Also, if the database is modified outside the schedule while it is still bound, the changes will be reflected on the Schedule control as well. A data source can be defined visually using the Visual Studio environment. In this way, you can create a strongly typed data source with appropriate columns and constraints.


Note: When the Schedule control is bound, make sure that there are no static appointments, if so the schedule control will throw an error. Also, ensure that the data type of the column matches with the data type of the Schedule Appointments, Resources and Categories properties.


 

For binding the Schedule control with the data source, you need to set the following properties.

 

[·      ]AppointmentDataSourceID

[·      ]CategoryDataSourceID

[·      ]ResourceDataSourceID

 

The below properties are used to map the various fields of Appointments, Categories and Resources properties of the Schedule control to particular fields from the Data Source.

 


  ---------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------
           Property        []   Fields[]
  AppointmentBindProperties                                  AllDayField, ContentField, SubjectField, UniqueIDField, OwnerField, EndTimeField, LocationValueField, StartTimeField
  CategoryBindProperties                                     DescriptionField, ExpandedField, InfoField, NameField, ShortNameField
  ResourceBindProperties                                     CategoryField, DescriptionField, InfoField, NameField
  ---------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------


 

More:







