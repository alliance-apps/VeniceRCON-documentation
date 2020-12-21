
## Permission Scopes

Permission Scopes are being saved as a bitmask, their validity can be for only a specific instance or globally.

|       scope                 |  bit                   | description
|---------------------------- | ---------------------- | --------------------
| `INSTANCE#ACCESS`           | `0x01`                 | read access for an instance
| `INSTANCE#CREATE`           | `0x02`                 | create an instance
| `INSTANCE#UPDATE`           | `0x04`                 | modify an instance
| `INSTANCE#DELETE`           | `0x08`                 | delete an instance
| `INSTANCE#LOGS`             | `0x08`                 | allows access to server logs
| `INSTANCE#CONSOLE`          | `0x08`                 | allows console events
| `INSTANCEUSER#ACCESS`       | `0x100`                | read access for an instance
| `INSTANCEUSER#CREATE`       | `0x200`                | create invite tokens for an instance
| `INSTANCEUSER#UPDATE`       | `0x400`                | update permissions from an instace
| `INSTANCEUSER#REMOVE`       | `0x800`                | remove users from an instance
| `BAN#ACCESS`                | `0x010000`             | view the current ban list
| `BAN#CREATE`                | `0x020000`             | create bans
| `BAN#DELETE`                | `0x040000`             | remove bans
| `PLAYER#KILL`               | `0x01000000`           | kill a player
| `PLAYER#KICK`               | `0x02000000`           | kick a player
| `PLAYER#MESSAGE`            | `0x04000000`           | messages a player
| `PLAYER#MOVE`               | `0x08000000`           | moves a player
| `PLAYER#TICKETS`            | `0x10000000`           | allows to set the team ticket counts
| `MAP#SWITCH`                | `0x0100000000`         | change map
| `MAP#MANAGE`                | `0x0200000000`         | delete or add new maps
| `RESERVEDSLOT#ACCESS`       | `0x010000000000`       | access the reserved slot list
| `RESERVEDSLOT#CREATE`       | `0x020000000000`       | adds someone to reserved slot list
| `RESERVEDSLOT#DELETE`       | `0x020000000000`       | deletes someone from the reserved slot list
| `PLUGIN#ACCESS`             | `0x01000000000000`     | access plugin informations
| `PLUGIN#MODIFY`             | `0x02000000000000`     | modify settings of plugins
| `PLUGIN#CREATE`             | `0x01000000000000`     | add a plugin
| `PLUGIN#REMOVE`             | `0x02000000000000`     | remove a plugin
| `VARIABLE#MODIFY`           | `0x0200000000000000`   | modify variables
| `EVENT#CHAT`                | `0x010000000000000000` | access chat events
| `EVENT#KILL`                | `0x020000000000000000` | access kill events
| `MOD#ACCESS`                | `0x0100000000000000000` | access mod related data
| `MOD#CREATE`                | `0x0200000000000000000` | add mods
| `MOD#UPDATE`                | `0x0400000000000000000` | update mod related stuff
| `MOD#DELETE`                | `0x0800000000000000000` | delete mods
| `PLUGINREPOSITORY#ACCESS`   | `0x010000000000000000000` | access repository informations
| `PLUGINREPOSITORY#MODIFY`   | `0x020000000000000000000` | modify a repository
| `PLUGINREPOSITORY#CREATE`   | `0x040000000000000000000` | add a repository
| `PLUGINREPOSITORY#REMOVE`   | `0x080000000000000000000` | delete a repository
| `USER#ACCESS`               | `0x01000000000000000000000` | allows access to the administrative instance user managment
| `USER#CREATE`               | `0x02000000000000000000000` | allows user creation
| `USER#REMOVE`               | `0x04000000000000000000000` | deletes user
| `USER#MODIFY`               | `0x08000000000000000000000` | modify email, password and permissions of users