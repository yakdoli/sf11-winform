---
title: 132events.md
original_path: WinForms_Docs/99_Uncategorized/132events.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### 1.3.2. Events {#events style="tab-stops: 0pt"}

The events of the ToggleButton control are listed and described below:

 

  -------------------------------------------------------------------------------------------------- ---------------------------------------- ----------------------------------------------------------------
  **[Event]** []   **[Parameters]**   **[Description]**
  [OnTouchStart]                                                               inst,args[]      Event triggers when the touch starts[]
  [OnTouchEnd]                                                                 inst,args[]      Event rtriggers when the touch ends[]
  -------------------------------------------------------------------------------------------------- ---------------------------------------- ----------------------------------------------------------------

 

Using Builder

The following steps will guide you in handling the client-side events through Builder:

3.   In the **view**, invoke the **ToggleButton** helper with the toggle button ID as the first argument and enable the **OnTouchStart** and **OnTouchEnd** with the respective handlers as shown below.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [        [\<%][=] Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                                                                                                                                          |
|                 .ToggleState([MobToggleState].On)\                                                                                                                                                                                                                         |
|                 .OnText([\"Enable\"])\                                                                                                                                                                                                                                     |
|                 .OffText([\"Disable\"])\                                                                                                                                                                                                                                   |
| ] [                .OnTouchStart([\"OnStart\"])\                                                                                                                                                                                       |
|                 .OnTouchEnd([\"OnEnd\"])\                                                                                                                                                                                                                                  |
| ] [                .AutoFormat([MobSkins].Spinach) [%\>]]                                                                                                              |
|                                                                                                                                                                                                                                                                                                    |
| **[\[Razor\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| [        ] [\@{] [\                                                                                                                                                                       |
|            ] [Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                                                                                                                                                           |
|                  .ToggleState([MobToggleState].On)\                                                                                                                                                                                                                        |
|                  .OnText([\"Enable\"])\                                                                                                                                                                                                                                    |
|                  .OffText([\"Disable\"])\                                                                                                                                                                                                                                  |
| ] [                 .OnTouchStart([\"OnStart\"])\                                                                                                                                                                                      |
|                  .OnTouchEnd([\"OnEnd\"])\                                                                                                                                                                                                                                 |
| ] [                .AutoFormat([MobSkins].Spinach).Render(); ] [}] [] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Define the callback methods in the script to handle the specified events.

**[]**  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                  |
|                                                                                                                                                                           |
| [    [\<][script][type][=\"text/javascript\"\>]] |
|                                                                                                                                                                           |
| [        [function] OnStart(inst, args) {]                                                                       |
|                                                                                                                                                                           |
| [            [//inst - instance of ToggleButton object]]                                                    |
|                                                                                                                                                                           |
| [            [//args :    args.element   - ToggleButton item ]]                                             |
|                                                                                                                                                                           |
| [            [//          args.value            - ToggleButton id]]                                         |
|                                                                                                                                                                           |
| [            [//          args.text          - on & off state text of the ToggleButton]]                    |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| [        [function] OnEnd(inst, args) {]                                                            |
|                                                                                                                                                                           |
| [            [//inst - instance of ToggleButton object]]                                       |
|                                                                                                                                                                           |
| [            [//args :    args.element   - ToggleButton item ]]                                |
|                                                                                                                                                                           |
| [            [//          args.value            - ToggleButton id]]                            |
|                                                                                                                                                                           |
| [            [//          args.text          - on & off state text of the ToggleButton]]       |
|                                                                                                                                                                           |
| [        }]                                                                                                              |
|                                                                                                                                                                           |
| [    [\</][script][\>]]                                 |
|                                                                                                                                                                           |
| []                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

5.   Run the application.

**[]**  

Using Properties Model     

The following steps guide you in handling the client-side events through the properties model.

6.   In the **controller**, create an instance of **MobToggleButtonModel**, define the **OnTouchStart** and **OnTouchEnd** events, and pass the instance through **ViewData** to **View** as given below:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                             |
|                                                                                                                                                                                                  |
| [        [public][ActionResult] ToggleButton()]                                                    |
|                                                                                                                                                                                                  |
| [        {]                                                                                                                                     |
|                                                                                                                                                                                                  |
| [            [MobToggleButtonModel] model = [new][MobToggleButtonModel]()] |
|                                                                                                                                                                                                  |
| [            {]                                                                                                                                 |
|                                                                                                                                                                                                  |
| [                  ] [OnText=[\"Enable\"],]                                         |
|                                                                                                                                                                                                  |
| [                OffText=[\"Disable\"],]                                                                                             |
|                                                                                                                                                                                                  |
| [                AutoFormat=[MobSkins].Spinach,]                                                                                     |
|                                                                                                                                                                                                  |
| [                OnTouchStart =[\"OnStart\"],]                                                                                       |
|                                                                                                                                                                                                  |
| [                OnTouchEnd ==[\"OnStop\"]] [                ]                      |
|                                                                                                                                                                                                  |
| [            };]                                                                                                                                |
|                                                                                                                                                                                                  |
| [            ViewData\[[\"Toggle\"]\] = model;]                                                                         |
|                                                                                                                                                                                                  |
| [            [return] View();]                                                                                             |
|                                                                                                                                                                                                  |
| [        }]                                                                                                                                     |
|                                                                                                                                                                                                  |
| []                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

7.   In the **view**, invoke the **ToggleButton** helper with the **ViewData** key as the first argument.

 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                   |
|                                                                                                                                      |
| **[]**                                                                                           |
|                                                                                                                                      |
| [        [\<%] {]                                                    |
|                                                                                                                                      |
| [               Html.MobSyncfusion().ToggleButton([\"Toggle\"])]         |
|                                                                                                                                      |
| [                       .Render();]                                                              |
|                                                                                                                                      |
| [           }[%\>]]                                                  |
|                                                                                                                                      |
| []                                                                                               |
|                                                                                                                                      |
| **[\[Razor\]]**                                                                                  |
|                                                                                                                                      |
| **[]**                                                                                           |
|                                                                                                                                      |
| [    [\@{]]                                                          |
|                                                                                                                                      |
| [        Html.MobSyncfusion().ToggleButton([\"Toggle\"])]                |
|                                                                                                                                      |
| [                .Render();]                                                                     |
|                                                                                                                                      |
| [    [}]] [] |
+--------------------------------------------------------------------------------------------------------------------------------------+

 

8.   Define the callback methods in the script to handle the specified events.

**[]**  

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                             |
|                                                                                                                                                                                                      |
| [    [\<][script][type][=\"text/javascript\"\>]]                            |
|                                                                                                                                                                                                      |
| [        [function] OnStart(inst, args) {]                                                                                                  |
|                                                                                                                                                                                                      |
| [            [//inst - instance of ToggleButton object]]                                                                               |
|                                                                                                                                                                                                      |
| [            [//args :    args.element   - ToggleButton item ]]                                                                        |
|                                                                                                                                                                                                      |
| [            [//          args.value            - ToggleButton id]]                                                                    |
|                                                                                                                                                                                                      |
| [            [//          args.text          - on & off state text of the ToggleButton]]                                               |
|                                                                                                                                                                                                      |
| [        }]                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [        [function] OnEnd(inst, args) {]                                                                                                    |
|                                                                                                                                                                                                      |
| [            [//inst - instance of ToggleButton object]]                                                                               |
|                                                                                                                                                                                                      |
| [            [//args :    args.element   - ToggleButton item ]]                                                                        |
|                                                                                                                                                                                                      |
| [            [//          args.value            - ToggleButton id]]                                                                    |
|                                                                                                                                                                                                      |
| [            [//          args.text          - on & off state text of the ToggleButton]]                                               |
|                                                                                                                                                                                                      |
| [        }]                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [    [\</][script][\>]] [] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

9.   Run the application.

 

The output is shown in the following screenshot:

{border="0"}

Figure 169: ToggleButton Control---Events

 

 

 

 

[]{#related-topics}

