# L2-03 — Adam Controller

Adam is the Tangri fleet controller for EVE-OS.

## Responsibilities

- EVE node enrollment
- node inventory
- host health
- application instance lifecycle
- application update and rollback
- EVE OS update and rollback
- operator/API access
- backup and restore

## Deployment boundary

Adam is hosted in AWS ap-south-1. Tangri application control-plane services consume Adam's fleet information; L2 remains the owner of EVE lifecycle operations.

## Development

For local development, run Adam as the upstream container and use the same API path that production will expose. Production deployment must be pinned to an immutable image/version and have persistent state plus tested restore.

Do not put Tangri desired-state semantics into Adam. Adam manages EVE; L4 Control Plane manages Tangri desired state.

## Acceptance

A test node must be able to:

1. enroll;
2. report host health;
3. receive an Edge VM application configuration;
4. start the application;
5. restart it;
6. update it;
7. roll it back.

The same sequence is executed by Eden before hardware qualification.
