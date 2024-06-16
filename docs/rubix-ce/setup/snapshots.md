---
sidebar_position: 7
---

# Backup & Restore

:::caution
To create a backup, you'll require either 2 x Rubix Computes or 1 x Rubix Compute along with 1 x Nube iO Cloud account.
:::

The backup & restoring service allows users to take a backup of a Rubix Compute or Nube iO Cloud. Once a backup is created, users can perform the following actions:

- Save the backup to your PC for safe keeping
- Restore a backup you took for a particular device


:::caution
A backup is stored in supervisor device (this could be the Rubix Compute or Nube iO Cloud) <br/>
:::

![snapshots.gif](img/snapshots.gif)

## Create a Backup
To create a backup in Rubix CE, follow these steps:
1. Open the device for which you wish to take a backup.
2. Navigate to the **settings->backups** section.
3. Click on ![Create new](../img/apps/add-button.png) to initiate the backup process.

Following these steps will allow you to generate a backup of the selected device in Rubix CE.

## Restore from backup
To restore from a backup in Rubix CE, follow these steps:
1. Open the device you want to restore a backup for.
2. Navigate to the **settings->backups** section.
3. Look for the **Restore Icon** and click on it to initiate the restoration process.

Following these steps will allow you to restore a backup for the selected device in Rubix CE.

:::info
Performing a backup or restore in Rubix CE may take several minutes, depending on factors such as the size of historical data and application files associated with the backup. Be prepared to wait for a few minutes while the restoration process completes
:::

![restore-snapshot.png](img/restore-snapshot.png)

# Restore History

In Rubix CE, there is a dedicated tab displaying the history of when users performed restores of the device you are currently working with. This feature allows you to track and review past restoration activities for the device, providing valuable insights into its maintenance and management history.
