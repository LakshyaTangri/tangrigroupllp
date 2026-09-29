# L2-04 — Eden System Tests

Eden is the L2 system-test harness. It exercises the real EVE-OS image and the real Tangri Edge VM deployment descriptor before hardware-in-loop.

## Required scenarios

1. EVE boot
2. EVE enrollment
3. Tangri Edge VM deployment
4. VM start
5. VM health verification
6. VM restart
7. application update
8. application rollback
9. simulated WAN loss
10. EVE reboot

## Local prerequisites

- Linux host
- Docker
- QEMU/KVM where available
- Eden
- pinned EVE image
- Adam test controller

Eden's upstream workflow supports named contexts, image setup and QEMU-backed EVE instances.

## Exit condition

A known-good L2 release must pass every scenario. A failing scenario blocks the L2 release.
