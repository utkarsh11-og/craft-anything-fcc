import struct
from pathlib import Path

root = Path("/mnt/c/Users/matrx/source/craft-anything-fcc")
source = root / "branding/generated"
output = source / "craft-anything-xfcc.icns"

# ICNS chunk identifiers and corresponding PNG sizes
icons = [
    ("icp4", 16),
    ("icp5", 32),
    ("icp6", 64),
    ("ic07", 128),
    ("ic08", 256),
    ("ic09", 512),
    ("ic10", 1024),
]

chunks = []

for chunk_type, size in icons:
    path = source / f"xfcc-{size}.png"
    data = path.read_bytes()

    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Invalid PNG: {path}")

    width, height = struct.unpack(">II", data[16:24])

    if (width, height) != (size, size):
        raise ValueError(f"Unexpected dimensions in {path}: {width}x{height}")

    chunks.append(
        chunk_type.encode("ascii")
        + struct.pack(">I", len(data) + 8)
        + data
    )

body = b"".join(chunks)
icns = b"icns" + struct.pack(">I", len(body) + 8) + body

output.write_bytes(icns)

print(f"SUCCESS: {output}")
print(f"Size: {len(icns):,} bytes")
print(f"Embedded resolutions: {[size for _, size in icons]}")
