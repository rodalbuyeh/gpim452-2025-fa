#!/usr/bin/env python3

import os
import shutil
import glob

def migrate_stash_to_modules():
    """Migrate files from _module_stash to _modules directory."""
    
    # Create _modules directory if it doesn't exist
    os.makedirs('_modules', exist_ok=True)
    
    # Find all week files in _module_stash
    stash_files = glob.glob('_module_stash/week-*.md')
    
    if not stash_files:
        print("No week files found in _module_stash directory")
        return
    
    print(f"Found {len(stash_files)} week files to migrate:")
    
    for stash_file in sorted(stash_files):
        filename = os.path.basename(stash_file)
        target_file = os.path.join('_modules', filename)
        
        print(f"  {stash_file} -> {target_file}")
        
        # Copy the file
        shutil.copy2(stash_file, target_file)
    
    print(f"\nMigration complete! {len(stash_files)} files copied to _modules/")
    print("\nYou can now:")
    print("1. Review the files in _modules/")
    print("2. Delete _module_stash/ directory if everything looks good")
    print("3. Use the generator scripts for new weeks")

def main():
    if not os.path.exists('_module_stash'):
        print("Error: _module_stash directory not found")
        return 1
    
    migrate_stash_to_modules()
    return 0

if __name__ == '__main__':
    exit(main()) 