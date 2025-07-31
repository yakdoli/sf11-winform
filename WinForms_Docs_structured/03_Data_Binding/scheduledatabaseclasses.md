---
title: scheduledatabaseclasses.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\scheduledatabaseclasses.md
created_at: 2025-07-03
---








  









### ScheduleData Base Classes[] {#scheduledata-base-classes style="tab-stops: 0pt"}

 

The **ScheduleControl** gets its data through its DataSource property, an IScheduleDataProvider object. So, it is this IScheduleDataProvider interface (and several other associated interfaces) that gives you the ability and facility to provide data to the ScheduleControl. To simplify this process of providing data, Essential Schedule also exposes these interfaces as base classes that include some pre-determine droplist settings that allow you to use the ScheduleControl with less coding work. But, you do have the option of working directly through the interfaces to construct your own data provider for the ScheduleControl.

 

The **Essential Schedule** library contains several base classes that implement the various data interfaces required by the ScheduleControl. These base classes use virtual methods which, you can override to provide a concrete data implementation. The classes in the SimpleScheduleDataProvider file that is shipped with the samples and used in the Tutorial section of this User Guide are derived from the ScheduleData base classes. Check out the shipped sample that uses the SimpleScheduleDataProvider as a data source for ScheduleControl.

 

The following sections discuss these ScheduleData base classes in more detail.

 

[] 

[] 

More:







