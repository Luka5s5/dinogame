#!/usr/bin/env python3
import json
import os

print("=" * 50)
print("SUCCESS! Portainer successfully cloned files from Git!")
print("=" * 50)

print(f"\n📁 Current directory: {os.getcwd()}")
print(f"👤 Running as user: {os.getuid()}")

print(f"\n📄 Listing files in current directory:")
for file in os.listdir():
    if os.path.isdir(file):
        print(f"   📁 {file}/")
    else:
        print(f"   📄 {file}")

print(f"\n📄 Checking app/ directory:")
if os.path.exists('app'):
    for file in os.listdir('app'):
        print(f"   📄 app/{file}")

print(f"\n📄 Contents of main.py:")
with open(__file__, 'r') as f:
    for i, line in enumerate(f.readlines()[:10], 1):
        print(f"   {i:2}: {line.rstrip()}")

print(f"\n🧪 Testing imports...")
try:
    import sys
    print(f"   ✓ sys imported successfully")
except ImportError as e:
    print(f"   ✗ Failed to import: {e}")

print(f"\n📊 System information:")
print(f"   Python: {sys.version}")
print(f"   Platform: {sys.platform}")

print(f"\n✅ Verification complete!")
print("Files were successfully cloned from Git!")#!/usr/bin/env python3
import json
import os

print("=" * 50)
print("SUCCESS! Portainer successfully cloned files from Git!")
print("=" * 50)

print(f"\n📁 Current directory: {os.getcwd()}")
print(f"👤 Running as user: {os.getuid()}")

print(f"\n📄 Listing files in current directory:")
for file in os.listdir():
    if os.path.isdir(file):
        print(f"   📁 {file}/")
    else:
        print(f"   📄 {file}")

print(f"\n📄 Checking app/ directory:")
if os.path.exists('app'):
    for file in os.listdir('app'):
        print(f"   📄 app/{file}")

print(f"\n📄 Contents of main.py:")
with open(__file__, 'r') as f:
    for i, line in enumerate(f.readlines()[:10], 1):
        print(f"   {i:2}: {line.rstrip()}")

print(f"\n🧪 Testing imports...")
try:
    import sys
    print(f"   ✓ sys imported successfully")
except ImportError as e:
    print(f"   ✗ Failed to import: {e}")

print(f"\n📊 System information:")
print(f"   Python: {sys.version}")
print(f"   Platform: {sys.platform}")

print(f"\n✅ Verification complete!")
print("Files were successfully cloned from Git!")
