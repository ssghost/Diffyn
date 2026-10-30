# Diffyn Plugin for Claude Code

A local Claude Code plugin providing native access to the Diffyn Rust MCP server and the canonical task-support workflow.

## Prerequisites

- Claude Code CLI installed with plugin support
- `diffyn` installed and available on your system `PATH`
  - To verify: `diffyn --version`

## Local Loading

Load the plugin directly by pointing Claude Code to this directory:

```bash
claude --plugin-dir ./integrations/claude-code/diffyn
```

## Discovery Verification

Once loaded in an interactive Claude Code session:

1. Inspect available MCP tools: run `/mcp`
2. Verify available skills: check the active skill list to confirm `diffyn-task-support` is recognized

## Stopping & Unloading

To stop using the plugin, exit the Claude Code session or launch Claude Code without the `--plugin-dir` argument:

```bash
claude
```

## Troubleshooting

### Missing Executable (`diffyn` not found)

If the MCP server fails to start with a command-not-found error:

1. Verify that the Diffyn binary has been compiled:
   ```bash
   cargo build --release
   ```
2. Add the compiled binary to your `PATH`, or copy it to a standard bin path:
   ```bash
   export PATH="$PATH:/path/to/diffyn/target/release"
   ```
3. Restart the Claude Code session.