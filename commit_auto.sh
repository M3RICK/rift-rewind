#!/bin/bash

for file in $(git ls-files); do
    git add "$file"
    git commit -m "[FIXED] $file"
done

echo "It is done my man"
