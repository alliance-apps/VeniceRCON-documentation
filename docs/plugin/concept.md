# Plugin Concept

Each Battlefield Instance gets its own worker assigned where it can run their Plugin inside, this allows to run possible blocking Plugins not affecting other instances because the NodeJS main event loop gets blocked.