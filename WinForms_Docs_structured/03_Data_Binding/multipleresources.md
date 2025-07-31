---
title: multipleresources.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\multipleresources.md
created_at: 2025-07-03
---








  









## Multiple Resources {#multiple-resources style="tab-stops: 0pt"}

Essential Schedule allows you to add multiple resources to the control. You can add appointments to each resource, drag appointments from resource column to the other, perform CRUD operations, set reminders, priority, recurrence, time mode and so on to appointments for each resource.Drag-and-drop can be performed directly on an appointment after it is added to the resource.

Adding multiple resources in the Schedule control allows you to perform a comparative analysis of resources. For example: If you want to track the agenda list for five employees of a company, for the month, you can create five resources in Essential Schedule and create appointments for each one of them as per the agenda. This will provide you a clear view on what the resources are occupied for a month and will let you assign tasks in accordance with the agenda.

You can also set header for resources created. This will help you to view the appointments for each resource with a resource name as the header.

[] 

Properties

Table 18: Multiple Resources - Properties

**[]** 


+-----------------------+-----------------------------------------------+----------------------+----------------------------------------------------+------------------------+
| Property              | Description                                   | Type of the property | Value it accepts                                   | Dependency             |
+=======================+===============================================+======================+====================================================+========================+
| Resources             | Used to add resource for Schedule             | List                 | [List\<ScheduleResource\>] | ShowResourceHeader,    |
|                       |                                               |                      |                                                    |                        |
|                       |                                               |                      | []                         | AllowMultipleResource  |
|                       |                                               |                      |                                                    |                        |
|                       |                                               |                      |                                                    |                        |
+-----------------------+-----------------------------------------------+----------------------+----------------------------------------------------+------------------------+
| AllowMultipleResource | Used to set enable/disable multiple resources | Boolean              | [True/False]               | ShowResourceHeader,    |
|                       |                                               |                      |                                                    |                        |
|                       |                                               |                      |                                                    | Resources              |
|                       |                                               |                      |                                                    |                        |
|                       |                                               |                      |                                                    |                        |
+-----------------------+-----------------------------------------------+----------------------+----------------------------------------------------+------------------------+
| ShowResourceHeader    | Used to show/hide the resource header.        | Boolean              | [True/False]               | AllowMultipleResource, |
|                       |                                               |                      |                                                    |                        |
|                       |                                               |                      |                                                    | Resources              |
|                       |                                               |                      |                                                    |                        |
|                       |                                               |                      |                                                    |                        |
+-----------------------+-----------------------------------------------+----------------------+----------------------------------------------------+------------------------+


[] 

More:





