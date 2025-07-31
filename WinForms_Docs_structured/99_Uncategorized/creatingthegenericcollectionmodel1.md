---
title: creatingthegenericcollectionmodel1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingthegenericcollectionmodel1.md
created_at: 2025-07-03
---








  









## Creating the Generic Collection Model {#creating-the-generic-collection-model style="tab-stops: 0pt"}

To create the Generic Collection Model:

1.   Right-click the **Models** folder in the **Solution Explorer** window and select the menu option **Add, New Item.**

2.   In the **Add New Item** dialog, select the Web category (see Figure 112).

[] 

{border="0"}

Figure 160: Select dialog

*[]* 

3.   Select the **Class** file and give the class file name **AppointmentClass.cs** and click **Add**.

4.   Create an **Appointment** class  containing the  Id, Subject, StartTime, EndTime, Description and Owner as properties.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    [///][ ][\<summary\>]]                                                  |
|                                                                                                                                                                                           |
| [    [///][ Appointment Class]]                                                                   |
|                                                                                                                                                                                           |
| [    [///][ ][\</summary\>]]                                                 |
|                                                                                                                                                                                           |
| [    [public] [class] [AppointmentClass]]                                  |
|                                                                                                                                                                                           |
| [    {]                                                                                                                                      |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
|                                                                                                                                                                                           |
| [        [private] [int] \_Id;]                                                                    |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
|                                                                                                                                                                                           |
| [        [private] [string] \_Subject;]                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
|                                                                                                                                                                                           |
| [        [private] [string] \_Location;]                                                           |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
|                                                                                                                                                                                           |
| [        [private] System.[Nullable]\<System.[DateTime]\> \_StartTime;] |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
|                                                                                                                                                                                           |
| [        [private] System.[Nullable]\<System.[DateTime]\> \_EndTime;]   |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
|                                                                                                                                                                                           |
| [        [private] [string] \_Description;]                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
|                                                                                                                                                                                           |
| [        [private] System.[Nullable]\<[int]\> \_Owner;]                    |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
|                                                                                                                                                                                           |
| [        [///][ ][\<summary\>]]                                              |
|                                                                                                                                                                                           |
| [        [///][ Gets or sets Appointment\'s Id]]                                                  |
|                                                                                                                                                                                           |
| [        [///][ ][\</summary\>]]                                             |
|                                                                                                                                                                                           |
| [        [public] [int] Id]                                                                        |
|                                                                                                                                                                                           |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                           |
| [            [get]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [return] [this].\_Id;]                                                            |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [set]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [if] (([this].\_Id != [value]))]                             |
|                                                                                                                                                                                           |
| [                {]                                                                                                                          |
|                                                                                                                                                                                           |
| [                    [this].\_Id = [value];]                                                       |
|                                                                                                                                                                                           |
| [                }]                                                                                                                          |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [        }]                                                                                                                                  |
|                                                                                                                                                                                           |
| [        [///][ ][\<summary\>]]                                              |
|                                                                                                                                                                                           |
| [        [///][ Gets or sets Appointment\'s Subject]]                                             |
|                                                                                                                                                                                           |
| [        [///][ ][\</summary\>]]                                             |
|                                                                                                                                                                                           |
| [        [public] [string] Subject]                                                                |
|                                                                                                                                                                                           |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                           |
| [            [get]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [return] [this].\_Subject;]                                                       |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [set]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [if] (([this].\_Subject != [value]))]                        |
|                                                                                                                                                                                           |
| [                {]                                                                                                                          |
|                                                                                                                                                                                           |
| [                    [this].\_Subject = [value];]                                                  |
|                                                                                                                                                                                           |
| [                }]                                                                                                                          |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [        }]                                                                                                                                  |
|                                                                                                                                                                                           |
| [        [///][ ][\<summary\>]]                                              |
|                                                                                                                                                                                           |
| [        [///][ Gets or sets Appointment\'s Location]]                                            |
|                                                                                                                                                                                           |
| [        [///][ ][\</summary\>]]                                             |
|                                                                                                                                                                                           |
| [        [public] [string] Location]                                                               |
|                                                                                                                                                                                           |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                           |
| [            [get]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [return] [this].\_Location;]                                                      |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [set]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [if] (([this].\_Location != [value]))]                       |
|                                                                                                                                                                                           |
| [                {]                                                                                                                          |
|                                                                                                                                                                                           |
| [                    [this].\_Location = [value];]                                                 |
|                                                                                                                                                                                           |
| [                }]                                                                                                                          |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [        }]                                                                                                                                  |
|                                                                                                                                                                                           |
| [        [///][ ][\<summary\>]]                                              |
|                                                                                                                                                                                           |
| [        [///][ Gets or sets Appointment\'s Start Time]]                                          |
|                                                                                                                                                                                           |
| [        [///][ ][\</summary\>]]                                             |
|                                                                                                                                                                                           |
| [        [public] System.[Nullable]\<System.[DateTime]\> StartTime]     |
|                                                                                                                                                                                           |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                           |
| [            [get]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [return] [this].\_StartTime;]                                                     |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [set]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [if] (([this].\_StartTime != [value]))]                      |
|                                                                                                                                                                                           |
| [                {]                                                                                                                          |
|                                                                                                                                                                                           |
| [                    [this].\_StartTime = [value];]                                                |
|                                                                                                                                                                                           |
| [                }]                                                                                                                          |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [        }]                                                                                                                                  |
|                                                                                                                                                                                           |
| [        [///][ ][\<summary\>]]                                              |
|                                                                                                                                                                                           |
| [        [///][ Gets or sets Appointment\'s End Time]]                                            |
|                                                                                                                                                                                           |
| [        [///][ ][\</summary\>]]                                             |
|                                                                                                                                                                                           |
| [        [public] System.[Nullable]\<System.[DateTime]\> EndTime]       |
|                                                                                                                                                                                           |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                           |
| [            [get]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [return] [this].\_EndTime;]                                                       |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [set]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [if] (([this].\_EndTime != [value]))]                        |
|                                                                                                                                                                                           |
| [                {]                                                                                                                          |
|                                                                                                                                                                                           |
| [                    [this].\_EndTime = [value];]                                                  |
|                                                                                                                                                                                           |
| [                }]                                                                                                                          |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [        }]                                                                                                                                  |
|                                                                                                                                                                                           |
| [        [///][ ][\<summary\>]]                                              |
|                                                                                                                                                                                           |
| [        [///][ Gets or sets Appointment\'s Description]]                                         |
|                                                                                                                                                                                           |
| [        [///][ ][\</summary\>]]                                             |
|                                                                                                                                                                                           |
| [        [public] [string] Description]                                                            |
|                                                                                                                                                                                           |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                           |
| [            [get]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [return] [this].\_Description;]                                                   |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [set]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [if] (([this].\_Description != [value]))]                    |
|                                                                                                                                                                                           |
| [                {]                                                                                                                          |
|                                                                                                                                                                                           |
| [                    [this].\_Description = [value];]                                              |
|                                                                                                                                                                                           |
| [                }]                                                                                                                          |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [        }]                                                                                                                                  |
|                                                                                                                                                                                           |
| [        [///][ ][\<summary\>]]                                              |
|                                                                                                                                                                                           |
| [        [///][ Gets or sets Appointment\'s Owner]]                                               |
|                                                                                                                                                                                           |
| [        [///][ ][\</summary\>]]                                             |
|                                                                                                                                                                                           |
| [        [public] System.[Nullable]\<[int]\> Owner]                        |
|                                                                                                                                                                                           |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                           |
| [            [get]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [return] [this].\_Owner;]                                                         |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [set]]                                                                                                     |
|                                                                                                                                                                                           |
| [            {]                                                                                                                              |
|                                                                                                                                                                                           |
| [                [if] (([this].\_Owner != [value]))]                          |
|                                                                                                                                                                                           |
| [                {]                                                                                                                          |
|                                                                                                                                                                                           |
| [                    [this].\_Owner = [value];]                                                    |
|                                                                                                                                                                                           |
| [                }]                                                                                                                          |
|                                                                                                                                                                                           |
| [            }]                                                                                                                              |
|                                                                                                                                                                                           |
| [        }]                                                                                                                                  |
|                                                                                                                                                                                           |
| [    }]                                                                                                                                      |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Create another **DataContext** class to generate the Appointments list as shown below.

[    ]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                            |
|                                                                                                                                                                                                                                                                                |
| [    [///][ Appointment context class]]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [    [///][ ][\</summary\>]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [    [public] [class] [AppointmentDataContext]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [        [///][ ][\<summary\>]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [        [///][ Gets  Appointment collection]]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [        [///][ ][\</summary\>]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [        [public] [List]\<[AppointmentClass]\> Appointments]                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [            [get]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [                [List]\<[AppointmentClass]\> AppointmentCollection = [new] [List]\<[AppointmentClass]\>();] |
|                                                                                                                                                                                                                                                                                |
| [                [int] code = 1;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [                [for] ([int] i = 0; i \< 31; i++)]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [                    [DateTime] today = [new] [DateTime](2010, 1, i + 1);]                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [                    [AppointmentClass]\[\] s = [new] [AppointmentClass]\[3\];]                                                                              |
|                                                                                                                                                                                                                                                                                |
| [                    s\[0\] = [new] [AppointmentClass]()]                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [                    {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [                        Id = code + 1,]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [                        Subject = [\"Build Test\"],]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                        StartTime = [new] [DateTime](today.Year, today.Month, today.Day, 7, 0, 0),]                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [                        EndTime = [new] [DateTime](today.Year, today.Month, today.Day, 9, 0, 0),]                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [                        Description = [\"Build Test\"],]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [                        Owner = 1]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [                    };]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [                    s\[1\] = [new] [AppointmentClass]()]                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [                    {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [                        Id = code + 2,]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [                        Subject = [\"Planning\"],]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [                        StartTime = [new] [DateTime](today.Year, today.Month, today.Day, 13, 0, 0),]                                                                                |
|                                                                                                                                                                                                                                                                                |
| [                        EndTime = [new] [DateTime](today.Year, today.Month, today.Day, 14, 30, 0),]                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [                        Description = [\"Planning to develop control\"],]                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [                        Owner = 1]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [                    };]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [                    s\[2\] = [new] [AppointmentClass]()]                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [                    {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [                        Id = code + 3,]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [                        Subject = [\"Document\"],]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [                        StartTime = [new] [DateTime](today.Year, today.Month, today.Day, 15, 0, 0),]                                                                                |
|                                                                                                                                                                                                                                                                                |
| [                        EndTime = [new] [DateTime](today.Year, today.Month, today.Day, 18, 0, 0),]                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [                        Description = [\"Prepare feature specification document\"],]                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                        Owner = 1]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [                    };]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [                    [foreach] ([AppointmentClass] app [in] s)]                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [                    {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [                        AppointmentCollection.Add(app);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [                    }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [                    code += 3;]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [                }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [                [return] AppointmentCollection;]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [            }]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

