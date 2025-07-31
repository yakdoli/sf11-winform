---
title: enhancementofgriddatacommandmanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\enhancementofgriddatacommandmanager.md
created_at: 2025-07-03
---






#### Enhancement of GridDataCommandManager {#enhancement-of-griddatacommandmanager style="tab-stops: 0pt"}

Command is an input mechanism, which provides input handling at a more semantic level.  Commands in WPF are created by implementing the ICommand interface. ICommand exposes two methods, **Execute**, and **CanExecute** and an event **CanExecuteChanged**.

[·      ]**Execute** performs the actions that are associated with the command

[·      ]**CanExecute** determines whether the command can execute on the current command target

[·      ]**CanExecuteChanged** is raised if the command manager that centralizes the commanding operations detects a change in the command source that might invalidate a command that has been raised but not yet executed by the command binding.

GridDataControl provides Commands for the following events. This will help to write the application in pure MVVM model.

[·      ]QueryCellInfoCommand

[·      ]SortColumnChangingCommand

More:







