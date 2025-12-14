# Week 6 – PowerShell Automation

## Description
This folder contains the Week 6 laboratory work for the Infrastructure as Code module. The focus of this week was to install, configure and verify PowerShell 7, followed by the development of a suite of customised PowerShell scripts. These scripts demonstrate essential automation concepts such as module discovery, variable handling, type conversion, conditional logic, loop structures, pipeline operations and basic module creation. A full academic report accompanies this folder, documenting the installation workflow, scripting methodology, test procedures, outputs and conclusions.

---

## Contents

### PowerShell Scripts
- **1. Setup.ps1** – Prepares the PowerShell execution environment and installs required package providers.  
- **2. DownloadPowerShell7.ps1** – Retrieves Microsoft’s official PowerShell 7 installation script.  
- **3. InstallPowerShell7.ps1** – Automates the installation of PowerShell 7 using parameterised values.  
- **4. VerifyPowerShell7.ps1** – Lists module paths and confirms successful installation.  
- **5. FindModules.ps1** – Counts all modules available in the PowerShell Gallery.  
- **6. FindModulesPSCore.ps1** – Identifies modules that support PowerShell Core.  
- **Creating a Module.ps1** – Builds a custom HelloWorld module and validates its availability.  
- **Variables.ps1** – Demonstrates variable assignments, data types and type conversions.  
- **Types.ps1** – Tests numeric casting, strings and floating-point types.  
- **Tax Calculation Script.ps1** – Performs VAT calculation using arithmetic operations.  
- **if and elseif.ps1** – Demonstrates branching logic based on conditional evaluation.  
- **Switch.ps1** – Uses switch-case logic to match and output predefined values.  
- **For Loop.ps1** – Iterates through numeric sequences using a standard for-loop.  
- **For Each.ps1** – Loops through elements in an array.  
- **While Loop.ps1** – Runs repeated logic until a condition changes.  
- **Do Until.ps1** – Repeats statements until a target value is reached.  
- **Piping Commands.ps1** – Demonstrates PowerShell’s object pipeline and formatted output.

### Lab Report
- **Academic Report - Powershell.pdf** – Includes description, aims, method, results, analysis and conclusion  
  (with appendices containing script files and execution outputs).

---

## Dependencies
- Windows 10 or Windows 11  
- PowerShell 5.1 (pre-installed)  
- PowerShell 7 (installed during the lab)  
- Visual Studio Code with PowerShell extension  
- Git + GitHub Desktop  
- VMware Workstation or Azure VM environment for isolated testing

---

## Author
- **LNumber:** L00187849  
- **Name:** Liam Saunders  
- **Course:** PG Dip Cloud Technologies  
- **Module:** Infrastructure as Code (IaC)

---

## License
This work is submitted as part of academic coursework. Redistribution or reuse should comply with ATU academic integrity policies.

