# L2-01 — EVE-OS Board Images

Tangri does not fork EVE-OS. This module records pinned EVE-OS releases, board qualification data and the reproducible image pipeline.

## Rules

- Never use `latest` for a release artifact.
- Every production image is identified by an immutable EVE-OS version/digest.
- Board-specific changes are kept separate from the generic EVE build.
- An accelerator is not considered supported until HIL proves passthrough.
- RK3588 remains a bring-up/qualification item; it is not assumed qualified.
- amd64 is the first development target.

## Deliverables

- installer/live image reference
- architecture
- board profile
- EVE version
- TPM status
- network adapter mapping
- accelerator/passthrough status
- upgrade and rollback evidence

## Current development target

Start with an amd64 machine capable of KVM/nested virtualization for Eden. EVE's documentation recommends testing EVE under virtualization only where nested virtualization is available; Eden also supports disabling acceleration when required for constrained environments.

The actual board image is promoted only after the board profile and HIL test are green.
