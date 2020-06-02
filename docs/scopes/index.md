
## Permission Scopes

Permission Scopes are being saved as a bitmask, their validity can be for only a specific instance or globally.

|       scope           |  bit           | description
|---------------------- | -------------- | --------------------
| `INSTANCE#ACCESS`     | `0x01`         | read access for an instance
| `INSTANCE#CREATE`     | `0x02`         | create an instance
| `INSTANCE#UPDATE`     | `0x04`         | modify an instance
| `INSTANCE#DELETE`     | `0x08`         | delete an instance
| `INSTANCEUSER#ACCESS` | `0x100`        | read access for an instance
| `INSTANCEUSER#CREATE` | `0x200`        | create invite tokens for an instance
| `INSTANCEUSER#UPDATE` | `0x400`        | update permissions from an instace
| `INSTANCEUSER#REMOVE` | `0x800`        | remove users from an instance
| `BAN#ACCESS`          | `0x010000`     | view the current ban list
| `BAN#CREATE`          | `0x020000`     | create bans
| `BAN#DELETE`          | `0x040000`     | remove bans
| `PLAYER#KILL`         | `0x01000000`   | kill a player
| `PLAYER#KICK`         | `0x02000000`   | kick a player
| `MAP#CHANGE`          | `0x0100000000` | change map
| `MAP#MANAGE`          | `0x0200000000` | delete or add new maps

