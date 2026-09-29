# L2 — Edge Platform

L2 owns the machine and application lifecycle. It does not own site semantics or EdgeX business logic.

## Components

- L2-01 EVE-OS board images
- L2-02 EVE application-instance manifests
- L2-03 Adam controller
- L2-04 Eden system-test harness

## Ownership

| Component | Tangri owns | External dependency |
|---|---|---|
| EVE-OS | board qualification, pinned releases, image pipeline | EVE-OS |
| App manifests | canonical Tangri deployment descriptors | EVE API / Adam |
| Adam | deployment, configuration, backup and operations | Adam |
| Eden | repeatable EVE system tests | LF Edge Eden |

## Boundary

L2 manages:

- host identity and enrollment
- EVE-OS lifecycle
- VM/application lifecycle
- CPU/RAM/storage/network allocation
- qualified hardware passthrough
- deployment and rollback

L2 does not manage:

- EdgeX configuration
- device semantics
- domain rules
- AI model semantics
- tenant policy

Those belong to L3-L6.

## First executable milestone

A supported amd64 development board must:

1. boot EVE-OS;
2. enroll in Adam;
3. receive the Tangri Edge VM descriptor;
4. start the VM;
5. report host and application state;
6. survive VM restart;
7. accept an application-version update and rollback.

Eden must exercise the same lifecycle before hardware qualification.
