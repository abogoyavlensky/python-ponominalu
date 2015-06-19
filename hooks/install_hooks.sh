#!/bin/bash
HOOK_NAMES="applypatch-msg pre-applypatch post-applypatch pre-commit prepare-commit-msg commit-msg post-commit pre-rebase post-checkout post-merge pre-receive update post-receive post-update pre-auto-gc"
# assuming the script is in a bin directory, one level into the repo
REPO_ROOT=$(git rev-parse --show-toplevel)
HOOK_DIR=$REPO_ROOT/.git/hooks


for hook in $HOOK_NAMES; do
    # If the hook already exists, is executable, and is not a symlink
    if [ ! -h $HOOK_DIR/$hook -a -x $HOOK_DIR/$hook ]; then
        mv $HOOK_DIR/$hook $HOOK_DIR/$hook.local
    fi
    if [ -a $REPO_ROOT/hooks/$hook.py ]; then
        ln $REPO_ROOT/hooks/$hook.py $HOOK_DIR/$hook
    fi
done

chmod +x $HOOK_DIR/*
