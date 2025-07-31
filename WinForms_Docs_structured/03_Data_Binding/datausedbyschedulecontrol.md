---
title: datausedbyschedulecontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\datausedbyschedulecontrol.md
created_at: 2025-07-03
---








  









## Data used by ScheduleControl {#data-used-by-schedulecontrol style="tab-stops: 0pt"}

 

There are generally two types of data required by ScheduleControl. Most of the data is what we described as ***Appointments data***. This data includes the time, subject, body, and so on. of each of the actual appointments.

The second type of data we refer to as the ***DropLists data***. This data consists of the several option lists that go into describing the actual appointment data. For example, each appointment may have a marker associated with it that indicates something of the nature of the appointment like whether it is business, personal, a must-attend, etc. This second type of data is more like schema data, as it suggests the content options of the actual Appointments data.

 

The ScheduleControl does all its data access through interfaces. To support custom data objects, you would have your data objects implement these particular interfaces that are discussed in the following sections. In addition, included in the Essential Schedule library are base classes that implement these required interfaces. So, you can also create data sources for the ScheduleControl by deriving these base classes. The SimpleScheduleDataProvider classes that were used in the Tutorial are derived from these base classes.

 

Base Classes

 

[·      ]**ScheduleDataProvider Class**: provides an empty implementation of the IscheduleDataProvider.

The implementation is done through virtual methods. You can then derive this class and through its overrides, set up an IScheduleDataProvider. See the SimpleScheduleDataProvider class in the ScheduleSample sample.

 

[·      ]**ScheduleAppointmentList Class**: provides an implementation of IScheduleAppointmentList and is essentially a wrapper class for an ArrayList that holds ScheduleAppointments

 

[·      ]**ScheduleAppointment Class**: provides an implementation of IScheduleAppointment and defines the objects that represent appointments in the ScheduleControl.

 

[·      ]**LookUpObjectList Class**: strongly typed ArrayList that holds list option values that are used in the new appointment form.

 

[·      ]**LookUpObject Class**: wrapper class for list choices that can have a valueMember, displayMember and colorMember associated with them.

 

 

The lists for the ShowTime and Label options on the Appointment forms use these objects.

 

Interfaces

 

[·      ]**IScheduleDataProvider Interface:** provides the framework for providing schedule item data to the ScheduleControl.

 

[·      ]**IScheduleAppointmentList Interface:** serves as a collection of ISchedule objects.

 

[·      ]**IScheduleAppointment Interface:** defines individual schedule items.

 

[·      ]**ILookUpObjectList Interface:** serves as a collection of IlookUpObjects.

 

[·      ]**ILookUpObject Interface:** enables Choice lists within the ScheduleControl, that are used to provide possible schedule item information (like location or a reminder), to have a ValueMember / DisplayMember associated with them, as well as a color that will be used in drop-downs showing these lists.

 Value members are normally the values serialized to data stores.

 

 

More:







