---
title: ischeduledatainterfaces.md
original_path: WinForms_Docs/03_Data_Binding/ischeduledatainterfaces.md
created_at: 2025-08-05
---








  









### IScheduleData Interfaces {#ischeduledata-interfaces style="tab-stops: 0pt"}

[] 

The ScheduleControl gets its data through its **DataSource** property, an **IScheduleDataProvider** object.

So, it is this IScheduleDataProvider interface (and several other associated interfaces) that gives you the ability and facility to provide data to the ScheduleControl.

This section discusses the actual interfaces required to provide data to the ScheduleControl. If you need the access your own custom datastore, then you can create objects that implement these interfaces on which the ScheduleControl relies to provide data from your custom datastore.

 If you just need a local disk file datastore, then using the implementation provided by the classes in the SimpleScheduleDataProvider file that is shipped with the samples, may serve your purpose.

 You also have the option of deriving the ScheduleData base classes to provide custom data to the ScheduleControl. But, implementing the required interfaces directly will give you the most flexibility.

[] 

There are five interfaces that you can use to provide data for a ScheduleControl. There are two \'object\' interfaces, **IScheduleAppointment** and **ILookUpObject**. These interfaces are primarily wrappers for a collection of properties.

 **IScheduleAppointment** wraps individual appointment data. **ILookUpObject** wraps the items you can see in droplists.

There are two \'list\' interfaces, **IScheduleAppointmentList** and **ILookUpObjectList**. As their names suggest, these two interfaces are essentially lists of **IScheduleAppointments** and **ILookUpItems** respectively.

The last interface, **IScheduleDataProvider,** is a wrapper that holds multiple ILookUpObjectLists and one IScheduleAppointmentList. It is through this interface that the ScheduleControl interacts with the source of data, and in fact, ScheduleControl.DataSource is an IScheduleDataProvider object.

The IScheduleDataProvider object exposes methods of interacting with the data like retrieving lookup lists and providing appointments for specified time periods. The Essential Schedule source code file **ScheduleAppointment.cs** provides a base class implementation of these interfaces, exposing a partially abstract set of classes (the ScheduleData classes) that you can use to indirectly implement these interfaces.

The **SimpleScheduleDataProvider** classes that were used in the Tutorial are derived from these base classes.

[] 

The following sections discuss these required data interfaces in more detail.

[] 

[] 

More:







