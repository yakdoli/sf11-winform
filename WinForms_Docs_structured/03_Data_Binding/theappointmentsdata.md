---
title: theappointmentsdata.md
original_path: WinForms_Docs/03_Data_Binding/theappointmentsdata.md
created_at: 2025-08-05
---






#### The Appointments Data {#the-appointments-data style="tab-stops: 0pt"}

[] 

Here are the ScheduleData base classes that provide the Appointments data used by ScheduleControl. For code details of deriving these ScheduleData base classes to implement a data provider for the ScheduleControl, please see the SimpleScheduleDataProvider code file that ships as part of the ScheduleSample sample.

[] 

ScheduleAppointment Class

[] 

**ScheduleAppointment** is the class that defines the objects that represent appointments in the Schedule Control. This class implements **IScheduleAppointment** to provide an object to hold the concrete data associated with appointments. You can either derive this class or implement IScheduleAppointment yourself to extend or modify the information managed by the ScheduleAppointment class. Here are the properties exposed in ScheduleAppointment.

[] 

[·      ]**UniqueID**: gets or sets a unique integer associated with this item

 

[·      ]**Owner**: gets or sets an integer that can be used to identify the owner (if any) of this item

 

[·      ]**StartTime**: gets or sets the start time for this item

 

[·      ]**EndTime**: gets or sets the end time for this item

 

[·      ]**Subject**: gets or sets a text string identifying the topic of this item

 

[·      ]**Content**: gets or sets a text string holding the details or comments for this appointment item

 

[·      ]**AllDay**: gets or sets whether this appointment is an all-day appointment

 

[·      ]**LabelValue**: gets or sets an integer categorizer value for this item

 

[·      ]**MarkerValue**: gets or sets an integer categorizer value for this item

 

[·      ]**Reminder**: gets or sets whether you want a reminder event raised when the StartTime of this item gets close

 

[·      ]**ReminderValue**: gets or sets the type of reminder event raised when the StartTime of this item gets close

 

[·      ]**LocationValue**: gets or sets a string associated with this item

 

[·      ]**Version**: gets in integer format the version number (used to support data format versioning)

 

[·      ]**Tag**: gets or sets an arbitrary object associated with this item

 

[·      ]**Dirty**: gets or sets whether this item has been modified

 

[·      ]**IgnoreChanges**: gets or sets whether changes to this item affect the Dirty property

[] 

[] 

ScheduleAppointmentList Class

[] 

