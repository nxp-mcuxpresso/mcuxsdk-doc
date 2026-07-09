# Prebuilt Binary Blobs

Some SDK components ship with prebuilt binary files (`.a`, `.lib`, `.bin`, etc.)
that are **not included in the git repository itself**. Instead they are fetched
on demand from a dedicated blob repository using the `west blobs` command.

This keeps the main SDK checkout small and fast while still making the binaries
available immediately when you need them.

---

## When do you need to fetch blobs?

You typically need blobs when:

- You are building an example that links against a prebuilt library (e.g. a machine
  learning inference engine, a wireless stack library, or a graphics middleware).
- After a fresh `west init` + `west update`, the build fails with a linker error
  about a missing `.a` or `.lib` file.
- You run `west blobs check` and see `MISSING` entries.

---

## Quick start

Run these commands from your SDK workspace root (the directory that contains
`manifests/` and `mcuxsdk/`):

```bash
# 1. See what blobs are available and whether they are already present
west blobs check

# 2. Fetch any missing blobs
west blobs fetch

# 3. Confirm everything is present
west blobs check
```

A green result looks like:

```
mcu-sdk-examples: 1078/1078 entries: OK
```

---

## Fetch blobs for a specific project only

If you only need blobs for one component, pass the west project name:

```bash
west blobs fetch mcu-sdk-examples
```

Use `west blobs list` to see available project names and their blob files:

```bash
west blobs list
```

---

## License

By fetching blobs you accept the license terms bundled with each blob set.
The applicable license file is located alongside `mcux_blobs.yml` in the
relevant SDK subdirectory (for example `mcuxsdk/examples/LICENSE`).

Some blob sets require explicit license acceptance. If a blob has
`click-through: True`, `west blobs fetch` will prompt you to confirm before
downloading.

---

## Keeping blobs up to date

After running `west update` (which updates the SDK source), re-run:

```bash
west blobs fetch
```

Blobs that are already present and whose sha256 matches are skipped automatically;
only new or changed blobs are downloaded.

---

## Troubleshooting

### Build error: cannot find `-lsomething` or missing `.a` / `.bin`

```bash
west blobs fetch          # fetch all missing blobs
west blobs check          # verify
```

### Re-fetch a corrupted or incomplete blob

```bash
# Remove locally cached blobs for one project and re-download
west blobs clean mcu-sdk-examples
west blobs fetch mcu-sdk-examples
```

### Network / proxy issues

`west blobs fetch` downloads files over HTTPS. If your network requires a proxy,
set the standard environment variables before running the command:

```bash
export HTTPS_PROXY=http://your-proxy:port
west blobs fetch
```

### Checking without downloading

```bash
west blobs check          # shows OK or MISSING per entry; does not download
west blobs list           # lists all declared blobs; does not download
```

---

## Next steps

- [Building Your First Project](first_build.md) — build and run an SDK example
- [Exploring the SDK](explore_sdk.md) — workspace layout and example organization
