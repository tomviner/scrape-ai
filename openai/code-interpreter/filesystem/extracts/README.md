# Code interpreter filesystem

See [listings.txt](listings.txt) for a full list of files (with UUIDs normalised).

The [extracts](extracts) folder contains files directly from code interpreter.
If you're wondering whether this investigation is _allowed_, I especially enjoyed reading [~/README](extracts/home/sandbox/README):

    Thanks for using the code interpreter plugin!

    Please note that we allocate a sandboxed Unix OS just for you, so it's expected that you can see
    and modify files on this system.

## Interesting paths

- /mnt/data/ _"can be used to save and persist user files"_
- [~/](extracts/home/sandbox/)
  - [README](extracts/home/sandbox/README)
  - [.openai_internal/](extracts/home/sandbox/.openai_internal)
  - [kernel-XXXXXXXX-XXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.json](extracts/home/sandbox/kernel-XXXXXXXX-XXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.json) (UUIDs and secrets hidden)
    - [ace_client/](extracts/home/sandbox/.openai_internal/ace_client)
    - [user_machine/](extracts/home/sandbox/.openai_internal/user_machine)