**ScheduleAppointmentList** is a collection of IScheduleAppointments that serves as the data for the Schedule Control. This class is a wrapper class for an ArrayList and implements **IComparer** to order this list by the item\'s StartTime. If two items start at the same time, then the EndTime is used as well to determine the order. Longer appointments rank higher. Here are the properties and methods exposed in ScheduleAppointmentList.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [///][ Gets or sets the i-th IScheduleAppointment in this list.]                                                                     |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [IScheduleAppointment] [this]\[[int] i\];] |
|                                                                                                                                                                                                                                         |
| [              ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [///][ Gets the number of IScheduleAppointments in this list.]                                                                       |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [int] Count]                                                                         |
|                                                                                                                                                                                                                                         |
| [                ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [///][ Sorts this list on the IScheduleAppointment.StartTime property.]                                                              |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [void] SortStartTime()]                                                              |
|                                                                                                                                                                                                                                         |
| [               ]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [///][ Adds an IScheduleAppointment to this list.]                                                                                   |
|                                                                                                                                                                                                                                         |
| [///][ item - The IScheduleAppointment to be added.]                                                                                 |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [void] Add(IScheduleAppointment item)]                                               |
|                                                                                                                                                                                                                                         |
| [                ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [///][ Inserts an IScheduleAppointment into this list.]                                                                              |
|                                                                                                                                                                                                                                         |
| [///][ index - The position in the list where the item is to be inserted. ]                                                          |
|                                                                                                                                                                                                                                         |
| [///][ item - The IScheduleAppointment to be inserted. ]                                                                             |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [void] Insert([int] index, IScheduleAppointment item)]          |
|                                                                                                                                                                                                                                         |
| [                ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [///][ Removes an IScheduleAppointment from this list.]                                                                              |
|                                                                                                                                                                                                                                         |
| [///][ item - The IScheduleAppointment to be removed. ]                                                                              |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [void] Remove(IScheduleAppointment item)]                                            |
|                                                                                                                                                                                                                                         |
| [               ]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [///][ Removes an IScheduleAppointment from this list.]                                                                              |
|                                                                                                                                                                                                                                         |
| [///][ index - The position of the item to be removed.]                                                                              |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [void] RemoveAt([int] index)]                                   |
|                                                                                                                                                                                                                                         |
| [                ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [///][ Returns the position of the specified item within this list.]                                                                 |
|                                                                                                                                                                                                                                         |
| [///][ item - The search item. ]                                                                                                     |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [int] IndexOf(IScheduleAppointment item)]                                            |
|                                                                                                                                                                                                                                         |
| [               ]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [///][ Returns a new ScheduleAppointment populated with default values.]                                                             |
|                                                                                                                                                                                                                                         |
| [public][ [virtual] [IScheduleAppointment] NewScheduleAppointment()  ]                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ScheduleDataProvider Class

[] 

**ScheduleDataProvider** has two functional roles.

One is to implement **IScheduleDataProvider** in a virtual manner so that derived classes can provide concrete implementations through virtual overrides. The IScheduleDataProvider virtual methods exposed in ScheduleDataProvider have empty implementations, so you are required to derive this class to use it.

The second role is to provide the **DropList** data. For this second role, the ScheduleDataProvider does provide concrete implementations for the virtual methods it exposes. So, in your derived class, you would have populated droplists without doing further work, though you can choose to customize these droplists through virtual overrides. Here is a list of the stub methods exposed by ScheduleDataProvider in its first role.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [///][ Return an IScheduleAppointmentList holding the schedule items for the given date. ]                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [IScheduleAppointmentList] GetScheduleForDay(DateTime day)]                                                                            |
|                                                                                                                                                                                                                                                                                           |
| [                ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [//// Return an IScheduleAppointmentList holding the schedule items between the given dates.]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [IScheduleAppointmentList] GetSchedule(DateTime startDate, [DateTime] endDate)]                                   |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ Return an IScheduleAppointmentList holding the schedule items for a particular owner on the given date. ]                                                                       |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [IScheduleAppointmentList] GetScheduleForDay(DateTime day, [int] owner)]                                          |
|                                                                                                                                                                                                                                                                                           |
| [                ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ Return an IScheduleAppointmentList holding the schedule items for a particular owner between the given dates.]                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [IScheduleAppointmentList] GetSchedule(DateTime startDate, [DateTime] endDate, [int] owner)] |
|                                                                                                                                                                                                                                                                                           |
| [                ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ Saves any modified ScheduleAppointments.]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [void] CommitChanges()]                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [                ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ Gets or sets whether CommitChanges is called when the ScheduleControl is disposed.]                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [public][ [SaveOnCloseBehavior] SaveOnCloseBehaviorAction]                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [                ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ Gets or sets whether data source is modified or not.]                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [bool] IsDirty]                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [                ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ Returns a new ScheduleAppointment populated with default values.]                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [IScheduleAppointment] NewScheduleAppointment()]                                                                                       |
|                                                                                                                                                                                                                                                                                           |
| [                ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ Adds a ScheduleAppointment to the list.]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [void] AddItem(IScheduleAppointment item)]                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [                ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ Removes a ScheduleAppointment from the list. ]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [public][ [virtual] [void] RemoveItem(IScheduleAppointment item)][]                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here are the methods and properties used as part of the ScheduleDataProvider\'s second role, providing the DropList data. The following is the actual implementation code which gives an indication of the exposed functionality.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [///][ Provides default droplists for entering IScheduleAppointment data. ]                                                              |
|                                                                                                                                                                                                                                             |
| [///][ You can override this method to provide customized droplists.]                                                                    |
|                                                                                                                                                                                                                                             |
| [public][ [virtual] [void] InitLists()]                                                                      |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [labelList = [new] [ListObjectList]();]                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](0,[\"None\"], [Color].White)); ]                                                |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](1,[\"Important\"], [Color].FromArgb(255,128,64)));]                             |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](2,[\"Business\"],  [Color].FromArgb(86,152,233)));]                             |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](3,[\"Personal\"],  [Color].FromArgb(57,210,53)));]                              |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](4,[\"Vacation\"],  [Color].FromArgb(199,198,182)));]                            |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](5,[\"Must Attend\"],  [Color].FromArgb(255,128,0)));]                           |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](6,[\"Travel Required\"],  [Color].FromArgb(0,255,255)));]                       |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](7,[\"Needs Preparation\"],  [Color].FromArgb(171,171,88)));]                    |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](8,[\"Birthday\"],  [Color].FromArgb(186,117,255)));]                            |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](9,[\"Anniversary\"],  [Color].FromArgb(255,128,64)));]                          |
|                                                                                                                                                                                                                                             |
| [labelList.Add([new] [ListObject](10,[\"Phone Call\"],  [Color].FromArgb(255,128,64)));]                          |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [markerList = [new] [ListObjectList]();]                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [//same as no Mark Color]                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [markerList.Add([new] [ListObject](0,[\"Free\"], [Color].FromArgb(50, [Color].RoyalBlue)));] |
|                                                                                                                                                                                                                                             |
| [markerList.Add([new] [ListObject](1,[\"Tentative\"], [Color].FromArgb(255, 206, 206)));]                         |
|                                                                                                                                                                                                                                             |
| [markerList.Add([new] [ListObject](2,[\"Busy\"],  [Color].FromArgb(0,0,242)));]                                   |
|                                                                                                                                                                                                                                             |
| [markerList.Add([new] [ListObject](3,[\"Out of Office\"],  [Color].FromArgb(128, 0 ,64)));]                       |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [reminderList = [new] [ListObjectList]();]                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](0,[\"0 minutes\"], [Color].White)); ]                                        |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](1,[\"5 minutes\"], [Color].White)); ]                                        |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](2,[\"10 minutes\"], [Color].White)); ]                                       |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](3,[\"15 minutes\"], [Color].White)); ]                                       |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](4,[\"30 minutes\"], [Color].White)); ]                                       |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](5,[\"1 hour\"], [Color].White)); ]                                           |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](6,[\"2 hours\"], [Color].White)); ]                                          |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](7,[\"3 hours\"], [Color].White)); ]                                          |
|                                                                                                                                                                                                                                             |
| [reminderList.Add([new] [ListObject](8,[\"4 hours\"], [Color].White)); ]                                          |
|                                                                                                                                                                                                                                             |
| [              ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [this][.locationList = [new] [ListObjectList]();]                                                            |
|                                                                                                                                                                                                                                             |
| [locationList.Add([new] [ListObject](0,[\"\"], [Color].White)); ]                                                 |
|                                                                                                                                                                                                                                             |
| [locationList.Add([new] [ListObject](1,[\"RoomB\"], [Color].White)); ]                                            |
|                                                                                                                                                                                                                                             |
| [locationList.Add([new] [ListObject](2,[\"RoomC\"], [Color].White)); ]                                            |
|                                                                                                                                                                                                                                             |
| [locationList.Add([new] [ListObject](3,[\"RoomD\"], [Color].White)); ]                                            |
|                                                                                                                                                                                                                                             |
| [locationList.Add([new] [ListObject](4,[\"RoomE\"], [Color].White)); ]                                            |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [///][ Returns the list for the LabelValue options.]                                                                                     |
|                                                                                                                                                                                                                                             |
| [public][ [virtual] [ILookUpObjectList] GetLabels()]                                                         |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [return] LabelList;]                                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Gets or sets the list for the LabelList options.]                                                                                 |
|                                                                                                                                                                                                                                             |
| [protected][ [ListObjectList] LabelList]                                                                                          |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [get]{[return] labelList;}]                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [   [set]{labelList = [value];}]                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Returns the list for the ReminderValue options.]                                                                                  |
|                                                                                                                                                                                                                                             |
| [public][ [virtual] [ILookUpObjectList] GetReminders()]                                                      |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [return] ReminderList;]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Gets or sets the list for the ReminderValue options.]                                                                             |
|                                                                                                                                                                                                                                             |
| [protected][ [ListObjectList] ReminderList]                                                                                       |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [get]{[return] reminderList;}]                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [   [set]{reminderList = [value];}]                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Returns the list for the MarkerValue options.]                                                                                    |
|                                                                                                                                                                                                                                             |
| [public][ [virtual] [ILookUpObjectList] GetMarkers()]                                                        |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [return] MarkerList;]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [                ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Gets or sets the list for the MarkerValue options.]                                                                               |
|                                                                                                                                                                                                                                             |
| [protected][ [ListObjectList] MarkerList]                                                                                         |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [get]{[return] markerList;}]                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [   [set]{markerList = [value];}]                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Returns the list for the LocationValue options.]                                                                                  |
|                                                                                                                                                                                                                                             |
| [public][ [virtual] [ILookUpObjectList] GetLocations()]                                                      |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [return] LocationList;]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [               ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [///][ Gets or sets the list for the LocationValue options.]                                                                             |
|                                                                                                                                                                                                                                             |
| [protected][ [ListObjectList] LocationList]                                                                                       |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [get]{[return] locationList;}]                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [   [set]{locationList = [value];}]                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Returns the list for the Owner options.]                                                                                          |
|                                                                                                                                                                                                                                             |
| [public][ [virtual] [ILookUpObjectList] GetOwners()]                                                         |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [return][ OwnerList;]                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [                ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [///][ Gets or sets the list for the Owner options.]                                                                                     |
|                                                                                                                                                                                                                                             |
| [protected][ [ListObjectList] OwnerList]                                                                                          |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [   [get]{[return] ownerList;}]                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [   [set]{ownerList = [value];}]                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p17} 

[]{#related-topics}

