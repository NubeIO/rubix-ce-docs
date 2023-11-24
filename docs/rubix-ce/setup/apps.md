---
sidebar_position: 5
---

# Apps

:::danger internet connection
A token must be added so the apps can be downloaded over the internet, the token is provided to each individual via the Nube iO Support team upon each request and is
valid for up one year. Support can be contacted at Support@nube-io.com
:::

:::danger user home directory
Installing apps will add zip files in your user home directory  **/home/my-user/rubix/store/apps**
:::

# Managing apps

Apps are installed on each Rubix Compute similar to an App on a PC, Smart Phone or Tablet.

Examples of Nube iO Apps:

* BACnet Server
* LoRaWAN Protocol
* Rubix Wires

# To install an App

1. Make sure your unique token is added.  Refer to the Settings section of the Support Docuemtnation to add a token.
2. Click on the Plus (+) icon add dropdown the Apps Manager.
3. Once in the Apps Manager you can install, uninstall or start, stop and restart any App.


Apps can be installed by using the `Download` icon (down arrow) on the row of the App/Service required.

1. Click the Green `Download` arrow icon on the row of the App/Service that is required to be installed.
2. On the opening of the `App Status` pop-up, click on the Blue `CONTINUE` button after verifying that it is not already
   installed (`Version` should be displaying -).
3. Using the `Select Release Version` drop-down, select the desired App version to install (usually the most recent version is
   available) and then click the Blue `DOWNLOAD` button.
4. Wait until the downloading is completed, and that the Green `Downloading Completed` status message is displayed.
   Verify that the correct version required is listed, and then click the Blue `INSTALL` button.
5. Wait for installation to be completed and for `Installation Complete` to be displayed. Click `OK` to finalise the
   installation.

![max800px](img/adding-app.gif)


# Apps/Service Status

On the respective tab for Apps/Services: There are tiles displayed; one for each installed App.

The coloured status label, displayed on each tile shows the current status of each service:

* **Running** (Green) - means that the App/Service is currently running.
* **Inactive** (Yellow) - means the App/Service is not running (may not be Enabled).
* **Stopped** (Red) - means the app/service is not running (may not be Enabled).
* **Activating** (Yellow) - means the App/Service is starting, but is not yet running.

# Enabling Apps/Services

On the respective tab for Apps/Services:  To Enable an App/Service, toggle the `Enable` switch on the required service
to the ON position. Enabling an App/Service will mean that the service will start on device reboot. To start an
App/Service you must also click the `Start` button.

# Starting Apps/Services

On the respective tab for Apps/Services:  To start an App/Service, click the `Start` button on the required service.
Refresh the page to next to see the updated status of the App/Service and confirm that the desired App/Service is
now running.

# Restarting Apps/Services

On the respective tab for Apps/Services:  To restart an App/Service, click the `Restart` button on the required service.
Refresh the page to next to see the updated the status of the App/Service and confirm that the desired App/Service is
now running (or starting). You can see the `Active` label displaying the time that the service has been running. After a
restart, the Active time should be very low.

# Disabling Services

On the respective tab for Apps/Services:  To disable the App/Service, click the `Stop` button on the required service.
Refresh the page to next to see the updated status of the App/Service and confirm that the desired app/service has
been stopped (or is stopping).


# Updating Existing Apps/Services

Updating an existing App/Service is very similar to installing an App/Service. The only difference is that the `Version`
displayed will be the currently installed version.

1. Click the green `Download` arrow button on the row of the App/Service that is required to be updated.
2. On the opening of the `App Status` pop-up, click on the Blue `CONTINUE` button a `Version` should be displaying the
   currently installed version.
3. Using the `Select Release Version` drop-down, select the desired version to install (usually the most recent version
   available) and then click the Blue `DOWNLOAD` button.
4. Wait until the downloading is completed, and that the green `Downloading Completed` status message is displayed.
   Verify that the correct version required is listed, then click the Blue `INSTALL` button.
5. Wait for installation to be completed and for `Installation Complete` to be displayed. Click `OK` to finalise
   installation of the updated version.

# Uninstalling or Deleting Apps/Services

Apps/Services can be uninstalled and deleted using the Red `DELETE` bin icon (under the `Actions` column) on the row of
the App/Service wishing to be removed. Once the Red `DELETE` bin icon is clicked, a confirmation window confirming
deletion will appear. Click `YES` to delete the App/Service. 
Wait for the process to complete, and the page will automatically refresh. 
Ensure the app/service has been successfully removed.
