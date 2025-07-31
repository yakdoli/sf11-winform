---
title: usingstatepersistenceinapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingstatepersistenceinapplication.md
created_at: 2025-07-03
---






##### Using State Persistence in Application {#using-state-persistence-in-application style="tab-stops: 0pt"}

[Y]ou can persist Ribbon States in two ways namely: []

[] 

[·      ]Persisting Ribbon States at Application Exit and Load

[·      ]Persisting Ribbon States Any Time while Running the Application

**[]** 

###### 3.31.2.16.1.1      Persisting Ribbon States at Application Exit and Load {#persisting-ribbon-states-at-application-exit-and-load style="tab-stops: 0pt"}

The user can persist the Ribbon States at application exit and load by handling the AutoPersist property. You can customize the persisting states in Ribbon control by handling the AutoPersist property individually in Ribbon, QAT and Ribbon window. The following code snippet shows how to handle the property in Ribbon elements.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][RibbonWindow][ x][:][Class][=\"RibbonSample.Window1\"][ x][:][Name][=\"ribbonwindow\"][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [   [ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [   [ xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [   [ xmlns][:][syncfusion][=\"http://schemas.syncfusion.com/wpf\"]   ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [      xmlns][:][sample][=\"clr-namespace:RibbonSample\"][  [ AutoPersist][=\"True\"]]                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [      WindowState][=\"Normal\"][ WindowStyle][=\"SingleBorderWindow\"][]                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [   [ Title][=\"Ribbon Sample Demo\"] [ WindowStartupLocation][=\"CenterScreen\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    ][\<][Grid][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        ][\<][syncfusion][:][Ribbon][ Name][=\"MyRibbon\"][ AutoPersist][=\"True\"\>][]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            ][\<][syncfusion][:][Ribbon.QuickAccessToolBar][\>][]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                ][\<][syncfusion][:][QuickAccessToolBar][ AutoPersist][=\"True\"\>][]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                ][\</][syncfusion][:][QuickAccessToolBar][\>][]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            ][\</][syncfusion][:][Ribbon.QuickAccessToolBar][\>][]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        ][\</][syncfusion][:][Ribbon][\>][]                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    ][\</][Grid][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][syncfusion][:][RibbonWindow][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

###### 3.31.2.16.1.2      Persisting Ribbon States Any Time while Running the Application {#persisting-ribbon-states-any-time-while-running-the-application style="tab-stops: 0pt"}

 

WPF Ribbon control now supports the persistence of its states any time while running the application. You can save and load the Ribbon states any time by using Ribbon methods. There are two methods to save and load the current Ribbon states. They are:

[] 

[·      ]SaveRibbonState

[·      ]LoadRibbonState

 

Before you call the methods, you have to specify the persisting Ribbon elements in PersistElements collection. You can change the collection any time. Save and Load states at runtime are fully based on this collection details. The following code snippet shows how to add Ribbon elements that are required to retain its state.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                     |
| [private][ [void] ribbonwindow_Loaded([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [  {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [       [this].MyRibbon.PersistElements.Add([RibbonElements].Ribbon);]                                                                             |
|                                                                                                                                                                                                                                     |
| [       [this].MyRibbon.PersistElements.Add([RibbonElements].RibbonWindow);                           ]                                            |
|                                                                                                                                                                                                                                     |
| [       [this].MyRibbon.PersistElements.Add([RibbonElements].QuickAccessToolbar);]                                                                 |
|                                                                                                                                                                                                                                     |
| [  }]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_Sample_Link}Saving Ribbon States

You can dynamically save and load the current Ribbon state at run time. You can save the current Ribbon State by using the SaveRibbonState method in Ribbon. This method has two overloaded methods for customizing the Save state process as follows:

1.   void SaveRibbonState()

2.   void SaveRibbonState(IsolatedStorageFile isoStorage, string storeFileName)

In the first method, there are no parameters. It will save the current state of the Ribbon Control to the default Isolated Storage file, which is built in the source.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [  private][ [void] SaveRibbonState_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                         |
| [     {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [       [this].MyRibbon.SaveRibbonState();       ]                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [     }]                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

You can also store the current Ribbon State in the custom Isolated Storage file by using the second overloaded method.  This method has two arguments namely IsolatedStorageFile and storeFileName. By using these two arguments you can define your own Isolated Storage file for saving the state.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [  private][ [void] SaveRibbonState_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                         |
| [     {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [       [IsolatedStorageFile] storage = ]                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                      [IsolatedStorageFile].GetStore([IsolatedStorageScope].User  ]                                                                |
|                                                                                                                                                                                                                                         |
| [                              \|[IsolatedStorageScope].Assembly, [null], [null]);]                                               |
|                                                                                                                                                                                                                                         |
| [       [this].MyRibbon.SaveRibbonState(storage,[\"Customfilename.dat\"]);       ]                                                                     |
|                                                                                                                                                                                                                                         |
| [     }]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_How_to_Save}Loading Ribbon States

Load state process is also having the similar procedures of save states. We can load the Ribbon State at any time from the last saved Isolated Storage file. LoadRibbonState method is used to load the Ribbon state from the last saved state. This method has two overloaded methods as follows:

1.   void LoadRibbonState()

2.   void LoadRibbonState(IsolatedStorageFile isoStorage, string storeFileName)

The first method with no arguments will load the Ribbon State from the last saved state in the default Isolated Storage file, which is stored by the SaveRibbonState method.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                       |
| [private][ [void] LoadRibbonState_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [            [this].MyRibbon.LoadRibbonState();]                                                                                                                             |
|                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The second overloaded method will load the Ribbon State from the given file name in the mentioned Isolated Storage file.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                       |
| [private][ [void] LoadRibbonState_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [            [IsolatedStorageFile] storage = ]                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [                       [IsolatedStorageFile].GetStore([IsolatedStorageScope].User ]                                                              |
|                                                                                                                                                                                                                                       |
| [                                 \|[IsolatedStorageScope].Assembly, [null], [null]);]                                          |
|                                                                                                                                                                                                                                       |
| [            [this].MyRibbon.LoadRibbonState(storage, [\"Customfilename.dat\"]);]                                                                    |
|                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Saving and Loading Many Ribbon States

You can easily maintain many Ribbon control states in the Isolated Storage files. You can save the consecutive or different states of the Ribbon control in different Isolated Storage filesand also  load any saved state from the Isolated Storage files which is in the old state. You can save the different states of the Ribbon control at various times as follows:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                       |
| [private][ [void] SaveLevel1State_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [    {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                       |
| [        [IsolatedStorageFile] storage = ]                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [             [IsolatedStorageFile].GetStore([IsolatedStorageScope].User \| ]                                                                     |
|                                                                                                                                                                                                                                       |
| [                                 [IsolatedStorageScope].Assembly, [null], [null]);]                                            |
|                                                                                                                                                                                                                                       |
| [        [this].MyRibbon.SaveRibbonState(storage,[\"RibbonState1.dat\"]);       ]                                                                    |
|                                                                                                                                                                                                                                       |
| [    }]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [private][ [void] SaveLevel2State_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [    {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                       |
| [        [IsolatedStorageFile] storage = ]                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [              [IsolatedStorageFile].GetStore([IsolatedStorageScope].User \| ]                                                                    |
|                                                                                                                                                                                                                                       |
| [                                [IsolatedStorageScope].Assembly, [null], [null]);]                                             |
|                                                                                                                                                                                                                                       |
| [        [this].MyRibbon.SaveRibbonState(storage, [\"RibbonState2.dat\"]);]                                                                          |
|                                                                                                                                                                                                                                       |
| [    }]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [private][ [void] SaveLevel3State_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [    {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                       |
| [       [IsolatedStorageFile] storage = ]                                                                                                                                 |
|                                                                                                                                                                                                                                       |
| [           [IsolatedStorageFile].GetStore([IsolatedStorageScope].User \| ]                                                                       |
|                                                                                                                                                                                                                                       |
| [                                [IsolatedStorageScope].Assembly, [null], [null]);]                                             |
|                                                                                                                                                                                                                                       |
| [       [this].MyRibbon.SaveRibbonState(storage, [\"RibbonState3.dat\"]);]                                                                           |
|                                                                                                                                                                                                                                       |
| [    }]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

After saving the different states of the Ribbon Control, you can load the Ribbon state to any of the old states. The following code snippet explains the implementation.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                       |
| [private][ [void] LoadLevel1State_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [            [IsolatedStorageFile] storage = ]                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [                  [IsolatedStorageFile].GetStore([IsolatedStorageScope].User \| ]                                                                |
|                                                                                                                                                                                                                                       |
| [                                [IsolatedStorageScope].Assembly, [null], [null]);]                                             |
|                                                                                                                                                                                                                                       |
| [            [this].MyRibbon.LoadRibbonState(storage, [\"RibbonState1.dat\"]);]                                                                      |
|                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [private][ [void] LoadLevel2State_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [            [IsolatedStorageFile] storage = ]                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [                   [IsolatedStorageFile].GetStore([IsolatedStorageScope].User \| ]                                                               |
|                                                                                                                                                                                                                                       |
| [                                [IsolatedStorageScope].Assembly, [null], [null]);]                                             |
|                                                                                                                                                                                                                                       |
| [            [this].MyRibbon.LoadRibbonState(storage, [\"RibbonState2.dat\"]);]                                                                      |
|                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [private][ [void] LoadLevel3State_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [            [IsolatedStorageFile] storage = ]                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [                  [IsolatedStorageFile].GetStore([IsolatedStorageScope].User \| ]                                                                |
|                                                                                                                                                                                                                                       |
| [                                 [IsolatedStorageScope].Assembly, [null], [null]);]                                            |
|                                                                                                                                                                                                                                       |
| [            [this].MyRibbon.LoadRibbonState(storage, [\"RibbonState3.dat\"]);]                                                                      |
|                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

