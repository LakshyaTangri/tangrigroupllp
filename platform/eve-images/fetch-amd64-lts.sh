#!/usr/bin/env bash
set -euo pipefail

VERSION="${EVE_VERSION:-17.0.0-lts}"
ARCH="amd64"
HYPERVISOR="kvm"
PLATFORM="generic"
ASSET="${ARCH}.${HYPERVISOR}.${PLATFORM}.installer.raw.zst"
BASE_URL="https://github.com/lf-edge/eve/releases/download/${VERSION}"

OUT_DIR="${OUT_DIR:-dist/eve/${VERSION}}"
mkdir -p "${OUT_DIR}"

curl --fail --location --retry 3 --output "${OUT_DIR}/${ASSET}" "${BASE_URL}/${ASSET}"
curl --fail --location --retry 3 --output "${OUT_DIR}/${ARCH}.${HYPERVISOR}.${PLATFORM}.sha256sums"   "${BASE_URL}/${ARCH}.${HYPERVISOR}.${PLATFORM}.sha256sums"

(
  cd "${OUT_DIR}"
  grep " ${ASSET}$" "${ARCH}.${HYPERVISOR}.${PLATFORM}.sha256sums" | sha256sum --check -
)

echo "Verified: ${OUT_DIR}/${ASSET}"
