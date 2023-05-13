---
sidebar_position: 5
---

# Apps

:::danger internet connection
A token must be added so the apps can be downloaded over the internet, the token is provided from Nube-IO support and is
valid for up one year
:::

:::danger user home directory
Installing apps will add zip files in your user home directory  **/home/my-user/rubix/store/apps**
:::

# Managing apps

Apps are installed on the Rubix-compute, much like any normal app on a PC or a cell phone.

Example of Nube apps:

* BACnet-server
* LoRaWAN protocol
* Rubix-Wires

# To install an app

1. Make sure a token is added see the settings section add add token
2. Click on the plus (+) icon add dropdown the apps manager
3. Once in the apps manager you can install, uninstall or start, stop and restart an app


Apps can be installed by using the `Download` icon (down arrow) on the row of the app/service required.

1. Click the green `Download` arrow button on the row of the app/service that is required to be installed.
2. On the opening of the `App Status` pop-up, click on the blue `CONTINUE` button after verifying that it isn't
   installed (`Version` should be displaying -).
3. Using the `Select Release Version` drop-down, select the desired version to install (usually the most recent version
   available) and then click the blue `DOWNLOAD` button.
4. Wait until the downloading is completed, and that the green `Downloading Completed` status message is displayed.
   Verify that the correct version required is listed, and then click the blue `INSTALL` button.
5. Wait for installation to be completed and for `Installation Complete` to be displayed. Click `OK` to finalise
   installation.

![max800px](img/adding-app.gif)


# Apps/Service Status

On the respective tab for Apps/Services: There are tiles displayed; one for each installed App.

The coloured status label, displayed on each tile

shows the current status of the service:

* **Running** (Green) - means that the app/service is currently running.
* **Inactive** (Yellow) - means the app/service is not running (may have crashed or not be enabled).
* **Stopped** (Red) - means the app/service is not running (may have crashed or not be enabled).
* **Activating** (Yellow) - means the app/service is starting, but is not yet running.

# Enabling Apps/Services

On the respective tab for Apps/Services:  To Enable an App/Service, toggle the `Enable` switch on the required service
to the ON position. Enabling an App/Service will mean that the service will start on controller reboot. To start an
App/Service you must also click the `Start` button.

# Starting Apps/Services

On the respective tab for Apps/Services:  To start an App/Service, click the `Start` button on the required service.
Refresh the page to next to see the updated the status of the app/service and confirm that the desired app/service is
now running.

# Restarting Apps/Services

On the respective tab for Apps/Services:  To restart an App/Service, click the `Restart` button on the required service.
Refresh the page to next to see the updated the status of the app/service and confirm that the desired app/service is
now running (or starting). You can see the `Active` label shows the time that the service has been running for. After a
restart, the Active time should be very low.

# Disabling Services

On the respective tab for Apps/Services:  To disable the App/Service, click the `Stop` button on the required service.
Refresh the page to next to see the updated the status of the app/service and confirm that the desired app/service has
been stopped (or is stopping).


# Updating Existing Apps/Services

Updating existing apps/services is very similar to installing apps/services. The only difference is that the `Version`
displayed will be the currently installed version.

1. Click the green `Download` arrow button on the row of the app/service that is required to be updated.
2. On the opening of the `App Status` pop-up, click on the blue `CONTINUE` button a(`Version` should be displaying the
   currently installed version).
3. Using the `Select Release Version` drop-down, select the desired version to install (usually the most recent version
   available) and then click the blue `DOWNLOAD` button.
4. Wait until the downloading is completed, and that the green `Downloading Completed` status message is displayed.
   Verify that the correct version required is listed, and then click the blue `INSTALL` button.
5. Wait for installation to be completed and for `Installation Complete` to be displayed. Click `OK` to finalise
   installation of the updated version.

# Uninstalling or Deleting Apps/Services

Apps/Services can be uninstalled and deleted using the red `DELETE` bin icon (under the `Actions` column) on the row of
the app/service wishing to be removed. Once the red `DELETE` bin icon is clicked, a confirmation window confirming
deletion pops-up. Click `YES` to delete the app/service. Wait for the process to complete, and the page will
automatically refresh. Ensure the app/service has been successfully removed.
